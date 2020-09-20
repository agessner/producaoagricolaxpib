from decimal import Decimal
from unittest import TestCase

from app.pib.pipeline import obter_dados_do_pib_do_xlsx


class ObterDadosDoPibDoXLSXTests(TestCase):
    def test_retorna_numero_de_linhas_esperado(self):
        dados_do_pib = obter_dados_do_pib_do_xlsx()

        self.assertEqual(576, len(dados_do_pib))

    def test_retorna_ano_do_primeiro_registro(self):
        dados_do_pib = obter_dados_do_pib_do_xlsx()

        self.assertEqual(1996, dados_do_pib[0]['ano'])

    def test_retorna_tipo_do_primeiro_registro(self):
        dados_do_pib = obter_dados_do_pib_do_xlsx()

        self.assertEqual('PIB-renda', dados_do_pib[0]['tipo'])

    def test_retorna_segmento_do_primeiro_registro(self):
        dados_do_pib = obter_dados_do_pib_do_xlsx()

        self.assertEqual('Agronegócio', dados_do_pib[0]['segmento'])

    def test_retorna_categoria_do_primeiro_registro(self):
        dados_do_pib = obter_dados_do_pib_do_xlsx()

        self.assertEqual('(A) Insumos', dados_do_pib[0]['categoria'])

    def test_retorna_valor_do_primeiro_registro(self):
        dados_do_pib = obter_dados_do_pib_do_xlsx()

        self.assertEqual(Decimal('31597.66'), dados_do_pib[0]['valor'])
