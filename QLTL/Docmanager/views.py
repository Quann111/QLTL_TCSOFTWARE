from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .model_serializers import *
from rest_framework import status


class BaseListAPIView(APIView):
    def get(self, request):
        bases = Base.objects.all()
        serializer = BaseSerializer(bases, many=True)
        return Response(serializer.data)

class BaseDetailAPIView(APIView):
    def get_object(self, pk):  # sourcery skip: raise-from-previous-error
        try:
            return Base.objects.get(pk=pk)
        except Base.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        base = self.get_object(pk)
        serializer = BaseSerializer(base)
        return Response(serializer.data)

    def put(self, request, pk):
        base = self.get_object(pk)
        serializer = BaseSerializer(base, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        base = self.get_object(pk)
        base.delete()
        return Response(status=204)
    
    

class FolderListAPIView(APIView):
    def get(self, request):
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FolderDetailAPIView(APIView):
    def get_object(self, pk):  # sourcery skip: raise-from-previous-error
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, pk):
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        folder = self.get_object(pk)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)