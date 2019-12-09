import telebot
from telebot import types
from face import feed
from config import TOKEN
import time, threading

bot = telebot.TeleBot(TOKEN)

chat_id = '@cs_go_pro_2000'

def send(photo, post):
    if len(photo) > 10:
        n = 10
    else:
        n = len(photo)
    try:
        caption = post
        try:
            media = [types.InputMediaPhoto(photo[0], caption = post)]
        except:
            media = [types.InputMediaPhoto(photo[0])]

        for photo_id in range(1, n):
            media.append(types.InputMediaPhoto(photo[photo_id]))
        bot.send_media_group(chat_id, media)
    except:
        try:
            bot.send_photo(chat_id, photo[0], caption = post)
        except:
            try:
                med = []
                for id in photo:
                    med.append(types.InputMediaPhoto(id))
                bot.send_media_group(chat_id, med)
                bot.send_message(chat_id, text = post)
            except:
                try:
                    bot.send_photo(chat_id, photo[0])
                    bot.send_message(chat_id, text = post)
                except:
                    bot.send_photo(chat_id, photo[0])

global arr_post
global arr_picture
arr_post = ['hello']
arr_picture = [1]

def array():
    try:
        new = feed()
        post_f = new[0]
        picture = new[1]
        
        for i in range(0, len(arr_picture)):
        if picture != arr_picture[len(arr_picture) - 1]:
            arr_picture.append(picture)
            arr_picture.pop(0)
            # print(arr_picture)

    for i in range(0, len(arr_post)):
        if post_f != arr_post[len(arr_post)-1]:
            arr_post.append(post_f)
            arr_post.pop(0)
            send(arr_picture[len(arr_picture) - 1],arr_post[len(arr_post) - 1])
            # print(arr_post)
            
    except:
        threading.Timer(3600, repeat).start()
        ph = 'https://scontent.fiev25-1.fna.fbcdn.net/v/t1.0-9/79334841_523098078275839_3956316945845846016_o.jpg?_nc_cat=106&_nc_ohc=Q8WMxX8t-sgAQmww_NMd1R2gCvx3QaEJB7bSD_TNzW5bFGjJ4uoZZsULw&_nc_ht=scontent.fiev25-1.fna&oh=b361f45ff4f9b4177907be8c2f130fc3&oe=5E7DA7ED'
        bot.send_photo('@metrogoldenma', ph)

# таймер на півгодини, через кожні півгодини перевірка відбувається
def repeat():
    # print(time.ctime())
    array()
    threading.Timer(3600, repeat).start()
repeat()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "hello", reply_markup = keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
    btn1 = types.InlineKeyboardButton("/get")
    btn2 = types.InlineKeyboardButton("/help")
    return markup.row(btn1,btn2)

@bot.message_handler(commands=['help'])
def send_help(message):
    news = "Прошу вибачення за неполадки.\nЧіп і Дейл уже спішать на допомогу.\nЮхххххххххххххххххххххуууууууууууууууууууу"
    bot.send_message(message.chat.id, text = news)

@bot.message_handler(commands=['get'])
def send_array(message):
    new = feed()
    post1 = new[0]
    picture1 = new[1]
    if len(picture1) > 10:
        n = 10
    else:
        n = len(picture1)
    try:
        caption = post1
        try:
            media = [types.InputMediaPhoto(picture1[0], caption = post1)]
        except:
            media = [types.InputMediaPhoto(picture1[0])]

        for photo_id in range(1, n):
            media.append(types.InputMediaPhoto(picture1[photo_id]))
        bot.send_media_group(chat_id, media)
    except:
        try:
            bot.send_photo(chat_id, picture1[0], caption = post1)
        except:
            try:
                med = []
                for id in picture1:
                    med.append(types.InputMediaPhoto(id))
                bot.send_media_group(chat_id, med)
                bot.send_message(chat_id, text = post1)
            except:
                try:
                    bot.send_photo(chat_id, picture1[0])
                    bot.send_message(chat_id, text = post1)
                except:
                    bot.send_photo(chat_id, picture1[0])

if __name__ == "__main__":
    bot.polling(none_stop = True)
