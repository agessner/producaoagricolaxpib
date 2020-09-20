from decimal import Decimal
from unittest.case import TestCase

from app.producao_agricola.pipeline import obter_dados_de_producao_agricola_do_xlsx, PERIODO_2019_MEDIA_ATE_ABRIL, \
    obter_percentual_de_participacao_por_regiao


class ObterDadosDeProducaoAgricolaDoXLSXTests(TestCase):
    def test_retorna_numero_de_linhas_esperado(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(81, len(dados_de_producao))

    def test_retorna_estado_do_primeiro_registro(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual('ACRE', dados_de_producao[0]['uf'])

    def test_retorna_regiao_do_primeiro_registro(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual('Norte', dados_de_producao[0]['regiao'])

    def test_retorna_periodo_do_primeiro_registro(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(PERIODO_2019_MEDIA_ATE_ABRIL, dados_de_producao[0]['periodo'])

    def test_retorna_area_do_primeiro_registro(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(44487, dados_de_producao[0]['area'])

    def test_retorna_producao_do_primeiro_registro(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(89948, dados_de_producao[0]['producao'])


class ObterPercentualDeParticipacaoPorPeriodoTests(TestCase):
    def test_retorna_percentual_por_regiao(self):
        producao_agricola = [
            {'regiao': 'Centro-oeste', 'producao': Decimal('10')},
            {'regiao': 'Centro-oeste', 'producao': Decimal('20')},
            {'regiao': 'Sul', 'producao': Decimal('5')},
        ]

        percentual_de_participacao = obter_percentual_de_participacao_por_regiao(producao_agricola)

        self.assertEqual(2, len(percentual_de_participacao))
        percentual_centro_oeste = [
            percentual for percentual in percentual_de_participacao
            if percentual['regiao'] == 'Centro-oeste'
        ][0]
        self.assertEqual(Decimal('85.71'), percentual_centro_oeste['percentual'])
        self.assertEqual(Decimal('30'), percentual_centro_oeste['producao'])
        percentual_sul = [
            percentual for percentual in percentual_de_participacao
            if percentual['regiao'] == 'Sul'
        ][0]
        self.assertEqual(Decimal('14.29'), percentual_sul['percentual'])
        self.assertEqual(Decimal('5'), percentual_sul['producao'])