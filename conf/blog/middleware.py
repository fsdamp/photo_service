from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import jwt

from conf.settings import SECRET_KEY


class CheckJWTTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if '/api/articles/' in str(request.path) and not jwt_checker(request):
            response = Response(
                data=err,
                status=status.HTTP_403_FORBIDDEN
            )

            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response
        return self.get_response(request)


def jwt_checker(request):
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']
        token = token.split(' ')[-1]
    # return 401 if token is not passed
    if not token:
        return False
    try:
        # decoding the payload to fetch the stored details
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        current_user = User.objects.get(id=data['user_id'])
        if not current_user:
            return False
        else:
            return True
    except Exception as error:
        return False


err = {
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
