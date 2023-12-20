# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib import messages
from .models import Journal
from .forms import JournalForm, JournalUpdateForm
from .choices import JOURNAL_STATUS, JOURNAL_TYPE


# journals/views.py
# from rest_framework import generics
# from .serializers import JournalSerializer

# class JournalListCreateView(generics.ListCreateAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer



def journal_list(request):
    # query = request.GET.get('q')
    # print(f"QUery ########### {query}")
    journals = Journal.objects.order_by('-write_date')
    search = request.GET
    
    if 'title' in search:
        title = search['title']
        if title:
            journals = journals.filter(title__icontains=title)

    if 'year' in search:
        year = search['year']
        if year:
            journals = journals.filter(write_date__icontains=year)


    if 'journal_type' in search:
        journal_type = search['journal_type']
        if journal_type:
            journals = journals.filter(journal_type__iexact=journal_type)

    if 'status' in search:
        status = search['status']
        if status:
            journals = journals.filter(status__iexact=status)

    # if query:
    #     journals = journals.filter(
    #         Q(title__icontains=query) | Q(write_date__icontains=query)
    #     )

    context = {
        'journals': journals,
        'journal_type': JOURNAL_TYPE,
        'status': JOURNAL_STATUS,
    }
    return render(request, 'publications/journal_list.html', context)



class JournalCreateView(SuccessMessageMixin, CreateView):
    model = Journal
    form_class = JournalForm  # Replace with your actual form
    template_name = 'publications/journal_create.html'  # Replace with your template name
    success_url = reverse_lazy('publications:journal_list')  # Replace with your success URL
    success_message =  "%(journal_name)s created successfully"

    def form_valid(self, form):
        form.instance.writer = self.request.user  # Set the writer to the current user
        return super().form_valid(form)




def journal_update(request, pk):
    journal = get_object_or_404(Journal, pk=pk)

    if request.method == 'POST':
        form = JournalUpdateForm(request.POST, request.FILES, instance=journal)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Update Successful')
            return redirect('publications:journal_list')
    else:
        form = JournalUpdateForm(instance=journal)

    context = {
        'form': form,
    }

    return render(request, 'publications/journal_update.html', context)


class JournalDetailView(DetailView):
    model = Journal
    template_name = 'publications/journal_detail.html'
    context_object_name = 'journal'




