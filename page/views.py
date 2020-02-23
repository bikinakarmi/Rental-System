from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
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
    queryset = Property.objects.order_by('-date_created')
    # ordering = ('-date_created')
    paginate_by = 6
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = Property.objects.all().order_by('-pk')
    #     return context
        


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

# def login(request):
#     return render(request, 'registration/login.html')

class PropertyCreateView(SuccessMessageMixin,CreateView):
    model = Property
    form_class = PropertyForm
    success_url = '/'
    success_message = "%(title)s was created successfully"

class PropertyDetailView(DetailView):
    model = Property

class PropertyUpdateView(SuccessMessageMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    success_url = '/'
    success_message = "%(title)s was Updated successfully"

def PropertyDeleteView(request,pk):
    if request.method =='POST':
        try:
            obj = Property.objects.get(id=pk)
            obj.delete()
            
        except:
            print('error')
    return redirect('home')


