import telebot
from pymongo import MongoClient
from Tokens import Token_mongodb
from Tokens import Token_tg
bot = telebot.TeleBot(Token_tg)
cluster = MongoClient(Token_mongodb)
db = cluster["Test_s"]
collections = db["one"]

question_0 = "Ваше имя"
question_1 = "Какая дата?"

@bot.message_handler(commands=["start"])
def start(message):
    collections.insert_one({
        "_id": message.chat.id,
        "name": "",
        "date": ""
    })
    bot.send_message(message.chat.id, question_0)

@bot.message_handler(content_types=['text'])
def name_user(message):
    message_text=message.text
    message_id=message.chat.id

    if question_0 == "Ваше имя":
        name_user = message_text
        collections.update_one({
            "_id": message_id},
            {"$set": {"name": name_user}
        })
        bot.send_message(message.chat.id, question_1)

        if question_1 == "Какая дата?":
            collections.update_one({
                "_id": message_id},
                {"$set": {"data": message_text}
            })




bot.polling()