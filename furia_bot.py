# Hora do show! Aqui é FURIA PORRAAAAAAA

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
import random
from time import sleep

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")


# Comandos
async def start(update: Update, context):
    mensagem = """
    🐆 *É FURIA, PORRA!* 🔥

    O que você quer saber?

    /jogadores - Time de jogadores
    /jogos - Próximos jogos
    /vitorias - Conquistas mais recentes
    /memes - Memes icônicos
    /contato - Links oficiais
    /ajuda
    """  # Bora deixar os links clicáveis com o Markdown - se não funcionar uso HTML
    await update.message.reply_text(mensagem, parse_mode="Markdown")


async def jogadores(update: Update, context):
    await update.message.reply_text("Peraê, vou checar quem saiu e quem entrou...")
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
    🗓 <b>Próximos Jogos</b>:

    05/08/2025 - FURIA vs Vitality (ESL Pro League)
    10/08/2025 - FURIA vs NAVI (BLAST Premier) <i>(provável/não divulgado)</i>
    """
    await update.message.reply_text(proximos_jogos, parse_mode="HTML")


async def vitorias(update: Update, context):
    await update.message.reply_text("Agora é só alegria!")
    sleep(1)
    mensagem_vitorias = """
    🏆 <b> ùltimas vitórias da FURIA (2025): </b>

    <b>15/04/2025</b> - FURIA 2x1 MIBR (ESL Pro League)
    <i>Inferno (13-10), Mirage (8-13), Ancient (16-14)</i>

    <b>10/04/2025</b> - FURIA 16x12 NiP (BLAST Premier)
    <i>Overpass (16-12)</i>
    """
    await update.message.reply_text(mensagem_vitorias, parse_mode="HTML")


async def contato(update: Update, context):
    await update.message.reply_text(
        "🔗 *Links Oficiais da FURIA*:\n\n"
        "🐆 Site: https://furia.gg\n"
        "📸 Instagram: [@furiagg](https://instagram.com/furiagg)",
        parse_mode="Markdown"
    )


async def ajuda(update: Update, context):
    await update.message.reply_text(
        "🐆 *COMANDOS DISPONÍVEIS*:\n\n"
        "/start - Inicia o bot\n"
        "/jogadores - Time atual\n"
        "/jogos - Próximas partidas\n"
        "/memes - Memes aleatórios\n"
        "/vitorias - Ùltimos resultados\n"
        "/contato - Links oficiais",
        parse_mode="Markdown"
    )


async def memes(update: Update, context):
    try:  # Usei um try/except pra evitar que o bot morra se o meme não carregar!
        meme_num = random.randint(1, 2)
        meme_path = f"memes/furia_meme{meme_num}.jpg"
        print(f"Tentando abrir: {meme_path}")  # debug
        await update.message.reply_photo(open(meme_path, "rb"))
    except Exception as e:
        print(f"Erro: {e}")  # Mostra o erro real do terminal
        await update.message.reply_text("Bugou, meu! Mas o KSCERATO já tá consertando 🛠️🐆")


# Configuração do ChatBot
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Adicionando os comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogadores", jogadores))
    app.add_handler(CommandHandler("jogos", jogos))
    app.add_handler(CommandHandler("memes", memes))  # Só tem 2 memes, por enquanto rsrs
    app.add_handler(CommandHandler("vitorias", vitorias))
    app.add_handler(CommandHandler("contato", contato))
    app.add_handler(CommandHandler("ajuda", ajuda))
    try:
        print("Tá saindo da jaula o monstro! 🐆")
        app.run_polling()
    except Exception as e:
        print(f"Putz, F5 for respect: {e}")
        print("Mas o arT já tá rushando B pra resolver! 💥")  # hahahahahha
