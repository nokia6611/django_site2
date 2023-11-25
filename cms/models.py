from django.db import models
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/media')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

#Строковое представление
    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'




