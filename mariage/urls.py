"""
URL configuration for mariage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from formulaire.views import*

urlpatterns = [
    path('book/', admin.site.urls),
    path('', generer_lien, name='generer_lien'),
    path('formulaire', remplir_formulaire, name='remplir_formulaire'),
    path('liste/', liste_liens, name='liste_liens'),
    path('base/', base, name='base'),
    path('erreur/', success, name='success'),
    path('telecharger_pdf/', telecharger_pdf, name='telecharger_pdf'),
    path('telecharger_xlsx/', telecharger_xlsx, name='telecharger_xlsx'),
    path('accounts/login/',authetification, name='authetification'),
    path('deco',logout_view, name='logout_view'),
]
