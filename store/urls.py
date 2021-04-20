from django.urls import path,include
from store.views import (CartView,StoreView,CheckoutView)


urlpatterns = [
    path('cart/',CartView.as_view(),name="cart"),
    path('checkout/',CheckoutView.as_view(),name="checkout"),
    path('store/',StoreView.as_view(),name="store"),
]
