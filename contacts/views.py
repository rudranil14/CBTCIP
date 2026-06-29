from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from .ai import ask_gemini

@login_required
def home(request):
    return render(request, 'contacts/home.html')


@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('list_contacts')

    else:
        form = ContactForm()

    return render(request, 'contacts/add_contact.html', {'form': form})


@login_required
def list_contacts(request):

    contacts = Contact.objects.filter(user=request.user)

    return render(
        request,
        'contacts/list_contacts.html',
        {'contacts': contacts}
    )


@login_required
def delete_contact(request, contact_id):

    contact = get_object_or_404(
        Contact,
        id=contact_id,
        user=request.user
    )

    contact.delete()

    return redirect('list_contacts')


@login_required
def search_contacts(request):

    query = request.GET.get("query", "").strip()

    if query:

        contacts = Contact.objects.filter(
            user=request.user,
            name__icontains=query
        )

    else:

        contacts = Contact.objects.filter(
            user=request.user
        )

    return render(
        request,
        'contacts/list_contacts.html',
        {'contacts': contacts}
    )


@login_required
def assistant(request):

    query = request.GET.get("query", "")

    result = None
    message = ""

    ai_response = ""

    if query:

        search = query.lower().strip()

        # Contact Search
        if search.startswith("find") or search.startswith("search"):

            search_text = (
                search.replace("find", "")
                .replace("search", "")
                .strip()
            )

            result = Contact.objects.filter(
                user=request.user,
                name__icontains=search_text
            )

            message = f"Searching for '{search_text}'..."

        # List Contacts
        elif search in [
            "show contacts",
            "show all contacts",
            "list contacts"
        ]:

            result = Contact.objects.filter(
                user=request.user
            )

            message = "Showing all your contacts."

        # Emergency
        elif search == "emergency":

            return redirect("emergency")

        # Everything else goes to Gemini
        else:

            ai_response = ask_gemini(query)

    return render(
        request,
        "contacts/assistant.html",
        {
            "query": query,
            "result": result,
            "message": message,
            "ai_response": ai_response,
        },
    )


@login_required
def emergency(request):
    return render(request, 'contacts/emergency.html')