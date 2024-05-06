import os
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView
from django.shortcuts import render, redirect
from peer_instruction.models import Question, Answer
from peer_instruction.forms import QuestionForm, AnswerForm
import qrcode
from io import BytesIO
from django.core.files import File
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from PIL import Image


def teacher_home(request):
    questions = Question.objects.all()
    return render(request, 'teacher_home.html', {'questions': questions})


# def QuestionListView(generic.ListView):
#     model = Question


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid form')
            form.save()
            return redirect('teacher_home')
        else:
            print('invalid form?')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})


def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('teacher_home')


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # qr_code_url = generate_qr_code_url(request, question_id)  # This now points to a static URL , 'qr_code_url': qr_code_url
    return render(request, 'question_detail.html', {'question': question})


def view_answers(request, question_id):
    # Retrieve all answers from the database
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'view_answers.html', {'question': question, 'answers': answers})


def student_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        print("\n\n\n\n\n anwser submitted by post")
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.instance.question = question
            form.save()
            messages.success(request, 'Your answer has been submitted successfully!')
            return redirect('thanks_page')
        else:
            messages.error(request, 'Please fill out all required fields.')
    else:
        print("\n\n\n\n\n anwser submitted not post")
        form = AnswerForm()
    return render(request, 'student_answer.html', {'form': form, 'question': question})


def thanks_page(request):
    return render(request, 'thanks_page.html')


def clear_answers(request, question_id):
    if request.method == 'POST':
        # Delete or clear answers logic here
        # For example, to clear all answers:
        Answer.objects.filter(question_id=question_id).delete()
    return redirect('view_answers', question_id=question_id)
