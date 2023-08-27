"""
URL configuration for flowershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flower_site.views import index, quiz, catalogue, consultation, card, order, order_payment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('quiz/', quiz, name='quiz'),
    path('catalogue/', catalogue, name='catalogue'),
    path('consultation/', consultation, name='consultation'),
    path('card/', card, name='card'),
    path('order/', order, name='order'),
    path('order/payment/', order_payment, name='order_payment')
]
urlpatterns += staticfiles_urlpatterns()