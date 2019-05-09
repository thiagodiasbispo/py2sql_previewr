class QueryObjectNotDefined(Exception):
    def __init__(self):
        super(QueryObjectNotDefined, self).__init__(
            "A query obj was not defined in the source code"
        )
