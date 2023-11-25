from django.contrib import admin
from .models import PriceCard, PriceTable
from django.utils.translation import gettext_lazy as _

# Register your models here.
admin.site.register(PriceTable)
admin.site.register(PriceCard)

