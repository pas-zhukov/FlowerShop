from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode
from django.views.decorators.http import require_http_methods

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction

from .serializers import ConsultationSerializer, BouquetIDSerializer, OrderSerializer

from .models import Bouquet


@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        serializer = ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            form_result = 'ok'
            serializer.save()
        else:
            form_result = 'error'
        return render(request, 'index.html', context={
            'form_result': form_result
        })
    else:
        recommended_bouquets = Bouquet.objects.all()[:3]
        return render(request, 'index.html', context={
            'recommended_bouquets': recommended_bouquets
        })


def quiz(request):
    return render(request, 'quiz.html')


def catalogue(request):
    bouquets = Bouquet.objects.all()[:3]
    return render(request, 'catalog.html', {'bouquets': bouquets})


def consultation(request):
    return render(request, 'consultation.html')


def card(request, pk):
    bouquet = get_object_or_404(Bouquet, pk=pk)
    components = bouquet.component_objects.all()
    context = {
        'bouquet': bouquet,
        'components': components
    }
    return render(request, 'card.html', context)


@require_http_methods(['GET'])
def order(request):
    if request.GET.get('error'):
        return render(request, 'order.html', context={
            'bouquet_id': request.GET.get('bouquet_id'),
            'bad_result': True
        })

    try:
        bouquet_id = request.GET['bouquet_id']
    except KeyError:
        return redirect('/')

    serializer = BouquetIDSerializer(data={'bouquet_id': bouquet_id})
    if serializer.is_valid():
        return render(request, 'order.html', context={
            'bouquet_id': bouquet_id,
        })
    else:
        return redirect('/')


@api_view(['POST'])
def order_payment(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, 'order-step.html')
    else:
        return order_error_redirect(order, error=True, bouquet_id=request.POST.get('bouquet_id'))


def order_error_redirect(url_name, *args, **kwargs):
    url = reverse(url_name, args=args)
    params = urlencode(kwargs)
    return redirect(url + "?%s" % params)
