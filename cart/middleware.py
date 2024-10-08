class AttachRequestToUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        response = self.get_response(request)

        # Attach the request to the user if the user is authenticated
        if request.user.is_authenticated:
            request.user.request = request

        return response
