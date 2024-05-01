import os
from django.views import generic
from django.views.generic import ListView
from django.shortcuts import render, redirect
from peer_instruction.models import Question, Answer
from peer_instruction.forms import QuestionForm
import qrcode
from io import BytesIO
from django.core.files import File
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from PIL import Image


def teacher_home(request):
    questions = Question.objects.all()
    return render(request, 'teacher_home.html', {'questions': questions})


# def QuestionListView(generic.ListView):
#     model = Question


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
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


# def generate_qr_code_url(request, question_id):
#     submission_url = reverse('student_answer', args=[question_id])
#     full_url = request.build_absolute_uri(submission_url)

#     print("Full URL:", full_url)

#     # Generate QR code
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(full_url)
#     qr.make(fit=True)
#     img = qr.make_image(fill='black', back_color='white')

#     buffer = BytesIO()
#     img.save(buffer, format='PNG')
#     # img.save(f"qrcodes/{question_id}.png")
#     buffer.seek(0)

#     # q = Question.objects.get(pk=question_id)
#     # q.qr_code_img = img
#     # q.save()
 
#     response = HttpResponse(buffer.getvalue(), content_type='image/png')
#     response['Content-Disposition'] = 'inline; filename="qr_code.png"'
    
#     # filename = 'qr_code.png'
#     # # Specify the path to your desktop folder
#     # desktop_path = os.path.expanduser("~/Desktop")
#     # # Join the desktop path with the filename
#     # filepath = os.path.join(desktop_path, filename)
#     # # Save the image to the specified filepath
#     # img.save(filepath)
#     # print("QR code image saved to:", filepath)

#     return response


def view_answers(request):
    # Retrieve all answers from the database
    answers = Answer.objects.all()
    context = {'answers': answers}
    return render(request, 'view_answers.html', context)


def student_answer(request, question_id):
    if request.method == 'POST':
        username = request.POST.get('username')
        answer_text = request.POST.get('answer')
        answer = Answer(username=username, answer_text=answer_text, question_id=question_id)
        answer.save()
        return redirect('thanks_page')
    else:
        return render(request, 'student_answer.html', {'question_id': question_id})


def thanks_page(request):
    return render(request, 'thanks_page.html')
