from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from fellowship.forms import TeamForm
from fellowship.models import Team, Member


def hello(request):
    return HttpResponse("Greetings, travellers.")


def team_create(request):
    template = "fellowship/team_form.html"
    context = {}

    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("team_list")
    context['form'] = form
    return render(request, template, context)


def team_list(request):
    template = "fellowship/team_list.html"
    context = {"teams": Team.objects.all()}
    return render(request, template, context)


def team_retrieve(request, id):
    template = "fellowship/team_detail.html"
    context = {"team": Team.objects.get(id=id)}
    return render(request, template, context)


def team_update(request, id):
    template = "fellowship/team_form.html"
    context = {}
    obj = get_object_or_404(Team, id=id)

    form = TeamForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("team_list")
    context['form'] = form
    return render(request, template, context)


def team_delete(request, id):
    template = "fellowship/team_delete.html"
    context = {}
    obj = get_object_or_404(Team, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect("team_list")
    return render(request, template, context)


class MemberCreate(CreateView):
    model = Member
    fields = ['first_name', 'last_name', 'race', 'team']
    success_url = reverse_lazy('member_list')


class MemberList(ListView):
    model = Member


class MemberRetrieve(DetailView):
    model = Member


class MemberUpdate(UpdateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('member_list')


class MemberDelete(DeleteView):
    model = Member
    success_url = reverse_lazy('member_list')
