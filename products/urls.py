from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('categories/', CategoryList.as_view()),
    path('productdetails/<int:pk>',ProductDetails.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)