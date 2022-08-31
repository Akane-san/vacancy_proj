from django.utils import timezone
from django.db.models import Q 
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import TemplateView, ListView

from vacancy_app.forms import *
from vacancy_app.models import *


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
    try:
        context = {}
        context['category_name'] = Specialty.objects.get(code=category_name).title
        context['vacancies'] = Vacancy.objects.filter(specialty__code=category_name)
        return render(request, "vacancy_app/vacancies.html", context=context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Ресурс не найден!')

def vacancy_view(request, vacancy_id):
    context = {}
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
        context['vacancy'] = vacancy
        if request.method == 'POST':
            form = ApplicationForm(request.POST, request.FILES)
            if form.is_valid():
                args= form.save(commit=False) # принимаем данные от формы
                setattr(args, 'user', User.objects.get(id=request.user.id))
                setattr(args, 'vacancy', Vacancy.objects.get(id=vacancy_id))
                args.save()
                return redirect(reverse('vacancy_send', kwargs={'vacancy_id': vacancy_id}))
        else:
            form = ApplicationForm()
        context['form'] = form
        return render(request, "vacancy_app/vacancy.html", context=context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Ресурс не найден!')

def company_view(request, company_id):
    context = {}
    company = Company.objects.get(id=company_id)
    context['company'] = company
    context['vacancies'] = Vacancy.objects.filter(company__id=company_id)
    return render(request, "vacancy_app/company.html", context=context)

def vacancy_send_view(request,vacancy_id):
    context = {}
    return render(request, "vacancy_app/sent.html", context=context)

def mycompany_letsstart_view(request):
    context = {}
    return render(request, "vacancy_app/company-create.html", context=context)

def mycompany_create_view(request):
    try:
        has_company = (request.user.company is not None)
        company = Company.objects.get(id=request.user.company.id)
        if request.method == "POST":
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                company = form.save(commit=False)
                company.owner = request.user
                company.save()
                return redirect('mycompany_create')
        else:
            form = CompanyForm(instance=company)
        return render(request, "vacancy_app/company-edit.html", {'form': form})
    except Company.DoesNotExist:
        if request.method == "POST":
            form = CompanyForm(request.POST, request.FILES)
            if form.is_valid():
                company = form.save(commit=False)
                company.owner = request.user
                company.save()
                return redirect('mycompany_create')
        else:
            form = CompanyForm()
        return render(request, "vacancy_app/company-edit.html", {'form': form})

def mycompany_vacancies_view(request):
    context = {}
    try:
        vacancies = Vacancy.objects.filter(company = request.user.company)
        context['vacancies'] = vacancies
        if(vacancies):
            context['company'] = True
    except ObjectDoesNotExist:
        pass
    return render(request, "vacancy_app/vacancy-list.html", context=context)
    

def mycompany_vacancies_create_view(request):
    context = {}
    context['vacancies'] = Vacancy.objects.filter(company = request.user.company)
    try:
        if request.method == "POST":
            form = VacancyForm(request.POST, request.FILES)
            if form.is_valid():
                vacancy = form.save(commit=False)
                vacancy.company = request.user.company
                vacancy.published_at = timezone.now()
                vacancy.save()
                return redirect('mycompany_vacancies')
        else:
            form = VacancyForm()
        context['form'] = form
        return render(request, "vacancy_app/vacancy-edit.html", context=context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Ресурс не найден!')

def mycompany_vacancy_view(request,vacancy_id):
    context = {}
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
        context['vacancy'] = vacancy
        context['applications'] = Application.objects.filter(vacancy=vacancy)
        if request.method == "POST":
            form = VacancyForm(request.POST, instance=vacancy)
            if form.is_valid():
                vacancy = form.save(commit=False)
                vacancy.company = request.user.company
                #vacancy.published_at = timezone.now()
                vacancy.save()
                return redirect('mycompany_vacancies')
        else:
            form = VacancyForm(instance=vacancy)
        context['form'] = form
        return render(request, "vacancy_app/vacancy-edit.html", context=context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Ресурс не найден!')

def search_view(request):
    context = {}
    query = request.GET.get('q')
    context['vacancies'] = Vacancy.objects.filter(
            Q(title__icontains=query) | Q(skills__icontains=query) | Q(description__icontains=query)
        )
    return render(request, "vacancy_app/search.html", context=context)
'''
class SearchResultsView(ListView):
    model = Vacancy
    template_name = 'vacancy_app/search.html'
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        print(query)
        vacancies = Vacancy.objects.filter(
            Q(title__icontains=query) | Q(skills__icontains=query) | Q(description__icontains=query)
        )
        print(vacancies)
        return vacancies
'''
def myresume_letsstart_view(request):
    context = {}
    return render(request, "vacancy_app/resume-create.html", context=context)

def myresume_create_view(request):
    context = {}
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('myresume')
    else:
        form = ResumeForm()
    context['form'] = form
    return render(request, "vacancy_app/resume-edit.html", context=context)

def myresume_view(request):
    context = {}
    resume = Resume.objects.get(id=request.user.resume.id)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('myresume')
    else:
        form = ResumeForm(instance=resume)
    context['form'] = form
    return render(request, "vacancy_app/resume-edit.html", context=context)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = 'login'
    template_name = 'vacancy_app/register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(LoginView):
    redirect_authenticated_user = True
    success_url = 'main'
    template_name = 'vacancy_app/login.html'


def logout_view(request):
    logout(request)
    return redirect('main')

def custom_handler500(request):
    # Call when PermissionDenied raised
    return HttpResponseServerError('Внутрення ошибка сервера!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')
