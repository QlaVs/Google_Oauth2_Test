from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import UserUpdateView, UserCreateView

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.index, name='my-login'),
    path('userslist/', views.usersList, name='users-list'),
    path('userpage/', views.userPage, name='user-page'),
    path('userpage/create/<int:pk>', UserCreateView.as_view(), name='user-page-create'),
    path('userpage/update/<int:pk>', UserUpdateView.as_view(), name='user-page-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
