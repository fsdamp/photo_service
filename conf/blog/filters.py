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
                    title='Вы можете сортировать по новый(new) или популярносты(popular)',
                    description='Вы можете сортировать по новый(new) или популярносты(popular)'
                ),
                type=str,
                description='order_by',
                example='new or popular'
            ),
        ]
