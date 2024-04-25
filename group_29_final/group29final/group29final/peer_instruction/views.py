from django.views import generic
from django.views.generic import ListView
from django.shortcuts import render, redirect
from peer_instruction.models import Question
from peer_instruction.forms import QuestionForm
import qrcode
from io import BytesIO
from django.core.files import File


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


def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    # qr_code_url = generate_qr_code_url(question.text)  # need to implement this 
    return render(request, 'question_detail.html', {'question': question})


# def generate_qr_code_url(data):
#     # Generate the QR code image
#     qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
#     qr.add_data(data)
#     qr.make(fit=True)

#     # Create an in-memory PNG image
#     img = qr.make_image(fill_color="black", back_color="white")

#     # Save the image to a file or return the URL
#     # For simplicity, let's just save it to a temporary file
#     filename = '/path/to/your/static/qr_codes/qr_code.png'  # Specify the path where you want to save the QR code image
#     img.save(filename)

#     # Assuming your Django project serves static files from a 'static' directory
#     qr_code_url = '/static/qr_codes/qr_code.png'  # This will be the URL to access the QR code image
#     return qr_code_url


def student_answer_submission(request, question_id):
    #  student answer submission  here
    pass

def generate_qr_code_url(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    filename = 'qr_codes/qr-{}.png'.format(text[:10])
    filebuffer = File(buffer, name=filename)
    return filebuffer.url