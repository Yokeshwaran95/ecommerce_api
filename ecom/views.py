from django.shortcuts import render
from rest_framework.response import Response
from ecom.models import Customer,Profession,DataSheet,Document
from rest_framework import viewsets
from ecom.serializers import (CustomerSerializer,
	ProfessionSerializer,
	DataSheetSerializer,
	DocumentSerializer,)

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.http.response import Http404,HttpResponseNotAllowed
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
	serializer_class=CustomerSerializer
	# queryset=Customer.objects.all()
	def get_queryset(self):
		# import pdb; pdb.set_trace()
		active_customers=Customer.objects.filter(active=True)
		return active_customers
	def list(self,request,*args,**kwargs):
		# import pdb; pdb.set_trace()
		# customers=Customer.objects.filter(id=3)
		customers=Customer.objects.all()
		serializer=CustomerSerializer(customers,many=True)
		return Response(serializer.data)

	def retrieve(self,request,*args,**kwargs):
		# import pdb; pdb.set_trace()
		obj=self.get_object()
		serializer=CustomerSerializer(obj)
		return Response(serializer.data)
		# return HttpResponseNotAllowed("not allowed")

class ProfessionViewSet(viewsets.ModelViewSet):
	queryset=Profession.objects.all()
	serializer_class=ProfessionSerializer

class DataSheetViewSet(viewsets.ModelViewSet):
	queryset=DataSheet.objects.all()
	serializer_class=DataSheetSerializer

class DocumentViewSet(viewsets.ModelViewSet):
	queryset=Document.objects.all()
	serializer_class=DocumentSerializer



