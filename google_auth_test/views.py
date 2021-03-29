from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView

from .forms import ProfileUpdateForm
from .models import CurrUser


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('user-page')
    else:
        return render(request, 'log.html')


def users_list(request):
    return check_if_logged(request, "list.html")


def user_page(request):
    return check_if_logged(request, "user.html")


def check_if_logged(request, specific_url):
    if request.user.is_authenticated:
        context = {
            'username': request.user.username,
            'curr_path': request.get_full_path(),
        }
        if specific_url == "user.html":
            context['site_user'] = CurrUser.objects.filter(user_id=request.user.id)
        elif specific_url == "list.html":
            context['site_user'] = CurrUser.objects.all()
        return render(request, specific_url, context)
    else:
        return render(request, 'must_be_logged.html')


class UserCreateView(LoginRequiredMixin, CreateView):
    model = CurrUser
    form_class = ProfileUpdateForm
    template_name = 'create_user.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u_id'] = self.request.user.id
        context['auth'] = self.kwargs.get("pk")
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CurrUser
    form_class = ProfileUpdateForm
    template_name = 'update_user.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u_id'] = self.request.user.id
        context['auth'] = self.kwargs.get("pk")
        return context
