from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .forms import SignupForm, UserEditForm, UsuarioEditForm
from .models import Usuario
from django.contrib import messages

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['usuario'] = self.request.user
        return ctx


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/profile_edit.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user_form = UserEditForm(instance=request.user)
        usuario_form = UsuarioEditForm(instance=request.user.usuario)
        return render(request, self.template_name, {
            'user_form': user_form,
            'usuario_form': usuario_form
        })

    def post(self, request, *args, **kwargs):
        user_form = UserEditForm(request.POST, instance=request.user)
        usuario_form = UsuarioEditForm(request.POST, request.FILES, instance=request.user.usuario)
        if user_form.is_valid() and usuario_form.is_valid():
            user_form.save()
            usuario_form.save()
            return redirect('profile')
        return render(request, self.template_name, {
            'user_form': user_form,
            'usuario_form': usuario_form
        })

