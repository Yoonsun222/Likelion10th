
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Board
from .serializers import BoardSerializer



@api_view(['GET', 'POST'])
def boardlst(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        boards_data = BoardSerializer(boards, many = True)
        return Response(boards_data.data)

    elif request.method == 'POST':
        boards = BoardSerializer(data = request.data)
        if boards.is_valid():
            boards.save()
            return Response(boards.data, status = status.HTTP_201_CREATED)
        return Response(boards.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def board_detail(request,board_id):
    board = get_object_or_404(Board, id = board_id)

    if request.method == 'GET':
        boards_data = BoardSerializer(board)
        return Response(boards_data.data)

    elif request.method == 'PUT':
        boards_data = BoardSerializer(instance = board, data = request.data)
        if boards_data.is_valid():
            boards_data.save()
            return Response(boards_data.data, status = status.HTTP_201_CREATED)
        return Response(boards_data.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        board.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
