from django.urls import path

from blinds import views

urlpatterns = [
    path('blind/', views.BlindDetail.as_view())
]
