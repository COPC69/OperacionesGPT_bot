import os
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Obtiene los tokens de las variables de entorno en Render
TELEGRAM_TOKEN = os.getenv("7887535168:AAHKR-X14zJuGP3klgd9zKz2DMCWaVNy8xo")
OPENAI_API_KEY = os.getenv("7035149323:AAFq_odbD1ph-G2xHyXYGTbuOrGaNOr6geM")

# Configurar OpenAI
openai.api_key = OPENAI_API_KEY

# Función para manejar mensajes y generar respuesta con GPT
def responder(update: Update, context: CallbackContext):
    mensaje_usuario = update.message.text

    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": mensaje_usuario}]
    )

    texto_respuesta = respuesta["choices"][0]["message"]["content"]
    update.message.reply_text(texto_respuesta)

def main():
    # Configurar el bot de Telegram
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Manejar mensajes de texto
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, responder))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
