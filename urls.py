from django.urls import path

from . import views

app_name = "kanban"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/<int:status>", views.update, name="update"),
    path("<int:pk>/", views.HistoryView.as_view(), name="history"),
    path("new_card", views.new_card, name="new_card"),
    path("new_note/<int:task>", views.new_card, name="new_note"),
]
