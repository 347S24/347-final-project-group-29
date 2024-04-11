# In urls.py

from django.urls import path
from ... import views

urlpatterns = [
    path('home/', views.teacher_home, name='teacher_home'),
    path('add/', views.add_question, name='add_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/submit/', views.student_answer_submission, name='student_answer_submission'),
]
