import hashlib

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import FormView, UpdateView

from MediDonor.models import nominee, Organ, post
from MediOrganisation.models import organisation

from MediUser.forms import SignUpForm, PasswordChangeForm
from MediUser.models import MediUser


def HomePage(request):
    return render(request, 'MediUser/home.html')


def DonorPage(request):
    return render(request, 'MediUser/base.html')


def profilepage(request):
    return render(request, 'MediUser/profile.html')


class RegisterPage(SuccessMessageMixin, FormView):
    template_name = 'MediUser/signup.html'
    form_class = SignUpForm
    success_message = "Your data saved successfully"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = MediUser()
        user1 = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'])
        user1.set_password(form.cleaned_data['password1'])
        user.username = form.cleaned_data['username']
        user.email = form.cleaned_data['email']
        user.mobile = form.cleaned_data['mobile']
        password = form.cleaned_data["password1"].encode()
        pwd = hashlib.sha256(password)
        hashing = pwd.hexdigest()
        user.password = hashing
        user1.save()
        user.save()

        # newthing learned
        # user.create(**form.cleaned_data)

        return super(RegisterPage, self).form_valid(form)


class LogingView(LoginView):
    template_name = 'MediUser/login.html'


class UserUpdateView(UpdateView):
    template_name = 'MediUser/signup.html'
    success_url = reverse_lazy('profile')
    model = MediUser
    fields = [
        "email",
        "mobile",
    ]


class PasswordUpdateView(UpdateView):
    template_name = 'MediUser/signup.html'
    success_url = reverse_lazy('profile')
    form_class = PasswordChangeForm
    queryset = MediUser.objects.all()


class LogingOutView(LogoutView):
    template_name = 'MediUser/logout.html'


@login_required
def profile_page(request):
    queryset = User.objects.get(username=request.user.username)
    queryset2 = MediUser.objects.filter(username=request.user.username).first()
    queryset3 = nominee.objects.filter(donor_id_id=queryset2.id).all()
    queryset4 = Organ.objects.filter(user_id_id=queryset2.id).all()
    queryset5 = organisation.objects.filter(donor_id_id=queryset2.id).all()
    queryset6 = post.objects.filter(user_id_id=queryset2.id).all()
    print(queryset6)
    context = {
        "profile_user": queryset,
        "detail_user": queryset2,
        "nominee_user": queryset3,
        "organs": queryset4,
        "organisation": queryset5,
        "post": queryset6,
    }
    return render(request, 'MediUser/profile.html', context)
