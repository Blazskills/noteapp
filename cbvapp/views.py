from django.contrib import messages
from django.db.utils import IntegrityError
from .models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

from cbvapp.forms import SignUpForm
from .models import Note, User
from django.views import generic
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import NoteCreationForm, NoteUpdateForm


# function based view
# login view
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("blog:dashboard")
    page = "login"
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("blog:dashboard")
        messages.info(request, "Wrong email or password")
        referrer_back = request.META["HTTP_REFERER"]
        return redirect(referrer_back)
    context = {
        "page": page,
    }
    return render(request, "dashboard/register.html", context)


# Register view
def register(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
        return redirect("blog:dashboard")
    if request.method == "POST":
        reg_form = SignUpForm(request.POST)
        if reg_form.is_valid():
            # after user fill the form correctly
            username = reg_form.cleaned_data.get("email")
            user = reg_form.save(commit=False)
            user.username = username
            user.save()
            print("done validating and saving")
            messages.success(request, "Account created successfully")
            return redirect("blog:login")
        else:
            password1 = reg_form.cleaned_data.get("password1")
            password2 = reg_form.cleaned_data.get("password2")
            email = reg_form.cleaned_data.get("email")

            if len(password1) < 8:
                messages.warning(request, "Password too short")
                return redirect("blog:register")
            if password1 != password2:
                messages.warning(request, "password does not match")
                return redirect("blog:register")
            try:
                match = User.objects.get(email=email)
                return match
            except:
                messages.warning(request, "Email already exist")
                return redirect("blog:register")
    return render(request, "dashboard/register.html")


# Blog views
class IndexView(generic.ListView):
    template_name = "cbv/index.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.all()[:5]


# Admin dashboard views
@method_decorator(login_required(login_url="blog:login"), name="dispatch")
class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        notes = Note.objects.all()
        context = {"note": notes}
        context["message"] = "context!"
        return context


# Notpost view
@method_decorator(login_required(login_url="blog:login"), name="dispatch")
class BlogPostView(TemplateView):
    template_name = "dashboard/blogpost.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogPostView, self).get_context_data(*args, **kwargs)
        form = NoteCreationForm()
        context = {"forms": form}
        return context

    def post(self, request):
        form = NoteCreationForm(request.POST)
        if form.is_valid:
            note_obj = form.save(commit=False)
            note_obj.posted_by = request.user
            note_obj.save()
            messages.success(request, "Post Created")
            return redirect("blog:dashboard")


@login_required
def update(request, id):
    page = "update"
    note_to_update = Note.objects.get(id=id)
    form = NoteUpdateForm(instance=note_to_update)
    if request.method == "POST":
        form = NoteUpdateForm(request.POST)
        if form.is_valid():
            note_to_update.Note_Title = form.cleaned_data["Note_Title"]
            note_to_update.Description = form.cleaned_data["Description"]
            note_to_update.Note_Priority = form.cleaned_data["Note_Priority"]
            note_to_update.Note_Color = form.cleaned_data["Note_Color"]
            note_to_update.Reminder_Date = form.cleaned_data["Reminder_Date"]
            note_to_update.save()
            messages.success(request, "Post updated Successfully")
            return redirect("blog:dashboard")
        messages.warning(request, "Invalid input")
        referrer_back = request.META["HTTP_REFERER"]
        return redirect(referrer_back)
    context = {"note": note_to_update, "forms": form, "page": page}
    return render(request, "dashboard/blogpost.html", context)


@login_required()
def deletepost(request, id):
    note_to_delete = Note.objects.get(id=id)
    note_to_delete.delete()
    messages.success(request, "Post deleted Successfully")
    return redirect("blog:dashboard")


def logoutpage(request):
    logout(request)
    return redirect("blog:login")


# class DashboardRegisterView(TemplateView):
#     template_name = 'dashboard/register.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(DashboardRegisterView,self).get_context_data(*args, **kwargs)
#         context['message'] = 'context!'

#         return context


# def register(request):
#     if request.method == "POST":
#         reg_form=SignUpForm(request.POST)
#         if reg_form.is_valid():
#             superuser=reg_form.cleaned_data['is_superuser']
#             username = reg_form.cleaned_data.get('email')
#             print(superuser)
#             print(username)
#             try:
#                  user = User.objects.create_user(username,email,password1)
#             User = reg_form.save(commit = False)
#             print(User)
#             # if User.objects.filter(username).exists():
#             #      print('Username already exist.')
#             User.username=username
#             User.save()
#             print('done validating and saving')
#         else:
#           print('Failed')

#     return render(request, 'dashboard/register.html')


# Create your views here.

# class IndexView(generic.ListView):
#     def get(self, request):
#         blogs = Blog.objects.all()
#         return render('cbv/index.html')

# class ContactView(View):
#     def get(self, request):
#          Code block for GET request

#     def post(self, request):
#         Code block for POST request


# urlpatterns = [
#     url(r'contact/$', views.ContactView.as_view(), name='contact'),
# ]
