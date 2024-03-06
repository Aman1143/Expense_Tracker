from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.urls import reverse
import jwt

class JWTMiddleware(MiddlewareMixin):
    EXCLUDED_PATHS = [reverse('login'), reverse('resgister')]   

    def __init__(self, get_response=None):
        super().__init__(get_response)

    def __call__(self, request):
        if self.should_skip_middleware(request.path):
            return self.get_response(request)

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

    def should_skip_middleware(self, path):
        return path in self.EXCLUDED_PATHS
