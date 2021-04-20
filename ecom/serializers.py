from rest_framework import serializers
from ecom.models import Customer,Profession, DataSheet, Document

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields=('id','name','profession','address','datasheet')

class ProfessionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Profession
		fields=('id','description')

class DataSheetSerializer(serializers.ModelSerializer):
	class Meta:
		model=DataSheet
		fields=('id','description','history')

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Document
		fields=('id','dtype','category','doc_number','customer')