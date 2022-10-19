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
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-id',)

    def __str__(self):
        return f"#{self.id} | {self.title}"
