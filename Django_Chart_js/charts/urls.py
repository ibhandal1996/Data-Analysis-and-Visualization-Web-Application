"""charts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import url
from django.contrib import admin

from MockData.views import mockdata, mockData_Upload, mockData_Download, MockData_update_view, MockData_delete_view, MockData_deleteall_view
from .views import HomeView, get_data, ChartData, DifferenceChartData, DifferenceView


urlpatterns = [
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/diffchart/data/$', DifferenceChartData.as_view()),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^diff/$', DifferenceView.as_view(), name='Diffhome'),
    url(r'^admin/', admin.site.urls),
    url(r'^mockdata/$', mockdata, name="mockdata"),
    url(r'^upload-csv/$', mockData_Upload, name='mockData_upload'),
    url(r'^download-csv/$', mockData_Download, name='mockData_download'),
    url(r'^update/(?P<id>[a-zA-Z0-9]+)$', MockData_update_view, name='mockData_update'),
    url(r'^deleteall/$', MockData_deleteall_view, name='mockData_deleteall'),
    url(r'^delete/(?P<id>[a-zA-Z0-9]+)$', MockData_delete_view, name='mockData_delete'),
]

