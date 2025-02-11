import discord
from discord.ext import commands
from discord import app_commands
import asyncio

# Setze deine Beleidigungen hier ein
BAD_WORDS = ["schimpfwort1", "schimpfwort2", "schimpfwort3"]  # Ersetze mit echten Wörtern
TIMEOUT_DURATION = 300  # 5 Minuten Timeout

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Prüfen, ob eine Beleidigung im Nachrichtentext vorkommt
    if any(word in message.content.lower() for word in BAD_WORDS):
        try:
            # Timeout setzen
            await message.author.timeout(discord.utils.utcnow() + discord.timedelta(seconds=TIMEOUT_DURATION))
            
            # Embed-Nachricht erstellen
            embed = discord.Embed(title="Timeout erteilt", color=discord.Color.red())
            embed.add_field(name="User", value=message.author.mention, inline=True)
            embed.add_field(name="Grund", value="Verwendung unerlaubter Sprache", inline=True)
            embed.add_field(name="Dauer", value=f"{TIMEOUT_DURATION // 60} Minuten", inline=True)
            embed.set_footer(text=f"Moderation durch {bot.user.name}")
            
            # Nachricht in den gleichen Kanal senden
            await message.channel.send(embed=embed)
        except Exception as e:
            print(f"Fehler beim Timeout: {e}")

    await bot.process_commands(message)

TOKEN = "DEIN_BOT_TOKEN_HIER"
bot.run(TOKEN)
