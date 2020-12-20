from django.urls import path, include
# useria varten
# from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [


    # ex: /polls/
    path('', views.index, name='index'),    
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
    #userlistaus
    path('users', views.user_list, name = "user_list"),
]