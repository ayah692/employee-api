from django.db import models
from departments.models import Department

class Employee(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employees")
    title = models.CharField(max_length=100, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="performance_reviews")
    review_date = models.DateField()
    score = models.DecimalField(max_digits=4, decimal_places=2)  # 0–100
    reviewer = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ["-review_date"]

    def __str__(self):
        return f"{self.employee} - {self.score} on {self.review_date}"
