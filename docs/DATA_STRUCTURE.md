# SambaGraph data structure

Recommended local structure:

```text
curated_dataset_wc22/
  _global/
    step2_5_outputs/
      master_episodes_with_coarse.parquet
      formal_pairs.parquet
      validation_report.json
  game_<game_id>/
    attack_windows_npz/
      <attack_id>.npz
    attack_view_npz/
      <attack_id>_ATT.npz
    defense_view_npz/
      <attack_id>_DEF.npz
    gifs/
      <attack_id>.gif
```

## Core files

### `master_episodes_with_coarse.parquet`

One row per curated episode. Expected fields may include:

- `attack_id` or `episode_id`;
- `game_id` / `gameId`;
- `split`;
- `period`;
- `anchor_type` / `anchorType`;
- `gameEventId`;
- `t0` or event time;
- `teamId` / `teamName`;
- `coarse_label`;
- paths to full, attack, and defense NPZ files.

### `formal_pairs.parquet`

One row per attack--defense training pair. Expected fields may include:

- query attack ID;
- candidate defense/episode ID;
- `pair_type`, such as `pos_same`, `pos_retrieved_success`, or `neg_hard_failure`;
- split metadata.

### NPZ graph windows

Each NPZ file should contain an `Xseq` array with shape approximately:

```text
T x N x F
```

where `N=23` for the full window and `N=12` for team view windows when using 11 players plus the ball.
