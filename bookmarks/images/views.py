from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *


# Create your views here.


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImagesCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Изображение успешно добавлено")
            return redirect(new_image.get_absolute_url())
    else:
        form = ImagesCreateForm()
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})
