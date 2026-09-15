import unittest
import utils

class TestRFC(unittest.TestCase):
    def test_1(self):
        bar = utils.validar_rfc("EEKI071024PU0")
        self.assertTrue(bar)
    def test_2(self):
        foo = utils.validar_rfc("ABCD010101A1B2")
        self.assertFalse(foo)
    def test_3(self):
        baz = utils.validar_rfc("abcd010101a1b")
        self.assertTrue(baz)

class testFormato(unittest.TestCase):
    def test_1(self):
        bar = utils.formatear_moneda(1250.5)
        self.assertEqual(bar, "$1,250.50")
    def test_2(self):
        foo = utils.formatear_moneda("47.53")
        self.assertEqual(foo, "$47.53")
    def test_3(self):
        baz = utils.formatear_moneda(-10.25)
        self.assertEqual(baz, "$-10.25")

class testNoALetras(unittest.TestCase):
    def test_1(self):
        bar = utils.numero_a_letras(49.51)
        self.assertEqual(bar, "CUARENTA Y NUEVE PESOS 51/100 MXN")
    def test_2(self):
        foo = utils.numero_a_letras("36.5")
        self.assertIsNone(foo)

    def test_3(self):
        baz = utils.numero_a_letras(1)
        self.assertEqual(baz, "UN PESO 00/100 MXN")

class testNoGrandeALetras(unittest.TestCase):
    def test_1(self):
        bar = utils.no_grande_a_letras(3829460.27)
        self.assertEqual(bar, "TRES MILLONES OCHOCIENTOS VEINTINUEVE MIL CUATROCIENTOS SESENTA PESOS 27/100 MXN")

    def test_2(self):
        foo = utils.no_grande_a_letras("54953.3")
        self.assertIsNone(foo)

    def test_3(self):
        baz = utils.no_grande_a_letras(57.23)
        self.assertIsNone(baz)