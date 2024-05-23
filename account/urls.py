from django.urls import path
from django.conf import settings
from account import views
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.user_login, name='login')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)