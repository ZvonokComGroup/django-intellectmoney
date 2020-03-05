import hashlib

from intellectmoney import settings


def checkHashOnReceiveResult(data):
    return getHashOnReceiveResult(data) == data.get('hash')


def getHashOnReceiveResult(data):
    secretKey = settings.SECRETKEY
    serviceName = data.get('serviceName', '')
    eshopId = data.get('eshopId', '')
    orderId = data.get('orderId', '')
    eshopAccount = data.get('eshopAccount')
    recipientAmount = data.get('recipientAmount', '')
    recipientCurrency = data.get('recipientCurrency', '')
    paymentStatus = data.get('paymentStatus', '')
    userName = data.get('userName', '')
    userEmail = data.get('userEmail', '')
    paymentData = data.get('paymentData')
    key = '%s::%s::%s::%s::%s::%s::%s::%s::%s::%s::%s' % (
        eshopId, orderId, serviceName, eshopAccount, recipientAmount,
        recipientCurrency, paymentStatus, userName, userEmail, paymentData,
        secretKey,
    )
    key = key.encode('windows-1251', errors='ignore')
    return hashlib.md5(key).hexdigest()


def getHashOnRequest(data):
    secretKey = settings.SECRETKEY
    serviceName = data.get('serviceName', '')
    eshopId = data.get('eshopId')
    orderId = data.get('orderId')
    purchaseAmount = data.get('recipientAmount')
    currency = data.get('recipientCurrency')
    key = '%s::%s::%s::%s::%s::%s' % (
        eshopId, orderId, serviceName, purchaseAmount, currency, secretKey,
    )
    key = key.encode('windows-1251', errors='ignore')
    return hashlib.md5(key).hexdigest()
