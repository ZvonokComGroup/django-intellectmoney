# -*- coding: utf-8 -*-
from django.db import models


class IntellectMoney(models.Model):

    created = models.DateTimeField(auto_now=True)
    orderId = models.CharField(unique=True, editable=False, max_length=255)
