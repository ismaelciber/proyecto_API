import unittest
from funcion_iva import calculariva
class tests_calculariva(unittest.TestCase):
    def test_calculariva(self):
        self.assertEqual(calculariva(1),0.21)
        self.assertEqual(calculariva(5),1.05)
        self.assertEqual(calculariva(10.102645),2.1215554500000002)
if __name__ == '__main__':
    unittest.main()
