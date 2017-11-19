from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TestPage(LoginRequiredMixin,TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        else :
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)


from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings

@csrf_exempt
def save_image(request):
    if request.body:
        f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpeg','wb')
        f.write(request.body)
        f.close()
        print('something found')
        return HttpResponse('http://127.0.0.1:8000/media/webcamimages/someimage.jpg')
    else:
        print('not get any data.')
        return HttpResponse('no data')
