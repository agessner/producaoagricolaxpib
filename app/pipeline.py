import app.producao_agricola as producao_agricola
import app.pib as pib


def executar():
    producao_agricola.executar_pipeline()
    pib.executar_pipeline()
