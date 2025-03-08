import unittest
from src.geometry import Pentagon

class TestPentagon(unittest.TestCase):
    def test_calcular_area(self):
        pentagon = Pentagon(5, 10)  # Apotema = 5, Lado = 10
        expected_area = (1.5 * 5 * 10) / 2
        self.assertAlmostEqual(pentagon.calcular_area(), expected_area, places=3)

if __name__ == '__main__':
    unittest.main()
