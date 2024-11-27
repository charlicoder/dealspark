import logging

logger = logging.getLogger("visitor_tracking")


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Log visitor IP, user agent, and requested URL
        logger.info(
            f"Visitor IP: {request.META.get('REMOTE_ADDR')}, User Agent: {request.META.get('HTTP_USER_AGENT')}, URL: {request.path}"
        )
        return response
