from django.http import HttpRequest
from django.views.generic.list import ListView
from django.views.generic import DetailView  
from jalali_date import datetime2jalali, date2jalali
from django.shortcuts import render
from django.views import View
from article_module.models import Article, ArticleCategory
from jdatetime import datetime

# Create your views here.


# class ArticleView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_atvie = True)
#         context = {
#             'articles' : articles
#         }
#         return render(request, 'article_module/articles_page.html', context)
    
    
class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'article_module/articles_page.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context
    
    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
                
        return query
    
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'
    
    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        
        return query
    
    
    
def article_categories_component(request : HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        'main_categories' : article_main_categories
    }
    return render(request, 'article_module/components/article_categories_component.html', context)