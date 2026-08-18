from pathlib import Path
import hashlib

ROOT = Path('.')

EXPECTED_SCREENPLAY_SHA256 = None


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def write(path, text):
    (ROOT / path).write_text(text, encoding='utf-8', newline='\n')


def replace_once(path, old, new):
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{path}: expected exactly one anchor, found {count}: {old[:120]!r}')
    write(path, text.replace(old, new, 1))


def insert_after(path, anchor, block):
    replace_once(path, anchor, anchor + block)


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


screenplay_before = sha256('01_SCREENPLAY.fountain')
pdf_before = sha256('output/pdf/EKPO_Screenplay.pdf')

# 1) Foundational mythology: distinguish the two brass objects and lock reveal control.
myth_anchor = "Kai did not release a trapped monster. He disrupted an existing regulator.\n\n## 5. The Entity"
myth_insert = """Kai did not release a trapped monster. He disrupted an existing regulator.\n\n## 4A. Brass continuity — retired sister-era piece and Solomon's replacement\n\nTwo visually related brass objects exist in the story and must never be collapsed into one object.\n\n### Retired sister-era brass carving\n\nThe small brass carving found in Solomon's blue drawer in Vancouver is a **retired regulatory component from the period when Solomon and his sister still performed the work together**. It is the same old brass piece whose compact silhouette is visible in the scratched Calabar photograph from their youth.\n\nIt belonged to their shared stewardship work. It was **not** the sister's personal magical amulet, soul vessel, hereditary badge, or private talisman. Its emotional meaning comes from history and custody, not from a separate supernatural power.\n\n### Active replacement brass talisman\n\nAfter Solomon's procedural failure destabilized the boundary and his sister restored equilibrium and died, Solomon rebuilt and stabilized the procedural side of the regulator. As part of that post-catastrophe work, he **retired the older brass component and installed a new active brass talisman**.\n\nThe brass talisman Kai removes from the hidden regulator in Sequence 6 is that later Solomon-era replacement. It is a functional component of the active regulator. Removing it contributes to destabilization because of its regulatory function, not because it contains the Entity or because of any sentimental connection to Solomon's sister.\n\nThe retired carving and the active talisman share the same regulatory design language — including the three-line motif — but they are intentionally **not identical objects**. Existing screenplay differences in angle, hollow, wear, and center treatment are meaningful evidence of related generations of workmanship, not continuity errors.\n\n### Solomon's private memento\n\nSolomon kept the retired sister-era brass piece after the catastrophe and ultimately carried it to Canada. At writer level it becomes his most concrete private memento of:\n\n- his sister;\n- the partnership they once had;\n- the regulatory system as it existed while she was alive;\n- the failure he never emotionally escaped.\n\nSolomon does not sentimentalize it publicly. He hides it among ordinary household remnants. That behavior is consistent with his psychology: he preserves grief as handled material and procedure rather than speaking it directly.\n\n### Reveal control\n\nThis relationship is **writer-level canon, not current character knowledge**. The screenplay must not explain it simply because the writers now know it. The connection should be earned later through physical evidence, records, dating, replacement history, wear, or another materially credible discovery.\n\nUntil that reveal:\n\n- Kai may recognize that the two brass objects are related without knowing how;\n- Bode does not automatically know the complete replacement history;\n- the ledger category `BRASS` remains broader than either single object and must not be treated as automatic proof that a given entry means the talisman;\n- no scene may call the retired carving the sister's magical amulet;\n- no scene may imply that simply returning the retired carving or the active talisman is a complete repair.\n\nSee `docs/BRASS_OBJECT_CONTINUITY.md`.\n\n## 5. The Entity"""
replace_once('EKPO_Canonical_Mythology_Refactor.md', myth_anchor, myth_insert)

