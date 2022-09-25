from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm
# Create your views here.

def home_view(request):
    return render(request,'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'
    
class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = '/classroom/thank_you/' # not 'thanks.html'
    # success_url = reverse_lazy('classroom:thank_you/') # not 'thanks.html'
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)