from .executor import SQLExecutor


class GenericTable(SQLExecutor):
    def __init__(self):
        super(GenericTable, self).__init__()

    def __call__(self, *args, **kwargs):
        if not self.table:
            raise ValueError

    def create(self, data):
        return self._create(table=self.table,
                            data=data)

    def list(self, *args, **kwargs):
        return self._list(table=self.table,
                          fields=kwargs.pop('fields', '*'),
                          fetch_all=kwargs.pop('fetch_all', True),
                          order_by=kwargs.pop('order_by', ['id']))

    def list2(self, *args, **kwargs):
        return self._list(table=self.table,
                          fields=kwargs.pop('fields', '*'),
                          fetch_all=kwargs.pop('fetch_all', True),
                          order_by=kwargs.pop('order_by', ['code']))

    def filter(self, *args, **kwargs):
        return self._filter(table=self.table,
                            fields=kwargs.pop('fields', '*'),
                            data=kwargs,
                            fetch_all=kwargs.pop('fetch_all', True),
                            order_by=kwargs.pop('order_by', ['-id']))

    def delete(self, *args, **kwargs):
        return self._delete(table=self.table,
                            filters=kwargs.pop('filters', None))

    def get(self, *args, **kwargs):
        return self._filter(table=self.table,
                            fields=kwargs.pop('fields', '*'),
                            data=kwargs,
                            fetch_all=kwargs.pop('fetch_all', False),
                            order_by=kwargs.pop('order_by', ['id']))

    def update(self, *args, **kwargs):
        return self._update(table=self.table,
                            values=kwargs.pop('values', None) or args[0],
                            filters=kwargs.pop('filters', None) or args[1])

    def join(self, *args, **kwargs):
        return self._join(table_1=self.table,
                          table_2=args[0],
                          kind=kwargs.pop('kind', None) or args[0],
                          on=kwargs.pop('on', None) or args[1],
                          filters=kwargs.pop('filters', None),
                          fields=kwargs.pop('fields', '*'),
                          fetch_all=kwargs.pop('fetch_all', True),
                          order_by=kwargs.pop('order_by', None))
