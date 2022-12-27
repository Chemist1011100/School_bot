import random   #нужен для выбора одного из нескольких персонажей
from config import stands   #импорт словарей из config
from config import link
from config import two, two_l
from config import three, three_l
from config import four, four_l
from config import five, five_l
from config import six, six_l
from config import seven, seven_l
from config import eight, eight_l
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message, CallbackQuery, InputMedia
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = ('5399899287:AAE-apYTLr9JooW23NdAgdqV1NA-zBvCo4c')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми на меня', callback_data='www'))
class Stand:    #класс для вывода картинки и персонажа пользователю
    def __init__(self, name, face, id, nums):
        if nums == "small":
            self.nums = str(random.randint(0, 2))
        elif nums == 'big':
            self.nums = str(random.randint(0, 2))
        self.name = name[self.nums]
        self.face = face[self.nums]
        self.id = id

    def send(self):
        await dp.bot.send_photo(chat_id=self.id, photo=self.face, caption=f"Твой стенд это {self.name}")
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
    new_url = 'https://www.mirf.ru/wp-content/uploads/2021/04/JoJos-Bizarre-Adventure-3.jpg'
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="1", callback_data="season1"),
        InlineKeyboardButton(text="2", callback_data="season2"),
        InlineKeyboardButton(text="3", callback_data="season3"),
        InlineKeyboardButton(text="4", callback_data="season4"),
        InlineKeyboardButton(text="5", callback_data="season5"),
        InlineKeyboardButton(text="6", callback_data="season6"),
        InlineKeyboardButton(text="7", callback_data="season7"),
        InlineKeyboardButton(text="8", callback_data="season8")
    )
    url = InputMedia(media=new_url, caption="Какой сезон ты выберишь?")

    await query.message.edit_media(url, reply_markup=reply_markup)

@dp.callback_query_handler(text=['season1'])            #при выборе одного из сезона работает отдельная функция для выбора из словаря конкретного сезона
async def season1_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'В первом сезоне стендов нет')
@dp.callback_query_handler(text=['season2'])
async def season2_command(message: types.Message):
    chat_id = message.from_user.id
    seas2 = Stand(two_l, two,chat_id,'small')
    seas2.send()
@dp.callback_query_handler(text=['season3'])
async def season3_command(message: types.Message):
    chat_id = message.from_user.id
    seas3 = Stand(three_l, three, chat_id,'small')
    seas3.send()
@dp.callback_query_handler(text=['season4'])
async def season4_command(message: types.Message):
    chat_id = message.from_user.id
    seas4 = Stand(four_l, four, chat_id,'small')
    seas4.send()
@dp.callback_query_handler(text=['season5'])
async def season5_command(message: types.Message):
    chat_id = message.from_user.id
    seas5 = Stand(five_l, five, chat_id,'small')
    seas5.send()
@dp.callback_query_handler(text=['season6'])
async def season6_command(message: types.Message):
    chat_id = message.from_user.id
    seas6 = Stand(six_l, six, chat_id,'small')
    seas6.send()
@dp.callback_query_handler(text=['season7'])
async def season7_command(message: types.Message):
    chat_id = message.from_user.id
    seas7 = Stand(seven_l, seven, chat_id,'small')
    seas7.send()
@dp.callback_query_handler(text=['season8'])
async def season8_command(message: types.Message):
    chat_id = message.from_user.id
    seas8 = Stand(eight_l, eight, chat_id,'small')
    seas8.send()
@dp.callback_query_handler(text='Mystery_arr')  #функция для вывода любого персонажа из любого сезона
async def send_photo(message: Message):
    chat_id = message.from_user.id
    myst = Stand(stands,link,chat_id,'big')
    myst.send()
@dp.callback_query_handler(text=['info'])
async def season1_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Стенд стрела - позволяет получить стенд из определённого сезона по твоему желанию\nТаинственная стрела - позволяет получить рандомный стенд из всех сезонов аниме")

if __name__ == '__main__':
   executor.start_polling(dp)   #bot.polling(non_stop= True) не работает
