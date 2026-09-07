import unittest
from src.tilenet import evaluate, predict, make_tile


class TileTests(unittest.TestCase):
    def test_acc_perfect_on_synthetic(self):
        out = evaluate(20)
        self.assertEqual(out["acc"], 1.0)

    def test_bright_call(self):
        self.assertEqual(predict(make_tile("bright")), "bright")


if __name__ == "__main__":
    unittest.main()
