from query_code_compiler.default_compiler import compile_code
from sql_formater.default_formater import format_sql


def compile_and_get_formated_sql(source_code):
    if not source_code:
        return ""

    query = compile_code(source_code)
    sql = format_sql(str(query))

    del query
    del source_code

    return sql
