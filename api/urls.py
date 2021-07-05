from django.urls import path,include
from .views import ProductList,ProductDetail,SearchProudct

urlpatterns = [
    path('product/',ProductList.as_view()),
    path('product/<int:pk>/',ProductDetail.as_view()),
    path('search/',SearchProudct.as_view())

]