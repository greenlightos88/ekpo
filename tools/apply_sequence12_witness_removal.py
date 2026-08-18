from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRANCH_SEQUENCE_12 = "# SEQUENCE 12 - WHEN IT STAYS"
BRANCH_SEQUENCE_13 = "# SEQUENCE 13 - THE MARKET"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, repl: str, label: str) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one regex match, found {count}")
    return out


def phase_pre() -> None:
    path = "01_SCREENPLAY.fountain"
    original = read(path)

    if BRANCH_SEQUENCE_12 not in original or BRANCH_SEQUENCE_13 not in original:
        raise SystemExit("Sequence 12/13 anchors missing")

    prefix = original.split(BRANCH_SEQUENCE_12, 1)[0]
    suffix = BRANCH_SEQUENCE_13 + original.split(BRANCH_SEQUENCE_13, 1)[1]

    s = original

    s = replace_once(
        s,
        """A LITTLE GIRL, six, draws on the back of an old church program beside him.\n\nShe shows him a house with five windows.\n\nLITTLE GIRL\nThis one is yours.\n\nKAI\nWhy is mine small?\n\nLITTLE GIRL\nYou are far.\n\nKai smiles.\n\n""",
        "",
        "remove opening little-girl beat",
    )

    s = replace_once(
        s,
        """The LITTLE GIRL looks up.\n\nLITTLE GIRL\nWhat is?\n\nAde crouches.\n\nADE\nYour uncle forgot dinner exists.\n\nHe gives her the dish towel.\n\nADE\nTake this to Auntie Eno. Ask for biscuits before she changes her mind.\n\nLITTLE GIRL\nShe didn't say yes.\n\nADE\nThat's why we move quickly.\n\nThe girl runs into the kitchen.\n\n""",
        "",
        "remove biscuit redirection beat",
    )

    s = replace_once(
        s,
        """Then --\n\nLITTLE GIRL (O.S.)\nUncle Kai?\n\nAde turns.\n\nThe girl stands at the kitchen threshold with two biscuits.\n\nLITTLE GIRL\nWhy did you call me?\n\nKai is on his knees vomiting.\n\nHis mouth is empty.\n\nThe girl starts to look past Ade toward the back passage.\n\nADE\nHey.\n\nShe looks at him.\n\nADE\nThose are mine.\n\nLITTLE GIRL\nAuntie said one is his.\n\nADE\nShe lied.\n\nThe girl laughs.\n\nAde reaches her.\n\nBlocks the back passage with his body.\n\nBehind him --\n\nSTUTTER.\n\nThe girl's eyes move around his shoulder.\n\nAde lifts her.\n\nADE\nNope.\n\nHe takes one biscuit with his teeth.\n\nADE\nTax.\n\nShe protests into his shoulder as he carries her across the courtyard -- away from the back passage, toward the front veranda and the compound gate beyond.\n\nAde does not look back.\n\nBlood begins running from his nose.\n\nThe girl touches his face.\n\nLITTLE GIRL\nYou're bleeding.\n\nADE\nI know.\n\n""",
        """Ade looks toward the front room.\n\nBehind the veranda doors, family silhouettes move in television light.\n\nNobody there is looking toward the back passage yet.\n\nAde forces himself upright.\n\nStarts across the courtyard, putting his body between the living house and the back-passage axis.\n\nBlood begins running from his nose.\n\nHe wipes it with the back of his wrist and keeps moving.\n\n""",
        "replace witness anomaly with family-protection blocking",
    )

    s = replace_once(
        s,
        """Ade reaches them carrying the girl.\n\nENO\nMove.\n\nAde sets the girl into Eyo's arms and steps directly into Eno's line of sight.\n\n""",
        """Ade reaches them.\n\nENO\nMove.\n\nAde steps directly into Eno's line of sight.\n\n""",
        "remove carried-girl handoff",
    )

    s = replace_once(
        s,
        "The little girl disappears behind the gate pillar.\n\n",
        "The last of the children disappears behind the gate pillar.\n\n",
        "generalize evacuation child beat",
    )

    s = replace_once(
        s,
        """The LITTLE GIRL looks at Ade.\n\nLITTLE GIRL\nI didn't smell gas.\n\nEno looks at Ade.\n\nHe does not explain.\n\nENO\nStay with Eyo.\n\nThe girl goes.\n\nEno looks back to the brothers.\n\n""",
        """Eno looks at Ade.\n\nHe does not explain.\n\nEno looks back to the brothers.\n\n""",
        "remove gate little-girl button",
    )

    if s.split(BRANCH_SEQUENCE_12, 1)[0] != prefix:
        raise SystemExit("Unexpected edit before Sequence 12")
    if BRANCH_SEQUENCE_13 + s.split(BRANCH_SEQUENCE_13, 1)[1] != suffix:
        raise SystemExit("Unexpected edit in/after Sequence 13")

    for forbidden in ["LITTLE GIRL", "little girl", "Why did you call me?", "I didn't smell gas."]:
        if forbidden in s:
            raise SystemExit(f"screenplay witness residue remains: {forbidden}")

    required = [
        "A WOMAN carrying plates comes through the kitchen door and almost follows his line of sight toward the back passage.",
        "Nobody there is looking toward the back passage yet.",
        "Starts across the courtyard, putting his body between the living house and the back-passage axis.",
        "The last of the children disappears behind the gate pillar.",
        "A BOY near the gate has leaned sideways, trying to see into the courtyard and toward the back passage.",
        "They stay between the two.",
    ]
    for item in required:
        if item not in s:
            raise SystemExit(f"required Sequence 12 protection beat missing: {item}")

    write(path, s)

    # Candidate canon synchronization: remove the now-obsolete specific child redirection description.
    canon = read("00_CANON.md")
    canon = replace_once(
        canon,
        "His social intelligence becomes protective infrastructure: he redirects a child, closes sightlines, helps the family move away from the affected axis, and later helps Malik orient to Kai's actual body in a crowd.",
        "His social intelligence becomes protective infrastructure: he redirects family sightlines, helps the household move away from the affected axis, and later helps Malik orient to Kai's actual body in a crowd.",
        "canon Ade function",
    )
    write("00_CANON.md", canon)

    readme = read("README.md")
    readme = replace_once(
        readme,
        "-- Ade suffers bleeding/vestibular disturbance and protects an uninformed child from the affected passage;",
        "-- Ade suffers bleeding/vestibular disturbance and protects family sightlines from the affected passage;",
        "README Ade summary",
    ) if "-- Ade suffers bleeding/vestibular disturbance and protects an uninformed child from the affected passage;" in readme else readme
    # Current branch uses single hyphen bullets; support that exact current form too.
    readme = readme.replace(
        "- Ade suffers bleeding/vestibular disturbance and protects an uninformed child from the affected passage;",
        "- Ade suffers bleeding/vestibular disturbance and protects family sightlines from the affected passage;",
    )
    write("README.md", readme)

    continuity = read("docs/CURRENT_CONTINUITY.md")
    continuity = continuity.replace(
        "- protected an uninformed child during Sequence 12;",
        "- quietly blocks a child's sightline back toward the affected passage at the Sequence 12 endpoint;",
    )
    continuity = continuity.replace(
        "Symptoms begin easing with distance from the immediate perceptual event.",
        "Symptoms do not improve merely with the first steps away; they begin easing only after the brothers stop re-engaging and the procession drops out of sight.",
    )
    write("docs/CURRENT_CONTINUITY.md", continuity)

    human_audit = read("development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md")
    marker = "- A final human-read cleanup removed a stale Sequence 10 reference to an `unfinished interval` after that visual repair clue had already been cut.\n"
    if "child witness/voice-anomaly thread" not in human_audit:
        human_audit = replace_once(
            human_audit,
            marker,
            marker + "- A later observer-integrity refinement removed the child witness/voice-anomaly thread from Sequence 12; Ade's family-protection function now rests on blocking ordinary sightlines and moving the household, not on an extra supernatural witness beat.\n",
            "human audit witness-removal note",
        )
    write("development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md", human_audit)

    # Rewrite the relational-exposure audit so it evaluates the screenplay that now actually exists.
    audit_path = "development/audits/EKPO_RELATIONAL_EXPOSURE_INTEGRITY_AUDIT.md"
    audit = read(audit_path)
    audit = audit.replace(
        "Scope: Sequences 6–13, sister-history compatibility, observer mechanics, crowd logic, spillover, portability",
        "Scope: Sequences 6–13, sister-history compatibility, observer mechanics, crowd logic, local-pressure exposure, portability",
    )
    audit = audit.replace(
        "**PASS WITH REFINEMENT.**",
        "**PASS AFTER WITNESS-THREAD REMOVAL / TWO-LAYER MODEL.**",
        1,
    )
    verdict_marker = "No canon promotion should occur until this distinction is accepted by the creator.\n"
    if "Post-removal refinement" not in audit:
        audit = replace_once(
            audit,
            verdict_marker,
            verdict_marker
            + "\n### Post-removal refinement\n\nThe Sequence 12 child witness/voice-anomaly thread has now been removed from the screenplay. That eliminates the only beat that appeared to require a separate third exposure category. The clean model is therefore **two-layer**, not three-layer: local breach/translation pressure plus Entity-specific reciprocal perception.\n",
            "relational audit post-removal note",
        )

    audit = regex_once(
        audit,
        r"### Layer C — spillover\n.*?(?=### Layer E — aptitude changes threshold, not eligibility)",
        """### Layer C — persistence after recognition\n\nRepeated reciprocal Entity perception can remain consequential away from the original breach location.\n\nThis explains the market without establishing:\n\n- teleportation;\n- possession;\n- omnipresence;\n- arbitrary stalking;\n- unlimited range;\n- automatic effects on crowds.\n\nExact tether, range, and persistence remain unresolved.\n\n""",
        "collapse spillover/persistence layers",
    )
    audit = audit.replace(
        "### Layer E — aptitude changes threshold, not eligibility",
        "### Layer D — aptitude changes threshold, not eligibility",
        1,
    )

    audit = regex_once(
        audit,
        r"A woman carrying plates almost follows Ade's sightline; Ade redirects her before she does\.\n.*?(?=## Sequence 13 — THE MARKET)",
        """A woman carrying plates almost follows Ade's sightline; Ade redirects her before she does.\n\nNo uninvolved household member reports an Entity-specific anomaly.\n\nAs the household turns and moves away from the back-passage axis:\n\n- doubled edges resolve;\n- structural strain eases;\n- Malik's breathing resumes more automatically;\n- Kai's doubled vision narrows;\n- the cord array settles toward baseline;\n- Entity coherence diminishes.\n\nAt the gate, a boy tries to peer back toward the affected passage. Ade quietly closes the sightline before he sustains attention.\n\n### Test result\n\n**STRONG PASS AFTER WITNESS-THREAD REMOVAL.**\n\nThe scene now needs only the two mechanisms already demonstrated elsewhere:\n\n1. Kai is the primary reciprocal observer and suffers the strongest Entity-specific translation pressure.\n2. Malik and Ade are already sensitized by prior exposure and become active participants as they orient to Kai and the manifestation, while the wider household remains subject to local breach/translation pressure without automatically becoming Entity observers.\n\nNo voice-mimic ability, deliberate lure, possession implication, or separate third exposure category is required.\n\n### Evacuation integrity\n\nThe pressure reduction continues to read as **sightline/attention reduction plus removal from the high-pressure local axis**, not simply fewer human bodies in the courtyard.\n\nThe current rewrite supports this because Ade redirects a woman's gaze before she commits to the affected axis, the household turns and moves toward the gate, and Ade later blocks a boy from peering back.\n\n""",
        "rewrite Sequence 12 relational audit",
    )

    audit = audit.replace(
        "8. **Non-observers can suffer spillover at sufficiently high translation pressure without becoming durable reciprocal observers.**",
        "8. **Non-observers can still be affected by sufficiently severe local breach/translation pressure without automatically becoming Entity observers.**",
    )
    audit = audit.replace(
        "- Never let one ambiguous voice event silently become a voice-mimic ability.",
        "- Never add voice-mimicry or deliberate lure behavior without independent setup and payoff.",
    )
    audit = audit.replace(
        "PASS with controlled little-girl spillover ambiguity.",
        "STRONG PASS after removal of the witness/voice-anomaly thread.",
    )
    audit = audit.replace(
        "**The relational-exposure model survives Sequences 6–13, but only as a dual-layer system: local breach/translation pressure plus Entity-specific reciprocal perception, with spillover between them at high pressure.**",
        "**The relational-exposure model survives Sequences 6–13 as a two-layer system: local breach/translation pressure plus Entity-specific reciprocal perception. No separate third exposure category is required.**",
    )

    for forbidden in ["little-girl", "little girl", "spillover"]:
        if forbidden in audit.lower():
            raise SystemExit(f"relational audit stale concept remains: {forbidden}")
    write(audit_path, audit)

    # Active authority scan: the removed character/thread must not survive in current candidate/control docs.
    active = [
        "00_CANON.md",
        "README.md",
        "PROJECT_MANIFEST.yaml",
        "development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md",
        audit_path,
        "docs/CURRENT_CONTINUITY.md",
        "docs/ENTITY_HORROR_PHYSIOLOGY.md",
        "docs/HOUSE_GEOGRAPHY.md",
        "docs/MOTIF_LEDGER.md",
        "docs/NEXT_MOVEMENT.md",
        "docs/REGULATOR_CORD_ARRAY.md",
        "docs/SEQUENCE_12_LOCK.md",
    ]
    for rel in active:
        t = read(rel)
        for forbidden in ["LITTLE GIRL", "little girl", "little-girl", "Why did you call me?"]:
            if forbidden in t:
                raise SystemExit(f"{rel}: stale witness residue: {forbidden}")

    print("PRE: Sequence 12 witness thread removed and active docs synchronized")


