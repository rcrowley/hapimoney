from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from hashlib import sha1
import forms, models

# Static pages.
def index(request):
    return render_to_response("index.html", RequestContext(request))
def process(request):
    return render_to_response("process.html", RequestContext(request))
def about(request):
    return render_to_response("about.html", RequestContext(request))

def signup(request):
    if "POST" == request.method:
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password1"]
            )
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            login(request, user)
            return HttpResponseRedirect(reverse("basic"))
    else:
        form = forms.SignupForm()
    return render_to_response("signup.html", RequestContext(request, {
        "form": form,
    }))

@login_required
def basic(request):
    if "POST" == request.method:
        form = forms.BasicForm(request.POST)
        if form.is_valid():
            try:
                finances = request.user.finances
            except models.Finances.DoesNotExist:
                finances = models.Finances()
                request.user.finances = finances
            for k in ("age", "retire", "yearly_salary"):
                setattr(finances, k, form.cleaned_data[k])
            finances.save()
            return render_to_response("basic_analysis.html",
                RequestContext(request, {
                    "form": form,
                })
            )
    else:
        form = forms.BasicForm()
    return render_to_response("basic.html", RequestContext(request, {
        "form": form,
    }))

@login_required
def budget(request):
    if "POST" == request.method:
        income_form = forms.IncomeForm(request.POST)
        expenses_form = forms.ExpensesForm(request.POST)
        if income_form.is_valid() and expenses_form.is_valid():
            income = request.user.finances.income
            if income is None:
                income = models.Income()
            for k in ("monthly_salary", "interest", "other"):
                setattr(income, k, income_form.cleaned_data[k])
            income.save()
            request.user.finances.income = income
            expenses = request.user.finances.expenses
            if expenses is None:
                expenses = models.Expenses()
            for k in ("rent", "credit_card", "cash", "checks"):
                setattr(expenses, k, expenses_form.cleaned_data[k])
            # TODO big_plans
            expenses.save()
            request.user.finances.expenses = expenses
            request.user.finances.save()
            return render_to_response("budget_analysis.html",
                RequestContext(request, {
                    "income_form": income_form,
                    "expenses_form": expenses_form,
                })
            )
    else:
        income_form = forms.IncomeForm()
        expenses_form = forms.ExpensesForm()
    return render_to_response("budget.html", RequestContext(request, {
        "income_form": income_form,
        "expenses_form": expenses_form,
    }))

@login_required
def balancesheet(request):
    if "POST" == request.method:
        assets_form = forms.AssetsForm(request.POST)
        liabilities_form = forms.LiabilitiesForm(request.POST)
        if assets_form.is_valid() and liabilities_form.is_valid():
            assets = request.user.finances.assets
            if assets is None:
                assets = models.Assets()
            for k in ("cash", "stock", "fixed", "ira"):
                setattr(assets, k, assets_form.cleaned_data[k])
            assets.save()
            request.user.finances.assets = assets
            liabilities = request.user.finances.liabilities
            if liabilities is None:
                liabilities = models.Liabilities()
            for k in ("credit_card", "mortgage", "loan", "other"):
                setattr(liabilities, k, liabilities_form.cleaned_data[k])
            for k in ("mortgage_interest", "loan_interest", "other_interest"):
                setattr(liabilities, k, 0)
            liabilities.save()
            request.user.finances.liabilities = liabilities
            request.user.finances.save()
            return render_to_response("balancesheet_analysis.html",
                RequestContext(request, {
                    "assets_form": assets_form,
                    "liabilities_form": liabilities_form,
                })
            )
    else:
        assets_form = forms.AssetsForm()
        liabilities_form = forms.LiabilitiesForm()
    return render_to_response("balancesheet.html", RequestContext(request, {
        "assets_form": assets_form,
        "liabilities_form": liabilities_form,
    }))

@login_required
def risk(request):
    if "POST" == request.method:
        form = forms.RiskForm(request.POST)
        if form.is_valid():
            # TODO Persist to database?
            return render_to_response("risk_analysis.html",
                RequestContext(request, {
                    "form": form,
                })
            )
    else:
        form = forms.RiskForm()
    return render_to_response("risk.html", RequestContext(request, {
        "form": form,
    }))

@login_required
def report(request):
    return render_to_response("report.html", RequestContext(request, {
    }))
