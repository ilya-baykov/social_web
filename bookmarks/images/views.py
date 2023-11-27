from django.shortcuts import render, redirect, get_object_or_404
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
            # return redirect(new_image.get_absolute_url())
            return redirect(new_image.get_absolute_url())
    else:
        form = ImagesCreateForm(request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Images, id=id, slug=slug)
    return render(request, 'images/image/image_detail.html', {'image': image})
