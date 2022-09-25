from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from classroom.forms import ContactForm
from classroom.models import Teacher

def home_view(request):
    return render(request,'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'
    
class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = '/classroom/thank_you/' # not 'thank_you.html'
    # success_url = reverse_lazy('classroom:thank_you') # not 'thank_you.html'
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    # automatically implements: `.save`
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')