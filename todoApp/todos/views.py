import os
from django.shortcuts import render
from django.contrib import messages 
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from zipfile import ZipFile

from .models import Todo, Uploads
from .forms import TodoForm, UploadsForm

class TodoList(View):
    form_class = TodoForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        all_items = Todo.objects.all
        all_images = Uploads.objects.all
        context = {'all_items': all_items, 'all_images': all_images}
        return render(request, self.template_name, context)

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

class UploadImage(View):
    form_class = UploadsForm
    template_name = 'uploads.html'

    def get(self,request):
        all_images = Uploads.objects.all
        return render(request, self.template_name, {'all_images': all_images} )

    def post(self, request):
        file_request = request.FILES
        form = self.form_class(request.POST, file_request)
        print("request.FILES:", request.FILES)

        if form.is_valid():
            file_name = request.FILES['uploaded_file']
            fs = FileSystemStorage()
            ext = os.path.splitext(file_name.name)[1]
            print(ext)

            if ext == '.zip':
                print("unzipping file processing......")
                with ZipFile(file_name, 'r') as zip:
                    zip.printdir()
                    all_files = zip.namelist()
                    for image in all_files:
                        if image.endswith('.jpg'):
                            print(image)
                            saveFile = fs.save(str(image), file_request)
            else:
                print(file_name)
                #saveFile = fs.save(str(file_name), file_request)
                form.save()
            print('Saving to database......')
            
            return HttpResponseRedirect('/todos')
        return render(request, self.template_name, {'form': form})
 