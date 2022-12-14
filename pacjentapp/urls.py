"""pacjentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pacjent.views import LoginView, AddNewPatient, Dashboard, SearchPatientView, AddTestResultView, Logout, ResultTest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add_new_patient/', AddNewPatient.as_view(), name='add-new-patient'),
    path('search_patient/', SearchPatientView.as_view(), name='search-patient'),
    path('add_test/', AddTestResultView.as_view(), name='add-test-result'),
    path('test_info/<int:number_test>', ResultTest.as_view(), name='result-test'),
    path('logout/', Logout.as_view(), name='logout'),
]
