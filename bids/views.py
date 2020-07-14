from django.shortcuts import render
from rest_framework import generics
from django.views.generic.base import TemplateView
from .models import *
from .serializers import *
import csv, io
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Sum
from bids.functions import Concat


class Table(TemplateView):
    template_name = 'bids/table.html'

    def get_context_data(self, **kwargs):
        qry = Bidding.objects.filter(title = Bidding.objects.latest('new').title)
        xxx = qry.values('customer').annotate(total_spent = Sum('total'), items = Concat('item')).order_by('-total_spent')
        items_total = ''
        top_5 = []
        for i in xxx[:5].values('items'):
            items_total += i['items'] + ','
        for i in xxx[:5]:
            top_5.append(i)
        for i in top_5:
	           i['items'] = ', '.join([i for i in i['items'].split(',') if items_total.count(i) > 1])
        ctx = super(Table, self).get_context_data(**kwargs)
        ctx['header'] = ['username', 'total_spent','gems']
        ctx['rows'] = [line for line in top_5]
        return ctx

class SubmitList(generics.CreateAPIView):
    queryset = UploadForm.objects.all()
    serializer_class = UploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = UploadSerializer(data = request.data)
        reading_file = request.FILES['file']
        data = File(reading_file).read().decode('utf-8')
        io_string = io.StringIO(data)
        next(io_string)
        if serializer.is_valid(UploadForm):
            serializer.save()
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                created = Bidding.objects.update_or_create(
                title = reading_file.name + ' - {}'.format(UploadForm.objects.latest('created').pk),
                customer = column[0],
                item = column[1],
                total = column[2],
                quantity = column[3],
                date = datetime.strptime(column[4], '%Y-%m-%d %H:%M:%S.%f')
                )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
