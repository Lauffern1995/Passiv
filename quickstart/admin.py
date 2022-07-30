from django.contrib import admin
from .models import Salesperson
from .models import Sale
from .models import Company
# Register your models here.


admin.site.register(Salesperson)
admin.site.register(Sale)
admin.site.register(Company)