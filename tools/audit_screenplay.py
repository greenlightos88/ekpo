#!/usr/bin/env python3
"""Run reproducible structural and continuity checks for the complete EKPO draft."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


EXPECTED_TITLES = [
    "THE LAST MORNING", "THE FUNERAL", "THE WILL AND DECISION", "ARRIVAL",
    "HOMECOMING", "THE LAND AND THE SHRINE", "THE RIVER BOUNDARY",
    "THE DISTANCE BETWEEN", "WHAT HE OPENED", "THE TWO RECORDS", "WHAT HE LEFT",
    "WHEN IT STAYS", "THE MARKET", "WHAT WAS DUE", "THE WESTERN STONES",
    "THE WORKING POSITION", "THE MAN BEFORE", "THE OTHER HALF", "TWO RHYTHMS",
    "THE FIRST CORRECTION", "THE LAST PAGE", "WHAT HAPPENED TO HER",
    "WHAT SOLOMON CLOSED", "THE BREACH", "GIVE ME ONE SIDE", "A WAY HOME",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    text = args.source.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^# SEQUENCE (\d+) - (.+)$", text, re.MULTILINE))
    checks: list[tuple[str, bool]] = []

    checks.append(("exactly 26 consecutive correctly named sequences", [
        (int(match.group(1)), match.group(2)) for match in headings
    ] == list(enumerate(EXPECTED_TITLES, start=1))))

    def sequence(number: int) -> str:
        start = headings[number - 1].start()
        end = headings[number].start() if number < len(headings) else len(text)
        return text[start:end]

    if len(headings) == 26:
        s6, s9, s10 = sequence(6), sequence(9), sequence(10)
        s14, s15, s17, s18, s19 = sequence(14), sequence(15), sequence(17), sequence(18), sequence(19)
        s20, s21, s22 = sequence(20), sequence(21), sequence(22)
        s24, s25, s26 = sequence(24), sequence(25), sequence(26)

        checks.extend([
            ("fracture precedes Kai's deliberate removal", s6.index("dark fracture") < s6.index("deliberately lifts the exposed half")),
            ("other active half remains seated in Sequence 6", "other half still sits in the recess" in s6),
            ("broken half disclosed in Sequence 9", "BROKEN HALF OF THE BRASS TALISMAN" in s9),
            ("old chamber replaced with deep closed dome", all(term in s10 for term in ["steep stone staircase", "high, closed dome", "No window", "Two open brass forearm bands"])),
            ("field inspection receives explicit household conditions", all(term in s14.lower() for term in ["no ravine. no repairs.", "you come back while i can see your faces", "bedding"])),
            ("camera left at market is explicitly retrieved before fieldwork", "retrieves the cracked camera he deliberately left behind" in s14),
            ("western truck/footpath route established before ending", "pickup stops at a locked irrigation gate" in s15),
            ("Bode remains a driver and witness rather than a co-steward", "I drove him to the gate. He walked the rest alone." in s15),
            ("young Solomon disclosed materially without live scene", all(term in s17 for term in ["cassette", "photograph", "Playing music"])),
            ("Malik confronts inherited control through Solomon's failure", all(term in s17 for term in ["the funeral I checked the flowers twice", "Did it work for him?"])),
            ("two historical brass objects compared separately", all(term in s18 for term in ["Vancouver carving", "active shrine half", "Two objects", "ORIGINAL REMOVED. NEW CENTER SET."])),
            ("both brass objects receive explicit separate custody on exit", all(term in s18 for term in ["returns it to his camera bag", "active shrine half", "carries it upstairs"])),
            ("two pressure rhythms recognized before climax", all(term in s19 for term in ["serrated", "rounded", "There are two"])),
            ("Kai's initial two-rhythm deduction is fallible and corrected", all(term in s19 for term in ["I matched the shape to the wrong sound", "Play it from before", "She separated them"])),
            ("Ade first intervention causes shoulder/rib injury", all(term in s20 for term in ["dead end", "shoulder hits first", "ribs"])),
            ("Ade privately confronts the cost before returning", all(term in s20 for term in ["It's going to hurt again", "You haven't.", "He stays."])),
            ("sister's non-ghost message says presence came afterward", all(term in s21 for term in ["IT WAS NOT THE ONE AT THE DOOR", "IT CAME AFTER"])),
            ("all three brothers materially uncover the sister's message", all(term in s21 for term in ["She pressed through", "Malik moves the lamp", "Kai watches the screen"])),
            ("historical death disclosed through material record", all(term in s22 for term in ["clinic record", "compression", "oxygen", "dance-hall receipt"])),
            ("family evacuation and brother consent precede final descent", all(term in s22 for term in ["compound gate", "you're not doing it alone", "We all leave"])),
            ("unauthorized and familiar signatures share controlled climax", all(term in s24 for term in ["dark-violet", "old-gold", "narrow physical antechamber", "fixed guides"])),
            ("funeral phrase returns as Ade's earned climax action", "Give me one side." in sequence(2) and "Give me one side." in s25),
            ("all brothers survive the distributed-load climax", all(term in s25 for term in ["Malik releases", "ADE\nI have this side", "We're here."])),
            ("final repair remains separate from chamber survival", all(term in s26.lower() for term in ["other half is still there", "western service track", "remaining half waits", "can still be opened"])),
            ("injuries carry through final shrine approach", all(term in s26.lower() for term in ["hand still shakes", "arm against his chest", "unable to make a fist", "stops twice"])),
            ("retired carving remains separate in final scene", "retired Vancouver carving remains wrapped" in s26 and "old carving" in s26),
            ("feature ends without a sequel sting", text.rstrip().endswith("FADE OUT.")),
        ])

    prohibited = [
        ("no superseded four-step chamber", r"FOUR STONE STEPS|four stone steps"),
        ("no superseded slatted chamber windows", r"slatted windows|high slats|beneath the window"),
        ("no flat-wall loose-tail diagnostic language", r"loose tail|cord field|field of red cords"),
        ("one consistent production heading for the pressure chamber", r"^INT\. OKU FAMILY HOUSE - MAINTENANCE ROOM"),
        ("no writer-room continuity commentary in screenplay prose", r"Nothing has changed custody because|without the film showing it again|No monster catalog"),
        ("no scene heading showing Solomon alive", r"^(?:INT\.|EXT\.).*(?:FLASHBACK|SOLOMON - YOUNG)"),
        ("no invented chosen-one or cult subplot", r"\bchosen one\b|\bsupernatural cult\b"),
    ]
    checks.extend((label, re.search(pattern, text, re.IGNORECASE | re.MULTILINE) is None) for label, pattern in prohibited)

    failed = []
    for label, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {label}")
        if not passed:
            failed.append(label)
    print(f"\n{len(checks) - len(failed)}/{len(checks)} screenplay integrity checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
