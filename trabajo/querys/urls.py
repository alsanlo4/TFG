from django.conf.urls import url
from querys import views

urlpatterns = [
    url('produccion/', views.search, name='search'),
    url('proyectos/', views.searchProject, name='projects'),
    url('articulos/', views.paperPublic, name='papersPublics'),
    url(r'people/([-\w]+)/$', views.personalPages, name='personalPages'),
]
