from django.urls import path, include
# useria varten
# from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),

    # ex: /polls/
    path('', views.index, name='index'),    
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    # useria varten?
    path('dashboard/', views.dashboard, name= 'dashboard'),
    
    #url(r"^dashboard/", dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
]