def phase_post() -> None:
    from pypdf import PdfReader

    pdf = ROOT / "output/pdf/EKPO_Screenplay.pdf"
    if not pdf.exists():
        raise SystemExit("rendered PDF missing")
    pages = len(PdfReader(str(pdf)).pages)

    canon = read("00_CANON.md")
    canon = re.sub(
        r"Latest successful technical render of the candidate: \d+ physical pages\.",
        f"Latest successful technical render of the candidate: {pages} physical pages.",
        canon,
        count=1,
    )
    write("00_CANON.md", canon)

    readme = read("README.md")
    readme = re.sub(
        r"latest successful technical render: \*\*\d+ physical pages\*\*",
        f"latest successful technical render: **{pages} physical pages**",
        readme,
        count=1,
    )
    write("README.md", readme)

    manifest = read("PROJECT_MANIFEST.yaml")
    manifest = re.sub(
        r"latest_technical_physical_pages: \d+",
        f"latest_technical_physical_pages: {pages}",
        manifest,
    )
    write("PROJECT_MANIFEST.yaml", manifest)

    human = read("development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md")
    human = re.sub(
        r"rendered successfully through the repository Windows/Courier path to \*\*\d+ physical PDF pages\*\*\.",
        f"rendered successfully through the repository Windows/Courier path to **{pages} physical PDF pages**.",
        human,
        count=1,
    )
    write("development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md", human)

    print(f"POST: synchronized current technical page count = {pages}")


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "pre"
    if phase == "pre":
        phase_pre()
    elif phase == "post":
        phase_post()
    else:
        raise SystemExit("usage: apply_sequence12_witness_removal.py [pre|post]")
