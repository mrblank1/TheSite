from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request,'website/index.html')
def contact_us(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        form.fields['subject'].required = False
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.name = 'Unknown'
            contact_instance.save()
            form.save() 
            messages.add_message(request, messages.SUCCESS , "your submitted successfully")
        else:
            messages.add_message(request, messages.ERROR , "your ticket did not validate")
    
    form=ContactForm()
    return render(request,'website/contact.html',{'form':form})
def about(request):
    return render(request,'website/about.html')


