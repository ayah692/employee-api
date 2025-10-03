from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from attendance.models import Attendance
from employees.serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Attendance.objects.select_related("employee").all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["employee", "status", "date"]
    search_fields = ["notes", "employee__first_name", "employee__last_name"]
    ordering_fields = ["date", "id"]
