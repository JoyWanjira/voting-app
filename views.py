from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
# from django.contrib.auth.models import User,Group,Question,Choice
# from rest_framework import viewsets
# from rest_framework import permissions
# from .serializers import UserSerializer,GroupSerializer,QuestionSerializer,ChoiceSerializer


#Create your views here.
# def index (request):
#     return HttpResponse("Hello, world.You're at the polls index")

# def detail(request,question_id):
#     return HttpResponse ("You're looking at question %s." %question_id)

# def results(request,question_id):
#     response="You're looking at the results of the question %s."
#     return HttpResponse(response %question_id)

# def vote (request,question_id):
#     return HttpResponse("You've voted on question %s." %question_id)

# def index(request):
#     latest_question_list=Question.objects.order_by('pub_date')[:5]
#     output=','.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context,request))


def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request,'polls/detail.html',{'question':question})
def results(request,questiont_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

def homepageview(request):
    print(Choice.objects.first().question.id)
    context={'Question':Question.objects.all(),'Choice':Choice.objects.all()}
    return render(request, 'polls/homepage.html', context)



def vote (request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        # import pdb;pdb.set_trace()
        selected_choice=question.choice_set.get(pk=request.POST['choice_id'])
    except (KeyError,Choice.DoesNotExist):
        return render (request,'polls/detail.html',{'question':question,'error_message':"You didnt select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



# class UserViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all().order_by('date_joined')
#     serializer_class=UserSerializer
#     permission_classes=[permissions.IsAuthenticated]

# class GroupViewSet(viewsets.ModelViewSet):
#     queryset=Group.objects.all()
#     serializer_class=GroupSerializer
#     permission_classes=[permissions.IsAuthenticated]

# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset=Question.objects.all()
#     serializer_class=QuestionSerializer
#     permission_classes=[permissions.IsAuthenticated]

# class ChoiceViewSet(viewsets.ModelViewSet):
#     queryset=Choice.objects.all()
#     serializer_class=ChoiceSerializer
#     permission_classes=[permissions.IsAuthenticated]