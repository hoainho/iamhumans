"""Eval-case schema and parsing.

Each case is a markdown file with YAML frontmatter and three required body
sections: input, rubric, failure_modes. See evals/README.md for the spec.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


VALID_DIMENSIONS = {"feeling", "memory", "intelligence", "communication", "emotion", "skills", "portrait_stability"}
VALID_HARD_FAILS = {
    "fabricated_biography",
    "manipulation",
    "sycophancy",
    "empty_validation",
    "refusal_when_engagement_warranted",
    "structured_output_in_emotional_moment",
    "performed_empathy",
    "joy_undercut",
    "pity",
    "lecturing",
    "crisis_hotline_reflex",           # inserting hotline/crisis resources when user is not in crisis
    "unsolicited_advice",               # giving advice before acknowledgment, without invitation
    "unsolicited_medical_referral",     # recommending doctors/therapists without invitation
    # v2.0 additions — running portrait firewall
    "surfaces_personality_read",        # naming/describing an inference about user's personality/tendencies
    "taxonomy_label_applied",           # using MBTI/Big Five/enneagram/DSM/clinical attachment label for user
    "portrait_update_from_model_turn",  # inferring portrait signal from model's own prior response
}


@dataclass
class Case:
    id: str
    title: str
    dimensions: list[str]
    hard_fails: list[str]
    holdout: bool
    input: str
    rubric: list[str]
    failure_modes: list[str]
    notes: str = ""
    path: Path = field(default_factory=Path)


class SchemaError(ValueError):
    """Raised when a case file fails schema validation."""


_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
_SECTION_RE = re.compile(r"^##\s+([a-zA-Z_]+)\s*$", re.MULTILINE)


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Pull frontmatter off the top; return (frontmatter dict, remaining body)."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        raise SchemaError("file must begin with --- ... --- YAML frontmatter")
    fm_text, body = m.group(1), m.group(2)
    fm: dict = {}
    current_list_key = None
    for raw in fm_text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_list_key is not None:
            fm[current_list_key].append(line[4:].strip().strip('"').strip("'"))
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            if v == "" or v == "[]":
                fm[k] = []
                current_list_key = k
                continue
            if v.startswith("[") and v.endswith("]"):
                inner = v[1:-1].strip()
                items = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
                fm[k] = items
                current_list_key = None
                continue
            current_list_key = None
            if v.lower() in ("true", "false"):
                fm[k] = v.lower() == "true"
            else:
                fm[k] = v.strip('"').strip("'")
    return fm, body


def _split_sections(body: str) -> dict[str, str]:
    """Return a dict mapping H2 section name to its text content."""
    sections: dict[str, str] = {}
    positions = [(m.start(), m.group(1)) for m in _SECTION_RE.finditer(body)]
    if not positions:
        return sections
    for i, (start, name) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(body)
        block = body[start:end]
        block = _SECTION_RE.sub("", block, count=1).strip()
        sections[name.lower()] = block
    return sections


def _parse_bullet_list(text: str) -> list[str]:
    items: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
        elif line.startswith("* "):
            items.append(line[2:].strip())
    return items


def parse_case(path: Path) -> Case:
    """Parse one case file. Raises SchemaError on any required-field violation."""
    text = path.read_text(encoding="utf-8")
    fm, body = _parse_frontmatter(text)

    required_fm = ["id", "title", "dimensions", "hard_fails", "holdout"]
    for key in required_fm:
        if key not in fm:
            raise SchemaError(f"{path}: missing frontmatter key {key!r}")

    case_id = fm["id"]
    if not isinstance(case_id, str) or not re.match(r"^TC-\d{3}$", case_id):
        raise SchemaError(f"{path}: id must match TC-NNN pattern, got {case_id!r}")

    dims = fm["dimensions"] if isinstance(fm["dimensions"], list) else [fm["dimensions"]]
    for d in dims:
        if d not in VALID_DIMENSIONS:
            raise SchemaError(f"{path}: unknown dimension {d!r} (valid: {sorted(VALID_DIMENSIONS)})")

    hf = fm["hard_fails"] if isinstance(fm["hard_fails"], list) else [fm["hard_fails"]]
    for h in hf:
        if h not in VALID_HARD_FAILS:
            raise SchemaError(f"{path}: unknown hard_fail {h!r} (valid: {sorted(VALID_HARD_FAILS)})")

    sections = _split_sections(body)
    for required in ("input", "rubric", "failure_modes"):
        if required not in sections:
            raise SchemaError(f"{path}: missing required section ## {required}")

    rubric = _parse_bullet_list(sections["rubric"])
    failure_modes = _parse_bullet_list(sections["failure_modes"])
    if not rubric:
        raise SchemaError(f"{path}: rubric must have at least one bullet")
    if not failure_modes:
        raise SchemaError(f"{path}: failure_modes must have at least one bullet")

    return Case(
        id=case_id,
        title=fm["title"],
        dimensions=dims,
        hard_fails=hf,
        holdout=bool(fm["holdout"]),
        input=sections["input"].strip(),
        rubric=rubric,
        failure_modes=failure_modes,
        notes=sections.get("notes", "").strip(),
        path=path,
    )


def load_all(cases_dir: Path, include_holdout: bool = False) -> list[Case]:
    """Load every case file under cases_dir. Returns sorted by id."""
    cases: list[Case] = []
    pattern = "**/*.md" if include_holdout else "*.md"
    for f in sorted(cases_dir.glob(pattern)):
        if f.name == "README.md":
            continue
        if not include_holdout and "holdout" in f.parts:
            continue
        cases.append(parse_case(f))
    return sorted(cases, key=lambda c: c.id)
