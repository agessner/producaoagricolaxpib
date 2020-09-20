from unittest.case import TestCase

from app.producao_agricola.pipeline import obter_dados_de_producao_agricola_do_xlsx, PERIODO_2019_MEDIA_ATE_ABRIL


class ObterDadosDeProducaoAgricolaDoXLSXTests(TestCase):
    def test_retorna_numero_de_linhas_esperado(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(81, len(dados_de_producao))

    def test_retorna_estado(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual('ACRE', dados_de_producao[0]['uf'])

    def test_retorna_regiao(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual('Norte', dados_de_producao[0]['regiao'])

    def test_retorna_periodo(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(PERIODO_2019_MEDIA_ATE_ABRIL, dados_de_producao[0]['periodo'])

    def test_retorna_area(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(44487, dados_de_producao[0]['area'])

    def test_retorna_producao(self):
        dados_de_producao = obter_dados_de_producao_agricola_do_xlsx()

        self.assertEqual(89948, dados_de_producao[0]['producao'])