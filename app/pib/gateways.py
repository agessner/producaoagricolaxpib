from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
import app.gateways as gateways

Base = declarative_base()


class Pib(Base):
    __tablename__ = 'pib'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ano = Column(Integer)
    tipo = Column(String(10))
    segmento = Column(String(30))
    categoria = Column(String(30))
    valor = Column(Numeric)


def recriar_tabelas_no_bd(engine):
    gateways.recriar_tabelas_no_bd(Base, engine)


def carregar_dados_do_pib_no_bd(engine, dados):
    gateways.carregar_dados(engine, Pib, dados)
