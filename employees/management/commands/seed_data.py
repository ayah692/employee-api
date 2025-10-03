from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from departments.models import Department
from employees.models import Employee, Performance
from attendance.models import Attendance
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = "Seeds initial departments, employees, attendance, and performance data"

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "adminpass")
            self.stdout.write(self.style.SUCCESS("Created superuser admin/adminpass (dev only)"))

        depts = ["Engineering", "HR", "Finance", "Marketing"]
        dept_objs = []
        for d in depts:
            obj, _ = Department.objects.get_or_create(name=d, defaults={"location": "HQ"})
            dept_objs.append(obj)

        base_people = [
            ("Alice","Smith","alice@example.com","Engineer"),
            ("Bob","Jones","bob@example.com","Engineer"),
            ("Carla","Diaz","carla@example.com","HR Specialist"),
            ("Dan","Kim","dan@example.com","Accountant"),
        ]
        employees = []
        for i, (fn, ln, email, title) in enumerate(base_people):
            emp, _ = Employee.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": fn,
                    "last_name": ln,
                    "title": title,
                    "department": dept_objs[i % len(dept_objs)],
                    "hire_date": date.today() - timedelta(days=365*(i+1)),
                    "is_active": True,
                }
            )
            employees.append(emp)

        for emp in employees:
            for d in range(5):
                day = date.today() - timedelta(days=d)
                Attendance.objects.get_or_create(
                    employee=emp, date=day,
                    defaults={"status": random.choice(["PRESENT","REMOTE","PRESENT"])}
                )

        for emp in employees:
            Performance.objects.get_or_create(
                employee=emp, review_date=date.today() - timedelta(days=90),
                defaults={"score": round(random.uniform(70, 98), 2), "reviewer": "Manager"}
            )

        self.stdout.write(self.style.SUCCESS("Seed data created/ensured."))

