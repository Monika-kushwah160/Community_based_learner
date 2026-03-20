from django.urls import path
from . import views

app_name = "sessions"

urlpatterns = [

    path("", views.session_list, name="session_list"),

    path("create/", views.create_session, name="create_session"),

    path("<int:pk>/", views.session_detail, name="session_detail"),

    path("join/<int:pk>/", views.join_session, name="join_session"),
    path(
    "feedback/<int:pk>/",
    views.leave_feedback,
    name="leave_feedback"
)
]