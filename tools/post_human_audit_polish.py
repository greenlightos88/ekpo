from pathlib import Path

# --- Screenplay surgical polish ---
p=Path('01_SCREENPLAY.fountain')
s=p.read_text(encoding='utf-8')

def exact(old,new,label):
    global s
    n=s.count(old)
    if n!=1:
        raise SystemExit(f'{label}: expected 1 match, found {n}')
    s=s.replace(old,new)

exact('''Some hang straight. Some hold slight tension. Some end exactly at pencil marks on the wall.

Nothing moves.

One lower interval remains unfinished: a pencil mark, an empty brass point, no cord.

The door is still.''','''Some hang straight. Some hold slight tension. Some end exactly at pencil marks on the wall.

Nothing moves.

The door is still.''','remove obvious missing-cord repair clue')

exact('''ENO
After she died, I never saw it open again.''','''ENO
After she died, Solomon stopped letting anybody down here.''','Eno inner-door knowledge boundary')

exact('''Behind them, the inner door remains closed.

The cord field around it hangs completely still.

One lower interval remains unfinished.''','''Behind them, the inner door remains closed.

The cord field around it hangs completely still.''','Sequence 10 ending repair clue')

exact('''She points through the open outer door toward the living house.''','''She points up the stone steps, toward the voices in the house.''','Sequence 11 geography')

exact('''Kai looks toward the inner door.

The field of red cords hangs completely still.

One lower interval remains unfinished.

He leaves it alone.''','''Kai looks toward the inner door.

The field of red cords hangs completely still.

He leaves it alone.''','Sequence 11 repair clue')

exact('''People spill from the front room onto the veranda and cross the courtyard toward the gate.

Nobody has to pass the back passage to leave.

A mother turns a child's face toward the gate.''','''People spill from the front room onto the veranda.

They cross the open courtyard toward the gate, leaving the mouth of the back passage behind them on the opposite side.

A mother turns a child's face toward the gate.''','Sequence 12 filmable evacuation geography')

exact('''ADE
Medical advice has changed.

ENO
You are alive enough to complain. Good.''','''ADE
That's your solution?

ENO
You are alive enough to complain. Good.''','Sequence 13 remove medical framing')

exact('''A woman counts money into a vendor's palm.

STUTTER.

The money is already in the other hand.

STUTTER.

Back between her fingers.

She notices nothing.

Ade does.''','''Ade watches a woman count money into a vendor's palm.

STUTTER.

The exchange jumps ahead -- the notes already in the vendor's hand.

STUTTER.

The same notes are back between her fingers, completing the motion again.

The woman never breaks rhythm.

Ade does.''','market stutter perceptual framing')

for forbidden in ['One lower interval remains unfinished','\nENO\nCar.\n','one turn short','The loose brass fastener remains on the sill.','Medical advice has changed.']:
    if forbidden.lower() in s.lower():
        raise SystemExit('screenplay legacy material remains: '+forbidden)

p.write_text(s,encoding='utf-8')

# --- Motif ledger synchronization ---
p=Path('docs/MOTIF_LEDGER.md')
m=p.read_text(encoding='utf-8')
m=m.replace('Last synchronized: 2026-08-13','Last synchronized: 2026-08-17',1)
m=m.replace('Canonical endpoint: End of Sequence 12 — `WHEN IT STAYS`','Revision-branch endpoint: End of Sequence 13 — `THE MARKET` (PR #3 candidate)',1)
m=m.replace('- the inner maintained door uses red-cord elements fixed at measured intervals.','- the inner maintained door is surrounded by a dense measured red-cord/knot diagnostic array;\n- Sequence 10 establishes that array completely still at baseline;\n- Sequence 12 objectively shows restrained tension/slack/alignment changes in the array under manifestation pressure while the inner door remains closed.',1)
m=m.replace('- never make it move by itself;\n- never imply any red string automatically performs magic;','- generic red cord never moves merely because it is red;\n- only the explicitly established inner diagnostic array may register pressure through restrained measurable tension/slack/alignment changes;\n- never imply any red string automatically performs magic;',1)
m=m.replace('- distinguish regulator binding, household closure, stored material, and inner-door maintenance;\n- a new knot, cut, opening, replacement, or unfinished section must change responsibility, consent, maintenance, or understanding.','- distinguish regulator binding, household closure, stored material, and the inner diagnostic array;\n- the diagnostic array must behave like material instrumentation, never sentient rope;\n- no writhing, reaching, levitation, or theatrical self-untying;\n- a new knot, cut, opening, or replacement must change responsibility, consent, maintenance, or understanding.',1)
m=m.replace('- unfinished inner-door point includes a brass fastener waiting beside a measured position.','- measured brass anchor points support the inner diagnostic cord array.',1)
m=m.replace('- inner maintained door/interface;\n- no occult spectacle;','- inner maintained door/interface;\n- dense measured cord/knot diagnostic array around the inner door;\n- semi-underground location beneath the rear of the house;\n- no occult spectacle;',1)
m=m.replace('- inner door combines measured red-cord placement with brass markers/unfinished point.','- inner door combines measured red-cord placement with brass markers in a dense diagnostic array.',1)
m=m.replace('- Sequence 8 makes naked attention itself dangerous: the presence becomes clearer/closer as Kai looks longer.','- Sequence 8 makes naked attention itself dangerous: the presence becomes clearer/closer as Kai looks longer;\n- Sequence 12 cracks the camera casing during the major manifestation;\n- Sequence 13 Kai deliberately leaves the damaged camera at the house before the market trip.',1)
if '## Masquerade / Public Cultural Performance' not in m:
    marker='## Sound\n'
    section='''## Masquerade / Public Cultural Performance\n\nMeaning:\n\n- ordinary living culture in Calabar;\n- public rhythm, continuity, recognition, and community life;\n- a visually dense human environment that the brothers may misperceive under Entity pressure without making the culture itself supernatural.\n\nRules:\n\n- the masquerade is never the Entity;\n- no performer is automatically possessed, cursed, or secretly monstrous;\n- the Entity may become perceptible in negative space around a procession while real performers continue as themselves;\n- do not invent restricted meanings, costume specifics, or ritual terminology before qualified Efik/Calabar cultural review;\n- public response should establish the event as belonging to the community, not as an omen staged for the Canadian brothers.\n\n'''
    if marker not in m: raise SystemExit('motif sound marker missing')
    m=m.replace(marker,section+marker,1)
p.write_text(m,encoding='utf-8')

# --- Entity physiology: portability without power inflation ---
p=Path('docs/ENTITY_HORROR_PHYSIOLOGY.md')
e=p.read_text(encoding='utf-8')
if '## Portability after reciprocal contact' not in e:
    e += '''\n\n## Portability after reciprocal contact\n\nAfter repeated reciprocal perception, physical distance from the Oku house does not automatically terminate Entity proximity. Sequence 13 may demonstrate renewed perceptual/physiological pressure in the Calabar market.\n\nThis does **not** establish that the Entity can freely teleport, control time, possess crowds, or follow every person indefinitely. Exact tether, range, and persistence remain unresolved.\n\nA crowd does not automatically strengthen manifestation merely by being nearby. The important pressure is directed awareness / attempted resolution of the Entity itself.\n\nMarket continuity errors experienced by the brothers must read as perceptual/local-coherence fracture from their point of view, not objective proof that uninvolved shoppers are being rewound or controlled.\n\nA public masquerade procession remains culturally normal and independent of the Entity. The Entity may become perceptible in negative space around it; no performer becomes supernatural merely because the brothers are under pressure.\n'''
p.write_text(e,encoding='utf-8')

print('post-human-audit polish applied')