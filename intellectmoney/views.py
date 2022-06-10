from django.core.mail import mail_admins
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from intellectmoney import settings
from intellectmoney.forms import ResultUrlForm
from intellectmoney.models import IntellectMoney
from intellectmoney.signals import result_received
import logging


logger = logging.getLogger('intellectmoney')


def _send_admin_email(subject, message):
    mail_admins(subject, message=message, fail_silently=settings.MAIL_FAIL_SILENTLY)
    logger.info(u'{}: {}'.format(subject, message))


@csrf_exempt
@require_POST
def receive_result(request):
    ip = request.META['REMOTE_ADDR']
    preffix = 'IntellectMoney: '
    info = request.POST
    if settings.CHECK_IP_ENABLED and ip != settings.IP:
        subject = u'{}Оповещение о платеже с неправильного ip={}'.format(preffix, ip)
        message = u'Дата: {}'.format(info)
        _send_admin_email(subject, message)
        raise Http404
    form = ResultUrlForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        orderId = data['orderId']
        recipientAmount = data['recipientAmount']
        paymentId = data['paymentId']
        try:
            invoice = IntellectMoney.objects.get(orderId=orderId)
        except IntellectMoney.DoesNotExist:
            invoice = None
        if not invoice:
            subject = u'{}Оповещение об оплате несуществующего счета #{}'.format(
                preffix, paymentId
            )
            _send_admin_email(subject, u'Дата: {}'.format(info))
            return HttpResponse('OK')
        paymentStatus = data['paymentStatus']
        if paymentStatus in [5, 6, 7]:
            subject = u'Оплата через intellectmoney #{}'.format(paymentId)
            if paymentStatus == 6:
                message = u'{}Оплачен счет {} (ЗАБЛОКИРОВАНО {} руб)'.format(
                    preffix, orderId, recipientAmount,
                )
            else:
                message = u'{}Оплачен счет {} ({} руб)'.format(
                    preffix, orderId, recipientAmount,
                )
            invoice.paymentId = paymentId
            invoice.paymentData = data['paymentData']
            invoice.eshopAccount = data['eshopAccount']
            invoice.eshopId = data['eshopId']
            invoice.recurringState = data['recurringState']
            invoice.save()
            result_received.send(
                sender=invoice, orderId=orderId, recipientAmount=recipientAmount,
            )
        elif paymentStatus == 3:
            return HttpResponse('OK')
        else:
            subject = u'{}Пришло оповещение с неожидаемым статусом'.format(preffix)
            _send_admin_email(subject, u'Дата: %s' % info)
        return HttpResponse('OK')
    else:
        subject = '{}Форма оповещения платежа: невалидные данные'.format(preffix)
        body = 'Ошибки в форме: {}\n\nДанные:{}'.format(form.errors, info)
        _send_admin_email(subject, body)
        return HttpResponse('Bad', status=400)


@csrf_exempt
def success(request):
    return render(request, 'intellectmoney/success.html')


@csrf_exempt
def fail(request):
    return render(request, 'intellectmoney/fail.html')
