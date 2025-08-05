from monto import conversion_tasa_anual

import unittest


class pruebas_credito(unittest.TestCase):

    def test_normal_1(self):
        #entradas
        monto_credito = 20000000
        duracion_periodo_meses = 48
        tasa_interes_anual = 12
        plazo_amortizacion = 120

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
        self.assertEqual(round(total, 2), 32244521.55)

    def test_normal_2(self):
        #entradas
        monto_credito = 22000000
        duracion_periodo_meses = 60
        tasa_interes_anual = 12
        plazo_amortizacion = 130

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)    
        self.assertEqual(round(total, 2), 39967327.37)

if __name__ == '__main__':
    unittest.main()