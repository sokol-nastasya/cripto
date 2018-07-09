from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from mainPage.models import News

def main(request):
	news = News.objects.all().order_by('-date')

	paginator = Paginator(news, 10)
	page = request.GET.get('page')

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)

	args = {'news':news}

	return render(request, 'mainPage/base.html', args)


def show_news(request, n_id):
	args = {}
	args.update(csrf(request))
	args['news'] = get_object_or_404(News, id = n_id)
	return render(request, 'mainPage/news.html', args)

def about(request):
	return render(request, 'mainPage/about.html')
