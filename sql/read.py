# encoding:utf-8
import pandas as pd
from .sqlEngine import *


def read_sqlServer(sql, user, password, host, database, port=3306):
    engine = createSqlServerEngine(user, password, host, database, port)
    df = pd.read_sql(sql, engine)
    return df


def read_mysql(sql, user, password, host, database, port=1433):
    engine = createMysqlEngine(user, password, host, database, port)
    df = pd.read_sql(sql, engine)
    return df
