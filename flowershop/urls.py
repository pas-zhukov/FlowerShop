from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from flower_site.views import index, quiz, quiz_step, catalogue, consultation, card, order, order_payment, result
from flowershop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('quiz/', quiz, name='quiz'),
    path('quiz_step/', quiz_step, name='quiz_step'),
    path('result/', result, name='result'),
    path('catalogue/', catalogue, name='catalogue'),
    path('consultation/', consultation, name='consultation'),
    path('card/<int:pk>', card, name='card'),
    path('order/', order, name='order'),
    path('order/payment/', order_payment, name='order_payment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
