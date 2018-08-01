from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

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
        # code snippet for deleting an article
        instance = Article.objects.get(id=kwargs['article_id'])
        instance.status = '6deleted'
        instance.save()
        serializer = ArticleSerializer(instance)

        return Response({'msg': 'success', 'data': serializer.data})


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
        # code snippet for deleting an article
        instance = Article.objects.all()

        serializer = ArticleSerializer(instance, many=True)

        import json
        s_dumps = json.dumps(serializer.data)
        s_json_list = json.loads(s_dumps)
        output_list = list()
        for s_json in s_json_list:
            if s_json['status'] != '6deleted':
                del s_json['body']
                output_list.append(s_json)

        return Response({'msg': 'success', 'data': output_list})

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


class BlindArticleLike(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'article_id'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def put(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글을 좋아요 선택
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = Article.objects.get(id=kwargs['article_id'])
        serializer = ArticleSerializer(instance)
        print(serializer.data)
        return Response({'msg': 'success'})
        #return self.update(request, *args, **kwargs)


class BlindArticleReport(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'article_id'

    def put(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글을 신고
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.update(request, *args, **kwargs)


class BlindArticleBookmark(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'article_id'

    def put(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        """
        해당 게시글을 북마크
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.update(request, *args, **kwargs)
