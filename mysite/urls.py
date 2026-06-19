

from django.contrib import admin
from django.urls import path, include
from . import views
from schema_graph.views import Schema


urlpatterns = [
    path('schema/', Schema.as_view()),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name="accounts"),
    path('polls/', include('polls.urls'), name="polls"),
]
