from django.db import models


class MenuItem(models.Model):
    title = models.CharField('Название', max_length=100)
    url = models.CharField('URL', max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                             null=True, blank=True,
                             related_name='children')
    menu_name = models.CharField('Имя меню', max_length=50)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']
        db_table = "menu_item"

    def __str__(self):
        return self.title


