import telebot
from telebot import types
from face import feed, feed_1, mine
from config import TOKEN
import time, threading
import datetime

bot = telebot.TeleBot(TOKEN)

chat_id = '@CS_VNTU'
#CS_VNTU
# cs_go_pro_2000
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

def auth(func):
    def wrapper(message):
        if message.from_user.id != 408288186:
            return bot.send_message(message.chat.id, "Вибачте, у Вас немає доступу!")
        return func(message)
    return wrapper


global arr_post
global arr_picture
try:
    fc = feed()
    arr_post = [fc[0]]
    arr_picture = [fc[1]]
except:
    try:
        fc = feed_1()
        arr_post = [fc[0]]
        arr_picture = [fc[1]]
    except:
        arr_post = ['1']
        arr_picture = ['1']

def array():
    try:
        new = feed()
        if len(new[0]) > 4096:
            post_f = new[0][0:4093]
        else:
            post_f = new[0]
        picture = new[1]

        for i in range(0, len(arr_picture)):
            if picture != arr_picture[len(arr_picture) - 1]:
                arr_picture.append(picture)
                arr_picture.pop(0)
                print(arr_picture)

        for i in range(0, len(arr_post)):
            if post_f != arr_post[len(arr_post)-1]:
                arr_post.append(post_f)
                if arr_post[len(arr_post)-1].index(post_f):
                    arr_post.pop(0)
                    arr_post.append(post_f + '...')
                else:
                    arr_post.pop(0)
                    arr_post.append(post_f)
                arr_post.pop(0)
                send(arr_picture[len(arr_picture) - 1],arr_post[len(arr_post) - 1])
                print(arr_post)
    except:
        # print('sorry')
        try:
            new = feed_1()
            if len(new[0]) > 4096:
                post_f = new[0][0:4093]
            else:
                post_f = new[0]
            picture = new[1]

            for i in range(0, len(arr_picture)):
                if picture != arr_picture[len(arr_picture) - 1]:
                    arr_picture.append(picture)
                    arr_picture.pop(0)
                    print(arr_picture)

            for i in range(0, len(arr_post)):
                if post_f != arr_post[len(arr_post)-1]:
                    arr_post.append(post_f)
                    if arr_post[len(arr_post)-1].index(post_f):
                        arr_post.pop(0)
                        arr_post.append(post_f + '...')
                    else:
                        arr_post.pop(0)
                        arr_post.append(post_f)
                    arr_post.pop(0)
                    send(arr_picture[len(arr_picture) - 1],arr_post[len(arr_post) - 1])
                    print(arr_post)
        except:
            print('three')
            threading.Timer(1800, repeat).start()
            ph = 'https://scontent.fiev25-1.fna.fbcdn.net/v/t1.0-9/79334841_523098078275839_3956316945845846016_o.jpg?_nc_cat=106&_nc_ohc=Q8WMxX8t-sgAQmww_NMd1R2gCvx3QaEJB7bSD_TNzW5bFGjJ4uoZZsULw&_nc_ht=scontent.fiev25-1.fna&oh=b361f45ff4f9b4177907be8c2f130fc3&oe=5E7DA7ED'
            bot.send_photo('@metrogoldenma', ph)

# таймер
def repeat():
    # print(time.ctime())
    now = datetime.datetime.now()
    time1 = datetime.time(15)
    time2 = datetime.time(23)
    if now.hour > time1.hour and now.hour < time2.hour:
        array()
        print('one')
        threading.Timer(900, repeat).start()
    else:
        array()
        print('two')
        threading.Timer(5400, repeat).start()
repeat()

@bot.message_handler(commands=['start'])
@auth
def start_message(message):
    bot.send_message(message.chat.id, "hello", reply_markup = keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
    btn1 = types.InlineKeyboardButton("/get")
    btn2 = types.InlineKeyboardButton("/help")
    btn3 = types.InlineKeyboardButton("/mine")
    btn4 = types.InlineKeyboardButton("/cs")
    return markup.row(btn1,btn2,btn3,btn4)

@bot.message_handler(commands=['help'])
@auth
def send_help(message):
    news = "/get - отримати пост з групи кафедри власноруч\n/mine -отримати пост в цей же чат моєї групи\n/cs - з моєї групи в група кафедри в телеграм"
    bot.send_message(message.chat.id, text = news)

@bot.message_handler(commands=['get'])
@auth
def send_array(message):
    try:
        try:
            new = feed()
            if len(new[0]) > 4096:
                post1 = new[0][0:4093] + '...'
            else:
                post1 = new[0]
            picture1 = new[1]
        except:
            new = feed_1()
            if len(new[0]) > 4096:
                post1 = new[0][0:4093] + '...'
            else:
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
    except:
        news = "Прошу вибачення за неполадки.\nЧіп і Дейл уже спішать на допомогу.\nЮхххххххххххххххххххххуууууууууууууууууууу"
        bot.send_message(message.chat.id, text = news)

@bot.message_handler(commands=['mine'])
@auth
def send_array(message):
    try:
        new = mine()
        if len(new[0]) > 4096:
            post1 = new[0][0:4093] + '...'
        else:
            post1 = new[0]
        picture1 = new[1]
        print(post1, picture1)
        # chat_id = "@metrogoldenma"
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
            bot.send_media_group(message.chat.id, media)
        except:
            try:
                bot.send_photo(message.chat.id, picture1[0], caption = post1)
            except:
                try:
                    med = []
                    for id in picture1:
                        med.append(types.InputMediaPhoto(id))
                    bot.send_media_group(message.chat.id, med)
                    bot.send_message(message.chat.id, text = post1)
                except:
                    try:
                        bot.send_photo(message.chat.id, picture1[0])
                        bot.send_message(message.chat.id, text = post1)
                    except:
                        bot.send_photo(message.chat.id, picture1[0])
    except:
        news = "Прошу вибачення за неполадки.\nЧіп і Дейл уже спішать на допомогу.\nЮхххххххххххххххххххххуууууууууууууууууууу"
        bot.send_message(message.chat.id, text = news)

@bot.message_handler(commands=['cs'])
@auth
def send_array(message):
    try:
        new = mine()
        if len(new[0]) > 4096:
            post1 = new[0][0:4093] + '...'
        else:
            post1 = new[0]
        picture1 = new[1]
        chat_id = "@CS_VNTU"
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
                bot.send_photo(message.chat.id, picture1[0], caption = post1)
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
    except:
        news = "Прошу вибачення за неполадки.\nЧіп і Дейл уже спішать на допомогу.\nЮхххххххххххххххххххххуууууууууууууууууууу"
        bot.send_message(message.chat.id, text = news)


if __name__ == "__main__":
    bot.polling(none_stop = True)
