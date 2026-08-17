from pathlib import Path
import re

p = Path('01_SCREENPLAY.fountain')
s = p.read_text(encoding='utf-8')

# Draft identity.
s = s.replace('Draft date: August 13, 2026', 'Draft date: August 17, 2026', 1)

# Human-read page 6 ambiguity.
old = "Ade takes the garment bags from him. For one brief moment, Malik has nothing in his hands. He looks toward the staircase. The three brothers follow his gaze. The landing is empty. Solomon's bedroom door stands open."
new = "Ade takes the garment bags from him. For one brief moment, Malik has nothing in his hands. He looks toward the staircase. Ade and Kai follow his gaze. The landing is empty. Solomon's bedroom door stands open."
if old not in s:
    raise SystemExit('Page-6 gaze source not found')
s = s.replace(old, new, 1)

# Seed stable house geography when the audience first enters the Oku house.
old = '''INT. OKU FAMILY HOUSE - FRONT ROOM - MOMENTS LATER

The front room carries several generations without arranging them for visitors. Family portraits. School certificates. A charging station crowded with phones.

An old cabinet of carved wood beneath a flat-screen television. The brass urn is placed on a sturdy side table. Malik checks the surface first. Solid. Level. Eno watches him test it.

ENO
If the table survived this family, it
can hold your father.

Malik removes his hand. Children peer through the doorway. Eno turns.

ENO
Give them air.

They disappear. Not far.

Beyond them, at the end of the passage, a narrow door is secured by a faded RED CORD looped between its handle and a brass wall hook. It is the only door in the house that does not stand open.

Kai notices. Eno notices him noticing.

Eyo crosses the passage with folded bedding. The door disappears behind ordinary work.'''
new = '''INT. OKU FAMILY HOUSE - FRONT ROOM - MOMENTS LATER

The front room carries several generations without arranging them for visitors. Family portraits. School certificates. A charging station crowded with phones.

An old cabinet of carved wood beneath a flat-screen television. Wide doors open onto the veranda and the courtyard beyond.

The kitchen has its own door onto that same courtyard. Between the kitchen wall and the older rear rooms, a narrow BACK PASSAGE runs deeper into the house and drops three shallow steps below the main floor.

The brass urn is placed on a sturdy side table. Malik checks the surface first. Solid. Level. Eno watches him test it.

ENO
If the table survived this family, it
can hold your father.

Malik removes his hand. Children peer through the doorway. Eno turns.

ENO
Give them air.

They disappear. Not far.

At the far end of the back passage, a narrow door is secured by a faded RED CORD looped between its handle and a brass wall hook. It is the only door in the house that does not stand open.

Kai notices. Eno notices him noticing.

Eyo crosses the mouth of the back passage with folded bedding. For a moment he blocks Kai's view. When he clears it, the red-corded door is still there.'''
if old not in s:
    raise SystemExit('Sequence 5 geography source not found')
s = s.replace(old, new, 1)

