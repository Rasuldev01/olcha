from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistraionForm, LoginForm

class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Ro'yhatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistraionForm()
        })

    def post(self, request):
        form = RegistraionForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, _("Siz muvaffaqiyatli ro'yhatdan o'tingiz!"))
            return redirect('main.index')
        return render(request, 'layouts/form.html', {
            'form': form
        })

class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Tizimga kirish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if not user is None:
                login(request, user)
                messages.success(request, _("Xush kelibsiz, {}!").format(user.username))

                return redirect('main:index')

            form.add_error('password', _("Login va/yoki parol noto'g'ri."))

        return render(request, 'layouts/form.html', {
            'form': form
        })