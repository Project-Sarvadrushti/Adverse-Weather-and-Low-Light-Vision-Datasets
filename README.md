# Adverse Weather & Low-Light Vision Datasets

[![Python 3.7+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-green.svg)](LICENSE)
[![Datasets](https://img.shields.io/badge/datasets-53-orange.svg)](#dataset-taxonomy)
![Dataset Links](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/JVSCHANDRADITHYA/Adverse-Weather-and-Low-Light-Vision-Datasets/main/link_status.json)


A curated, unified index of public datasets for **fog, haze, rain, snow, low-light, underwater, and sandstorm** image restoration and perception research. This repository is intended as a single, consistent reference for discovering and programmatically accessing datasets used in image restoration, enhancement, and robust perception under adverse conditions.

---

## Overview

The core of this repository is a normalized CSV file:

datasets.csv

with the schema:

INDEX, NAME, CATEGORY, SIZE, DESCRIPTION, MAIN_LINK

![Dataset Image](./assets/image.png)

All datasets are mapped to this schema so downstream code can operate without dataset-specific assumptions or ad-hoc parsing.

---

## Repository Contents

- datasets.csv — master dataset registry with IDs, categories, descriptions, sizes, and official links
- loaders/registry.py — lightweight Python registry for querying dataset metadata
- README.md — documentation (this file)

The structure is intentionally minimal and designed to scale.

---

## Dataset Taxonomy

Each dataset is tagged with a CATEGORY to enable fast filtering.

| CATEGORY          | DATASETS                                                                                                                                        |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Haze / Fog**    | Foggy Cityscapes, O-HAZY, NH-HAZE, RESIDE-Standard, RESIDE-Beta, HazeSpace2M, Haze1K, RS-Haze, Foggy Zurich, SynthRSF, NTIRE Nighttime Dehazing |
| **Snow**          | Snow100K, SnowCityScapes, SnowKITTI2012, SRRS, CSD, SITD, NTIRE Desnowing                                                                       |
| **Rain**          | Rain100L, Rain1400, Rain Cityscapes, HQ-NightRain, LWDDS, WeatherBench, **Raindrop Clarity (2025)**, **URIR-8K (2024)**                         |
| **Low-Light**     | LOL (v1, v2), SID (Sony, Fuji, Full), ExDark, LLVIP, LoLI-Street, SICE, LIME, DPED, LoL-SRW, **HDRT (2024)**                                    |
| **Underwater**    | **UIEB, EUVP, MOUD (2025 release), LSUI**                                                                                                       |
| **Sand / Dust**   | **Sand11K (2025 release), SIRB**                                                                                                                |
| **Smoke**         | SmokeBench (surveillance), LSD3K (medical / endoscopic)                                                                                         |
| **Multi-Weather** | allweather-TRANSWEATHER, WeatherBench, MCASD                                                                                                    |
| **Super-Res**     | NKUSR8K                                                                                                                                         |

All entries are normalized into the same CSV format for consistent downstream usage.

## Using the Dataset Registry

Example Python usage:

```python
from loaders.registry import DatasetRegistry

# Initialize the registry
reg = DatasetRegistry("datasets.csv")

# 1. Search for datasets by keyword (e.g., "underwater", "2025", "low light")
results = reg.search("underwater")
print(f"Found {len(results)} datasets matching your query.")

# 2. Retrieve metadata by Index
meta = reg.get(46)
print(f"Name: {meta['NAME']}")
print(f"Category: {meta['CATEGORY']}")
print(f"Direct Link: {reg.link(46)}")

# 3. Retrieve metadata by Name (Case-insensitive)
snow = reg.get_by_name("Snow100K")
print(f"Index: {snow['INDEX']} | URL: {snow['MAIN_LINK']}")

# 4. Print all datasets in a clean, human-readable format
for row in reg.list_all():
    print(reg.pretty(row["INDEX"]))

```

The CSV remains the single source of truth; the registry is only a thin lookup layer.

## Intended Use

This repository supports:

Training and benchmarking dehazing, deraining, desnowing, desmoking, and low-light enhancement models

Cross-weather and multi-domain generalization studies

Joint tasks such as dehaze + low-light or restoration + detection

Robust perception research under adverse environmental conditions

Remote sensing under atmospheric degradation

## Project History

This repository originates from the Sarvadrushti research initiative, which began in early 2024 as an exploration of situational awareness and robust computer vision under adverse conditions.

During its active development phase, the work was conducted under institutional oversight, incubation review cycles, and external evaluations. Due to confidentiality and evaluation constraints, intermediate code and artifacts were not publicly released.

Following the conclusion of evaluations and internal reviews, the dataset index and supporting tooling have been consolidated, cleaned, and released publicly as a research artifact. The Git history reflects the open-source release timeline and does not represent the original inception date of the research.

### Project status: Completed / Archived.

## Licenses and Citation

This repository does not host datasets. Each entry links to the official source; users must verify licenses and citation requirements before use. When using a dataset, cite the original paper or benchmark.

If referencing this collection as a whole, you may cite it as:

“We use the Adverse Weather & Low-Light Dataset Collection, which aggregates public datasets for fog, haze, rain, snow, smoke, and low-light vision research.”

## Contributors

This repository was developed as part of the Sarvadrushti research initiative.

## Core contributors:

Chandradithya and Siddharth Verma — dataset curation, vision research, and codebase development, workflows, and documentation.

Sarvadrushti Research Team — experimentation, evaluation, and review