# 2) Active canon.
replace_once('00_CANON.md', 'Version: 6.1 — Human-Audit Spatial Revision / Sequence 13 Market Candidate', 'Version: 6.2 — Brass Continuity Lock / Sequence 13 Market Candidate')
insert_after('00_CANON.md', 'Cord-array authority: `docs/REGULATOR_CORD_ARRAY.md`\n', 'Brass-object authority: `docs/BRASS_OBJECT_CONTINUITY.md`\n')
canon_shrine_anchor = "Kai destabilized the regulator. He did not release a trapped creature.\n\n## The Entity"
canon_shrine_block = """Kai destabilized the regulator. He did not release a trapped creature.\n\n## Brass object continuity\n\nTwo related but distinct brass objects are locked at writer level.\n\n**Retired sister-era brass carving:** the small brass carving hidden in Solomon's blue drawer in Vancouver is the same old regulatory piece visible in the scratched photograph from the period when Solomon and his sister worked together. It belonged to their shared work, not to a separate personal-magic system. After the catastrophe it was retired from active use. Solomon kept it and later carried it to Canada as a private material memento of his sister, their partnership, and his failure.\n\n**Active replacement brass talisman:** after his sister restored equilibrium and died, Solomon rebuilt/stabilized the procedural side and installed a later replacement talisman in the regulator. This is the active brass talisman Kai removes in Sequence 6. Its removal destabilizes the regulator because it is a functioning regulatory component. It does not contain the Entity.\n\nThe two pieces share regulatory design language but are intentionally not identical. The screenplay must preserve their distinct custody and function. Current characters do not yet know the complete relationship.\n\nSee `docs/BRASS_OBJECT_CONTINUITY.md`.\n\n## The Entity"""
replace_once('00_CANON.md', canon_shrine_anchor, canon_shrine_block)
old_obj = """### Brass talisman\n\n- removed by Kai from the regulator;\n- disclosed in Sequence 9;\n- remains under ordinary cloth in the house;\n- not returned or used as a magical solution.\n"""
new_obj = """### Retired sister-era brass carving\n\n- discovered by Kai in Solomon's blue drawer in Vancouver;\n- same old regulatory component visible in the scratched Calabar photograph;\n- dates to the period when Solomon and his sister worked together;\n- retired from active regulatory use after the catastrophe;\n- carried to Canada and kept privately by Solomon;\n- functions emotionally as a material memento of his sister/shared work/failure, not as a personal magical amulet;\n- current characters have not yet established this full history on-page.\n\n### Active replacement brass talisman\n\n- installed by Solomon during post-catastrophe procedural rebuilding/stabilization after his sister's death;\n- distinct from, but visually related to, the retired sister-era carving;\n- removed by Kai from the regulator in Sequence 6;\n- disclosed in Sequence 9;\n- remains under ordinary cloth in the house;\n- not returned or used as a magical solution;\n- removal destabilized the regulator because this was the active regulatory component, not because it contained the Entity.\n"""
replace_once('00_CANON.md', old_obj, new_obj)
insert_after('00_CANON.md', '- a repair procedure;\n', '- the full historical relationship between Solomon\'s retired brass carving and the active replacement talisman;\n')
insert_after('00_CANON.md', '- Ade has no supernatural office;\n', '- the brass carving Solomon kept in Canada is the retired sister-era regulatory component, while the shrine talisman Kai removed is Solomon\'s later active replacement;\n')

# 3) Current continuity/object custody.
old_cont_obj = """### Brass talisman\n\n- removed intentionally by Kai from the regulator;\n- disclosed in Sequence 9;\n- remains under ordinary clean cloth in the house;\n- has not been returned or used as a magical solution.\n"""
new_cont_obj = """### Retired sister-era brass carving\n\n- found by Kai in Solomon's blue drawer in Vancouver;\n- same old regulatory component visible in the scratched photograph from Solomon/Bode/sister youth;\n- writer-level date/function: part of the regulator architecture from the era when Solomon and his sister worked together;\n- retired after the catastrophic rupture and sister's death;\n- later carried to Canada and privately preserved by Solomon;\n- emotional function: material memento of sister, partnership, and failure;\n- not a personal magical amulet and not the currently active regulator talisman;\n- full relationship remains unrevealed to the brothers.\n\n### Active replacement brass talisman\n\n- installed by Solomon as part of post-catastrophe procedural rebuilding/stabilization;\n- visually related to but physically distinct from the older carving;\n- removed intentionally by Kai from the regulator;\n- disclosed in Sequence 9;\n- remains under ordinary clean cloth in the house;\n- has not been returned or used as a magical solution;\n- removal destabilized an active regulator component; it did not release or contain the Entity.\n"""
replace_once('docs/CURRENT_CONTINUITY.md', old_cont_obj, new_cont_obj)
insert_after('docs/CURRENT_CONTINUITY.md', '- a complete repair procedure;\n', '- the replacement history connecting Solomon\'s Vancouver brass carving to the active shrine talisman;\n')
insert_after('docs/CURRENT_CONTINUITY.md', '- Ade has no supernatural office;\n', '- Solomon kept the retired sister-era brass component in Canada while the regulator used a later replacement talisman;\n')

