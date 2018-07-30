from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema

import coreapi, coreschema


class BlindDetail(APIView):

    def get(self, request: HttpRequest, board_id: int, article_id: int):
        """
        해당 게시판 ID에서 요청된 게시글 세부 정보 조회
        :param request:
        :param board_id:
        :param article_id:
        :return:
        """

        return Response({'msg': 'success'})

    def put(self, request: HttpRequest, board_id: int, article_id: int):
        """
        해당 게시판 ID에서 요청된 게시글 편집
        :param request:
        :param board_id:
        :param article_id:
        :return:
        """

        return Response({'msg': 'success'})

    def delete(self, request: HttpRequest, board_id: int, article_id: int):
        """
        해당 게시판 ID에서 요청된 게시글 삭제
        :param request:
        :param board_id:
        :param article_id:
        :return:
        """
        return Response({'msg': 'success'})


class BlindList(APIView):
    lookup_board_kwarg = 'board_id'

    def get(self, request: HttpRequest, board_id: int):
        """
        해당 게시판 ID의 전체 게시글 리스트 조회
        :param request:
        :param board_id:
        :return:
        """

        return Response({'msg': 'success'})

    def post(self, request: HttpRequest, board_id: int):
        """
        해당 게시판 ID의 전체 게시글 작성
        :param request: 
        :param board_id: 
        :return: 
        """
        data = JSONParser().parse(request)
        title = data['title']
        body = data['body']
        data[self.lookup_board_kwarg] = board_id
        print(data)
        return Response({'msg': 'success'})

'''
class BlindCreateArticle(APIView):
    schema = ManualSchema(
        description='해당 게시판 ID의 전체 게시글 작성',
        fields=[
            coreapi.Field("content_body", required=True, location="body", schema=coreschema.String()),
            coreapi.Field("board_id", required=True, location="path", schema=coreschema.Integer()),
        ])
'''
