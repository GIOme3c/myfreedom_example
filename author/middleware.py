import django.shortcuts

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.set_cookie('user_data', "some_data")
        response.delete_cookie('user_data')
        return response