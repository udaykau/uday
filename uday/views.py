from django.http import HttpResponse
import datetime
from django.core.mail import send_mail

def index(request):
    now = datetime.datetime.now()
    send_mail(
        'Subject',
        'Message.',
        'from@example.com', ['udaykau9520@gmail.com'],fail_silently=False)
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)