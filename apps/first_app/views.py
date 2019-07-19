from django.shortcuts import render, HttpResponse, redirect
from apps.first_app.models import *
from django.contrib import messages

# redirect localhost/8000 to localhost/8000/shows
def redirect_url(request):
    return redirect("/shows")

# read all page
def read_all_show(request):
    all_shows = Show.objects.all()
    context = {
        "all_shows": all_shows
    }
    return render(request, "first_app/read-all-show.html", context)

# create page
def create_show(request):
    return render(request, "first_app/create-show.html")

# add button
def add_show(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/shows/new')
    else:
        show = Show.objects.create(title=request.POST["show_title"], network=request.POST["show_network"],
                                releaseDate=request.POST["show_date"], description=request.POST["show_description"])
        return redirect("/shows/" + str(show.id))

# read one page
def read_one_show(request, id):
    show_id = int(id)
    show = Show.objects.get(id=show_id)
    context = {
        "show": show
    }
    return render(request, "first_app/read-one-show.html", context)

# update button
def update_show(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/" + str(id) + "/edit")
    else:
        show_id = int(id)
        show = Show.objects.get(id=show_id)
        show.title = request.POST["show_title"]
        show.network = request.POST["show_network"]
        show.releaseDate = request.POST["show_date"]
        show.description = request.POST["show_description"]
        show.save()
        return redirect("/shows/" + str(id) + "/edit")

# update page
def edit_show(request, id):
    show_id = int(id)
    show = Show.objects.get(id=show_id)
    context = {
        "show": show
    }

    return render(request, "first_app/update-show.html", context)

# delete show
def delete_show(request, id):
    show_id = int(id)
    show = Show.objects.get(id=show_id)
    show.delete()

    return redirect("/shows")