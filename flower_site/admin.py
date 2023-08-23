from django.contrib import admin

from .models import ComponentType
from .models import Component
from .models import ComponentObject
from .models import Bouquet
from .models import ConsultationSignUp
from .models import Order
from .models import OrderedBouquet


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


@admin.register(OrderedBouquet)
class OrderedBouquetAdmin(admin.ModelAdmin):
    pass


class OrderBouquetsInline(admin.TabularInline):
    model = OrderedBouquet


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderBouquetsInline]
