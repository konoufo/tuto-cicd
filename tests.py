import unittest

import calcul


class TestCalculs(unittest.TestCase):
    def test_double_de_5_est_10(self):
        self.assertEqual(calcul.doubleNombre(5), 10)

if __name__ == '__main__':
    unittest.main()
