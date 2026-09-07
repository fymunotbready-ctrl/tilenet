

![Tests](https://github.com/fymunotbready-ctrl/tilenet/actions/workflows/test.yml/badge.svg)




![Python](https://img.shields.io/badge/python-3.10%2B-blue)




![License](https://img.shields.io/badge/license-MIT-green)



# TileNet

Tiny image rules + a score. Upgrade to a trained model after the eval table exists.

**Internship signal (vision / NVIDIA-shaped):** measured accuracy, not a vibe.
**Dream:** what a camera or satellite tile is showing.

## v1
Synthetic 8×8 tiles:
- `bright` = mean pixel > 0.6
- `dark` = mean pixel ≤ 0.6

Report hits / total. Later: swap in a public land-cover set.

## Not v1
Foundation model, 94% on a dataset you did not hold out.

## Project Structure

.
├── src/            # source code
├── tests/          # unit tests
├── .github/workflows/test.yml   # CI: runs tests on every push
├── LICENSE
└── README.md

## Running

python3 -m unittest discover -s tests -t .
