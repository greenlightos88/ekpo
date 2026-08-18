from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def sequence(src: str, n: int) -> str:
    m = re.search(rf"^# SEQUENCE {n} - .*$", src, flags=re.M)
    if not m:
        raise SystemExit(f"missing Sequence {n}")
    nxt = re.search(r"^# SEQUENCE \d+ - .*$", src[m.end():], flags=re.M)
    end = m.end() + nxt.start() if nxt else len(src)
    return src[m.start():end]


def pre() -> None:
    s = text("01_SCREENPLAY.fountain")
    headings = [int(x) for x in re.findall(r"^# SEQUENCE (\d+) - ", s, flags=re.M)]
    if headings != list(range(1, 14)):
        raise SystemExit(f"sequence headings/order failure: {headings}")

    for bad in ["LITTLE GIRL", "little girl", "little-girl", "Why did you call me?", "I didn't smell gas."]:
        if bad in s:
            raise SystemExit("witness residue in screenplay: " + bad)

    required_screenplay = [
        "A WOMAN carrying plates comes through the kitchen door and almost follows his line of sight toward the back passage.",
        "Nobody there is looking toward the back passage yet.",
        "Starts across the courtyard, putting his body between the living house and the back-passage axis.",
        "The last of the children disappears behind the gate pillar.",
        "A BOY near the gate has leaned sideways, trying to see into the courtyard and toward the back passage.",
        "The inner door does not move.",
        "The inner door remains closed.",
        "For Ade, the exchange is already finished -- the notes in the vendor's hand.",
        "Nothing in their movement acknowledges what Ade sees.",
        "For several steps, nothing improves.",
        "MALIK\nWe left the house.",
        "They stay between the two.",
    ]
    for item in required_screenplay:
        if item not in s:
            raise SystemExit("required screenplay beat missing: " + item)

    forbidden_legacy = [
        "ENO\nCar.",
        "one turn short",
        "The real performers continue around it without recognition.",
        "The exchange jumps ahead -- the notes already in the vendor's hand.",
        "Ten steps.\n\nFifteen.\n\nKai's hand tremor begins to ease.",
    ]
    for item in forbidden_legacy:
        if item in s:
            raise SystemExit("legacy screenplay beat remains: " + item)

    canon = text("00_CANON.md")
    for item in [
        "Reality survives not through power, but through stewardship.",
        "Attention creates proximity.",
        "Kai destabilized the regulator. He did not release a trapped creature.",
        "The Entity is an independent ancient intelligence native to the Unseen",
        "Kai naturally mirrors his aunt's perceptual aptitude. He is not a Chosen One.",
        "Ade has no supernatural office.",
        "The inner maintained door is surrounded by a dense measured red-cord/knot field",
        "the masquerade is never the Entity",
    ]:
        if item not in canon:
            raise SystemExit("canon regression: " + item)

    rel = text("development/audits/EKPO_RELATIONAL_EXPOSURE_INTEGRITY_AUDIT.md")
    for item in [
        "Status: AUDIT RESULT — NOT YET CANON",
        "PASS AFTER WITNESS-THREAD REMOVAL / TWO-LAYER MODEL.",
        "local breach/translation pressure plus Entity-specific reciprocal perception",
        "No separate third exposure category is required.",
    ]:
        if item not in rel:
            raise SystemExit("relational audit requirement missing: " + item)
    if "spillover" in rel.lower():
        raise SystemExit("obsolete third-layer spillover language remains")

    continuity = text("docs/CURRENT_CONTINUITY.md")
    if "Symptoms begin easing with distance from the immediate perceptual event." in continuity:
        raise SystemExit("stale distance-as-cause continuity language remains")
    if "stop re-engaging and the procession drops out of sight" not in continuity:
        raise SystemExit("withdrawal causality not synchronized in continuity")

    active = [
        "00_CANON.md", "README.md", "PROJECT_MANIFEST.yaml",
        "development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md",
        "development/audits/EKPO_RELATIONAL_EXPOSURE_INTEGRITY_AUDIT.md",
        "docs/CURRENT_CONTINUITY.md", "docs/ENTITY_HORROR_PHYSIOLOGY.md",
        "docs/HOUSE_GEOGRAPHY.md", "docs/MOTIF_LEDGER.md", "docs/NEXT_MOVEMENT.md",
        "docs/REGULATOR_CORD_ARRAY.md", "docs/SEQUENCE_12_LOCK.md",
    ]
    for relpath in active:
        t = text(relpath)
        for bad in ["LITTLE GIRL", "little girl", "little-girl", "Why did you call me?"]:
            if bad in t:
                raise SystemExit(f"{relpath}: witness residue {bad}")

    main = subprocess.check_output(
        ["git", "show", "origin/main:01_SCREENPLAY.fountain"], text=True, encoding="utf-8"
    )
    for n in [2, 3, 4, 6, 7, 8, 9]:
        if sequence(s, n) != sequence(main, n):
            raise SystemExit(f"unexpected regression in retained Sequence {n}")

    print("SOURCE/MYTHOLOGY/CONTINUITY INTEGRITY PASS")


