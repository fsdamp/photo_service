from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCountMixin, HitCount
from hitcount.settings import MODEL_HITCOUNT


# Create your models here.

class Article(models.Model, HitCountMixin):
    title = models.CharField('Титле', max_length=250)
    poster = models.ImageField('Постер', upload_to='articles/poster')
    description = RichTextUploadingField('Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    is_main = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        # ordering = ('-id',)

    def __str__(self):
        return f"#{self.id} | {self.title}"

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)
        self.__original_is_main = self.is_main

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.is_main != self.__original_is_main:
            Article.objects.filter(is_main=True).update(is_main=False)
        super(Article, self).save(force_insert, force_update, *args, **kwargs)
