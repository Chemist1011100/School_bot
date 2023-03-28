import time
import random   #нужен для выбора одного из нескольких персонажей
from config import stands   #импорт словарей из config
from config import links
from config import two
from config import three
from config import four
from config import five
from config import six
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message, CallbackQuery, InputMedia
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

print("Запуск успешен")  # Проверка

TOKEN = ('5399899287:AAE-apYTLr9JooW23NdAgdqV1NA-zBvCo4c')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми на меня', callback_data='www'))
class Stand:    #класс для вывода картинки и персонажа пользователю
    def __init__(self, name, face, id):
        self.name = str(random.choice(name))
        self.face = face[self.name]
        self.id = id
@dp.message_handler(commands=["start"])
async def photo(message: Message):  #начальная кнопка
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Стенд стрела", callback_data="Stand_arr"),
        InlineKeyboardButton(text="Таинственная стрела", callback_data="Mystery_arr"),
        InlineKeyboardButton(text="Чтобы узнать в чем их разница, нажмите сюда", callback_data="info")
    )
    photo_url = 'https://static.jojowiki.com/images/6/62/latest/20200308004007/Arrowheads_anime.png'

    await bot.send_photo(
        message.chat.id,
        photo=photo_url,
        reply_markup=reply_markup,
        caption="Вы нашли две стрелы, какую хотите использовать?",
    )

@dp.callback_query_handler(text="Stand_arr")
async def photo_update(query: CallbackQuery):   #добавление кнопок для выбора сезона
    time.sleep(1)
    new_url = 'https://www.mirf.ru/wp-content/uploads/2021/04/JoJos-Bizarre-Adventure-3.jpg'
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="1", callback_data="season1"),
        InlineKeyboardButton(text="2", callback_data="season2"),
        InlineKeyboardButton(text="3", callback_data="season3"),
        InlineKeyboardButton(text="4", callback_data="season4"),
        InlineKeyboardButton(text="5", callback_data="season5"),
        InlineKeyboardButton(text="6", callback_data="season6")
    )
    url = InputMedia(media=new_url, caption="Какой сезон ты выберишь?")

    await query.message.edit_media(url, reply_markup=reply_markup)

@dp.callback_query_handler(text=['back'])
async def photo(query: CallbackQuery):
    time.sleep(1)
    back_url = "https://static.jojowiki.com/images/6/62/latest/20200308004007/Arrowheads_anime.png"
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Стенд стрела", callback_data="Stand_arr"),
        InlineKeyboardButton(text="Таинственная стрела", callback_data="Mystery_arr"),
        InlineKeyboardButton(text="Чтобы узнать в чем их разница, нажмите сюда", callback_data="info")
    )
    url = InputMedia(media=back_url, caption="Какой сезон ты выберишь?")

    await query.message.edit_media(url, reply_markup=reply_markup)

@dp.callback_query_handler(text=['info'])
async def inform(query: CallbackQuery):
    time.sleep(1)
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Назад", callback_data="back"))
    new_url = "https://cdnb.artstation.com/p/assets/images/images/020/254/449/large/patt-martin-requiemarrow-keyshot01-png.jpg?1567022732"
    url = InputMedia(media=new_url, caption="Стенд стрела - позволяет получить стенд из определённого сезона по твоему желанию\nТаинственная стрела - позволяет получить рандомный стенд из всех сезонов аниме")
    await query.message.edit_media(url, reply_markup=reply_markup)

@dp.callback_query_handler(text=['season1'])            #при выборе одного из сезона работает отдельная функция для выбора из словаря конкретного сезона
async def season1_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'В первом сезоне стендов нет')
@dp.callback_query_handler(text=['season2'])
async def season2_command(message: types.Message):
    chat_id = message.from_user.id
    seas2 = Stand(two, links, chat_id)
    await bot.send_photo(chat_id=seas2.id, photo=seas2.face, caption=f"Твой стенд это {seas2.name}")
@dp.callback_query_handler(text=['season3'])
async def season3_command(message: types.Message):
    chat_id = message.from_user.id
    seas3 = Stand(three, links, chat_id)
    await bot.send_photo(chat_id=seas3.id, photo=seas3.face, caption=f"Твой стенд это {seas3.name}")
@dp.callback_query_handler(text=['season4'])
async def season4_command(message: types.Message):
    chat_id = message.from_user.id
    seas4 = Stand(four, links, chat_id)
    await bot.send_photo(chat_id=seas4.id, photo=seas4.face, caption=f"Твой стенд это {seas4.name}")
@dp.callback_query_handler(text=['season5'])
async def season5_command(message: types.Message):
    chat_id = message.from_user.id
    seas5 = Stand(five, links, chat_id)
    await bot.send_photo(chat_id=seas5.id, photo=seas5.face, caption=f"Твой стенд это {seas5.name}")
@dp.callback_query_handler(text=['season6'])
async def season6_command(message: types.Message):
    chat_id = message.from_user.id
    seas6 = Stand(six, links, chat_id)
    await bot.send_photo(chat_id=seas6.id, photo=seas6.face, caption=f"Твой стенд это {seas6.name}")

@dp.callback_query_handler(text='Mystery_arr')  #функция для вывода любого персонажа из любого сезона
async def send_photo(message: Message):
    chat_id = message.from_user.id
    myst = Stand(stands,links,chat_id)
    await bot.send_photo(chat_id=myst.id, photo=myst.face, caption=f"Твой стенд это {myst.name}")

if __name__ == '__main__':
   executor.start_polling(dp)   #bot.polling(non_stop= True) не работает
