# contacts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm

@login_required
def home(request):
    return render(request, 'contacts/home.html')
@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})
@login_required
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})
@login_required
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('list_contacts')
@login_required
def search_contacts(request):
    query = request.GET.get('query')
    contacts = Contact.objects.filter(name__icontains=query) if query else Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})
@login_required
def assistant(request):

    query = request.GET.get("query", "")
    result = None
    message = ""

    if query:

        search = query.lower().strip()

        # Find/Search by name
        if search.startswith("find") or search.startswith("search"):

            search_text = (
                search.replace("find", "")
                      .replace("search", "")
                      .strip()
            )

            result = Contact.objects.filter(
                name__icontains=search_text
            )

            message = f"Searching for '{search_text}'..."

        # Show all contacts
        elif search in ["show all contacts", "list contacts", "show contacts"]:

            result = Contact.objects.all()

            message = "Showing all contacts."

        # Emergency
        elif search == "emergency":

            return redirect("emergency")

        else:

            # Default search
            result = Contact.objects.filter(
                name__icontains=search
            )

            message = f"Searching for '{search}'..."

    return render(
        request,
        "contacts/assistant.html",
        {
            "query": query,
            "result": result,
            "message": message,
        },
    )
@login_required
def emergency(request):
    return render(request, 'contacts/emergency.html')