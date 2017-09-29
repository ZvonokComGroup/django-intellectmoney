# coding: utf-8
import json


CONTENT_TYPE_RECEIPT = 1
CONTENT_TYPE_RETURN_RECEIPT = 2
CONTENT_TYPE_EXPENSES = 3
CONTENT_TYPE_RETURN_EXPENSES = 4


def getMerchantReceiptPosition(quantity, price, tax, text):
    return {
        'quantity': quantity,
        'price': price,
        'tax': tax,
        'text': text,
    },


def getMerchantReceiptString(inn, customer_contact, positions,
            group='Main', content_type=CONTENT_TYPE_RECEIPT, skipAmountCheck=False):
    data = {
        'inn': inn,
        'group': group,
        'skipAmountCheck': int(skipAmountCheck),
        'content': {
            'type': content_type,
            'customerContact': customer_contact,
            'positions': positions,
        },
    }
    return json.dumps(data, ensure_ascii=False)