# 4) Character authority.
solomon_anchor = "Afterward he became obsessive, maintained his procedural side meticulously, studied his sister's perceptual records, tried to compensate for her missing function, and increasingly isolated himself.\n\nTrue failure:"
solomon_new = """Afterward he became obsessive, maintained his procedural side meticulously, studied his sister's perceptual records, tried to compensate for her missing function, and increasingly isolated himself.\n\n### Brass continuity after the catastrophe\n\nThe brass carving later hidden in Solomon's Vancouver blue drawer is a retired regulatory component from the period when he and his sister worked together. After the catastrophic rupture and her death, Solomon retired that older piece and installed a new active brass talisman as part of rebuilding/stabilizing his procedural side. The new talisman is the one Kai removes from the shrine.\n\nSolomon kept the retired piece and carried it to Canada. It is a material memento of his sister, their partnership, and his own failure — exactly the kind of grief object Solomon would preserve without explaining. It is not the sister's personal magical amulet and does not contain her.\n\nTrue failure:"""
replace_once('docs/CHARACTER_CANON.md', solomon_anchor, solomon_new)
sister_anchor = "Relationship with Solomon:\n\nComplementary partner, not rival successor.\n\nDeath canon:"
sister_new = """Relationship with Solomon:\n\nComplementary partner, not rival successor.\n\nBrass continuity:\n\nThe retired brass carving later kept by Solomon in Canada comes from the period of their shared stewardship work. It is evidence of the partnership that existed while she was alive, not proof that she personally owned a magical talisman. Solomon's later active shrine talisman is a replacement installed after her death.\n\nDeath canon:"""
replace_once('docs/CHARACTER_CANON.md', sister_anchor, sister_new)
insert_after('docs/CHARACTER_CANON.md', '- whether he will accept responsibility.\n', '- the historical relationship between the retired Vancouver brass carving and the active shrine talisman.\n')

# 5) Master development bible: backstory + motif.
bible_tragedy = "He became obsessive, maintained his side meticulously, studied his sister's records, tried to compensate for her missing role, isolated himself, and attempted both halves despite weaker perceptual aptitude.\n\nHis final failure was succession."
bible_tragedy_new = """He became obsessive, maintained his side meticulously, studied his sister's records, tried to compensate for her missing role, isolated himself, and attempted both halves despite weaker perceptual aptitude.\n\nAs part of the post-catastrophe procedural rebuild, Solomon retired the older brass component from the era of his partnership with his sister and installed a new active brass talisman in the regulator. He kept the retired piece and eventually carried it to Canada. It became a private material memento of his sister, their shared work, and the failure he could not release.\n\nHis final failure was succession."""
replace_once('02_MASTER_BIBLE.md', bible_tragedy, bible_tragedy_new)
replace_once('02_MASTER_BIBLE.md', '### Brass\n\nHandled continuity and regulatory material; never universal magic.', """### Brass\n\nHandled continuity and regulatory material; never universal magic.\n\nTwo specific brass objects must remain distinct:\n\n- the **retired sister-era carving** hidden in Solomon's Vancouver blue drawer, originating in the period when Solomon and his sister worked together and later kept by Solomon as a private memento of sister/partnership/failure;\n- the **active replacement talisman** installed by Solomon after the catastrophe as part of rebuilding/stabilizing the regulator and later removed by Kai.\n\nTheir related design language signals continuity of workmanship, not object identity. Neither object contains the Entity, and the retired carving is not the sister's personal magical amulet.\n\nSee `docs/BRASS_OBJECT_CONTINUITY.md`.""")

# 6) Motif ledger: global brass motif and object-specific sections.
old_brass_block = """## Brass\n\nMeaning:\n\n- continuity;\n- inheritance;\n- handled material;\n- human workmanship;\n- regulatory instrument only where function has been established.\n\nCanonical appearances:\n\n- brass objects in Solomon's Vancouver environment;\n- brass carving found in the blue drawer;\n- one brass urn carrying Solomon;\n- brass talisman inside the regulator;\n- brass wall hook at the red-corded household door;\n- brass-cleaning cloths and small brass markers in the maintenance room;\n- measured brass anchor points support the inner diagnostic cord array.\n\nRules:\n\n- brass is not automatically supernatural;\n- do not make every brass object a conduit;\n- object meaning comes from custody, handling, wear, placement, maintenance, and established function;\n- the talisman is part of the regulator, not a prison key;\n- patina, fingerprints, cleaning, correction, and repair may reveal labor without explaining mythology.\n"""
new_brass_block = """## Brass\n\nMeaning:\n\n- continuity;\n- inheritance;\n- handled material;\n- human workmanship;\n- grief preserved as an object rather than spoken;\n- regulatory instrument only where function has been established.\n\nCanonical appearances:\n\n- ordinary brass objects in Solomon's Vancouver environment;\n- **retired sister-era brass carving** found in the blue drawer — the same old regulatory piece visible in the scratched photograph, from the period when Solomon and his sister worked together;\n- one brass urn carrying Solomon;\n- **active replacement brass talisman** inside the regulator — installed by Solomon after the catastrophe and later removed by Kai;\n- brass wall hook at the red-corded household door;\n- brass-cleaning cloths and small brass markers in the maintenance room;\n- measured brass anchor points support the inner diagnostic cord array.\n\nRules:\n\n- brass is not automatically supernatural;\n- do not make every brass object a conduit;\n- the retired carving and active talisman are visually related but physically distinct generations of regulatory workmanship;\n- the retired carving is not the sister's personal magical amulet, soul vessel, or badge of office;\n- Solomon kept the retired carving as a private material memento of sister/partnership/failure;\n- the active talisman is part of the regulator, not a prison key;\n- Kai's removal of the active replacement contributed to destabilization because of function, not because the object contains the Entity;\n- object meaning comes from custody, handling, wear, placement, maintenance, and established function;\n- patina, fingerprints, cleaning, correction, and repair may reveal labor without explaining mythology.\n\nSee `docs/BRASS_OBJECT_CONTINUITY.md`.\n"""
replace_once('docs/MOTIF_LEDGER.md', old_brass_block, new_brass_block)
retired_section = """## The Retired Sister-Era Brass Carving\n\nMeaning:\n\n- Solomon's private material memory of his sister;\n- evidence of a working partnership that existed before the family erased her from speech and image;\n- continuity between old and replacement regulatory workmanship;\n- grief converted into custody rather than confession.\n\nWriter-level history:\n\n- used as part of the regulatory architecture during the era when Solomon and his sister worked together;\n- visible in the old Calabar photograph;\n- retired after the catastrophic rupture and sister's death;\n- carried to Canada and hidden by Solomon in the blue drawer;\n- discovered by Kai in Sequence 1 before Kai knows what it means.\n\nRules:\n\n- not the active shrine talisman;\n- not the sister's private magical jewelry;\n- not a vessel for her spirit;\n- not a repair shortcut;\n- full history remains deferred on-page until earned by evidence.\n\n"""
insert_after('docs/MOTIF_LEDGER.md', '## The Brass Talisman\n', retired_section + '## The Active Replacement Brass Talisman\n')
# The insertion above leaves the original heading after the inserted text only if replacement is wrong; normalize exact duplicate.
text = read('docs/MOTIF_LEDGER.md')
text = text.replace('## The Brass Talisman\n## The Retired Sister-Era Brass Carving', '## The Retired Sister-Era Brass Carving', 1)
write('docs/MOTIF_LEDGER.md', text)
replace_once('docs/MOTIF_LEDGER.md', "Meaning:\n\n- regulatory instrument;\n- inheritance handled without understanding;\n- difference between seeing, taking, and accepting responsibility.\n\nCurrent custody:", """Meaning:\n\n- Solomon-era replacement regulatory instrument;\n- inheritance handled without understanding;\n- difference between seeing, taking, and accepting responsibility.\n\nWriter-level history:\n\n- installed by Solomon after his sister's death during post-catastrophe procedural rebuilding/stabilization;\n- visually related to, but not identical with, the retired sister-era carving;\n- active in the regulator until Kai removes it.\n\nCurrent custody:""")

# 7) Project manifest authority/laws.
replace_once('PROJECT_MANIFEST.yaml', 'version: 4.3', 'version: 4.4')
insert_after('PROJECT_MANIFEST.yaml', '      - docs/REGULATOR_CORD_ARRAY.md\n', '      - docs/BRASS_OBJECT_CONTINUITY.md\n')
# Add to canonical decision list as well, only first decisions block occurrence after canonical_sources.
text = read('PROJECT_MANIFEST.yaml')
needle = '    - docs/REGULATOR_CORD_ARRAY.md\n    - docs/DECISION_LOG.md\n'
if text.count(needle) != 1:
    raise SystemExit(f'PROJECT_MANIFEST.yaml canonical decisions anchor count={text.count(needle)}')
text = text.replace(needle, '    - docs/REGULATOR_CORD_ARRAY.md\n    - docs/BRASS_OBJECT_CONTINUITY.md\n    - docs/DECISION_LOG.md\n', 1)
write('PROJECT_MANIFEST.yaml', text)
insert_after('PROJECT_MANIFEST.yaml', '  - "Shrine = regulator/alignment point, never prison."\n', '  - "Two related brass objects are distinct: Solomon kept the retired sister-era regulatory carving; the shrine used a later active replacement talisman."\n  - "The retired brass carving is a material memento of sister/partnership/failure, not the sister\'s personal magical amulet or a soul vessel."\n  - "Kai removed Solomon\'s post-catastrophe replacement talisman; its active regulatory function, not containment, makes the removal consequential."\n')

# 8) Decision log: newest locked decision at top.
decision_anchor = "Older decisions remain historical when superseded and must not silently return.\n\n---\n"
decision_block = """Older decisions remain historical when superseded and must not silently return.\n\n---\n\nDATE:\n2026-08-17\n\nTITLE:\nTwo Brass Objects — Sister-Era Retired Component + Solomon-Era Active Replacement\n\nDECISION:\nThe brass carving found by Kai in Solomon's blue drawer in Vancouver and the brass talisman Kai later removes from the regulator are **two distinct, historically related objects**.\n\nThe Vancouver carving is the retired regulatory component visible in the old scratched Calabar photograph from the period when Solomon and his sister still worked together. It belonged to their shared stewardship system. It was not the sister's personal magical amulet, soul vessel, or hereditary badge.\n\nAfter Solomon's procedural failure destabilized the boundary and his sister restored equilibrium and died, Solomon rebuilt/stabilized the procedural side of the regulator. He retired the older sister-era brass component and installed a new active brass talisman. The talisman removed by Kai in Sequence 6 is this Solomon-era replacement.\n\nSolomon kept the retired brass piece, later carried it to Canada, and privately preserved it as a material memento of his sister, their partnership, and his own failure. This emotional significance does not create a separate magical function.\n\nThe two objects share regulatory design language but are intentionally not identical. Existing screenplay differences in angle/hollow/center treatment support this generational relationship. `BRASS` in Solomon's records remains a category of material/work and must not automatically be interpreted as either one specific object.\n\nThis is writer-level canon. The brothers do not yet know the complete replacement history, and the screenplay must earn the reveal through evidence rather than immediate exposition.\n\nSTATUS:\nLOCKED / FOUNDATIONAL OBJECT + SOLOMON BACKSTORY CANON\n\nCLARIFIES:\n- why the page-one brass carving matters;\n- why the old photograph and shrine talisman visually rhyme without being identical;\n- what Solomon carried to Canada from the sister era;\n- why Kai's removal of the shrine talisman destabilizes the regulator;\n- why returning either brass object alone cannot be assumed to repair the breach.\n\nSUPERSEDES:\nAny interpretation treating the Vancouver carving and shrine talisman as the same physical object, the sister's personal magical amulet, a soul vessel, or an Entity-containment key.\n\n---\n"""
replace_once('docs/DECISION_LOG.md', decision_anchor, decision_block)

# 9) Dedicated authority document.
brass_doc = """# EKPO — BRASS OBJECT CONTINUITY\n\nStatus: LOCKED / ACTIVE OBJECT AUTHORITY\nEffective: 2026-08-17\nAuthority: explicit creator canon\n\n## Purpose\n\nThis document prevents the two major brass objects from collapsing into one continuity object or mutating into a separate magic system.\n\n## Locked distinction\n\nEKPO contains two historically related but physically distinct regulatory brass objects.\n\n### A. Retired sister-era brass carving\n\nCurrent screenplay appearance:\n\n- discovered by Kai in Solomon's blue drawer in Vancouver in Sequence 1;\n- visible by silhouette in the scratched Calabar photograph showing young Solomon, Bode, and their sister;\n- later compared by Kai against Oku boundary/regulator design language.\n\nWriter-level history:\n\n- originated in the regulatory architecture during the period when Solomon and his sister performed complementary stewardship together;\n- belonged to their shared work rather than to the sister personally;\n- was retired from active regulatory use after the catastrophic rupture in which Solomon failed his procedural side and his sister restored equilibrium and died;\n- remained in Solomon's custody;\n- was eventually carried by Solomon to Canada and hidden among ordinary household remnants.\n\nEmotional function:\n\nThe carving is Solomon's material memento of:\n\n- his sister;\n- their functioning partnership;\n- the regulator as it existed while she was alive;\n- the failure he spent the rest of his life trying to compensate for.\n\nThis is consistent with Solomon's psychology: he preserves grief as objects, records, maintenance, and custody rather than speaking it plainly.\n\nProhibitions:\n\n- not the active talisman Kai removes;\n- not the sister's personal magical amulet;\n- not a soul vessel;\n- not a hereditary badge of office;\n- not a prison key;\n- not a complete repair component by itself.\n\n### B. Active Solomon-era replacement brass talisman\n\nCurrent screenplay appearance:\n\n- sits inside the hidden regulator in Sequence 6;\n- carries related three-line design language with a different center/hollow treatment;\n- is deliberately removed by Kai;\n- is disclosed to the family in Sequence 9;\n- remains under ordinary clean cloth in the Oku house.\n\nWriter-level history:\n\nAfter the catastrophic rupture and the sister's death, Solomon rebuilt/stabilized the procedural side of the regulator. During that post-catastrophe work, he installed a new active brass talisman to replace the retired sister-era component.\n\nFunction:\n\n- active regulatory component;\n- part of the maintained physical alignment system;\n- removal contributes directly to regulator destabilization.\n\nProhibitions:\n\n- does not contain the Entity;\n- is not the Entity's prison key;\n- is not a weapon;\n- is not a battery;\n- cannot be assumed to repair the breach merely by being put back.\n\n## Why the two objects resemble one another\n\nThey belong to the same regulatory tradition/system and therefore share design language. They are not duplicates. Existing screenplay distinctions are intentional evidence of generations of workmanship:\n\n- related three-line motif;\n- differing angles;\n- differing hollow/center treatment;\n- different wear and custody histories.\n\nThe relationship should feel like an old component and its later replacement, not two magical collectibles.\n\n## Reveal control\n\nThe full relationship is **writer-level canon only** at the current screenplay position.\n\nThe brothers presently have enough evidence to notice that the objects rhyme, but not enough to know:\n\n- which came first;\n- that the Vancouver carving was retired after the sister-era catastrophe;\n- that Solomon installed the active replacement afterward;\n- why Solomon took the retired piece to Canada;\n- that he kept it as a memento of his sister/shared work/failure.\n\nThe reveal must be earned materially through one or more of:\n\n- dated records;\n- replacement notation;\n- measurements;\n- wear/fit differences;\n- old photographs;\n- Solomon's travel/maintenance history;\n- a credible physical comparison.\n\nDo not solve it through an unearned Bode exposition speech.\n\n## `BRASS` ledger rule\n\n`BRASS` in Solomon's procedural index is a **material/work category**, not automatically the name of the active talisman. It may include:\n\n- talisman inspection;\n- markers;\n- anchor points;\n- fittings;\n- cleaning;\n- replacement pieces;\n- other brass regulatory hardware already supported by the maintenance room.\n\nSequence 14 may therefore treat `BRASS` as unresolved until the records identify the specific object or task.\n\n## Dramatic payoff\n\nThe page-one carving gains retrospective emotional force without changing its early behavior. Kai unknowingly holds a physical remnant of the partnership Solomon lost before he ever sees the active replacement in the regulator.\n\nThat connection should deepen Solomon rather than turn him into a posthumous puzzle-master. He kept the old piece because he could not discard what it represented, while still failing to tell his sons the truth.\n\n## Anti-drift laws\n\n- Never merge the two brass objects into one physical object.\n- Never call the retired carving the sister's magical amulet.\n- Never imply her spirit inhabits it.\n- Never make all brass supernatural.\n- Never use either object as a one-step repair solution.\n- Never make Kai's original discovery proof that Solomon planned Kai's breach.\n- Never reveal the complete history before the dramatic evidence earns it.\n\n## Current custody\n\nRetired sister-era carving: Solomon's Vancouver effects / brought into the brothers' investigation through the original estate materials; exact immediate physical location should remain tracked when next handled on-page.\n\nActive replacement talisman: Oku house, under ordinary clean cloth following Sequence 9; not returned to the regulator.\n"""
write('docs/BRASS_OBJECT_CONTINUITY.md', brass_doc)

# 10) Sanity: screenplay/PDF are unchanged by a writer-level canon sync.
if sha256('01_SCREENPLAY.fountain') != screenplay_before:
    raise SystemExit('01_SCREENPLAY.fountain changed during writer-level canon sync')
if sha256('output/pdf/EKPO_Screenplay.pdf') != pdf_before:
    raise SystemExit('output/pdf/EKPO_Screenplay.pdf changed during writer-level canon sync')

# 11) Validate required canon statements and anti-drift constraints.
required = {
    'EKPO_Canonical_Mythology_Refactor.md': [
        'Retired sister-era brass carving',
        'Active replacement brass talisman',
        'private memento',
        'writer-level canon, not current character knowledge',
    ],
    '00_CANON.md': [
        '## Brass object continuity',
        'Retired sister-era brass carving',
        'Active replacement brass talisman',
        'docs/BRASS_OBJECT_CONTINUITY.md',
    ],
    'docs/CURRENT_CONTINUITY.md': [
        '### Retired sister-era brass carving',
        '### Active replacement brass talisman',
    ],
    'docs/CHARACTER_CANON.md': [
        '### Brass continuity after the catastrophe',
        'material memento of his sister',
    ],
    '02_MASTER_BIBLE.md': [
        'retired sister-era carving',
        'active replacement talisman',
    ],
    'docs/MOTIF_LEDGER.md': [
        '## The Retired Sister-Era Brass Carving',
        '## The Active Replacement Brass Talisman',
    ],
    'PROJECT_MANIFEST.yaml': [
        'docs/BRASS_OBJECT_CONTINUITY.md',
        'Two related brass objects are distinct',
    ],
    'docs/DECISION_LOG.md': [
        'Two Brass Objects — Sister-Era Retired Component + Solomon-Era Active Replacement',
        'LOCKED / FOUNDATIONAL OBJECT + SOLOMON BACKSTORY CANON',
    ],
    'docs/BRASS_OBJECT_CONTINUITY.md': [
        'Never merge the two brass objects into one physical object.',
        '`BRASS` in Solomon\'s procedural index is a **material/work category**',
    ],
}
for path, needles in required.items():
    text = read(path)
    for needle in needles:
        if needle not in text:
            raise SystemExit(f'{path}: missing required canon text: {needle!r}')

# The executed screenplay already establishes distinct objects and related-but-not-identical design.
sp = read('01_SCREENPLAY.fountain')
for needle in [
    'A small BRASS CARVING.',
    'Inside: A BRASS TALISMAN.',
    'The angles differ. Both hollows sit slightly off-center.',
]:
    if needle not in sp:
        raise SystemExit(f'screenplay support line missing: {needle!r}')

print('BRASS OBJECT CANON SYNC PASS')
print('screenplay_sha256', screenplay_before)
print('pdf_sha256', pdf_before)
