# -*- coding: utf-8 -*-
from django.db import models


class IntellectMoney(models.Model):

    created = models.DateTimeField(auto_now=True)
    orderId = models.CharField(unique=True, editable=False, max_length=255)
    paymentId = models.CharField(null=True, max_length=255)
    paymentData = models.DateTimeField(null=True)
    eshopAccount = models.CharField(null=True, max_length=255)
    eshopId = models.CharField(null=True, max_length=255)

    def __str__(self):
        return 'IntellectMoney payment (orderId: {})'.format(self.orderId)
