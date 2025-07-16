from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("about/", views.AboutTemplateView.as_view(), name="about"),
    # queries
    path("queries/", views.QueryListView.as_view(), name="query_list"),
    path(
        "query_detail/<int:pk>/", views.QueryDetailView.as_view(), name="query_detail"
    ),
    path("query_edit/<int:pk>/", views.QueryUpdateView.as_view(), name="query_edit"),
    path(
        "query_delete/<int:pk>/", views.QueryDeleteView.as_view(), name="query_delete"
    ),
    path("query_create/", views.QueryCreateView.as_view(), name="query_create"),
    # query_groups
    path("query_groups/", views.QueryGroupListView.as_view(), name="query_group_list"),
    path(
        "query_group_detail/<int:pk>/",
        views.QueryGroupDetailView.as_view(),
        name="query_group_detail",
    ),
    path(
        "query_group_edit/<int:pk>/",
        views.QueryGroupUpdateView.as_view(),
        name="query_group_edit",
    ),
    path(
        "query_group_delete/<int:pk>/",
        views.QueryGroupDeleteView.as_view(),
        name="query_group_delete",
    ),
    path(
        "query_group_create/",
        views.QueryGroupCreateView.as_view(),
        name="query_group_create",
    ),
]
