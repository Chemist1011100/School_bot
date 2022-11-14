import telebot

bot = telebot.TeleBot("5552541973:AAGk3conF_cM8AX2Hxp-TL4pClnnDXkL8cQ")
various = {"Сложение": "+", "Вычитание": "-", "Умножение": "*", "Деление": "/"}
numb = [1,2,3,4,5,6,7,8,9,0]
class Calc:
	def __init__(self,a,b,v):
		self.a = a
		self.b = b
		self.v = v
	def mat(self):
		if self.v == various[0]:
			num = self.a + self.b
		elif self.v == various[1]:
			num = self.a - self.b
			return num
		elif self.v == various[2]:
			num = self.a * self.b
			return num
		elif self.v == various[3]:
			num = self.a / self.b
			return num

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message, "Бот - калькулятор запущен")
	#bot.send_message(message, "Бот - калькулятор запущен")
	#bot.send_message(message, "Какое действие хотите совершить? \nСложение\nВычитание\nУмножение\nДеление")
@bot.message_handler(content_types=['text'])
def varios(message):
	if message.text in various:
		with open('C:/Users/Полина/Desktop/Worker.txt', 'a') as file:
			file.write(f"{various[message.text]}\n")
		bot.send_message(message, f"Вы выбрали {message.text}, напишите первое число")
@bot.message_handler(content_types=['text'])
def first(message):
	if message.text in numb:
		with open('C:/Users/Полина/Desktop/Worker.txt', 'a') as file:
			file.write(f"{int(message.text)}\n")
		bot.send_message(message, f"Первое число - {message.text}, напишите второе")
@bot.message_handler(content_types=['text'])
def second(message):
	if message.text in numb:
		with open('C:/Users/Полина/Desktop/Worker.txt', 'a') as file:
			file.write(f"{int(message.text)}\n")
		bot.send_message(message, f"Второе число - {message.text}")
	with open('C:/Users/Полина/Desktop/Worker.txt', 'r') as file:
		v = file.readline(0)
		a = file.readline(1)
		b = file.readline(2)
		count = Calc(a,b,v)
		bot.send_message(message, f"{count.mat()}")

#def send_welcome(message):
#	bot.reply_to(message, "Howdy, how are you doing?")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

bot.infinity_polling()
