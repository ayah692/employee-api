from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    STATUS_CHOICES = [("PRESENT", "PRESENT"), ("ABSENT", "ABSENT"), ("REMOTE", "REMOTE")]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PRESENT")
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ("employee", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"
