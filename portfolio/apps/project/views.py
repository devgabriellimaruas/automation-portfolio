import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Project
from ..about.models import Tools
from .forms import ProjectForm


def projects(request):
    filter_type = request.GET.get('type')
    if filter_type:
        projects_qs = Project.objects.filter(type=filter_type)
    else:
        projects_qs = Project.objects.all()

    for project in projects_qs:
        project.tools_list = project.tools.split(',') if project.tools else []

    filters_list = ["Destaques", "RPA", "Dados", "Sistemas"]

    return render(request, 'projects.html', {
        'projects': projects_qs,
        'filters_list': filters_list,
        'filter_type': filter_type
    })


def read_projects(request):
    tools = Tools.objects.all().order_by('order')
    projects = Project.objects.all()

    return render(request, 'read_projects.html', {
        'tools': tools,
        'projects': projects
    })


def view_project(request, pk):
    current_project = get_object_or_404(Project, pk=pk)
    tools_list = [tag.strip() for tag in current_project.tools.split(
        ",")] if current_project.tools else []
    projects_qs = Project.objects.filter(
        type=current_project.type).exclude(pk=current_project.pk)

    return render(request, 'view_projects.html', {
        'current_project': current_project,
        'projects': projects_qs,
        'tools_list': tools_list
    })


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        tools = Tools.objects.all().order_by('order')
        projects = Project.objects.all()

        if form.is_valid():
            project = form.save(commit=False)
            selected_tools = request.POST.getlist("tools")
            project.tools = ", ".join(selected_tools)
            project.save()
            messages.success(request, "Projeto adicionado com sucesso!")
            return redirect('/read/?status=success&msg=Projeto+adicionado+com+sucesso')
        else:
            return redirect(f'/read/?status=error&msg=Erro+ao+atualizar+o+projeto\n{form.errors}')

    return render(request, 'read_projects.html', {
        'form': form,
        'tools': tools,
        'projects': projects,
    })


@receiver(post_delete, sender=Project)
def delete_project_files(sender, instance, **kwargs):
    if instance.video:
        instance.video.delete(save=False)
    if instance.thumbnail:
        instance.thumbnail.delete(save=False)


def delete_project(request, pk):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return redirect('/read/?status=success&msg=Projeto+deletado+com+sucesso')
    else:
        return redirect('/read/?status=error&msg=Erro+ao+deletar+o+projeto')


def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tools = Tools.objects.all().order_by('order')
    selected_tools = [tool.strip() for tool in project.tools.split(
        ',')] if project.tools else []

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            updated_project = form.save(commit=False)
            updated_project.name = form.cleaned_data['name']
            updated_project.description = form.cleaned_data['description']
            updated_project.type = form.cleaned_data['type']
            updated_project.link_project = form.cleaned_data['link_project']
            updated_project.tools = ', '.join(request.POST.getlist('tools'))
            updated_project.save()
            return redirect('/read/?status=success&msg=Projeto+atualizado+com+sucesso')
        else:
            return redirect(f'/read/?status=error&msg=Erro+ao+atualizar+o+projeto\n{form.errors}')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'update_projects.html', {
        'form': form,
        'tools': tools,
        'selected_tools': selected_tools,
        'project': project,
    })
