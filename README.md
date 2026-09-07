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
