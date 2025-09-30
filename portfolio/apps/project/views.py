import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project
from ..about.models import Tools
from .forms import ProjectForm
from django.db.models.signals import post_delete
from django.dispatch import receiver


def projects(request):
    filter_type = request.GET.get('type')
    if filter_type:
        projects = Project.objects.filter(type=filter_type)
    else:
        projects = Project.objects.all()

    # Transformar tools em lista
    for project in projects:
        project.tools_list = project.tools.split(',') if project.tools else []

    filters_list = ["Destaques", "RPA", "Dados", "Sistemas"]

    return render(request, 'projects/projects.html', {
        'projects': projects,
        'filters_list': filters_list,
        'filter_type': filter_type
    })


def create_project(request):
    tools = Tools.objects.all().order_by('order')
    projects = Project.objects.all()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            selected_tools = request.POST.getlist("tools")
            tools_str = ", ".join(selected_tools)
            project.tools = tools_str
            project.save()
            messages.success(request, "Projeto adicionado com sucesso!")
            return redirect('projects')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ProjectForm()

    return render(request, 'projects/create_projects.html', {
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
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('create_project')


def view_project(request, pk):
    current_project = get_object_or_404(Project, pk=pk)
    tools_list = [tag.strip()
                  for tag in current_project.tools.split(",")] if current_project.tools else []
    projects = Project.objects.filter(type=current_project.type).exclude(pk=current_project.pk)
    return render(request, 'projects/view_project.html', {
        'current_project': current_project,
        'projects': projects,
        'tools_list': tools_list
    })


def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        # Cria um form apenas com os campos que podem ser editados
        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            # Atualiza apenas os campos permitidos
            project.name = form.cleaned_data['name']
            project.description = form.cleaned_data['description']
            project.tools = ', '.join(request.POST.getlist('tools'))
            project.link_project = form.cleaned_data['link_project']
            project.type = form.cleaned_data['type']
            project.save()

            messages.success(request, "Projeto atualizado com sucesso!")
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)
        selected_tools = [tool.strip() for tool in project.tools.split(',')]

    tools = Tools.objects.all().order_by('order')

    return render(request, 'projects/update_project.html', {
        'form': form,
        'tools': tools,
        'editing': True,
        'project': project,
        'selected_tools': selected_tools,
    })
