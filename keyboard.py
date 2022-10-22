import requests

TOKEN = '5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
chat_id = 5575549228

def send_message(chat_id,text,TOKEN):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    button1 = {'text':'CAT'}
    button2 = {'text':'DOG'}

    keyboard = [[button1,button2]]

    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    
    data = {
        'chat_id':chat_id,
        'text':text,
        'reply_markup':reply_markup
    }
    r = requests.post(url,json=data)
    print(r.status_code)


send_message(chat_id, 'Hi', TOKEN)
