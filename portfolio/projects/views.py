import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project
from tools.models import Tools
from .forms import ProjectForm
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Exemplo:


def get_projects(request):
    filter_type = request.GET.get('type')
    if filter_type:
        projects = Project.objects.filter(type=filter_type)
    else:
        projects = Project.objects.all()

    # Transformar tags em lista
    for project in projects:
        project.tags_list = project.tags.split(',') if project.tags else []

    filters_list = ["Destaques", "RPA", "Dados", "No/Low Code"]

    return render(request, 'projects/projects.html', {
        'projects': projects,
        'filters_list': filters_list,
        'filter_type': filter_type
    })


def post_project(request):
    tools = Tools.objects.all().order_by('order')

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            selected_tags = request.POST.getlist("tags")
            tags_str = ", ".join(selected_tags)
            project.tags = tags_str
            project.save()
            messages.success(request, "Projeto adicionado com sucesso!")
            return redirect('projects')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ProjectForm()

    return render(request, 'projects/add_projects.html', {
        'form': form,
        'tools': tools,
    })


@receiver(post_delete, sender=Project)
def delete_project_files(sender, instance, **kwargs):
    if instance.video:
        instance.video.delete(save=False)
    if instance.thumbnail:
        instance.thumbnail.delete(save=False)


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('projects')


def view_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tags_list = [tag.strip() for tag in project.tags.split(",")] if project.tags else []
    projects = Project.objects.filter(type=project.type).exclude(pk=project.pk)
    return render(request, 'projects/view_project.html', {
        'project': project,
        'projects': projects,
        'tags_list': tags_list
    })
