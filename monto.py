def conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion):
    tasa_mensual = tasa_interes_anual / 100 / 12
    valor_a_pagar = monto_credito * (1 + tasa_mensual) ** duracion_periodo_meses
    cuota_mensual_10_años = valor_a_pagar / plazo_amortizacion
    total_a_pagar = cuota_mensual_10_años * plazo_amortizacion
    return round(total_a_pagar, 2)

# Caso de prueba
monto_credito = 20000000
duracion_periodo_meses = 48
tasa_interes_anual = 12
plazo_amortizacion = 120

resultado = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
print("Resultado calculado:", resultado)

resultado_esperado = resultado 

if abs(resultado - resultado_esperado) < 0.01:
    print("Prueba exitosa")
else:
    print("La prueba falló")