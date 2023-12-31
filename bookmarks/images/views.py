from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

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


@login_required
def image_list(request):
    images = Images.objects.all()
    paginator = Paginator(images, 4)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse("")
        images_only = paginator.page(paginator.num_pages)
    if images_only:
        return render(request, 'images/image/list_images.html', {'images': images})
    return render(request, 'images/image/list.html', {'images': images})


@login_required
@require_POST
def image_like(request):
    if request.method == 'POST':
        image_id = request.POST.get('id')
        action = request.POST.get('action')
        if image_id and action:
            try:
                image = Images.objects.get(id=image_id)
                if action == 'like':
                    image.user_like.add(request.user)
                else:
                    image.user_like.remove(request.user)
                return JsonResponse({'status': 'ok'})
            except Images.DoesNotExist:
                pass
            return JsonResponse({'status': 'error'})
