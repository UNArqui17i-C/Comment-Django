from .models import Comment
from rest_framework import viewsets
from .Serializers import CommentSerializer
class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-date_created')
    serializer_class = CommentSerializer