# Replace Sequence 10 with the same dramatic reveal, now spatially coherent and with
# the diagnostic cord array embedded as part of Solomon's existing system.
seq10_start = s.index('# SEQUENCE 10 - THE TWO RECORDS')
seq11_start = s.index('# SEQUENCE 11 - WHAT HE LEFT')
seq10 = '''# SEQUENCE 10 - THE TWO RECORDS

FADE IN:

INT. OKU FAMILY HOUSE - BACK PASSAGE - MORNING

Courtyard daylight reaches only the first half of the passage.

Three shallow steps drop into the oldest part of the house. The RED-CORDED DOOR waits at the low end, away from the front rooms and out of sight from most of the courtyard.

Children argue somewhere at the front of the house.

A radio gives the weather.

Bode stands before the door with a small ring of household keys.

Malik, Ade and Kai behind him.

Eno arrives carrying nothing.

The brass talisman remains in the kitchen beneath the dishcloth.

Bode touches the cord.

A simple hitch between handle and brass wall hook.

Nothing like the worked binding at the shrine.

His fingers pause.

ENO
Bode.

He undoes it.

The door is unlocked.

He opens it.

Beyond it --

FOUR STONE STEPS descend beneath the rear of the house.

INT. OKU FAMILY HOUSE - MAINTENANCE ROOM - CONTINUOUS

Semi-underground.

Camphor.

Paper.

Machine oil.

High slatted windows sit near the ceiling, level with the yard outside. Feet can pass beyond them without anyone in the courtyard seeing into the room.

A long worktable beneath the windows.

A measuring line worn dark where fingers held it.

Brass cloths blackened at the folds.

Bundles of red cotton wrapped by weight and date.

A boundary map punctured and corrected until the western edge is nearly soft.

Malik stops at the table.

Kai does not enter as far.

At the opposite wall --

AN INNER DOOR.

Older wood inside newer plaster.

Pencil measurements climb the frame beside small brass markers.

Around it, the plaster nearly disappears beneath a FIELD OF RED CORD.

Short lengths fixed between measured brass points. Worked knots. Loose tails. Old cut ends pinned behind newer work. Hundreds visible at once; years of replacement layered deeply enough that counting them would be useless.

Some hang straight. Some hold slight tension. Some end exactly at pencil marks on the wall.

Nothing moves.

One lower interval remains unfinished: a pencil mark, an empty brass point, no cord.

The door is still.

Kai looks at Bode.

KAI
What's behind it?

BODE
I don't know.

Malik looks over.

BODE
Solomon never opened it for me.

Eno watches the unfinished interval.

ENO
After she died, I never saw it open again.

Bode looks at her.

Eno does not add anything.

Bode opens a cabinet.

Ledgers wrapped against humidity.

He places one on the table.

Malik opens it.

Narrow block letters.

Dates.

Measurements.

A ruled margin corrected where the pencil drifted.

WEST BINDING — REPLACED
RIVER +11 CM
BRASS — CLEAN

Malik's thumb stops beside a knot diagram.

MALIK
Dad.

Bode nods.

Malik turns pages.

A date from years after Solomon moved to Canada.

Then another.

He looks at Eno.

MALIK
He was here.

ENO
Yes.

On another shelf, Kai sees thinner cloth-bound notebooks.

He looks at Bode.

Bode does not move.

BODE
Hers.

Kai looks to Eno.

She nods once.

He takes one.

Curved handwriting.

No columns.

Kai finds a date.

Looks across at Malik's ledger.

KAI
Same day.

Malik turns the ledger toward him.

Solomon:

WEST BINDING — REPLACED
RIVER +11 CM
BRASS — CLEAN

The sister:

Insects stopped before the rain.

Below it:

Distance on the west path changed when I looked directly.

Kai reads the sentence twice.

Ade comes closer.

Kai turns several pages.

A later entry.

Tall form beyond the palm line.

One bend where a shoulder should be.

The next did not stay in the same place.

Kai stops.

His hand rises toward the back of his neck.

He catches it halfway.

Malik sees.

No one speaks.

Kai turns the page.

Then another.

The handwriting stops halfway down one sheet.

The rest of the notebook is blank.

Malik looks back to Solomon's ledger.

The dates continue.

Page after page.

Then, months later, beneath a column of measurements:

DISTANCE UNCERTAIN.
RE-MEASURE.

Malik reads it without moving his lips.

Across the table, Kai still holds the open notebook.

Ade reaches between them.

He rotates Solomon's ledger until both books face the same direction.

Same table.

Same light.

Malik's hand remains beside Solomon's knot diagram.

Kai's beside the line about the tall form.

Ade looks from one brother to the other.

Behind them, the inner door remains closed.

The cord field around it hangs completely still.

One lower interval remains unfinished.

CUT TO BLACK.

'''
s = s[:seq10_start] + seq10 + s[seq11_start:]

# Sequence 11 should preserve the stable baseline, not foreshadow a moving fastener.
old = '''Kai looks toward the inner door.

The loose brass fastener remains on the sill.

Exactly where it was.

He leaves it there.'''
new = '''Kai looks toward the inner door.

The field of red cords hangs completely still.

One lower interval remains unfinished.

He leaves it alone.'''
if old not in s:
    raise SystemExit('Sequence 11 fastener source not found')
s = s.replace(old, new, 1)

