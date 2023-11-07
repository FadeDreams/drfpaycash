from rest_framework.views import exception_handler

def custom_exception_handler(exp, context):
    handlers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
    }
    response = exception_handler(exp, context)

    exception_class = exp.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exp, context, response)
    return response


def _handle_generic_error(exc, context, response):
    # response = _handle_error(exc, context)
    response.data = {
        'error': 'Generic Error',
    }
    return response

def _handle_authentication_error(exc, context, response):
    # response = _handle_error(exc, context)
    response.data = {
        'error': 'Authentication Error',
    }
    return response
