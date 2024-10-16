import logging
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)

class AttachRequestToUserMiddleware(MiddlewareMixin):
    """
    Custom middleware addition
    """
    def process_request(self, request):

        if request.user.is_authenticated:
            logger.debug(f"Attaching request object to user: {request.user}")
            request.user.request = request
        else:
            logger.debug("Request is anonymous, no user to attach request to.")