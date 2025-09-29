from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .forms import ToolsForm
from .models import Tools


# Create your views here.
def about(request):
    tools = Tools.objects.all().order_by('order')
    return render(request, 'about/about.html', {'tools': tools})


def tools(request):
    tools = Tools.objects.all().order_by('order')
    return render(request, 'about/tools.html', {'tools': tools})


def create_tool(request):
    form = ToolsForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("salvo")
        return redirect('tools')
    else:
        print(form.errors)
    tools = Tools.objects.all().order_by('order')
    return render(request, 'about/tools.html', {'form': form, 'tools': tools})


def delete_tool(request, pk):
    tool = get_object_or_404(Tools, pk=pk)
    tool.delete()
    return redirect('tools')


def move_tool(request, tool_id):
    if request.method == 'POST':
        direction = request.POST.get('direction')
        tool = get_object_or_404(Tools, pk=tool_id)

        if direction == 'up':
            swap_tool = Tools.objects.filter(
                order__lt=tool.order).order_by('-order').first()
        elif direction == 'down':
            swap_tool = Tools.objects.filter(
                order__gt=tool.order).order_by('order').first()
        else:
            swap_tool = None

        if swap_tool:
            tool.order, swap_tool.order = swap_tool.order, tool.order
            tool.save()
            swap_tool.save()

    return redirect('tools')
