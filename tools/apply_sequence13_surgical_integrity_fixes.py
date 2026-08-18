from pathlib import Path

p = Path('01_SCREENPLAY.fountain')
s = p.read_text(encoding='utf-8')

replacements = [
    (
'''Ade watches a woman count money into a vendor's palm.

STUTTER.

The exchange jumps ahead -- the notes already in the vendor's hand.

STUTTER.

The same notes are back between her fingers, completing the motion again.

The woman never breaks rhythm.

Ade does.

His face empties.

The market has too many bodies to verify one at a time.''',
'''Ade watches a woman count money into a vendor's palm.

STUTTER.

For Ade, the exchange is already finished -- the notes in the vendor's hand.

STUTTER.

His vision catches the release again -- the same notes leaving her fingers.

The woman never breaks rhythm.

Ade does.

His face empties.

The market has too many bodies to verify one at a time.''',
        'subjective money stutter'
    ),
    (
'''Between two moving bodies --

STUTTER.

The Entity is there.

Not wearing a mask.

Not part of the procession.

The real performers continue around it without recognition.

STUTTER.

Gone.''',
'''Between two moving bodies --

STUTTER.

The Entity resolves in the gap between them.

Not wearing a mask.

Not part of the procession.

The performers cross the same patch of lane. Nothing in their movement acknowledges what Ade sees.

STUTTER.

Gone.''',
        'remove objective occupied-coordinate implication'
    ),
    (
'''Bode cuts through a narrow lane between fabric stalls and a row of locked metal shutters.

Malik keeps one hand on Kai's shoulder.

Ade keeps hold of Malik's wrist until there is room to walk side by side.

Nobody runs.

Their bodies want to.

The market noise changes behind them by ordinary distance.

The metallic taste remains.

Ten steps.

Fifteen.

Kai's hand tremor begins to ease.

Ade's doubled drumbeat becomes one rhythm again.

Malik takes a breath without checking it first.''',
'''Bode cuts through a narrow lane between fabric stalls and a row of locked metal shutters.

Malik keeps one hand on Kai's shoulder.

Ade keeps hold of Malik's wrist until there is room to walk side by side.

Nobody runs.

Their bodies want to.

Kai starts to turn toward the drums.

Malik's hand tightens on his shoulder.

Kai stops himself.

Ade hears another beat behind them.

He keeps his eyes forward.

They round the shutters. The procession drops out of sight.

The market noise continues behind them.

The metallic taste remains.

For several steps, nothing improves.

Then Kai's hand tremor begins to ease.

Ade's doubled drumbeat becomes one rhythm again.

Malik takes a breath without checking it first.''',
        'break attention before symptom release'
    ),
]

for old, new, label in replacements:
    count = s.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly one source match, found {count}')
    s = s.replace(old, new, 1)

# Guard against accidental power inflation or distance-as-mechanism remnants.
for forbidden in [
    'The real performers continue around it without recognition.',
    'The exchange jumps ahead -- the notes already in the vendor\'s hand.',
    'Ten steps.\n\nFifteen.\n\nKai\'s hand tremor begins to ease.',
]:
    if forbidden in s:
        raise SystemExit('forbidden legacy market beat remains: ' + forbidden)

required = [
    'For Ade, the exchange is already finished -- the notes in the vendor\'s hand.',
    'Nothing in their movement acknowledges what Ade sees.',
    'Kai starts to turn toward the drums.',
    'He keeps his eyes forward.',
    'For several steps, nothing improves.',
]
for phrase in required:
    if phrase not in s:
        raise SystemExit('missing required surgical correction: ' + phrase)

p.write_text(s, encoding='utf-8')
print('Sequence 13 surgical integrity fixes applied')