
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from ecom.views import ( CustomerViewSet,
						ProfessionViewSet,
						DataSheetViewSet,
						DocumentViewSet,)


router=routers.DefaultRouter()
router.register(r'customers',CustomerViewSet,basename="customers")
router.register(r'profession',ProfessionViewSet)
router.register(r'datasheet',DataSheetViewSet)
router.register(r'document',DocumentViewSet)

urlpatterns = [
	path('api-auth/',include(router.urls)),
	path('', include(('store.urls', 'store'),namespace='store')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'),)
]
