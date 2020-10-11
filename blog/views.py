# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post
from .form import EmailPostForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# def post_list(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 2)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     context = {
#         'posts': posts,
#         'page': page,
#     }
#     return render(
#         request=request,
#         template_name='blog/post/list.html',
#         context=context
#     )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request=request,
        template_name='blog/post/detail.html',
        context={'post': post}
    )

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #  Form fields passed validations
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n{cd['name']}\'s "
                f"comments: {cd['comments']}"
            )
            send_mail(subject, message, 'sergiodm.dev@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request=request,
        template_name='blog/post/share.html',
        context={
            'post': post,
            'form': form,
            'sent': sent,
        })
