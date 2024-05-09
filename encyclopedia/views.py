from django.shortcuts import render, redirect

from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if request.method == "POST":
        pass

    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"{title} not found."
        })
    
    content = markdown(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def search(request):
    if request.method == "POST":
        q = request.POST.get('q')
        entries = util.list_entries()
        ansQ = []
        for entry in entries:
            if q.lower() == entry.lower():
                return redirect('encyclopedia:title', title=entry)
            elif q.lower() in entry.lower():
                ansQ.append(entry)

        return render(request, "encyclopedia/index.html", {
            "entries": ansQ, 
            "q": q
        })