from django.shortcuts import render

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

