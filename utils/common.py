from fastapi import HTTPException


class RaiseError(HTTPException):
    def __init__(self, error: str, statuscode):
        super().__init__(status_code=statuscode, detail=error)
