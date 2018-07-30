from django.urls import path

from blinds import views

urlpatterns = [
    path('blinds/<int:board_id>/', views.BlindList.as_view()),
    path('blinds/<int:board_id>/', views.BlindCreateArticle.as_view()),
    path('blinds/<int:board_id>/articles/<int:article_id>/', views.BlindDetail.as_view()),
]
