# contacts/views.py

from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def home(request):
    return render(request, 'contacts/home.html')

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})

def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('list_contacts')

def search_contacts(request):
    query = request.GET.get('query')
    contacts = Contact.objects.filter(name__icontains=query) if query else Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})
