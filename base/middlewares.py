from django.shortcuts import HttpResponse


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self ,request,exception):
        msg=exception
        print(msg)
        return HttpResponse(msg)
#==========================================

# class MyTemplateMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#
#     def process_view(request,*args, **kwargs):
#         print("this is process view -> before view")
#         # return HttpResponse("this is before view")
#         return None
#==========================================



# class FirstMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time first_middleware Initialization")
#
#     def __call__(self, request):
#         print("This is first_middleware before view")
#         response = self.get_response(request)
#         print("This is first_middleware after view")
#         return response
#
# class SecondMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time second_middleware Initialization")
#
#     def __call__(self, request):
#         print("This is second_middleware before view")
#         response = self.get_response(request)
#         # response = HttpResponse(request)
#         print("This is second_middleware after view")
#         return response
#
# class ThirdMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time third_middleware Initialization")
#
#     def __call__(self, request):
#         print("This is third_middleware before view")
#         response = self.get_response(request)
#         print("This is third_middleware after view")
#         return response
#==========================================

# def my_middleware(get_response):
#     print("One time Initialization")
#     def my_function(request):
#         print("This is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_function

#==========================================



