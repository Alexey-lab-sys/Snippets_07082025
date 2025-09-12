from django.urls import path
from MainApp import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('snippets/add/', views.add_snippet_page, name='snippets-add'),
    path('snippets/list/', views.snippets_page, name='snippets-list'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
