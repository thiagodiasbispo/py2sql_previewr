from exceptions import QueryObjectNotDefined

DEFAULT_CONTENT = (
    "from pypika.queries import Query, Table, make_tables"
    "\n\nquery = Query.from_('tracks').select('*')"
)


def compile_code(source_code):
    code_objs = {}
    exec(source_code, code_objs)
    try:
        query = code_objs["query"]
    except KeyError:
        raise QueryObjectNotDefined()

    del code_objs

    return query
