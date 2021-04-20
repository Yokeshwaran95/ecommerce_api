from django.db import models

# Create your models here.
choices=(('PP',"Passport"),
	('AD',"Adhar Card"),
	('DL',"Driving License"))

class Profession(models.Model):
	description=models.CharField(max_length=250)

	def __str__(self):
		return self.description

class DataSheet(models.Model):
	description=models.CharField(max_length=250)
	history=models.TextField()

	def __str__(self):
		return self.description



class Customer(models.Model):
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	# document=models.ManyToManyField(Document)
	profession=models.ManyToManyField(Profession)
	datasheet=models.OneToOneField(DataSheet,null=True,on_delete=models.CASCADE)
	active=models.BooleanField(default=True)
	def __str__(self):
		return self.name


class Document(models.Model):
	dtype=models.CharField(max_length=50)
	category=models.CharField(choices=choices,default="PP",max_length=100)
	doc_number=models.IntegerField()
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

	def __str__(self):
		return self.name
	


