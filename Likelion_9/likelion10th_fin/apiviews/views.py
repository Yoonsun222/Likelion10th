from rest_framework.views import APIView

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .models import Board2
from .serializers import BoardSerializer




class BoardCRAPIView(APIView):
    def get(self, request):
        boards = Board2.objects.all()
        boards_data = BoardSerializer(boards, many = True)
        return Response(boards_data.data)

    def post(self, request):
        boards = BoardSerializer(data = request.data)
        if boards.is_valid():
            boards.save()
            return Response(boards.data, status = status.HTTP_201_CREATED)
        return Response(boards.errors, status = status.HTTP_400_BAD_REQUEST)


blog_post_list = BoardCRAPIView.as_view()

class BoardDetailCRUDAPIView(APIView):
    def get_object(self,board_id):
        board = get_object_or_404(Board2, id = board_id)
        return board
        
    def get(self, request, board_id):
        board = self.get_object(board_id)
        boards_data = BoardSerializer(board)
        return Response(boards_data.data)

    def put(self, request, board_id):
        board = self.get_object(board_id)
        boards_data = BoardSerializer(instance = board, data = request.data)
        if boards_data.is_valid():
            boards_data.save()
            return Response(boards_data.data, status = status.HTTP_201_CREATED)
        return Response(boards_data.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, board_id):
        board = self.get_object(board_id)
        board.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

blog_detail_post_list = BoardDetailCRUDAPIView.as_view()
