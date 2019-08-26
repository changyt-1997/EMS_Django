# encoding: utf-8
from django.urls import path,include
from loginapp import views
app_name = 'loginapp'


urlpatterns = [
    path('login/',views.login,name='login'),
    path('regist/',views.regist,name='regist'),
    path('judge_login/',views.judge_login,name='judge_lo'),
    path('judge_regist/',views.judge_regist,name='judge_re'),

]