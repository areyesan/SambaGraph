from pathlib import Path
import os
import pandas as pd
import numpy as np


def get_root(root=None):
    return Path(root or os.environ.get("SAMBAGRAPH_ROOT", "curated_dataset_wc22"))


def load_tables(root=None):
    root = get_root(root)
    global_dir = root / "_global" / "step2_5_outputs"
    episodes = pd.read_parquet(global_dir / "master_episodes_with_coarse.parquet")
    pairs = pd.read_parquet(global_dir / "formal_pairs.parquet")
    return episodes, pairs


def load_xseq(npz_path):
    with np.load(npz_path, allow_pickle=True) as z:
        if "Xseq" not in z:
            raise KeyError(f"Xseq not found in {npz_path}; keys={list(z.keys())}")
        return z["Xseq"]
