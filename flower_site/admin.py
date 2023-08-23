from django.contrib import admin

from .models import ComponentType
from .models import Component
from .models import ComponentObject
from .models import Bouquet
from .models import ConsultationSignUp


@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(ComponentObject)
class ComponentObjectAdmin(admin.ModelAdmin):
    pass


class BouquetComponentInline(admin.TabularInline):
    model = ComponentObject
    extra = 0


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    inlines = [BouquetComponentInline]


@admin.register(ConsultationSignUp)
class ConsultationAdmin(admin.ModelAdmin):
    pass
