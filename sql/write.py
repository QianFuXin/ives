# encoding:utf-8
import pandas as pd
from .sqlEngine import *


def write_sqlServer(df, tableName, user, password, host, database, port=3306):
    engine = createSqlServerEngine(user, password, host, database, port)
    df.to_sql(tableName, engine, index=False)


def write_mysql(df, tableName, user, password, host, database, port=1433):
    engine = createMysqlEngine(user, password, host, database, port)
    df.to_sql(tableName, engine, index=False)
