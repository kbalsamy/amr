from django.shortcuts import render
from .api import main
from django.http import HttpResponse
from .models import ServiceGroup
# Create your views here.


def mainView(request):

    return render(request, 'dashboard/index.html')


def downloadView(request):

    month = request.GET.get('month')
    year = request.GET.get('year')
    consumer = request.GET.get('customer')
    consumerList = []

    consumer_query = ServiceGroup.objects.filter(customer__customer_name=consumer)
    print(consumer_query)
    for consumer in consumer_query:
        consumerList.append({'EDC': consumer.edc.code, 'id': consumer.serviceNumber})

    data = main(month, year, consumerList)

    return HttpResponse(data)
