# Dataset Card: SambaGraph

## Dataset summary

SambaGraph is a curated action--reaction soccer dataset for tactical response modeling. It converts event and tracking data into spatio-temporal graph episodes centered on tactical anchors such as corners, free kicks, shots, goals, penalties, and fouls.

## Intended use

The dataset is intended for research on:

- sports computer vision;
- spatio-temporal graph learning;
- tactical response classification;
- attack-to-defense retrieval;
- grounded LLM/VLM analysis over graph-derived summaries.

The dataset is not intended for individual player ranking, scouting decisions, or claims about player quality without additional validation.

## Data instances

Each episode may include:

- full 23-node graph sequence: 22 players + ball;
- attack view: attacking team + ball;
- defense view: defending team + ball;
- episode metadata;
- coarse and/or fine response labels;
- pair identifiers for retrieval and contrastive learning.

## Labels

Recommended coarse labels:

- `SUCCESS`
- `STOPPED_BY_DEFENSE`
- `FOUL_STOP`
- `UNKNOWN_OTHER`

## Splits

The recommended split is match-level train/validation/test splitting to avoid leakage across episodes from the same match.

## Known limitations

SambaGraph models observed outcomes rather than optimal tactical decisions. A response may depend on unobserved context such as score state, fatigue, attacker error, goalkeeper skill, or coaching instructions. Broadcast tracking can contain occlusion, identity, and positional noise. Coarse labels simplify rich tactical behavior into discrete outcomes.

## Licensing

Dataset redistribution depends on the terms of the original source data. If raw or derived tracking/event files cannot be redistributed, this repository should provide code, schemas, manifests, and validation notebooks, while requiring users to obtain the source data through the official provider.
