from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("telegram_token")


# Comandos
async def start(update: Update, context):
    mensagem = """
    🐆 *É FURIA, PORRA!* 🔥

    O que você quer saber?

    /jogadores - Time de jogadores
    /jogos - Próximos jogos
    /memes - Memes icônicos
    """
    await update.message.reply_text(mensagem, parse_mode="Markdown")


from time import sleep


async def jogadores(update: Update, context):
    await update.message.reply_text("Loading...")
    sleep(1)
    players = """
    BR *Time Furia CS2*:

    - KSCERATO (AWP)
    - FalleN (IGL)
    - arT (Entry)
    - chelo (Support)
    - guerri (Técnico)
    """
    await update.message.reply_text(players, parse_mode="Markdown")


async def jogos(update: Update, context):
    proximos_jogos = """
    🗓 *Próximos Jogos*:

    05/08 - FURIA vs Vitality (ESL Pro League)
    10/08 - FURIA vs NAVI (BLAST Premier)
    """
    await update.message.reply_text(proximos_jogos, parse_mode="Markdown")


async def memes(update: Update, context):
    meme_num = random.randint(1, 2)
    await update.message.reply_photo(open(f"memes/furia_meme{meme_num}.jpg", "rb"))


# Configuração do ChatBot

if __name__ == "__main__":
    app = application.builder().token(token).build()

    # Adicionando os comandos
    app.add_handler(commandhandler("start", start))
    app.add_handler(commandhandler("jogadores", jogadores))
    app.add_handler(commandhandler("jogos", jogos))

    print(" O bot tá rodando! 🐆")
    app.run_polling()