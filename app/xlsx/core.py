from openpyxl import load_workbook


def obter_pagina_de_arquivo(arquivo_path, pagina):
    return load_workbook(filename=arquivo_path)[pagina]


def obter_valores_da_coluna(pagina, coluna_config):
    return [
        pagina[_obter_posicao(coluna_config.coluna, linha)].value
        for linha
        in coluna_config.linhas
    ]


def _obter_posicao(coluna, linha):
    return '{coluna}{linha}'.format(coluna=coluna, linha=linha)
