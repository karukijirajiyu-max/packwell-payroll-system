from django.db import models
from employees.models import Employee

class SalaryRecord(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    month = models.DateField()

    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    overtime = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    insurance = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee} - {self.month}"