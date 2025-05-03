from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("journey/", views.journey, name="journey"),
    path("walk/", views.walk, name="walk"),
    path("during-walk/", views.during_walk, name="during-walk"),
    path("after-walk/", views.after_walk, name="after-walk"),
    path("history/", views.history, name="history"),
    path("sponsorship/", views.sponsorship, name="sponsorship"),
    path("serve/", views.serve, name="serve"),
    path("agape/", views.agape, name="agape"),
    path("about/", views.about, name="about"),
    path("columbus/", views.columbus, name="columbus"),
    path("manchester/", views.manchester, name="manchester"),
    path("phenixcity/", views.phenixcity, name="phenixcity"),
    path("board/", views.board, name="board"),
    path("pilgrim/", views.pilgrim, name="pilgrim"),
    path("event/", views.event, name="event"),
    path("manage_board/", views.update_board, name="manage_board"),
    path("manage_board_confirmation/", views.board_confirmation, name="manage_board_confirmation"),
    path("manage_clusters/", views.add_cluster, name="manage_clusters"),
    path("manage_clusters_confirmation/", views.cluster_confirmation, name="manage_clusters_confirmation")
]