from pathlib import Path

replacements = {
    '00_CANON.md': [
        ('the prior moving-fastener / `one turn short` beat is removed from canon;', 'the prior moving-fastener endpoint is removed from canon;'),
    ],
    'README.md': [
        ('Moving-fastener / `one turn short` material is superseded and removed.', 'The prior moving-fastener endpoint is superseded and removed.'),
    ],
    'docs/SEQUENCE_12_LOCK.md': [
        ('- `one turn short` as a supernatural clue;', '- the former fastener-state clue;'),
    ],
}

for path, pairs in replacements.items():
    p=Path(path)
    s=p.read_text(encoding='utf-8')
    for old,new in pairs:
        if old not in s:
            raise SystemExit(f'{path}: expected active-language source not found: {old}')
        s=s.replace(old,new,1)
    p.write_text(s,encoding='utf-8')

print('active fastener language cleaned')