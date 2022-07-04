from rest_framework import serializers,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Books
from .serializers import BooksSerializer


class BooksCatalogueView(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

    def create(self, request):
        params = request.data.copy()
        serializer = BooksSerializer(data=params)
        if serializer.is_valid():
            book = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)