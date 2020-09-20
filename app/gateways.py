import os

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


def obter_engine():
    db_socket_dir = os.environ['DB_SOCKET_DIR']
    cloud_sql_connection_name = os.environ['INSTANCE_CONNECTION_NAME']
    unix_socket = '{}/{}'.format(db_socket_dir, cloud_sql_connection_name)
    return create_engine(
        URL(
            drivername="mysql+pymysql",
            username=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            host='127.0.0.1',
            port='3306',
            database=os.environ.get('DB_NAME'),
            query={'unix_socket': unix_socket}
        ),
        pool_recycle=3600
    )


def recriar_tabelas_no_bd(Base, engine):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(engine)


def carregar_dados(engine, model, dados):
    session = sessionmaker(bind=engine)()
    for dado in dados:
        session.add(model(**dado))
    session.commit()
