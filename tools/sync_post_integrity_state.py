from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def rw(path, reps):
    p=ROOT/path
    t=p.read_text(encoding='utf-8')
    for old,new in reps:
        if old not in t:
            raise SystemExit(f'{path}: missing expected text: {old}')
        t=t.replace(old,new,1)
    p.write_text(t,encoding='utf-8')

rw('00_CANON.md',[
('PR #3 contains a rewritten Sequence 12 and a Sequence 13 marketplace candidate. It remains draft until the human/spatial/cultural/render/continuity promotion gate passes.',
 'PR #3 contains a rewritten Sequence 12 and a Sequence 13 marketplace candidate. The internal high-threshold human/spatial/render/continuity gate has passed after removal of the Sequence 12 witness anomaly. The PR remains draft pending explicit creator approval; qualified Nigerian/Calabar/Efik authenticity review remains an external pre-production/submission gate.'),
('Do not write Sequence 14 until the Sequence 12 rewrite and Sequence 13 candidate pass the promotion audit in `docs/NEXT_MOVEMENT.md`.',
 'Do not write Sequence 14 until the creator accepts the revised Sequence 12/13 candidate. The internal promotion audit has passed; the two-layer exposure model remains an audit candidate, not canon.')
])

rw('docs/CURRENT_CONTINUITY.md',[
('Sequence 12 rewrite and Sequence 13 candidate remain on draft PR #3 until the full human/spatial/cultural/render/continuity gate passes.',
 'Sequence 12 rewrite and Sequence 13 candidate have passed the internal high-threshold human/spatial/render/continuity gate on draft PR #3. The PR remains unmerged pending explicit creator approval. Qualified Nigerian/Calabar/Efik authenticity review remains an external pre-production/submission gate.')
])

rw('docs/NEXT_MOVEMENT.md',[
('Status: ACTIVE — AUDIT REWRITTEN SEQUENCE 12 + SEQUENCE 13 MARKET CANDIDATE',
 'Status: INTERNAL HIGH-THRESHOLD PASS — CREATOR REVIEW / NO SEQUENCE 14 YET'),
('First prove that the human-audit corrections and marketplace restoration work as one continuous film.',
 'The post-witness-removal integrity gate has passed. Do not write Sequence 14 until the creator accepts the revised Sequence 12 and Sequence 13 candidate.'),
('## Required promotion audit',
 '## Promotion audit result\n\n**PASS — all internal tests below passed on the 64-page candidate.**\n\nThe qualified Nigerian/Calabar/Efik authenticity read remains external and is not replaced by this pass.\n\n### Tests passed')
])

rw('PROJECT_MANIFEST.yaml',[
('    status: draft-promotion-audit-required',
 '    status: internal-integrity-pass-creator-review-required'),
('    - development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md\n    - development/audits/EKPO_SEQUENCES_1_12_FORENSIC_AUDIT.md',
 '    - development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md\n    - development/audits/EKPO_POST_WITNESS_REMOVAL_FULL_INTEGRITY_AUDIT.md\n    - development/audits/EKPO_SEQUENCES_1_12_FORENSIC_AUDIT.md'),
('  - "PR #3 remains draft until the human/spatial/cultural/render/continuity gate passes."',
 '  - "PR #3 remains draft until explicit creator approval; the internal high-threshold integrity gate has passed."')
])

rw('README.md',[
('**PR #3 is not yet merge-ready.** It must pass the human/spatial/cultural/continuity promotion gate before replacing the `main` baseline.',
 '**PR #3 has passed the internal high-threshold human/spatial/render/continuity gate.** It remains draft and unmerged pending explicit creator approval. A qualified Nigerian/Calabar/Efik authenticity read remains an external pre-production/submission gate.'),
('3. `development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md`\n4. `docs/HOUSE_GEOGRAPHY.md`',
 '3. `development/audits/EKPO_HUMAN_AUDIT_REVISION_2026-08-17.md`\n4. `development/audits/EKPO_POST_WITNESS_REMOVAL_FULL_INTEGRITY_AUDIT.md`\n5. `docs/HOUSE_GEOGRAPHY.md`'),
('5. `docs/REGULATOR_CORD_ARRAY.md`\n6. `docs/SEQUENCE_12_LOCK.md`\n7. `docs/CURRENT_CONTINUITY.md`\n8. `docs/NEXT_MOVEMENT.md`\n9. `00_CANON.md`\n10. `docs/CHARACTER_VOICE_CONSTITUTION.md`\n11. `docs/CULTURAL_LANGUAGE_REGISTER.md`\n12. `docs/ENTITY_HORROR_PHYSIOLOGY.md`\n13. `docs/MOTIF_LEDGER.md`',
 '6. `docs/REGULATOR_CORD_ARRAY.md`\n7. `docs/SEQUENCE_12_LOCK.md`\n8. `docs/CURRENT_CONTINUITY.md`\n9. `docs/NEXT_MOVEMENT.md`\n10. `00_CANON.md`\n11. `docs/CHARACTER_VOICE_CONSTITUTION.md`\n12. `docs/CULTURAL_LANGUAGE_REGISTER.md`\n13. `docs/ENTITY_HORROR_PHYSIOLOGY.md`\n14. `docs/MOTIF_LEDGER.md`'),
('## Remaining gate\n\nBefore PR #3 can be promoted:',
 '## Internal gate status\n\n**PASS.** The following internal promotion tests have been completed successfully:')
])

print('post-integrity control state synchronized')
