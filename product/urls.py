from django.urls import path
from .views import *
urlpatterns = [
    path('', BookListCreateView.as_view(), name='twoinone'),
    path('detail/<int:id>/', BookDetailView.as_view(), name='thereinone')
]