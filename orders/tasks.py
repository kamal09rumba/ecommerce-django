from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send email notification when an order is sucessfully created
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = "Order number {}".format(order.id)
    message = 'Dear {}, \n\nYou have sucessfully placed and order.\
                 \nYour Order id is {}.'.format(order.first_name,order.id)
    mail_sent = send_mail(subject,message,'onlineshop@mail.com',[order.email])
    return mail_sent