# Rebuild Sequence 12 from coherent geography and carry into the marketplace sequence.
seq12_start = s.index('# SEQUENCE 12 - WHEN IT STAYS')
seq12_13 = '''# SEQUENCE 12 - WHEN IT STAYS

EXT. OKU FAMILY HOUSE - COURTYARD - NIGHT

The courtyard is the house's shared center.

On one side: the front veranda and family room, television bright inside.

On another: the kitchen door.

Between the kitchen wall and the older rear rooms, the BACK PASSAGE drops three shallow steps into the house toward the red-corded maintenance-room door.

Across the open yard, the compound gate leads away from the house.

No one is near the back passage tonight.

Dinner aftermath.

Plastic chairs.

Children underfoot.

A football match on television draws periodic SHOUTS from the front room.

Generator vibration beneath everything.

Mosquitoes worry bare ankles.

Eno directs plates from one hand to another without appearing to move.

Ade dries dishes beside the kitchen door.

ADE
I crossed an ocean to become unpaid labor.

ENO
Then work. Nobody invited you to stand there.

Ade goes back to the towel.

Kai sits in the courtyard with his camera resting in his lap.

He is not looking through it.

A LITTLE GIRL, six, draws on the back of an old church program beside him.

She shows him a house with five windows.

LITTLE GIRL
This one is yours.

KAI
Why is mine small?

LITTLE GIRL
You are far.

Kai smiles.

Then --

METAL in his mouth.

He swallows.

It gets stronger.

His fingers tighten around the camera.

Across the courtyard, Malik sees his face change.

MALIK
Kai?

Kai looks at him.

KAI
Don't --

Pressure seals his ears.

The football crowd stretches into a thin electrical whine.

Then -- nothing.

The television still plays.

Men inside still react.

A cheer reaches Kai after the players have already reset.

He stands.

His body pitches hard left.

The courtyard does not.

He catches the chair.

Malik is already moving.

MALIK
Look at me.

Kai tries.

Malik's face will not become one face.

Two images overlap by half an inch.

Separate.

Rejoin.

KAI
It's here.

Ade sets the plate down.

The LITTLE GIRL looks up.

LITTLE GIRL
What is?

Ade crouches.

ADE
Your uncle forgot dinner exists.

He gives her the dish towel.

ADE
Take this to Auntie Eno. Ask for biscuits before she changes her mind.

LITTLE GIRL
She didn't say yes.

ADE
That's why we move quickly.

The girl runs into the kitchen.

Ade rises.

His balance drops out from under him.

He catches the table.

His palm stops six inches before the edge his eyes insist is there.

He freezes.

ADE
Malik.

No joke now.

The GENERATOR HUM disappears.

The bulb above them burns steadily.

No mosquitoes circle it.

Kai looks toward the mouth of the back passage.

MALIK
No.

Kai doesn't turn.

MALIK
Kai. Me.

Kai tries.

The descending passage behind Malik is empty.

STUTTER.

Empty back passage.

And something impossibly tall inside it.

No transition between the two.

Kai's knees strike tile.

He never feels himself fall.

His camera cracks against the floor.

MALIK
Kai!

Malik lunges.

STUTTER.

He is already beside him.

Momentum arrives afterward and nearly throws him past Kai.

Malik tries to inhale.

Nothing starts.

His chest is ready.

His body does not remember the next step.

He forces air out.

Drags one breath in.

Again.

Again.

INT. OKU FAMILY HOUSE - MAINTENANCE ROOM - SAME

Empty.

The high slatted windows show only black yard beyond.

The field of red cord around the inner door hangs in stale air.

One measured row draws taut.

Three loose tails lift together by an inch.

A knot slips the width of a pencil mark.

Another row falls slack.

The inner door does not move.

EXT. OKU FAMILY HOUSE - COURTYARD - SAME

Ade takes one step toward his brothers.

His inner ear rotates the courtyard ninety degrees.

He drops to one hand.

A WOMAN carrying plates comes through the kitchen door and almost follows his line of sight toward the back passage.

Ade gets up before she can.

ADE
Kitchen. Please.

He takes the plates from her and turns her back toward the door.

She goes.

Kai is staring past Malik.

MALIK
Don't.

Kai's eyes flood.

A red capillary spreads across the white of his right eye.

STUTTER.

The Entity occupies the descending back passage.

Its height has nowhere to go.

One articulation folds beneath the ceiling.

Another begins behind plaster and finishes in open air.

STUTTER.

The arrangement changes.

The head occupies a position the neck cannot support.

STUTTER.

Closer.

No step.

Wood CREAKS somewhere down the back passage.

Dust lifts from the low ceiling --

hangs --

falls.

Kai's nose begins to bleed.

MALIK
Kai. Stop looking.

Kai tries to answer.

His tongue has gone numb.

KAI
I ca --

His mouth floods with saliva.

He turns and vomits onto the tile.

STUTTER.

A surface where a face might be tries to acquire depth.

STUTTER.

Almost human arrangement.

STUTTER.

Gone.

STUTTER.

There again.

The back-passage walls double.

The doorway doubles.

Malik doubles.

Kai doubles.

The Entity does not.

Ade sees enough.

A high tone drills through his ears.

Then --

LITTLE GIRL (O.S.)
Uncle Kai?

Ade turns.

The girl stands at the kitchen threshold with two biscuits.

LITTLE GIRL
Why did you call me?

Kai is on his knees vomiting.

His mouth is empty.

The girl starts to look past Ade toward the back passage.

ADE
Hey.

She looks at him.

ADE
Those are mine.

LITTLE GIRL
Auntie said one is his.

ADE
She lied.

The girl laughs.

Ade reaches her.

Blocks the back passage with his body.

Behind him --

STUTTER.

The girl's eyes move around his shoulder.

Ade lifts her.

ADE
Nope.

He takes one biscuit with his teeth.

ADE
Tax.

She protests into his shoulder as he carries her across the courtyard -- away from the back passage, toward the front veranda and the compound gate beyond.

Ade does not look back.

Blood begins running from his nose.

The girl touches his face.

LITTLE GIRL
You're bleeding.

ADE
I know.

At the back-passage mouth --

Malik grips Kai's face with both hands.

MALIK
Me.

Kai's eyes keep pulling sideways.

MALIK
Kai.

STUTTER.

Malik's hands are on him --

and Kai is six feet closer to the back passage.

STUTTER.

Back in Malik's hands.

Kai SCREAMS.

His right arm goes dead.

It drops against his body.

MALIK
Can you move it?

Kai tries.

Nothing.

Behind Malik --

one unresolved articulation occupies the same apparent space as Kai's shoulder.

No strike.

No impact.

Kai convulses.

Sensation returns all at once.

His fingers claw the tile.

Malik starts to turn.

KAI
DON'T.

Malik stops.

Inside the front room --

a chair scrapes.

Eno and Bode step onto the veranda.

Eyo behind them.

Their sightline crosses the courtyard toward Malik, Kai, and the mouth of the back passage beyond.

Ade reaches them carrying the girl.

ENO
Move.

Ade sets the girl into Eyo's arms and steps directly into Eno's line of sight.

ADE
Gas. Back of the house.

ENO
What?

ADE
Get everybody to the gate.

Eno sees the blood beneath his nose.

Looks once at Malik and Kai.

Then turns to the front room.

ENO
Eyo. Children first.

EYO
Come. Everybody move.

ENO
Gate. Now.

People spill from the front room onto the veranda and cross the courtyard toward the gate.

Nobody has to pass the back passage to leave.

A mother turns a child's face toward the gate.

The doubled edge of the back-passage mouth resolves to one.

Two men abandon the television and move after Eyo without looking back.

The wood down the passage releases with a soft tick.

The little girl disappears behind the gate pillar.

Malik's next breath begins before he forces it.

Kai's two images of the courtyard pull closer together.

INT. OKU FAMILY HOUSE - MAINTENANCE ROOM - SAME

The cord field eases.

Most rows settle toward their pencil marks.

Not all.

Two knots remain lower than the rows beside them.

One loose tail continues a small rotation after everything else is still.

The inner door remains closed.

EXT. OKU FAMILY HOUSE - COURTYARD - SAME

STUTTER.

Entity.

STUTTER.

Empty back passage.

STUTTER.

Something impossibly far beyond the descending steps.

Then --

nothing.

Sound SLAMS back.

Generator.

Television crowd inside an empty front room.

A baby crying near the gate.

Plates clattering.

Insects.

Malik flinches from ordinary sound.

Kai curls around his right arm.

Ade presses one hand to his ear.

He looks toward the gate.

Family clustered there.

Safe enough for this second.

Eno steps halfway back into the courtyard but stops well short of the back passage.

ENO
Bring him here.

Ade returns to Kai.

He gets under one side.

Malik takes the other.

The three brothers cross the courtyard together, away from the house, toward the gate.

EXT. OKU FAMILY COMPOUND - BY THE GATE - MOMENTS LATER

The family gives them room without being asked.

Eno takes in the three brothers.

Kai's bloodshot eye.

Malik breathing through his nose, counting without numbers.

Ade wiping blood from his lip.

The LITTLE GIRL looks at Ade.

LITTLE GIRL
I didn't smell gas.

Eno looks at Ade.

He does not explain.

ENO
Stay with Eyo.

The girl goes.

Eno looks back to the brothers.

ENO
Nobody goes near that back passage.

Then --

ENO
What happened?

No one answers.

Malik looks at Kai's hanging arm.

MALIK
Fingers.

Kai moves them.

Slow.

MALIK
Again.

Kai does.

The tremor remains.

Ade looks past them.

A BOY near the gate has leaned sideways, trying to see into the courtyard and toward the back passage.

Ade shifts one step.

Closes the sightline with his body.

Malik sees him do it.

Kai sees the boy.

Behind the brothers: the house.

In front of them: their family.

No one tells them where to stand.

They stay between the two.

CUT TO BLACK.

# SEQUENCE 13 - THE MARKET

FADE IN:

EXT. OKU FAMILY HOUSE - FRONT VERANDA - MORNING

Breakfast has moved outside.

Not ceremonially.

Nobody suggests taking plates deeper into the house.

Tea. Bread. Eggs. Fried plantain.

Conversation that starts and dies before becoming conversation.

The brothers look like men who slept without ever fully arriving at sleep.

Kai's right eye is webbed red. His right hand trembles when he lifts his cup.

His camera sits beside him. A crack runs through the casing from last night.

Malik inhales once through his nose before drinking, checking a sequence his body used to perform without permission.

Ade has cotton beneath one nostril. He removes it before a child can ask.

Eno sees all of it.

Bode eats quietly.

Eyo reaches for pepper.

The bowl is full.

Eno looks at it.

Then at the brothers.

ENO
Bode.

BODE
Hmm?

ENO
Market.

Bode looks at the full table.

BODE
For what?

ENO
Pepper. Tomatoes. Fish.

Eyo looks at the pepper bowl.

EYO
We have --

Eno looks at him.

EYO
We need pepper.

Ade almost smiles.

Eno points at the brothers with her chin.

ENO
Take them.

MALIK
We have work.

ENO
You have been looking at that passage since sunrise.

Malik does not deny it.

ENO
Go and look at pepper.

ADE
Medical advice has changed.

ENO
You are alive enough to complain. Good.

Kai looks toward the old house.

KAI
Crowds might be worse.

Malik looks at him.

MALIK
We don't know that.

ADE
We don't know staying here is better.

Bode wipes his hands.

BODE
We go. We come back.

He looks at all three.

BODE
Together.

Malik considers it.

Kai looks at his cracked camera.

His hand reaches toward it.

Stops.

He leaves it on the veranda.

CUT TO:

EXT. CALABAR MARKET - LATE MORNING

Bargaining.

Generators.

Fish smoke under corrugated shade.

Peppers piled in red and green mounds.

Fabric hanging above phone cases and plastic buckets.

A motorcycle horn trapped behind a handcart.

Two women argue over change and begin laughing before either one wins.

Bode moves through it without thinking about where his body should go.

The brothers do not.

Ade gets clipped by a basket and apologizes to the basket.

ADE
Sorry.

The WOMAN carrying it looks back.

WOMAN
Na basket you dey beg?

ADE
It looked offended.

She laughs and keeps moving.

Bode buys tomatoes.

A VENDOR adds one more than he asked for.

BODE
I said six.

VENDOR
This one small.

BODE
Then it should cost small.

The vendor waves him away, smiling.

For several minutes, nothing is wrong.

Malik carries two bags because nobody stopped him early enough.

Ade tastes a piece of fruit he did not intend to buy.

Kai reaches toward his chest when a burst of color crosses the lane.

No camera there.

His hand closes on his shirt instead.

Ahead --

DRUMS.

Not the earth-borne pressure from the shrine.

Real drums.

Human hands.

A MASQUERADE PROCESSION moves into the market lane with attendants and musicians.

Vendors make room without panic.

Children climb onto low walls.

People grin, call to one another, keep selling around the edges.

An attendant exchanges a familiar greeting with Bode as the procession approaches.

Bode answers and steps aside.

The brothers follow his lead.

Ade watches the movement.

For the first time this morning, some life reaches his face.

Kai watches too.

Then --

METAL.

Faint.

Back of his tongue.

His smile never arrives.

Malik sees him swallow.

MALIK
Kai.

Kai keeps his eyes on the ground between them.

KAI
I know.

Ade hears that.

The festive drums continue.

One strike reaches Ade twice.

The second arrives after the drummer's hand has already lifted for the next beat.

Ade presses two fingers beneath his ear.

BODE
What?

ADE
Nothing.

He knows it is not nothing.

The procession crosses their lane.

Bright movement fills the space between bodies.

For one instant, two masquerade figures overlap in Kai's peripheral vision.

Between them --

A VERTICAL INTERRUPTION where no performer stands.

Too tall for the awning.

Kai looks up before he can stop himself.

STUTTER.

Masquerade cloth crossing foreground.

Behind it, an articulation bends where the market lane has no room for it.

STUTTER.

Only stalls.

STUTTER.

The procession keeps its rhythm.

Something behind it does not.

Kai drops his gaze.

His right hand starts shaking harder.

KAI
Don't let me look.

Malik steps directly into his sightline.

Not touching him yet.

MALIK
Me.

Kai fixes on Malik.

A group of shoppers crosses between them.

For half a second Malik cannot see Kai.

They clear.

Kai is farther away than the space they crossed should allow.

Malik's diaphragm misses one automatic breath.

He catches Ade's sleeve.

MALIK
Kai.

Ade already sees him.

He takes Malik's wrist and keeps it.

ADE
Don't chase the gap.

Malik looks at him.

Ade points with his chin to Kai's actual body.

They move together.

The crowd continues around them.

Nobody screams.

Nobody else appears sick.

A woman counts money into a vendor's palm.

STUTTER.

The money is already in the other hand.

STUTTER.

Back between her fingers.

She notices nothing.

Ade does.

His face empties.

The market has too many bodies to verify one at a time.

Bode reaches Kai first.

BODE
Kai.

Kai looks at Bode's shirt, not his face.

BODE
What happened?

Kai cannot answer without looking past him.

He does not.

The procession moves farther down the lane.

The drums should be receding.

One beat lands inside Malik's chest at full volume.

He flinches.

Ade looks back despite himself.

Between two moving bodies --

STUTTER.

The Entity is there.

Not wearing a mask.

Not part of the procession.

The real performers continue around it without recognition.

STUTTER.

Gone.

ADE
Bode.

Bode looks at him.

ADE
Move us.

No explanation.

Bode does not ask for one.

He takes the shortest route he knows.

EXT. MARKET SIDE LANE - CONTINUOUS

Bode cuts through a narrow lane between fabric stalls and a row of locked metal shutters.

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

Malik takes a breath without checking it first.

They stop beneath the shade of a closed awning.

Bode looks at all three.

BODE
What did you see?

No one answers immediately.

Malik looks back toward the market entrance.

Then in the opposite direction -- toward where the house would be, far beyond buildings and traffic.

MALIK
We left the house.

Kai finally looks at him.

Ade releases Malik's wrist.

Behind them, the market keeps going.

CUT TO BLACK.
'''
s = s[:seq12_start] + seq12_13

# Hard source checks before writing.
required = [
    '# SEQUENCE 13 - THE MARKET',
    'Ade and Kai follow his gaze.',
    'FIELD OF RED CORD',
    'Nobody has to pass the back passage to leave.',
    'The inner door does not move.',
    'We left the house.',
]
for phrase in required:
    if phrase not in s:
        raise SystemExit('Missing revision: ' + phrase)

forbidden = [
    'The three brothers follow his gaze.',
    '\nENO\nCar.\n',
    'One turn short.',
    'The loose brass fastener remains on the sill.',
    'Return what was dislodged.',
]
for phrase in forbidden:
    if phrase.lower() in s.lower():
        raise SystemExit('Forbidden old material remains: ' + phrase)

heads = re.findall(r'^# SEQUENCE (\d+) - ', s, re.M)
if heads != [str(i) for i in range(1, 14)]:
    raise SystemExit('Sequence heading order failure: ' + repr(heads))

p.write_text(s, encoding='utf-8')
print('Human-audit screenplay revision applied')
