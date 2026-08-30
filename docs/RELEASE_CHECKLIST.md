# Release checklist

Before public release:

## Repository

- [ ] Choose one final dataset name and use it consistently.
- [ ] Add the final paper citation.
- [ ] Add the final Google Drive/institutional data link.
- [ ] Add code license.
- [ ] Add clear data license / access terms.
- [ ] Add a small sample manifest or toy example if licensing permits.

## Data

- [ ] Verify all expected parquet files exist.
- [ ] Verify all NPZ paths resolve.
- [ ] Verify split safety at match level.
- [ ] Verify no duplicate episode IDs.
- [ ] Verify label values are documented.
- [ ] Verify pair IDs join to existing episodes.
- [ ] Verify Drive folder contains the same version described in the README.

## Reproducibility

- [ ] Include dataset exploration notebook.
- [ ] Include validation script.
- [ ] Include benchmark scripts or links to benchmark notebooks.
- [ ] Include requirements file.
- [ ] Include expected output tables/metrics.
