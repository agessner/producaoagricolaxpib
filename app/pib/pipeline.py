import os
from decimal import Decimal

from app.gateways import obter_engine
from app.numeros import arredondar_decimal
from app.pib.gateways import recriar_tabelas_no_bd, carregar_dados_do_pib_no_bd
from app.structs import ColunaXLSXConfig
from app.xlsx import obter_pagina_de_arquivo, obter_valores_da_coluna

ARQUIVO = 'PIB_Cepea.xlsx'
ARQUIVO_PATH = os.path.join(os.path.dirname(__file__), ARQUIVO)

PIB_LINHAS_PADRAO = list(range(9, 33))
ANOS = ColunaXLSXConfig(coluna='A', linhas=PIB_LINHAS_PADRAO)
RENDA_AGRONEGOCIO_INSUMOS = ColunaXLSXConfig(coluna='B', linhas=PIB_LINHAS_PADRAO)
RENDA_AGRONEGOCIO_AGROPECUARIA = ColunaXLSXConfig(coluna='C', linhas=PIB_LINHAS_PADRAO)
RENDA_AGRONEGOCIO_INDUSTRIA = ColunaXLSXConfig(coluna='D', linhas=PIB_LINHAS_PADRAO)
RENDA_AGRONEGOCIO_SERVICOS = ColunaXLSXConfig(coluna='E', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_AGRICOLA_INSUMOS = ColunaXLSXConfig(coluna='H', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_AGRICOLA_AGROPECUARIA = ColunaXLSXConfig(coluna='I', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_AGRICOLA_INDUSTRIA = ColunaXLSXConfig(coluna='J', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_AGRICOLA_SERVICOS = ColunaXLSXConfig(coluna='K', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_PECUARIO_INSUMOS = ColunaXLSXConfig(coluna='N', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_PECUARIO_AGROPECUARIA = ColunaXLSXConfig(coluna='O', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_PECUARIO_INDUSTRIA = ColunaXLSXConfig(coluna='P', linhas=PIB_LINHAS_PADRAO)
RENDA_RAMO_PECUARIO_SERVICOS = ColunaXLSXConfig(coluna='Q', linhas=PIB_LINHAS_PADRAO)
AGRONEGOCIO_INSUMOS = ColunaXLSXConfig(coluna='T', linhas=PIB_LINHAS_PADRAO)
AGRONEGOCIO_AGROPECUARIA = ColunaXLSXConfig(coluna='U', linhas=PIB_LINHAS_PADRAO)
AGRONEGOCIO_INDUSTRIA = ColunaXLSXConfig(coluna='V', linhas=PIB_LINHAS_PADRAO)
AGRONEGOCIO_SERVICOS = ColunaXLSXConfig(coluna='X', linhas=PIB_LINHAS_PADRAO)
RAMO_AGRICOLA_INSUMOS = ColunaXLSXConfig(coluna='AA', linhas=PIB_LINHAS_PADRAO)
RAMO_AGRICOLA_AGROPECUARIA = ColunaXLSXConfig(coluna='AB', linhas=PIB_LINHAS_PADRAO)
RAMO_AGRICOLA_INDUSTRIA = ColunaXLSXConfig(coluna='AC', linhas=PIB_LINHAS_PADRAO)
RAMO_AGRICOLA_SERVICOS = ColunaXLSXConfig(coluna='AD', linhas=PIB_LINHAS_PADRAO)
RAMO_PECUARIO_INSUMOS = ColunaXLSXConfig(coluna='AF', linhas=PIB_LINHAS_PADRAO)
RAMO_PECUARIO_AGROPECUARIA = ColunaXLSXConfig(coluna='AG', linhas=PIB_LINHAS_PADRAO)
RAMO_PECUARIO_INDUSTRIA = ColunaXLSXConfig(coluna='AH', linhas=PIB_LINHAS_PADRAO)
RAMO_PECUARIO_SERVICOS = ColunaXLSXConfig(coluna='AI', linhas=PIB_LINHAS_PADRAO)


def executar():
    engine = obter_engine()
    recriar_tabelas_no_bd(engine)
    pib = obter_dados_do_pib_do_xlsx()
    carregar_dados_do_pib_no_bd(engine, pib)


def obter_dados_do_pib_do_xlsx():
    pagina = obter_pagina_de_arquivo(ARQUIVO_PATH, 'PIB')
    return \
        _obter_pib(pagina, 'PIB-renda', 'Agronegócio', '(A) Insumos', RENDA_AGRONEGOCIO_INSUMOS) + \
        _obter_pib(pagina, 'PIB-renda', 'Agronegócio', '(B) Agropecuária', RENDA_AGRONEGOCIO_AGROPECUARIA) + \
        _obter_pib(pagina, 'PIB-renda', 'Agronegócio', '(C) Indústria', RENDA_AGRONEGOCIO_INDUSTRIA) + \
        _obter_pib(pagina, 'PIB-renda', 'Agronegócio', '(D) Serviços', RENDA_AGRONEGOCIO_SERVICOS) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Agrícola', '(A) Insumos', RENDA_RAMO_AGRICOLA_INSUMOS) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Agrícola', '(B) Agropecuária', RENDA_RAMO_AGRICOLA_AGROPECUARIA) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Agrícola', '(C) Indústria', RENDA_RAMO_AGRICOLA_INDUSTRIA) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Agrícola', '(D) Serviços', RENDA_RAMO_AGRICOLA_SERVICOS) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Pecuário', '(A) Insumos', RENDA_RAMO_PECUARIO_INSUMOS) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Pecuário', '(B) Agropecuária', RENDA_RAMO_PECUARIO_AGROPECUARIA) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Pecuário', '(C) Indústria', RENDA_RAMO_PECUARIO_INDUSTRIA) + \
        _obter_pib(pagina, 'PIB-renda', 'Ramo Pecuário', '(D) Serviços', RENDA_RAMO_PECUARIO_SERVICOS) + \
        _obter_pib(pagina, 'PIB', 'Agronegócio', '(A) Insumos', AGRONEGOCIO_INSUMOS) + \
        _obter_pib(pagina, 'PIB', 'Agronegócio', '(B) Agropecuária', AGRONEGOCIO_AGROPECUARIA) + \
        _obter_pib(pagina, 'PIB', 'Agronegócio', '(C) Indústria', AGRONEGOCIO_INDUSTRIA) + \
        _obter_pib(pagina, 'PIB', 'Agronegócio', '(D) Serviços', AGRONEGOCIO_SERVICOS) + \
        _obter_pib(pagina, 'PIB', 'Ramo Agrícola', '(A) Insumos', RAMO_AGRICOLA_INSUMOS) + \
        _obter_pib(pagina, 'PIB', 'Ramo Agrícola', '(B) Agropecuária', RAMO_AGRICOLA_AGROPECUARIA) + \
        _obter_pib(pagina, 'PIB', 'Ramo Agrícola', '(C) Indústria', RAMO_AGRICOLA_INDUSTRIA) + \
        _obter_pib(pagina, 'PIB', 'Ramo Agrícola', '(D) Serviços', RAMO_AGRICOLA_SERVICOS) + \
        _obter_pib(pagina, 'PIB', 'Ramo Pecuário', '(A) Insumos', RAMO_PECUARIO_INSUMOS) + \
        _obter_pib(pagina, 'PIB', 'Ramo Pecuário', '(B) Agropecuária', RAMO_PECUARIO_AGROPECUARIA) + \
        _obter_pib(pagina, 'PIB', 'Ramo Pecuário', '(C) Indústria', RAMO_PECUARIO_INDUSTRIA) + \
        _obter_pib(pagina, 'PIB', 'Ramo Pecuário', '(D) Serviços', RAMO_PECUARIO_SERVICOS)


def _obter_pib(pagina, tipo, segmento, categoria, coluna_config):
    return _criar_linhas(
        obter_valores_da_coluna(pagina, ANOS),
        tipo,
        segmento,
        categoria,
        _converter_valores_numericos(obter_valores_da_coluna(pagina, coluna_config))
    )


def _converter_valores_numericos(valores):
    return [arredondar_decimal(Decimal(valor)) for valor in valores]


def _criar_linhas(anos, tipo, segmento, categoria, valores):
    return [
        {
            'ano': ano,
            'tipo': tipo,
            'segmento': segmento,
            'categoria': categoria,
            'valor': valor
        }
        for ano, valor
        in zip(anos, valores)
    ]