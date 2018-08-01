from django.urls import path

from blinds import views

urlpatterns = [
    path('blinds/<int:board_id>/articles', views.BlindList.as_view()),
    path('blinds/<int:board_id>/articles/<int:article_id>', views.BlindDetail.as_view()),
    path('blinds/<int:board_id>/articles/<int:article_id>/like', views.BlindArticleLike.as_view()),
    path('blinds/<int:board_id>/articles/<int:article_id>/report', views.BlindArticleReport.as_view()),
    path('blinds/<int:board_id>/articles/<int:article_id>/bookmark', views.BlindArticleBookmark.as_view()),
    path('blinds/<int:board_id>/articles/<int:article_id>/comments', views.BlindCommentList.as_view()),
]
