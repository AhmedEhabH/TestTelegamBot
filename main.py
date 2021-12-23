import os
import telegram.ext

from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.environ.get('API_TOKEN')





def start(update, context):
    update.message.reply_text("Hello!\nWelecome to TestBot!")

def help(update, context):
    update.message.reply_text("""
    The following commands are available:
    
    /start      -> Welecome Message.
    /help       -> This message.
    /content    -> Information about TestBot.
    /contact    -> Information about Contact.
    """)

def content(update, context):
    update.message.reply_text("We test bot")

def contact(update, context):
    update.message.reply_text("u can contact me whenever you want")

def message_handler(update, context):
    update.message.reply_text(f"You said {update.message.text}")

def search(update, context):
    base_url = "https://www.google.com/search?q="
    text = " ".join(context.args)
    url = base_url + text.replace(" ", "+")
    update.message.reply_text(f"You search about \" {text} \" \n{url}")

updater = telegram.ext.Updater(API_TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("search", search))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))



updater.start_polling()
updater.idle()