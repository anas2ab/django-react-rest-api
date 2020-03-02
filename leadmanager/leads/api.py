from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    serializer_class = LeadSerializer
