from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import jwt

class JWTMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)

    def __call__(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth_header = request.META['HTTP_AUTHORIZATION']
            try:
                _, token = auth_header.split(' ')  
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256']) 
                request.id = decoded.get('user_id')  
            except jwt.ExpiredSignatureError: 
                pass
            except jwt.InvalidTokenError: 
                pass

        response = self.get_response(request) 
        return response
