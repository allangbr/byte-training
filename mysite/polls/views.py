from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    authors = Author.objetc.all()
    context = { 'authors': authors, }

    return render(request, 'index.html', context=context)