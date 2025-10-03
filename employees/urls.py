from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet, PerformanceViewSet

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"performance", PerformanceViewSet, basename="performance")

urlpatterns = [ path("", include(router.urls)) ]

