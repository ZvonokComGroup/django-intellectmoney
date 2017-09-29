# coding: utf-8
import json


CONTENT_TYPE_RECEIPT = 1
CONTENT_TYPE_RETURN_RECEIPT = 2
CONTENT_TYPE_EXPENSES = 3
CONTENT_TYPE_RETURN_EXPENSES = 4


TAX_NDS_18 = 1  # ставка НДС 18%
TAX_NDS_10 = 2  # ставка НДС 10%
TAX_NDS_18_118 = 3  # ставка НДС расч. 18/118
TAX_NDS_10_110 = 4  # ставка НДС расч. 10/110
TAX_NDS_0 = 5  # ставка НДС 0%
TAX_NO_NDS = 6  # НДС не облагается


def getMerchantReceiptPosition(quantity, price, tax, text):
    return {
        'quantity': quantity,
        'price': price,
        'tax': tax,
        'text': text,
    }


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
