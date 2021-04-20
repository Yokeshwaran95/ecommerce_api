from django.shortcuts import render
from django.views.generic import ( TemplateView, ListView, 
	DetailView, CreateView, UpdateView )


class StoreView(ListView):
	template_name="store.html"
	def get_queryset(self):


class CartView(ListView):
	template_name="cart.html"
	def get_queryset(self):

class CheckoutView(ListView):
	template_name="checkout.html"
	def get_queryset(self):
