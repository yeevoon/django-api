from django.shortcuts import render
from django.contrib import messages 
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import Todo
from .forms import TodoForm

class TodoList(View):
    form_class = TodoForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        all_items = Todo.objects.all
        return render(request, self.template_name, {'all_items': all_items})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            all_items = Todo.objects.all
            messages.success(request, ('New to-do has been added to the list!'))
            return HttpResponseRedirect('/todos/')

        return render(request, self.template_name, {'all_items': all_items})

class DeleteItems(View):
    template_name = 'index.html'

    def get(self, request, itemId, *args, **kwargs):
        item = Todo.objects.get(pk=itemId)
        item.delete()
        all_items = Todo.objects.all
        messages.success(request, ('Item checked off!'))
        return HttpResponseRedirect('/todos/')



