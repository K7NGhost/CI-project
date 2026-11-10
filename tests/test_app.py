"""Behavioral tests, including the public command-line interface."""

from pathlib import Path
import subprocess
import sys
import unittest

from app import add_numbers


class AdditionTests(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_mixed_signs(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_identity(self):
        self.assertEqual(add_numbers(7, 0), 7)

    def test_decimals(self):
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)

    def test_large_integers(self):
        self.assertEqual(add_numbers(10**30, 1), 10**30 + 1)


class CommandLineTests(unittest.TestCase):
    def run_app(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[1] / "app.py"), *args],
            capture_output=True, text=True, check=False,
        )

    def test_default_example(self):
        result = self.run_app()
        self.assertEqual(result.returncode, 0)
        self.assertIn("2 + 3 = 5", result.stdout)

    def test_custom_numbers(self):
        result = self.run_app("-2", "3.5")
        self.assertEqual(result.returncode, 0)
        self.assertIn("-2 + 3.5 = 1.5", result.stdout)

    def test_invalid_input(self):
        result = self.run_app("abc", "3")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid float value", result.stderr)


if __name__ == "__main__":
    unittest.main()
