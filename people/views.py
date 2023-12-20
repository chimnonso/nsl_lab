from django.shortcuts import render
from .models import Bio
from django.views.generic import CreateView, UpdateView, DetailView

# Create your views here.

def professors_list(request):

    bio = Bio.objects.filter(position=1)
    context = {
        'bios': bio,
        'total': len(bio)
        }
    return render(request, 'people/professors.html', context)

def post_docs_list(request):

    bio = Bio.objects.filter(position=2)
    context = {
        'bios': bio,
        'total': len(bio)
        }
    return render(request, 'people/post_docs.html', context)


class PostDoctDetailView(DetailView):
    model = Bio
    template_name = 'people/post_doc_detail.html'
    context_object_name = 'post_doc'
