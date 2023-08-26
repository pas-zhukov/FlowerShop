from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction

from .serializers import ConsultationSerializer


@api_view(['GET', 'POST'])
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
        return render(request, 'index.html', context={

        })


def quiz(request):
    return render(request, 'quiz.html')


def catalogue(request):
    return render(request, 'catalog.html')