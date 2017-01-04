from django.shortcuts import render
from django_web.models import ArtiInfo
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Create your views here.
def index(request):
    limit = 6
    arti_info = ArtiInfo.objects
    paginator = Paginator(arti_info, limit)
    page = request.GET.get('page',  paginator.num_pages )
    print(request)
    print(request.GET)
    loaded = paginator.page(page)
    context = {
        'ArtiInfo': loaded
    }
    return render(request, 'sb.html', context)

def post_new(request):
    if request.method == 'GET':
        return render(request, 'post_edit.html')
    if request.method == 'POST':
        title = request.POST.get('title')
        des = request.POST.get('des')
        tag1 = request.POST.get('tag1')
        tag2 = request.POST.get('tag2')
        tags = [tag1, tag2]
        try:
            import pymongo
            client = pymongo.MongoClient('localhost', 27017)
            wbsit = client['wbsit']
            art_info3 = wbsit['arti_info3']
            art_info3.insert_one({"des": des, "title": title, "tags": tags, "scores": "23"})
            return HttpResponseRedirect('/index')
        except Exception as e:
            print(e)
            return "网站错误"