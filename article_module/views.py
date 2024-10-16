from django.http import HttpRequest
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali
from django.shortcuts import render
from django.views import View
from article_module.models import Article
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
    paginate_by = 5
    template_name = 'article_module/articles_page.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context
    
    
def article_categories_component(request : HttpRequest):
    context = {}
    return render(request, 'article_module/components/article_catefories_component.html', context)