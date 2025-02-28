import os
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Obtiene los tokens de las variables de entorno en Render
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Obtiene el token desde Render
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Obtiene la API Key de OpenAI desde Render

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
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
