from django.urls import path
from notes import views

urlpatterns = [
    path("", views.NotesListView.as_view(), name="notes_list"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note_detail"),
    path("note_create/", views.NoteCreateView.as_view(), name="note_create"),

]

app_name = "notes"