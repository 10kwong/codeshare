import telegram as tg
import telegram.ext
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

# local file
from keys import get_telegram_key
from news import simple_search

FEED_EACH_DISPLAY = 2



def hello(update, context):
   update.message.reply_text('hello, {}'.format(update.message.from_user.first_name))
def greet(update, context):
   hello(update, context)
   update.message.reply_text('do you want to check out what this bot can do? \nclick this: /command_board')

def command_board(update, context):
   # show all commands of this bots
   update.message.reply_text('/news India')

def trying(update, context):
   args = update.message.text.lower()
   update.message.reply_text(args.split(' '))

def echo(update, context):
   user_input = update.message.text
   update.message.reply_text(user_input)

def news(update, context):
   args = update.message.text.split(' ')[1:]
   if len(args) == 1:
      results = simple_search(args[0])
      results = results['articles']
      if len(results) == 0:
         update.message.reply_text(f'No Result of {args}\n')
      else: 
         update.message.reply_text(f'Found {len(results)} results:\n')
         choice = ['Yes', 'No']
         emoji = {'Yes':'✅', 'No':'❌'}
         
         for i, article in enumerate(results):
            if i % FEED_EACH_DISPLAY == 0 and i != 0:
               update.message.reply_text('more result?',
                  reply_markup = InlineKeyboardMarkup([[
                     InlineKeyboardButton(emoji, callback_data=choice) for choice, emoji in emoji.items()
                     ]]))
               respond = update.callback_query.message.reply_text(text=update.callback_query.data)
               print("efjighfnkm\n\n\n\n", respond)
               
            update.message.reply_text(article['url'])
   update.message.reply_text(f'End of Searching\n')
   # else:
   
def continue_display(update, context):
   respond = update.callback_query.message.reply_text()
   return True if respond == 'Yes' else False


updater = Updater(token=get_telegram_key())
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('greet', greet))
dispatcher.add_handler(CommandHandler('news', news))
dispatcher.add_handler(CallbackQueryHandler(continue_display)) 
dispatcher.add_handler(CommandHandler('command_board', command_board))
# dispatcher.add_handler(CommandHandler(Filters.text, trying))
dispatcher.add_handler(MessageHandler(Filters.text, echo))


updater.start_polling()
updater.idle()
updater.stop()