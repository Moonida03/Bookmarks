from django.urls import path
from django.conf import settings
from account import views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name='logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)