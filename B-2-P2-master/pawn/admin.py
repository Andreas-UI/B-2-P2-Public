from django.contrib import admin
from .widgets import AdminPawnWidget
from .models import PawnField

# Register your models here.
class PawnAdmin(admin.ModelAdmin):

    formfield_overrides = {
        PawnField: {
            'widget': AdminPawnWidget
        }
    }