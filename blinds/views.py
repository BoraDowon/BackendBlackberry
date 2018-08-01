from django.http import HttpRequest

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from blinds.models import Article
from blinds.models import Comment
from blinds.serializers import ArticleSerializer
from blinds.serializers import CommentSerializer


class BlindCommentList(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'article_id'

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글의 댓글 리스트를 조회
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글의 댓글 등록
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.create(request, *args, **kwargs)


class BlindDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
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
        return self.destroy(request, *args, **kwargs)


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
        :param kwargs: path variables
        :return:
        """
        print(kwargs)
        print(request.data)
        if kwargs[self.lookup_url_kwarg] == request.data[self.lookup_url_kwarg]:
            return self.create(request, *args, **kwargs)
        else:
            return Response({'msg': 'invalid board_id'})
