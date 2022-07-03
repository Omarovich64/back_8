from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from albums.models import Album
from albums.api.serializers import AlbumsSerializer, AlbumImageSerializer


########################## GENERIC method ##########################



class AlbumCreate(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = AlbumsSerializer

    
    def perform_create(self, serializer):
        owner = self.request.user
        print (owner)
        serializer.save(owner=owner)


class AlbumList(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer




class AlbumImageCreate(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = AlbumImageSerializer

    
    def perform_create(self, serializer):
        owner = self.request.user
        print (owner)
        serializer.save(owner=owner)


class AlbumImageList(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumImageSerializer


class AlbumImageDetail(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumImageSerializer



########################### MIXINS method ##########################



# class AlbumListMIXIN(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = Album.objects.all()
#     serializer_class = AlbumsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class AlbumDetailMIXIN(mixins.RetrieveModelMixin, generics.GenericAPIView):

#     queryset = Album.objects.all()
#     serializer_class = AlbumsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)



# ########################## APIView method ##########################



# class AlbumList(APIView):

#     def get(self, request):
#         queryset = Album.objects.all()
#         serializer = AlbumsSerializer(queryset, many=True)
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = AlbumsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class AlbumDetail(APIView):

#     def get(self, request, pk):

#         try:
#             myalbum = Album.objects.get(pk=pk)
#         except Album.DoesNotExist:
#             return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = AlbumsSerializer(myalbum)
#         return Response(serializer.data)


#     def put(self, request, pk):

#         myalbum = Album.objects.get(pk=pk)
#         serializer = AlbumsSerializer(myalbum, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


#     def delete(self, request, pk):
#         myalbum = Album.objects.get(pk=pk)
#         myalbum.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


