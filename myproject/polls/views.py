from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .models import Choice, Question, Answer
from .forms import CustomUserCreationForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@login_required(login_url='/accounts/login/')
def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer_text = request.POST['answer_text']
    answer = Answer(question = question, answer_text = answer_text)
    answer.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


@login_required(login_url='/accounts/login/')
def index(request):
  if request.method == "GET":
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
  elif request.method == "POST":
    queryParam = request.POST.get("param", "")
    question_list = Question.objects.raw("select id, question_text from polls_question where question_text like '%" + queryParam + "%'")
    template = loader.get_template('polls/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required(login_url='/accounts/login/')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


#useria varten
def dashboard(request):
    return render(request, "users/dashboard.html")

#useria varten
def register(request):
  if request.method == "GET":
      return render(
          request, "users/register.html",
          {"form": CustomUserCreationForm}
      )
  elif request.method == "POST":
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          return redirect(reverse("login")) 
      
      return render(
          request, "users/register.html",
          {"form": form}
      )

# userien listaus

def user_list(request):
  user_list = User.objects.all()
  template = loader.get_template('users/userlist.html')
  context = {
    'user_list': user_list,
    }
  return HttpResponse(template.render(context, request))

