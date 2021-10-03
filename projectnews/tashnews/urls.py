from django.urls import path
from . import views
from .views import NewDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('news/<int:pk>/', NewDetailView.as_view(), name='news-detail'),
]
