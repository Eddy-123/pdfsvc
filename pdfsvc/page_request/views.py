from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import PageRequest, PageRequestSerializer
from .models import PageRequest


class PageRequestViewSet(viewsets.ModelViewSet):
    queryset = PageRequest.objects.none()
    serializer_class = PageRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PageRequest.objects.filter(owner=self.request.user)
    
