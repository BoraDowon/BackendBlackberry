from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from blinds.models import Article
from blinds.serializers import ArticleSerializer


class BlindList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'board_id'

    def get(self, request: HttpRequest, *args, **kwargs):
        """
        해당 게시판 ID의 전체 게시글 조회
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        """
        해당 게시판 ID의 게시글 작성
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        print(kwargs)
        print(request.data)
        if kwargs[self.lookup_url_kwarg] == request.data[self.lookup_url_kwarg]:
            return self.create(request, *args, **kwargs)
        else:
            return Response({'msg': 'invalid board_id'})
