from django.db import models
from django.contrib import auth

class MoneyField(models.DecimalField):
    def __init__(self, **kwargs):
        super(MoneyField, self).__init__(
            max_digits=15, decimal_places=2, **kwargs)

class Income(models.Model):
    monthly_salary = MoneyField()
    interest = MoneyField()
    other = MoneyField()

class Expenses(models.Model):
    rent = MoneyField()
    credit_card = MoneyField()
    cash = MoneyField()
    checks = MoneyField()

class Assets(models.Model):
    cash = MoneyField()
    stock = MoneyField()
    fixed = MoneyField()
    ira = MoneyField()

class Liabilities(models.Model):
    credit_card = MoneyField()
    mortgage = MoneyField()
    mortgage_interest = MoneyField()
    loan = MoneyField()
    loan_interest = MoneyField()
    other = MoneyField()
    other_interest = MoneyField()

class Finances(models.Model):
    user = models.OneToOneField(auth.models.User, related_name="finances")
    age = models.IntegerField()
    retire = models.IntegerField()
    yearly_salary = MoneyField()
    income = models.OneToOneField(Income, null=True, blank=True)
    expenses = models.OneToOneField(Expenses, null=True, blank=True)
    assets = models.OneToOneField(Assets, null=True, blank=True)
    liabilities = models.OneToOneField(Liabilities, null=True, blank=True)
