"""TileNet v0 — baseline classifier on synthetic tiles."""

import random

random.seed(7)


def make_tile(kind: str) -> list[list[float]]:
    if kind == "bright":
        return [[random.uniform(0.7, 1.0) for _ in range(8)] for _ in range(8)]
    return [[random.uniform(0.0, 0.4) for _ in range(8)] for _ in range(8)]


def mean(tile: list[list[float]]) -> float:
    vals = [v for row in tile for v in row]
    return sum(vals) / len(vals)


def predict(tile: list[list[float]]) -> str:
    return "bright" if mean(tile) > 0.6 else "dark"


def evaluate(n: int = 40) -> dict:
    hits = 0
    for i in range(n):
        kind = "bright" if i % 2 == 0 else "dark"
        if predict(make_tile(kind)) == kind:
            hits += 1
    return {"n": n, "hits": hits, "acc": hits / n}


if __name__ == "__main__":
    print(evaluate())
