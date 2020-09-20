import os
from decimal import Decimal

from app.listas import indexar_lista
from app.numeros import arredondar_decimal
from app.producao_agricola.estados_enum import REGIOES_POR_ESTADO
from app.gateways import obter_engine
from app.producao_agricola.gateways import carregar_dados_de_producao_agricola_no_bd, recriar_tabelas_no_bd, \
    carregar_dados_de_participacao_por_regiao_no_bd, carregar_dados_de_media_da_area_produtiva_por_estado_no_bd, \
    carregar_dados_de_media_de_producao_por_estado_no_bd
from app.structs import ColunaXLSXConfig
from app.xlsx import obter_pagina_de_arquivo, obter_valores_da_coluna

ARQUIVO = 'produção_2019.xlsx'
ARQUIVO_PATH = os.path.join(os.path.dirname(__file__), ARQUIVO)

LINHAS_PADRAO = list(range(7, 34))
ESTADOS = ColunaXLSXConfig(coluna='A', linhas=LINHAS_PADRAO)
PERIODO_2019_MEDIA_ATE_ABRIL = '2019 (media ate Abril/2019)'
AREA_2019_MEDIA_ATE_ABRIL = ColunaXLSXConfig(coluna='B', linhas=LINHAS_PADRAO)
PRODUCAO_2019_MEDIA_ATE_ABRIL = ColunaXLSXConfig(coluna='E', linhas=LINHAS_PADRAO)
PERIODO_2019_MAIO = 'Maio/2019'
AREA_2019_MAIO = ColunaXLSXConfig(coluna='C', linhas=LINHAS_PADRAO)
PRODUCAO_2019_MAIO = ColunaXLSXConfig(coluna='F', linhas=LINHAS_PADRAO)
PERIODO_2019_JUNHO = 'Junho/2019'
AREA_2019_JUNHO = ColunaXLSXConfig(coluna='D', linhas=LINHAS_PADRAO)
PRODUCAO_2019_JUNHO = ColunaXLSXConfig(coluna='G', linhas=LINHAS_PADRAO)


def executar():
    engine = obter_engine()
    recriar_tabelas_no_bd(engine)

    producao_agricola = obter_dados_de_producao_agricola_do_xlsx()
    carregar_dados_de_producao_agricola_no_bd(engine, producao_agricola)

    participacao_por_regiao = obter_percentual_de_participacao_por_regiao(producao_agricola)
    carregar_dados_de_participacao_por_regiao_no_bd(engine, participacao_por_regiao)

    media_da_area_produtiva = obter_media_da_area_produtiva(producao_agricola)
    carregar_dados_de_media_da_area_produtiva_por_estado_no_bd(engine, media_da_area_produtiva)

    media_de_producao = obter_media_de_producao_por_estado(producao_agricola)
    carregar_dados_de_media_de_producao_por_estado_no_bd(engine, media_de_producao)


def obter_dados_de_producao_agricola_do_xlsx():
    pagina = obter_pagina_de_arquivo(ARQUIVO_PATH, 'area prod uf')
    return \
        _obter_producao_e_area_no_periodo(pagina, AREA_2019_MEDIA_ATE_ABRIL, PRODUCAO_2019_MEDIA_ATE_ABRIL, PERIODO_2019_MEDIA_ATE_ABRIL) + \
        _obter_producao_e_area_no_periodo(pagina, AREA_2019_MAIO, PRODUCAO_2019_MAIO, PERIODO_2019_MAIO) + \
        _obter_producao_e_area_no_periodo(pagina, AREA_2019_JUNHO, PRODUCAO_2019_JUNHO, PERIODO_2019_JUNHO)


def _obter_producao_e_area_no_periodo(pagina, area_config, producao_config, periodo):
    return _criar_linhas_para_inserir_na_tabela(
        obter_valores_da_coluna(pagina, ESTADOS),
        _converter_valores_numericos(obter_valores_da_coluna(pagina, area_config)),
        _converter_valores_numericos(obter_valores_da_coluna(pagina, producao_config)),
        periodo
    )


def _converter_valores_numericos(valores):
    return [int("".join(valor.split())) for valor in valores]


def _criar_linhas_para_inserir_na_tabela(estados, areas, producoes, periodo):
    return [
        {
            'uf': estado,
            'regiao': REGIOES_POR_ESTADO[estado.lower()],
            'periodo': periodo,
            'area': area,
            'producao': producao
        }
        for estado, area, producao
        in zip(estados, areas, producoes)
    ]


def obter_percentual_de_participacao_por_regiao(producao_agricola):
    lista_de_producao_indexada_por_regiao = indexar_lista(
        producao_agricola,
        fn_chave=lambda producao: producao['regiao']
    )
    soma_total_de_producao = Decimal(sum(producao['producao'] for producao in producao_agricola))
    soma_de_producao_por_regiao = {
        regiao: Decimal(sum(producao['producao'] for producao in lista_de_producao_indexada_por_regiao[regiao]))
        for regiao
        in lista_de_producao_indexada_por_regiao
    }
    return [
        {
            'regiao': regiao,
            'producao': soma_de_producao_por_regiao[regiao],
            'percentual': arredondar_decimal(
                soma_de_producao_por_regiao[regiao] / soma_total_de_producao * Decimal('100')
            )
        }
        for regiao
        in soma_de_producao_por_regiao
    ]


def obter_media_da_area_produtiva(producao_agricola):
    dados_por_estado = indexar_lista(producao_agricola, fn_chave=lambda producao: producao['uf'])
    media_da_area_produtiva_por_estado = {
        estado: sum(producao['area'] for producao in dados_por_estado[estado]) / len(dados_por_estado[estado])
        for estado in dados_por_estado
    }
    return [
        {'uf': estado, 'media': media_da_area_produtiva_por_estado[estado]}
        for estado in media_da_area_produtiva_por_estado
    ]


def obter_media_de_producao_por_estado(producao_agricola):
    dados_por_estado = indexar_lista(producao_agricola, fn_chave=lambda producao: producao['uf'])
    media_de_producao_por_estado = {
        estado: sum(producao['producao'] for producao in dados_por_estado[estado]) / len(
            dados_por_estado[estado])
        for estado in dados_por_estado
    }
    return [
        {'uf': estado, 'media': media_de_producao_por_estado[estado]}
        for estado in media_de_producao_por_estado
    ]
