git clone https://github.com/eternnoir/pyTelegramBotAPI.git
cd pyTelegramBotAPI
python setup.py install


import telebot # Importamos las librería

TOKEN = '<token string>' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
 enviar mensaje:
tb.send_message(chatid, text) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
enviar una foto:
photo = open('/home/lordsergio/Gatito_Feliz.jpg', 'rb')
tb.send_photo(chat_id, photo)
 enviar un archivo pdf:
doc = open('/home/lordsergio/Documentos/deberes_de_verano.pdf', 'rb') # Es la función equivalente a enviar un archivo desde telegram.
tb.send_document(chat_id, doc)

tb.send_message(109556849, 'Disfruta de tu verano ;)')
 enviar video: 
video = open('/home/lordsergio/Vídeos/Reportaje_sobre_UNIX.mp4', 'rb')
tb.send_video(chat_id, video)
 enviar audio:
audio = open('/home/lordsergio/Música/Audios/1.ogg', 'rb')
tb.send_audio(chat_id, audio) # No tengo muy claro si lo enviá como una nota de audio o como cuando enviar una canción desde Telegram :(
 Enviar un Sticker:
sti = open('/tmp/sti.webp', 'rb')
tb.send_sticker(chat_id, sti)
 enviar localización:
tb.send_location(chat_id, latitud, longitud)
 Reenviar un mensaje (Cualquier tipo de mensaje):
tb.forward_message(to_chat_id, from_chat_id, message_id)
 enviar acciones de chat:
tb.send_chat_action(chat_id, action_string) # Están disponibles todas estas acciones typing,upload_photo,record_video,upload_video,record_audio,upload_audio,upload_document,find_location (Me gustaría que existiera una acción de "Durmiendo...", estaría gracioso :D).
 Obtener Actualizaciones:
tb.get_update()
 
from telebot import types
 Crear teclado de acciones:
markup = types.ReplyKeyboardMarkup()
markup.add('a', 'v', 'd')
tb.send_message(chat_id, message, None, None, markup)
# or use row method
markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')
tb.send_message(chat_id, message, None, None, markup)

tb.get_me()