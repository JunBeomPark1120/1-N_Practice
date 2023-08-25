from django.shortcuts import render,redirect
from .models import Article, Comment
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

def comment_create(request, article_id):
    # 사용자가 입력한 정보를 form에 입력
    comment_form = CommentForm(request.POST)
    
    # 유효성 검사
    if comment_form.is_valid():
        # form을 저장 => 추가로 넣어야 하는 데이터를 넣기 위해 저장을 맘춤
        comment = comment_form.save(commit=False)
        
        # 첫 번째 방법
        # article_id을 기준으로 article obj를 가져와서
        # article_id = Article.objects.get(id=article_id)
        # article 컬럼에 추가
        # comment.article = article
        
        # 두 번째 방법
        comment.article_id = article_id
        
        # 이 후, 저장
        comment.save()
        
        return redirect('articles:detail', id=article_id)

def comment_detail(request, article_id, id):
    comment = Comment.objects.get(id=id)
    
    comment.delete()
    
    return redirect('articles:detail', id=article_id)