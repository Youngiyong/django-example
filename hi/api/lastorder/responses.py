from django.http import JsonResponse

class Response(JsonResponse):
    """
    response
    """

    def __init__(
            self,
            status=200,
            data="",
            msg="",
            code="",
            **kwargs
    ):

        response_data = {}
        if data:
            response_data['data'] = data

        if msg:
            response_data['msg'] = msg

        if code:
            response_data['code'] = code

        super().__init__(
            response_data,
            status=status,
            **kwargs
        )

class ErrorResponse(Response):
    """
    error response
    """

    def __init__(
            self,
            code="",
            status=400,
            msg="",
            **kwargs
    ):

        super().__init__(
            msg=msg,
            code=code,
            status=status,
            **kwargs
        )

class ExceptionResponse(ErrorResponse):
    """
    exception response
    """

    def __init__(self, ex):
        super().__init__(msg=ex.detail, code=ex.code)
