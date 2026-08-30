import argparse
from pathlib import Path
import pandas as pd
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Path to curated_dataset_wc22")
    args = parser.parse_args()
    root = Path(args.root)
    global_dir = root / "_global" / "step2_5_outputs"

    episodes_path = global_dir / "master_episodes_with_coarse.parquet"
    pairs_path = global_dir / "formal_pairs.parquet"

    assert episodes_path.exists(), f"Missing {episodes_path}"
    assert pairs_path.exists(), f"Missing {pairs_path}"

    episodes = pd.read_parquet(episodes_path)
    pairs = pd.read_parquet(pairs_path)

    print("Episodes:", episodes.shape)
    print("Pairs:", pairs.shape)

    id_col = "attack_id" if "attack_id" in episodes.columns else episodes.columns[0]
    assert episodes[id_col].astype(str).is_unique, f"Episode IDs are not unique in {id_col}"
    print("Unique episode IDs: OK")

    if "split" in episodes.columns:
        print("Splits:")
        print(episodes["split"].value_counts())

    label_col = "coarse_label" if "coarse_label" in episodes.columns else None
    if label_col:
        print("Labels:")
        print(episodes[label_col].value_counts())

    print("Basic validation completed.")


if __name__ == "__main__":
    main()
