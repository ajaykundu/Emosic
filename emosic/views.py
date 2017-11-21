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
from django.shortcuts import redirect
from django.conf import settings

@csrf_exempt
def save_image(request):
    if request.body:
        f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpeg','wb')
        f.write(request.body)
        f.close()
        print('something found')
        return HttpResponse('http://127.0.0.1:8000/media/webcamimages/someimage.jpeg')
    else:
        print('not get any data.')
        return HttpResponse('no data')


import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import json
from musicapp import views
from musicapp.models import Song

def EmotionTemp(request):

    songList = Song.objects.all()

    print('hello')
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'dc5a9336dc024bc69d4a4d49b481be47',
    }
    params = urllib.parse.urlencode({
    })
    pathtoImage = settings.MEDIA_ROOT + '/webcamimages/someimage.jpeg'
    pathtoImage = 'https://engineering.unl.edu/images/staff/Kayla_Person-small.jpg'
    print(pathtoImage)
    # Replace the example URL below with the URL of the image you want to analyze.

    body = "{ 'url': 'http://everydayshouldbefun.com/wp-content/uploads/2017/01/1435305770-36a7c3951a2bb484f033814ee652156a-600x398.jpg' }"
    emotionFound = ''
    Emotions = ['fear','contempt','anger','sadness','surprise','neutral','disgust','happiness']
    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
        #   URL below with "westcentralus".
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        my_json = data.decode('utf8')
        data = json.loads(my_json)
        print(data)
        maxval = 0
        for emotion in Emotions:
            if maxval < data[0]['scores'][emotion]:
                maxval = data[0]['scores'][emotion]
                emotionfound = emotion
        print(emotionfound)
        conn.close()
    except Exception as e:
        print(e.args)

    return render(request,'emotion.html',{'emotionFoundtag':emotionfound,'songlist':songList})
