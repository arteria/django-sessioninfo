from django.contrib.sessions.models import Session
from compat import get_user_model

def get_session_user(request):
    '''
    Extracts user from POST request.
    Returns None if there is no session or method is not POST
    '''
    if request.method == 'POST' and 'session_key' in request.POST:
        try:
            session_key = request.POST['session_key']
            session = Session.objects.get(session_key=session_key)
            uid = session.get_decoded().get('_auth_user_id')
            return get_user_model().objects.get(pk=uid)
        except Session.DoesNotExist:
            pass
    return None