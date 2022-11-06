import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

from hidden import *

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

 
MOVE = 0
C_S = ['1', '2', '3','4','5','6','7','8','9']  # CURRENT_STATE - TABLO
keys = ['1', '2', '3','4','5','6','7','8','9']
PL = ['Игрок-1', 'Игрок-2']
pl_1 = set(); pl_2 = set() 
active_player = 0


def check_game_over(check_set: set, update, pos):
    victory_set = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
    result = 0
    for i in range(len(victory_set)):
        if victory_set[i] <= check_set: 
            show_play_field(update, pos)
            result = 1
            break
    return result


def check_game_over_draw(update, pos):
    global pl_1, pl_2, keys
    victory_set = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
    result = 0
    
    if len(keys) == 2:
        pl_11 = set(pl_1)
        for i in range(len(keys)):
            pl_11.add(int(keys[i]))

        for i in range(len(victory_set)):
            if (victory_set[i] <= pl_11): 
                result = 0
                break
            else:
                result = 2
                
    if len(keys) == 1:    
        pl_22 = set(pl_2)
        for i in range(len(keys)):
            pl_22.add(int(keys[i]))
        
        for i in range(len(victory_set)):
            if (victory_set[i] <= pl_22): 
                result = 0
                break
            else:
                result = 2
                
    if result: show_play_field(update, pos)
    return result


def show_digit(sign):
    if (sign == '❌') or (sign == '⭕'):
        return sign
    else:
        return '[' + str(sign) + ']'

def show_play_field(update, pos=-1):
    global active_player
    if (pos >= 0): 
        C_S[pos] = '❌' if active_player else '⭕' 
    str_ = '________________\n'
    str1 = '' + show_digit(C_S[0]) +'   |   ' +  show_digit(C_S[1]) + '   |   ' +  show_digit(C_S[2]) + '\n'
    str2 = '' + show_digit(C_S[3]) +'   |   ' +  show_digit(C_S[4]) + '   |   ' +  show_digit(C_S[5]) + '\n'
    str3 = '' + show_digit(C_S[6]) +'   |   ' +  show_digit(C_S[7]) + '   |   ' +  show_digit(C_S[8]) + '\n'
    str__ = str1 + str_ + str2 + str_ + str3
    update.message.reply_text( str__ )
    return MOVE


def end_play(update):
    global active_player
    msg = 'Победил ' + PL[active_player] + '\n' + 'Поздравляю!'
    update.message.reply_text( msg, 
        reply_markup=ReplyKeyboardRemove() )
    user = update.message.from_user
    logger.info("Maestro %s: %s", user.first_name, msg)
    return ConversationHandler.END    


def end_play_draw(update):
    msg = 'Оставшиеся ходы не приведут к чьей-либо победе.' + '\n' + 'НИЧЬЯ!'
    update.message.reply_text( msg, 
        reply_markup=ReplyKeyboardRemove() )
    user = update.message.from_user
    logger.info("Maestro %s: %s", user.first_name, msg)
    return ConversationHandler.END    


def start(update, _):
    reply_keyboard = [['1', '2', '3','4','5','6','7','8','9']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    show_play_field(update, -1)
    update.message.reply_text(
        'Привет! Это игра "Крестики-нолики".\nИграем в режиме "человек - человек".\n'
        'Игрок-1 играет "ноликами",\n соответственно, Игрок-2 - "крестиками"\n'
        'Команда /cancel, чтобы прекратить игру.\n'
        'Игрок-1, Ваш ход?',
        reply_markup=markup_key,)

    return MOVE

# Обрабатываем ввод пользователя
def move(update, _):
    global active_player, pl_1, pl_2, keys
    game_over = False
    user = update.message.from_user
    logger.info("Maestro %s: %s", user.first_name, update.message.text)

    reply_keyboard = [keys]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    pos = update.message.text
    pos_ = int(update.message.text)
    pos__ = update.message.text
    try:
        pos = C_S.index(pos)
        keys.pop(keys.index(pos__))
        reply_keyboard = [keys]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    except ValueError:
        pos = -1
    
    if (pos != -1):
        if active_player: 
            pl_1.add(pos_)
            game_over = check_game_over(pl_1, update, pos)
        else:
            pl_2.add(pos_)       
            game_over = check_game_over(pl_2, update, pos)
        
        if ((not game_over) and (len(keys) <= 2)):
            game_over = check_game_over_draw(update, pos)
        
        if not game_over:     
            show_play_field(update, pos)
            active_player = not active_player
            
            invitation = ''+ PL[active_player] + ', Ваш ход?'
            update.message.reply_text(
                'Команда /cancel, чтобы прекратить игру.\n'+
                invitation,
                reply_markup=markup_key,)
        else:
            if game_over == 1:
                end_play(update)
            else:
                end_play_draw(update)
    return MOVE


# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    logger.info("Пользователь %s отменил игру.", user.first_name)
    update.message.reply_text(
        'Захочешь поиграть - приходи!', 
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(token)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            MOVE: [MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9)$'), move)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