def post() -> None:
    from pypdf import PdfReader
    import pymupdf

    pdf = ROOT / "output/pdf/EKPO_Screenplay.pdf"
    if not pdf.exists() or pdf.stat().st_size < 50000:
        raise SystemExit("PDF missing or implausibly small")

    reader = PdfReader(str(pdf))
    pages = len(reader.pages)
    doc = pymupdf.open(pdf)
    blank, edges, tiny, noncourier, texts = [], [], [], [], []
    for i, page in enumerate(doc):
        t = page.get_text("text")
        texts.append(t)
        if i > 0 and len(t.strip()) < 80:
            blank.append(i + 1)
        rect = page.rect
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            if x0 < 8 or y0 < 8 or x1 > rect.width - 8 or y1 > rect.height - 8:
                edges.append(i + 1)
        spans = []
        for block in page.get_text("dict").get("blocks", []):
            for line in block.get("lines", []):
                spans.extend(line.get("spans", []))
        if spans:
            if min(float(sp.get("size", 99)) for sp in spans) < 7:
                tiny.append(i + 1)
            if i > 0:
                names = [str(sp.get("font", "")).lower() for sp in spans if str(sp.get("text", "")).strip()]
                if names and sum("courier" in name for name in names) / len(names) < 0.90:
                    noncourier.append(i + 1)
    if blank:
        raise SystemExit("blank/sparse pages " + repr(blank))
    if edges:
        raise SystemExit("edge/clipping risks " + repr(sorted(set(edges))))
    if tiny:
        raise SystemExit("tiny-text pages " + repr(tiny))
    if noncourier:
        raise SystemExit("non-Courier screenplay pages " + repr(noncourier))

    alltext = " ".join(" ".join(texts).split())
    for bad in ["LITTLE GIRL", "Why did you call me?", "I didn't smell gas."]:
        if bad in alltext:
            raise SystemExit("rendered witness residue: " + bad)
    for item in [
        "Nobody there is looking toward the back passage yet.",
        "The last of the children disappears behind the gate pillar.",
        "They stay between the two.",
        "For Ade, the exchange is already finished",
        "Nothing in their movement acknowledges what Ade sees.",
        "For several steps, nothing improves.",
        "We left the house.",
    ]:
        if item not in alltext:
            raise SystemExit("render missing required beat: " + item)

    checks = {
        "00_CANON.md": f"Latest successful technical render of the candidate: {pages} physical pages.",
        "README.md": f"latest successful technical render: **{pages} physical pages**",
        "PROJECT_MANIFEST.yaml": f"latest_technical_physical_pages: {pages}",
        "development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md": f"**{pages} physical PDF pages**",
    }
    for relpath, item in checks.items():
        if item not in text(relpath):
            raise SystemExit(f"page-count authority mismatch in {relpath}: expected {item}")

    allowed = {
        "00_CANON.md", "01_SCREENPLAY.fountain", "PROJECT_MANIFEST.yaml", "README.md",
        "development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md",
        "development/audits/EKPO_RELATIONAL_EXPOSURE_INTEGRITY_AUDIT.md",
        "docs/CURRENT_CONTINUITY.md", "output/pdf/EKPO_Screenplay.pdf",
    }
    status = subprocess.check_output(["git", "status", "--porcelain"], text=True, encoding="utf-8")
    unexpected = []
    for line in status.splitlines():
        path = line[3:].strip().strip('"')
        if path.startswith(".github/workflows/") or path.startswith("tools/"):
            continue
        if path not in allowed:
            unexpected.append(path)
    if unexpected:
        raise SystemExit("unexpected files changed: " + repr(unexpected))

    print(f"PDF/REPOSITORY INTEGRITY PASS physical_pages={pages} bytes={pdf.stat().st_size}")


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "pre"
    if phase == "pre":
        pre()
    elif phase == "post":
        post()
    else:
        raise SystemExit("usage: check_sequence12_witness_removal_integrity.py [pre|post]")
