from time import sleep

import app.pipeline as pipeline


def executar():
    _espera_por_conexao_com_o_banco()
    pipeline.executar()


def _espera_por_conexao_com_o_banco():
    sleep(10)


if __name__ == '__main__':
    executar()
