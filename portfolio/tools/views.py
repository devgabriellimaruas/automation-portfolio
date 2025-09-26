from django.shortcuts import render, get_object_or_404, redirect
from .models import Tools
from .forms import ToolsForm


def get_tools(request):
    tools = Tools.objects.all().order_by('order')
    return render(request, 'tools/add_tools.html', {'tools': tools})


def post_tool(request):
    form = ToolsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('get_tools')
    return render(request, 'tools/add_tools.html', {'form': form})


def delete_tool(request, pk):
    tool = get_object_or_404(Tools, pk=pk)
    tool.delete()
    return redirect('get_tools')


def move_tool(request, tool_id):
    if request.method == 'POST':
        direction = request.POST.get('direction')
        tool = get_object_or_404(Tools, pk=tool_id)
        
        if direction == 'up':
            # Trocar com a ferramenta acima (order - 1)
            swap_tool = Tools.objects.filter(order__lt=tool.order).order_by('-order').first()
        elif direction == 'down':
            # Trocar com a ferramenta abaixo (order + 1)
            swap_tool = Tools.objects.filter(order__gt=tool.order).order_by('order').first()
        else:
            swap_tool = None
        
        if swap_tool:
            # Troca os valores de order
            tool.order, swap_tool.order = swap_tool.order, tool.order
            tool.save()
            swap_tool.save()

    return redirect('tools')