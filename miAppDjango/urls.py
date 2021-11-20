from  django.urls import path
from django.urls.conf import include


from . import views as views 

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'personas', views.PersonaViewSet)
 
urlpatterns = [
      path('', views.index, name='index'),
      path('persona/<int:persona_id>/', views.detail, name='detail'),
      path('api/', include(router.urls)),
  ]