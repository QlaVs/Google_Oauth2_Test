from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView
from .forms import ProfileUpdateForm
from .models import Curr_User


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('user-page')
    else:
        return render(request, 'log.html')


def usersList(request):
    if request.user.is_authenticated:
        context = {
            'username': request.user.username,
            'site_user': Curr_User.objects.all()
        }
        return render(request, 'list.html', context)
    else:
        return render(request, 'mustbelogged.html')


def userPage(request):
    if request.user.is_authenticated:
        context = {
            'username': request.user.username,
            'site_user': Curr_User.objects.filter(user_id=request.user.id),
        }
        return render(request, 'user.html', context)
    else:
        return render(request, 'mustbelogged.html')


class UserCreateView(LoginRequiredMixin, CreateView):
    model = Curr_User
    form_class = ProfileUpdateForm
    template_name = 'create_user.html'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u_id'] = self.request.user.id
        context['auth'] = self.kwargs.get("pk")
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Curr_User
    form_class = ProfileUpdateForm
    # fields = ['name', 'image', 'user_info', 'user_id']
    template_name = 'update_user.html'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u_id'] = self.request.user.id
        context['auth'] = self.kwargs.get("pk")
        return context


