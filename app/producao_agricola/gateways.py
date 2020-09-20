from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
import app.gateways as gateways

Base = declarative_base()


class ProducaoAgricola(Base):
    __tablename__ = 'producao_agricola'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(String(20))
    regiao = Column(String(20))
    periodo = Column(String(30))
    area = Column(Integer)
    producao = Column(Integer)


class MediaDaAreaProdutivaPorEstado(Base):
    __tablename__ = 'media_da_area_produtiva_por_estado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(String(20))
    media = Column(Numeric)


class MediaDaProducaoPorEstado(Base):
    __tablename__ = 'media_da_producao_por_estado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(String(20))
    media = Column(Numeric)


def recriar_tabelas_no_bd(engine):
    gateways.recriar_tabelas_no_bd(Base, engine)


def carregar_dados_de_producao_agricola_no_bd(engine, dados):
    gateways.carregar_dados(engine, ProducaoAgricola, dados)