from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from employees.models import Employee, Performance
from employees.serializers import EmployeeSerializer, PerformanceSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Employee.objects.select_related("department").all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["department", "is_active", "title"]
    search_fields = ["first_name", "last_name", "email", "title"]
    ordering_fields = ["first_name", "last_name", "hire_date", "id"]

class PerformanceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Performance.objects.select_related("employee").all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["employee", "score", "review_date", "reviewer"]
    search_fields = ["comments", "reviewer", "employee__first_name", "employee__last_name"]
    ordering_fields = ["score","review_date","id"]
