from django.urls import path

from accounts import views

urlpatterns = [
    path('profiles/<int:user_id>', views.ProfileDetail.as_view()),
]
