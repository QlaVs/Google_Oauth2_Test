from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, TemplateView

from .forms import ProfileUpdateForm
from .models import CurrUser


class Index(TemplateView):
    template_name = 'log.html'


class UserPageView(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_user'] = CurrUser.objects.filter(user_id=self.request.user.id)
        context['username'] = self.request.user.username
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(self.request, 'must_be_logged.html')
        else:
            return super().dispatch(request, *args, **kwargs)


class UsersListView(LoginRequiredMixin, TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_user'] = CurrUser.objects.all()
        context['username'] = self.request.user.username
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(self.request, 'must_be_logged.html')
        else:
            return super().dispatch(request, *args, **kwargs)


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(self.request, 'must_be_logged.html')
        else:
            return super().dispatch(request, *args, **kwargs)


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(self.request, 'must_be_logged.html')
        else:
            return super().dispatch(request, *args, **kwargs)
