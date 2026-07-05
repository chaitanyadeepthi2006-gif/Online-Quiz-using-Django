from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    from .forms import RegisterForm
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('/login/')

    else:

        form = RegisterForm()

    return render(request, 'register.html',
                  {'form': form})
def user_login(request):
    from .forms import LoginForm   
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('/quiz/')

            else:

                return render(request,
                              'login.html',
                              {
                                  'form': form,
                                  'error': 'Invalid Username or Password'
                              })

    else:

        form = LoginForm()

    return render(request,
                  'login.html',
                  {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')
from .models import Question

from .models import Question

def quiz(request):

    questions = Question.objects.all()

    if request.method == "POST":

        score = 0
        wrong_answers = []

        for question in questions:

            selected = request.POST.get(str(question.id))

            if selected == question.answer:
                score += 1
            else:
                wrong_answers.append({
                    'question': question.question,
                    'selected': selected,
                    'correct': question.answer
                })

        return render(request, 'result.html', {
            'score': score,
            'total': questions.count(),
            'wrong_answers': wrong_answers
        })

    return render(request, 'quiz.html', {'questions': questions})