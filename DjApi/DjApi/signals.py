from django.core.signals import request_finished


def first_signal(sender, **kwargs):
    print('first signal')
request_finished.connect(first_signal)