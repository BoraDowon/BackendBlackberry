from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Profile
from accounts.serializers import ProfileSerializer


class ProfileDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_url_kwarg = 'article_id'

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글의 상세 내용 조회
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글을 수정
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글 삭제
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.delete(request, *args, **kwargs)
