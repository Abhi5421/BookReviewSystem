from fastapi import HTTPException
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema


class RaiseError(HTTPException):
    def __init__(self, error: str, statuscode):
        super().__init__(status_code=statuscode, detail=error)


conf = ConnectionConfig(
    MAIL_USERNAME="mail_username",
    MAIL_PASSWORD="mail_password",
    MAIL_FROM="mail_from",
    MAIL_PORT="mail_port",
    MAIL_SERVER="mail_host",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


async def send_email():
    try:
        subject = "Review For Book"
        content = "Your Book got {5} rating and {comments} from the {reader} !."
        email = "author@gmail.com"
        message = MessageSchema(
            subject=subject,
            recipients=[email],
            body=content,
            subtype="html"
        )
        fm = FastMail(conf)
        await fm.send_message(message)
        return {"success": True}
    except Exception as e:
        return {"success": False}
