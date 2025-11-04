from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, ProfileView, ProfileEditView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='editar_perfil'),
    
]


