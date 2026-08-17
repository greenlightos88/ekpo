from pathlib import Path

p = Path('01_SCREENPLAY.fountain')
s = p.read_text(encoding='utf-8')
old = '''Eno watches the unfinished interval.

ENO
After she died, Solomon stopped letting anybody down here.'''
new = '''Eno watches the boys take in the room.

ENO
After she died, Solomon stopped letting anybody down here.'''
if s.count(old) != 1:
    raise SystemExit(f'expected one stale interval beat, found {s.count(old)}')
s = s.replace(old, new, 1)
if 'unfinished interval' in s.lower():
    raise SystemExit('stale unfinished interval language remains')
p.write_text(s, encoding='utf-8')
print('Sequence 10 stale interval beat fixed')