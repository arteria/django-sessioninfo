from django.http import HttpResponse

from sessioninfo.utils import get_session_user


def get_session_user_view(request):
    user = get_session_user(request)
    return HttpResponse(user.id)