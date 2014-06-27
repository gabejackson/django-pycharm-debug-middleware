django-pycharm-debug-middleware
===============================

A django middleware to debug exceptions in PyCharm's PyDev debugger.

Simply add the ExceptionMiddleware to your middleware classes and run PyCharm in Debug mode to handle Exceptions within PyCharm's PyDev Debugger.

Usage
=====

Append the middleware to your MIDDLEWARE_CLASSES and activate DEBUG_PROPAGATE_EXCEPTIONS::

    MIDDLEWARE_CLASSES += ('pycharm_debug_middleware.middleware.ExceptionMiddleware', )
    DEBUG_PROPAGATE_EXCEPTIONS = True
