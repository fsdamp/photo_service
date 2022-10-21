from rest_framework.filters import BaseFilterBackend
import coreapi, coreschema


class ArticlesListFilter(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='order_by',
                required=False,
                location='query',
                schema=coreschema.String(
                    title='Сортировка по: new (новые) / popular (популярные)',
                    description='Сортировка по: new (новые) / popular (популярные)'
                ),
                type=str,
                description='order_by',
                example='new or popular'
            ),
        ]
