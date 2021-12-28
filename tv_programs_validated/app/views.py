from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Show
from django.contrib import messages

# Create your views here.
def add_new_show_page(request):
    return render(request, "app/add-show.html")

def create_show(request):
    post = request.POST
    
    errors = Show.objects.basic_validator(post)
    
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        
        return redirect("/shows/new")
    
    created_show = Show.objects.create(
        title = post["title"],
        network = post["network"],
        release_date = post["release_date"],
        description = post["description"],
    )
    return redirect(f"/shows/{created_show.id}")

def show_details(request, show_id):
    context = {
        "individual_show": Show.objects.get(id=show_id)
    }
    return render(request, "app/show-details.html", context)

def delete_show(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect("/shows")

def all_shows(request):
    context = {
        "shows" : Show.objects.all()
    }
    return render(request, "app/all-shows.html", context)

def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.release_date = show.release_date.strftime("%Y-%m-%d")
    context = {
        "show" : show
    }
    
    return render(request, "app/edit-show.html", context)

def update_show(request, show_id):
    show = Show.objects.get(id=show_id)
    
    post = request.POST
    
    errors = Show.objects.basic_validator(post)
    
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        
        return redirect(f"/shows/{show_id}/edit")
    
    show.title = post["title"]
    show.network = post["network"]
    show.release_date = post["release_date"]
    show.description = post["description"]
    
    show.save()
    return redirect(f"/shows/{ show_id }")