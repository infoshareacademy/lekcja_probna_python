from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.hello, name="hello"),
    path('teams', views.team_list, name='team_list'),
    path('teams/create', views.team_create, name='team_create'),
    path('teams/retrieve/<int:id>', views.team_retrieve, name='team_retrieve'),
    path('teams/update/<int:id>', views.team_update, name='team_update'),
    path('teams/delete/<int:id>', views.team_delete, name='team_delete'),

    path('members', views.MemberList.as_view(), name='member_list'),
    path('members/create', views.MemberCreate.as_view(), name='member_create'),
    path('members/retrieve/<int:pk>', views.MemberRetrieve.as_view(), name='member_retrieve'),
    path('members/update/<int:pk>', views.MemberUpdate.as_view(), name='member_update'),
    path('members/delete/<int:pk>', views.MemberDelete.as_view(), name='member_delete'),
]
