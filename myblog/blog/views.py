from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    _post_list = Post.published.all()

    # Pagination with 3 items per page
    paginator = Paginator(_post_list, 3)
    page_number = request.GET.get("page", 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page number not an integer, serve first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page number out of range, serve last page
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    _post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": _post})
