from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import SignupForm, PropertyForm 
from .models import Property


# Create your views here.

# @login_required
# def home(request):
#     return render(request,'index.html')


class home(ListView):
    model = Property
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Property.objects.all().order_by('-pk')
        return context


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        
        form = SignupForm()
    return render(request, 'registration/signup.html',{'form':form})

def login(request):
    return render(request, 'registration/login.html')

class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm