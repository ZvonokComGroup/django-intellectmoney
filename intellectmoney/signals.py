from django.dispatch import Signal

# providing_args: "orderId", "recipientAmount"
result_received = Signal()
