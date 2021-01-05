from django.core.mail import send_mail
from django.http import HttpResponse

def emailfunc(request):
    send_mail(
        'タイトル',
        '本文',
        '送信元のメールアドレス',
        ['送信先のメールアドレス'],
        fail_silently=False,
    )
    return HttpResponse('')