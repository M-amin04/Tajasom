from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomerRequest


@shared_task
def send_customer_request_notification(request_id):
    try:
        request = CustomerRequest.objects.get(id=request_id)

        subject = f'درخواست جدید از {request.full_name}'
        message = f"""
        درخواست جدید دریافت شد:

        نام: {request.full_name}
        ایمیل: {request.email}
        تلفن: {request.phone}
        خدمات: {request.get_service_type_display()}

        توضیحات:
        {request.description}
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['amin@gamil.com'],
            fail_silently=False,
        )

    except CustomerRequest.DoesNotExist:
        pass


