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
    # queries_in_groups
    path(
        "queries_in_groups/",
        views.QueryInGroupListView.as_view(),
        name="query_in_group_list",
    ),
    path(
        "query_in_group_detail/<int:pk>/",
        views.QueryInGroupDetailView.as_view(),
        name="query_in_group_detail",
    ),
    path(
        "query_in_group_edit/<int:pk>/",
        views.QueryInGroupUpdateView.as_view(),
        name="query_in_group_edit",
    ),
    path(
        "query_in_group_delete/<int:pk>/",
        views.QueryInGroupDeleteView.as_view(),
        name="query_in_group_delete",
    ),
    path(
        "query_in_group_create/",
        views.QueryInGroupCreateView.as_view(),
        name="query_in_group_create",
    ),
]
