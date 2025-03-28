import smtplib

from pydantic import EmailStr

from app.config import settings
# from app.tasks.celerys import celery
# from PIL import Image
# from pathlib import Path

from app.tasks.email_templates import create_mechanic_confirmation_template, create_driver_confirmation_template


# @celery.task
# def process_pic(
#     path: str,
# ):
#     im_path = Path(path)
#     im = Image.open(im_path)
#     for width, height in [
#         (1000, 500),
#         (200, 100)
#     ]:
#         resized_img = im.resize(size=(width, height))
#         resized_img.save(f"app/static/images/resized_{width}_{height}_{im_path.name}.webp")

# @celery.task  # Раскомментировать, если нужен celery вместо BackgroundTasks
def send_mechanic_confirmation_email(
    description: str,
    email_to: EmailStr,
):
    # Удалите строчку ниже для отправки сообщения на свой email, а на пользовательский
    # email_to = settings.smtp_user
    msg_content = create_mechanic_confirmation_template(description, email_to)

    with smtplib.SMTP_SSL(settings.smtp_host, settings.smtp_port) as server:
        server.login(settings.smtp_user, settings.smtp_pass)
        server.send_message(msg_content)
    # logger.info(f"Successfully send email message to {email_to}")

def send_driver_confirmation_email(
    bid_id: int,
    description: str,
    email_to: EmailStr,
):
    # Удалите строчку ниже для отправки сообщения на свой email, а на пользовательский
    # email_to = settings.smtp_user
    msg_content = create_driver_confirmation_template(bid_id, description, email_to)

    with smtplib.SMTP_SSL(settings.smtp_host, settings.smtp_port) as server:
        server.login(settings.smtp_user, settings.smtp_pass)
        server.send_message(msg_content)
