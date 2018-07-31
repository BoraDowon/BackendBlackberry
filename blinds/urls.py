from django.urls import path

from blinds import views

urlpatterns = [
    path('blinds/<int:board_id>/', views.BlindList.as_view()),
]
