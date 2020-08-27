from django.shortcuts import render

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        user = request.user
        
        try:
            title = models.jsonContent.object.filter(author=user)
        except:
            pass

    return render(request, 'welcome.html', locals())
