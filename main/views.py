from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@require_http_methods(['POST'])
@csrf_exempt
def register_device(request):
    import json
    from push_notifications.models import GCMDevice

    _body = request.body if request.body else '{}'
    body = json.loads(_body)

    device_token = body.get('device_token')

    if device_token is not None:
        device = GCMDevice.objects.filter(registration_id=device_token, cloud_message_type='FCM').first()
        if not device:
            device = GCMDevice.objects.create(registration_id=device_token, cloud_message_type='FCM')

        device.send_message(title='Congratulations!', message='You are able to receive notifications from Altix')

        return HttpResponse(status=200)

    return HttpResponse(status=400)


@require_http_methods(['POST'])
@csrf_exempt
def send_push_notification(request):
    import json
    from push_notifications.gcm import send_bulk_message
    from push_notifications.models import GCMDevice

    _body = request.body if request.body else '{}'
    body = json.loads(_body)

    message = body.get('message', 'This is a test notification sent from Altix')
    topic_message = 'You are receiving this notification because you are subscribed to \'test_topic\''

    # send message to all registered devices
    GCMDevice.objects.filter(cloud_message_type='FCM').send_message(title='Hi!', message=message, extra={'a_key': 'a_value', 'another_key': 'another_value'})

    # send message to devices subscribed to 'test_topic'
    send_bulk_message(None, {'title': 'Interesting for you...', 'message': topic_message}, to='/topics/test_topic', cloud_type='FCM')

    return HttpResponse(status=200)


def home(request):
    return HttpResponse('<h1>It worked!</h1>'
                        '<div>Made by <a href="http://altix.co" target="_blank">Grupo Altix</a></div>')
