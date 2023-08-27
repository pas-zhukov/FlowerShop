from django.contrib import admin

from .models import ComponentType
from .models import Component
from .models import ComponentObject
from .models import Bouquet
from .models import ConsultationSignUp
from .models import Order
from .models import OrderedBouquet
from .models import BouquetCategory


@admin.register(BouquetCategory)
class BouquetCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'is_available']
    pass


@admin.register(ComponentObject)
class ComponentObjectAdmin(admin.ModelAdmin):
    pass


class BouquetComponentInline(admin.TabularInline):
    model = ComponentObject
    extra = 0


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'height', 'width', 'is_available']
    inlines = [BouquetComponentInline]


@admin.register(ConsultationSignUp)
class ConsultationAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderedBouquet)
class OrderedBouquetAdmin(admin.ModelAdmin):
    pass


class OrderBouquetsInline(admin.TabularInline):
    model = OrderedBouquet
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'стоимость_заказа', 'payment_status','name', 'phone', 'address', 'delivery_interval',]
    inlines = [OrderBouquetsInline]

    def стоимость_заказа(self, obj):
        items = obj.bouquets.all()
        return sum(item.fixed_price * item.count for item in items)
