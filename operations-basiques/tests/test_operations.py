import unittest

from operations_basiques.operations import multiplier, diviser


class TestOperationsBasiques(unittest.TestCase):
    """Tests unitaires simples pour les fonctions du module operations."""

    def test_multiplier_cases_simples(self):
        self.assertEqual(multiplier(2, 3), 6)
        self.assertEqual(multiplier(-1, 5), -5)
        self.assertEqual(multiplier(0, 10), 0)

    def test_diviser_cases_simples(self):
        self.assertEqual(diviser(10, 2), 5.0)
        self.assertAlmostEqual(diviser(3, 2), 1.5)

    def test_diviser_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            diviser(1, 0)


if __name__ == "__main__":
    unittest.main()