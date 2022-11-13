from telegram.ext import *
from telegram import *
from hidden import *
from decimal import Decimal
from cmath import *
import logging

MOVE = 0
complex_list = []
state = 0


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("Пользователь %s: %s", user.first_name, update.message.text)
    reply_keyboard = [['Complex', 'Real']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        'Привет! Это калькулятор.\n' \
            'С какими числами будем работать? \n' \
                '(клавиатура: Complex/Real)\n',
                reply_markup=markup_key)
    return MOVE


# Обрабатываем команду /cancel если пользователь отменил разговор
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # определяем пользователя
    user = update.message.from_user
    logger.info("Пользователь %s остановил калькулятор", user.first_name)
    await update.message.reply_text('Пока!')
    return ConversationHandler.END

def complex_count(list_num):
    num1 = list_num[1]
    num2 = list_num[2]
    oprd = list_num[3]
    
    match oprd:
        case "+":
            res = complex(num1) + complex(num2)
        case "-":
            res = complex(num1) - complex(num2)
        case "/":
            res = complex(num1) / complex(num2)
        case "*":
            res = complex(num1) * complex(num2)
            
    result = ''+ num1 + ' ' + oprd + ' ' + num2 + ' = ' + str(res)
    return result


def real_count(list_num):
    num1 = list_num[1]
    num2 = list_num[2]
    oprd = list_num[3]
    if num1.find(','): num1 = num1.replace(',','.')
    if num2.find(','): num2 = num2.replace(',','.')
    
    match oprd:
        case "+":
            res = Decimal(num1) + Decimal(num2)
        case "-":
            res = Decimal(num1) - Decimal(num2)
        case "/":
            res = Decimal(num1) / Decimal(num2)
        case "*":
            res = Decimal(num1) * Decimal(num2)
            
    result = ''+ num1 + ' ' + oprd + ' ' + num2 + ' = ' + str(res)
    return result


# Обрабатываем ввод пользователя
async def move(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global state, complex_list
    user = update.message.from_user
    logger.info("Пользователь %s: %s", user.first_name, update.message.text)

    match state:
        case 0: 
            complex_list.append(update.message.text)
            if complex_list[0] == 'Real':
                msg = 'Введите первое число:'
            else:
                msg = 'Введите первое число (образец: 4+7j):'
            await update.message.reply_text(msg)
        case 1: 
            complex_list.append(update.message.text)
            if complex_list[0] == 'Real':
                msg = 'Введите второе число:'
            else:
                msg = 'Введите второе число (образец: 2-8j):'
            await update.message.reply_text(msg)
        case 2: 
            msg = 'Выберите действие ("+",  "-",  "/",  "*"):'
            reply_keyboard = [['+', '-', '/', '*']]
            markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text(msg,reply_markup=markup_key)
            complex_list.append(update.message.text)
        case 3: 
            complex_list.append(update.message.text)
            match complex_list[0]:
                case "Real": 
                    try:
                        msg = real_count(complex_list)
                    except:
                        msg = 'Ошибка!'
                        logger.info("Ошибка! Данные для Real:  %s", complex_list)
                case "Complex": 
                    try:
                        msg = complex_count(complex_list)
                    except:
                        msg = 'Ошибка!'
                        logger.info("Ошибка! Данные для Complex: %s", complex_list)
                case _:
                        msg = 'Ошибка!'
                        logger.info("Ошибка! Данные для Unknown: %s", complex_list)
                    
            ReplyKeyboardRemove(True)
            reply_keyboard = [['Complex', 'Real']]
            markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text(msg + '\n' \
                'Продолжим? \n' \
                'С какими числами будем работать? \n',
                reply_markup=markup_key)
            complex_list.clear()
            state = -1
            
    state += 1
    return MOVE


if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    conv_handler = ConversationHandler( # здесь строится логика разговора
        entry_points=[CommandHandler('start', start)], \
        states={
            MOVE: [MessageHandler(filters.TEXT, move)],
                }, \
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    app.add_handler(conv_handler)
    

    app.run_polling()
 