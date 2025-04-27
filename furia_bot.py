from telegram import Update  
from telegram.ext import Application, CommandHandler, MessageHandler, filters  

from dotenv import load_dotenv
import os

load_dotenv()  # Carrega o .env
TOKEN = os.getenv("TELEGRAM_TOKEN")  # Lê o token com segurança

TOKEN = "SEU_TOKEN_AQUI"  

# ---- COMANDOS ---- #
async def start(update: Update, context):
    mensagem = """  
    🐆 *É FURIA, PORRA!* 🔥  

    O que você quer saber?  

    /elenco - Elenco atual  
    /jogos - Próximos jogos  
    /memes - Memes icônicos  
    """
    await update.message.reply_text(mensagem, parse_mode="Markdown")

async def elenco(update: Update, context):
    jogadores = """  
    🇧🇷 *Elenco FURIA CS2*:  

    - KSCERATO (AWP)  
    - FalleN (IGL)  
    - arT (Entry)  
    - chelo (Support)  
    - guerri (Técnico)  
    """
    await update.message.reply_text(jogadores, parse_mode="Markdown")

async def jogos(update: Update, context):
    proximos_jogos = """  
    🗓 *Próximos Jogos*:  

    05/08 - FURIA vs Vitality (ESL Pro League)  
    10/08 - FURIA vs NAVI (BLAST Premier)  
    """
    await update.message.reply_text(proximos_jogos, parse_mode="Markdown")

# ---- CONFIGURAÇÃO DO BOT ---- #
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Adiciona os comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("elenco", elenco))
    app.add_handler(CommandHandler("jogos", jogos))

    print("Bot está rodando! 🐆")
    app.run_polling()  