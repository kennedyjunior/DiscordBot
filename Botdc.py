import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("access.env")

TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

intents = discord.Intents.default()
intents.members = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f'{bot.user} online!')

@bot.tree.command(name="games", description="Mostra os nossos jogos", guild=discord.Object(id=GUILD_ID))
async def games(interaction: discord.Interaction):
    SvGame =  [":gun:  __**Cs 1.6**__ \n" "      🔥 Pipa Raiz (BETA)\n" "      💥 Pipa Combate (BETA)\n" "      🧟‍♂️ Zombie Plague\n"
                "      ☣️ Zombie Biohazard\n" "      🏃‍♂️ Zombie Escape\n" "      🎨 PaintBall (BETA)",
                " \n :pick: __**Minecraft**__ \n" "      💎Logikoz Network" " __(Java e bedrock)__", "### **X----se divirta em nossos servidores agora mesmo!----X**"]
    
    SvGameL = "\n".join(SvGame) #Quebra de linha
    await interaction.response.send_message(f"🚀**Atualmente nossos servidores são:**\n\n{SvGameL}\n" "||Para ver nossos IP utilize o comando /ip||")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="moderator-only") #,file=discord.File('gifBoasVindas')
    if channel:
        await channel.send(f"Bem-vindo ao servidor, {member.mention}!")

bot.run(TOKEN)