"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Views da aplicação
from chamados import views

# JWT views da biblioteca simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Para servir arquivos de mídia no modo dev
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Painel de administração Django
    path('admin/', admin.site.urls),

    # Rotas web (interface HTML do projeto)
    path('', include('chamados.urls')),

    # Rotas da API REST (endpoints JSON)
    path('api/', include('chamados.urls_api')),

    # Login e logout da interface web
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Endpoints para autenticação JWT (API)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Rota para servir arquivos de mídia no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    