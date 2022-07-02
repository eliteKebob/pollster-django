from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import datetime

from .models import Todo

# Get todos and display them
def index(request):
    latest_todo_list = Todo.objects.order_by("-create_date")[:10]
    context = {"latest_todo_list": latest_todo_list}
    return render(request, "todo/index.html", context)


# Show specific todo
def detail(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist!")
    return render(request, "todo/detail.html", {"todo": todo})


# Create a new todo
def create(request):
    if request.method == "POST":
        text = request.POST["text"]
        t = Todo(todo_text=text, create_date=datetime.datetime.now())
        t.save()
        return HttpResponseRedirect(reverse("todo:detail", args=(t.id,)))
    else:
        return render(request, "todo/create.html")
    return render(request, "todo/create.html")


# Edit an existing todo
def edit(request, todo_id):
    t = Todo.objects.get(pk=todo_id)
    return render(request, "todo/edit.html", {"todo": t})


def update(request, todo_id):
    t = Todo.objects.get(pk=todo_id)
    text = request.POST["text"]
    if text:
        t.todo_text = text
        t.save()
        return HttpResponseRedirect(reverse("todo:detail", args=(t.id,)))
    return render(request, "todo/edit.html", {"todo": t})


# Delete a todo
def delete(request, todo_id):
    try:
        t = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist!")
    else:
        t.delete()
        return HttpResponseRedirect(
            reverse(
                "todo:index",
            )
        )
    return render(request, "todo/detail.html", todo_id)
