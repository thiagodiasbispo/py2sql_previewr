import sqlparse


def format_sql(sql):
    return sqlparse.format(str(sql), reindent=True)
