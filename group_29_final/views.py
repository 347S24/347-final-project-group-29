from django.shortcuts import render, redirect
from .group29final.group29final.models import Question
from .group29final.group29final.forms import QuestionForm


def teacher_home(request):
    questions = Question.objects.all()
    return render(request, 'teacher_home.html', {'questions': questions})


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})


# def question_detail(request, question_id):
#     question = Question.objects.get(pk=question_id)
#     qr_code_url = generate_qr_code_url(question.text)  # need to implement this 
#     return render(request, 'question_detail.html', {'question': question, 'qr_code_url': qr_code_url})


def student_answer_submission(request, question_id):
    #  student answer submission  here
    pass