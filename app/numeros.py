from decimal import ROUND_HALF_UP, Decimal


def arredondar_decimal(numero, casas_decimais=2, rounding=ROUND_HALF_UP):
    precisao = Decimal('1.{0}'.format('0' * casas_decimais))

    return numero.quantize(precisao, rounding)
