from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm, CommentForm
# Create your views here.

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles
    }
    
    return render(request, 'index.html', context)

def create(request):
    
    # 요청방식이 POST형식이라면?
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    # GET요청 시
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'form.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    comment_form = CommentForm()
    
    # comment 목록
    # 첫 번째 방법
    # comment_list = Comment.objects.filter(article=article)
    
    # 두 번째 방법
    # comment_list = article.comment_set.all()
    
    # 세 번째 방법
    # html코드에서 article.comment_set.all로 사용
    context = {
        'article': article,
        'comment_form': comment_form,
        # 'comment_list' : comment_list
    }
    
    return render(request, 'detail.html', context)