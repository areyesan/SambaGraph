# SambaGraph: Action--Reaction Graphs for Soccer Tactical Response Modeling

> **Status:** research dataset and benchmark.  
> Replace this placeholder with the final paper link, dataset link, and citation before public release.

SambaGraph is a curated soccer analytics dataset for studying **tactical response modeling** from event and tracking data. Starting from action anchors such as corners, free kicks, penalties, shots, goals, and fouls, each episode is represented as a synchronized spatio-temporal graph of players and ball positions. The benchmark supports two main tasks: (i) coarse response classification and (ii) attack-to-defense retrieval/reranking.

## Overview

SambaGraph contains action-centered episodes from the 2022 FIFA World Cup. Each episode includes:

- a full player--ball graph window with 23 nodes: 22 players + ball;
- attack-team and defense-team views;
- metadata describing the action anchor, time window, and response label;
- coarse response labels such as `SUCCESS`, `STOPPED_BY_DEFENSE`, `FOUL_STOP`, and `UNKNOWN_OTHER`;
- curated attack--defense pairs for retrieval and contrastive learning.

The dataset is intended for research on **aggregate tactical patterns**, not individual player evaluation.

## Data access

The curated dataset files are hosted externally due to size and licensing constraints.

**Dataset download:** `[https://drive.google.com/file/d/1OaXGBKboqjjrnnfuT0H7SeToddlY7xi5/view?usp=sharing]`

After downloading, the expected local structure is:

```text
curated_dataset_wc22/
  _global/
    step2_5_outputs/
      master_episodes_with_coarse.parquet
      formal_pairs.parquet
      validation_report.json              # optional but recommended
  game_<game_id>/
    attack_windows_npz/
      *.npz
    attack_view_npz/
      *_ATT.npz
    defense_view_npz/
      *_DEF.npz
    gifs/                                 # optional media previews
      *.gif
```

If redistribution of the raw source tracking/event data is not permitted by the data license, this repository should release only the curation code, schemas, manifests, validation notebooks, and benchmark scripts. Users must obtain the original source data through the official provider before recreating the dataset.

## Repository contents

```text
.
├── README.md
├── DATASET_CARD.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── .gitignore
├── docs/
│   ├── DATA_STRUCTURE.md
│   └── RELEASE_CHECKLIST.md
├── notebooks/
│   ├── 01_sambagraph_dataset_exploration.ipynb
│   └── README.md
├── src/
│   └── sambagraph/
│       ├── __init__.py
│       └── io.py
└── scripts/
    └── validate_dataset.py
```

## Quick start

Clone the repository:

```bash
git clone https://github.com/<your-org-or-user>/sambagraph.git
cd sambagraph
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set the dataset path:

```bash
export SAMBAGRAPH_ROOT=/path/to/curated_dataset_wc22
```

On Windows PowerShell:

```powershell
$env:SAMBAGRAPH_ROOT="C:\path\to\curated_dataset_wc22"
```

Explore the dataset:

```bash
jupyter notebook notebooks/01_sambagraph_dataset_exploration.ipynb
```

Run a basic validation:

```bash
python scripts/validate_dataset.py --root /path/to/curated_dataset_wc22
```

## Benchmark tasks

### 1. Coarse response classification

Given an attack-centered graph window, predict a coarse response label:

```text
SUCCESS
STOPPED_BY_DEFENSE
FOUL_STOP
UNKNOWN_OTHER
```

Recommended metrics:

- accuracy;
- balanced accuracy;
- macro-F1;
- weighted-F1.

### 2. Attack-to-defense retrieval

Given a query attack, retrieve candidate defensive responses from the training memory. Recommended metrics:

- Hit@1, Hit@5, Hit@10;
- MRR;
- nDCG@10.

### 3. Optional LLM graph-summary reranking

A local LLM may rerank a short candidate list using graph-derived text summaries. This should be reported separately from full-bank retrieval because the candidate protocol is different.

## Minimal Python example

```python
from pathlib import Path
import os
import pandas as pd
import numpy as np

root = Path(os.environ.get("SAMBAGRAPH_ROOT", "curated_dataset_wc22"))
episodes = pd.read_parquet(root / "_global" / "step2_5_outputs" / "master_episodes_with_coarse.parquet")
pairs = pd.read_parquet(root / "_global" / "step2_5_outputs" / "formal_pairs.parquet")

print(episodes.shape)
print(pairs.shape)
print(episodes["coarse_label"].value_counts())

row = episodes.iloc[0]
npz_path = root / row["npz_full"] if "npz_full" in episodes.columns else None
if npz_path is not None and npz_path.exists():
    with np.load(npz_path, allow_pickle=True) as z:
        Xseq = z["Xseq"]
        print("Xseq shape:", Xseq.shape)
```

## Dataset release checklist

Before making the repository public, update:

- [ ] final dataset name and paper title;
- [ ] dataset download link;
- [ ] citation information;
- [ ] license statement for code and dataset artifacts;
- [ ] source-data access instructions;
- [ ] validation report and dataset statistics;
- [ ] benchmark result tables;
- [ ] notebook paths and expected artifact names.

## Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{sambagraph2026,
  title     = {SambaGraph: Action--Reaction Graphs for Soccer Tactical Response Modeling},
  author    = {Anonymous Authors},
  booktitle = {CVSports Workshop},
  year      = {2026}
}
```

Update this entry after acceptance or arXiv release.

## License and data terms

The code in this repository is released under the license specified in `LICENSE`. The dataset artifacts may be subject to separate terms depending on the source data license. Users are responsible for ensuring that their use of the source event/tracking data complies with the official data provider's terms.
