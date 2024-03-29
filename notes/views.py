from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from notes import models
from django.views.generic import ListView, DetailView, CreateView
from notes.forms import NoteForm
# Create your views here.

class NotesListView(ListView):
    model = models.Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NoteDetailView(DetailView):
    model = models.Note
    context_object_name = "note"
    template_name  = "notes/note_detail.html"

class NoteCreateView(CreateView):
    model = models.Note
    template_name = "notes/note_form.html"
    form_class = NoteForm
    success_url = reverse_lazy("notes:notes_list")