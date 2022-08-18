from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render

from vacancy_app.models import Company, Specialty, Vacancy


# Create your views here.
def main_view(request):
    context = {}
    context['specialties'] = list(Specialty.objects.all())
    context['companies'] = list(Company.objects.all())
    return render(request, "vacancy_app/index.html", context=context)


def vacancies_view(request):
    context = {}
    context['all'] = True
    context['vacancies'] = Vacancy.objects.all()
    return render(request, "vacancy_app/vacancies.html", context=context)


def vacancies_cat_view(request, category_name):
    context = {}
    context['all'] = False
    context['category_name'] = Specialty.objects.get(code=category_name).title
    context['vacancies'] = Vacancy.objects.filter(specialty__code=category_name)
    return render(request, "vacancy_app/vacancies.html", context=context)


def vacancy_view(request, vacancy_id):
    context = {}
    context['vacancy'] = Vacancy.objects.get(id=vacancy_id)
    return render(request, "vacancy_app/vacancy.html", context=context)


def company_view(request, company_id):
    context = {}
    company = Company.objects.get(id=company_id)
    context['company'] = company
    context['vacancies'] = Vacancy.objects.filter(company__id=company_id)
    return render(request, "vacancy_app/company.html", context=context)


def custom_handler500(request):
    # Call when PermissionDenied raised
    return HttpResponseServerError('Внутрення ошибка сервера!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')
