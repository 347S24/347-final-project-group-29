# In urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.teacher_home, name='teacher_home'),
    path('add/', views.add_question, name='add_question'),
    path('question_detail/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/submit/', views.student_answer, name='student_answer'),
    path('view-answers/<int:question_id>/', views.view_answers, name='view_answers'),
    path('question/<int:question_id>/view_answers/', views.view_answers, name='view_answers'),
    path('question/delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('thanks/', views.thanks_page, name='thanks_page'),
    path('clear_answers/<int:question_id>/', views.clear_answers, name='clear_answers'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
