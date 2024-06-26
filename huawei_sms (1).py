import huaweisms.api.user
import huaweisms.api.sms
import time
import subprocess
import os


#login modem
user = "admin"
password = "admin"

ctx = huaweisms.api.user.quick_login(user, password)


def getSMS(context):
    response = huaweisms.api.sms.get_sms(context)
    if 'Messages' in response['response'] and 'Message' in response['response']['Messages']:
        return response['response']['Messages']['Message']
    else:
        return []

def switch_case(message):
    for msg in message:
        content = msg['Content']
        phone_number = msg['Phone']
        index = msg['Index']
        
        #print(f"Pesan dari {phone_number}: {content}")
        if content.lower() == "ping":
            check_ping(svr)
            huaweisms.api.sms.send_sms(ctx, phone_number, 'pong')
            print(f"Membalas sms: {content}")
            huaweisms.api.sms.sms_set_read(ctx,index)
            print(f"Membaca sms: {content}")
            #huaweisms.api.sms.delete_sms(ctx, index)
            #print(f"Menghapus sms: {content}")
        elif content.lower() == "menu":
            huaweisms.api.sms.send_sms(ctx, phone_number, 'Ini menu')
            print(f"Membalas sms: {content}")
            huaweisms.api.sms.sms_set_read(ctx,index)
            print(f"Membaca sms: {content}")
            #huaweisms.api.sms.delete_sms(ctx, index)
            #print(f"Menghapus sms: {content}")
            break
        else:
            break

while True:
    messages = getSMS(ctx)
    if messages:
        switch_case(messages)
    time.sleep(5)