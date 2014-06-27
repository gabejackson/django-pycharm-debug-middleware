class ExceptionMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            import pydevd_breakpoints
            import pydevd
            dbg = pydevd.GetGlobalDebugger()
            exception = 'exceptions.Exception'
            eb = pydevd_breakpoints.ExceptionBreakpoint(exception, True, False)
            dbg.exception_set[exception] = eb
            pydevd_breakpoints.update_exception_hook(dbg)
            dbg.setTracingForUntracedContexts()
        except ImportError:
            pass