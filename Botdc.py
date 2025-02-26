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

pipaR_ip = "167.250.71.186:27082"
pipaC_ip = "167.250.71.186:27086"
zPlague_ip ="167.250.71.186:27083"
zBiohazard_ip = "167.250.71.186:27081"
zEscape_ip = "167.250.71.186:27084"
PB_ip = "167.250.71.186:27085"
MC_ip = "play.logikoz.net"

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

@bot.tree.command(name="ipcs", description= "ips de cs", guild=discord.Object(id=GUILD_ID))
async def ipcs(interaction: discord.Interaction):
    SvIpc = ["** 🔥 Pipa Raiz (BETA)** \n" "        ⮑ **__167.250.71.186:27082__**\n" "** 💥 Pipa Combate (BETA)** \n" "        ⮑ **__167.250.71.186:27086__**\n" 
    "** 🧟‍♂️ Zombie Plague** \n" "        ⮑ **__167.250.71.186:27083__**\n" "** ☣️ Zombie Biohazard** \n" "        ⮑ **__167.250.71.186:27081__**\n" 
    "** 🏃‍♂️ Zombie Escape** \n" "        ⮑ **__167.250.71.186:27084__**\n" "** 🎨 PaintBall (BETA)** \n" "        ⮑ **__167.250.71.186:27085__**\n"]
    SvIpLc = "\n".join(SvIpc)
    await interaction.response.send_message(f"{SvIpLc}")

@bot.tree.command(name="ipmine", description= "ips de minecraft", guild=discord.Object(id=GUILD_ID))
async def ipmine(interaction: discord.Interaction):
    SvIpm = ["** :pick: Minecraft ** \n" "        ⮑ **__play.logikoz.net__**\n"        "              ⮑ **__bedrock:  (19132)__**\n"     "               ⮑ **__java:  (25565)__**"]
    SvIpLm = "\n".join(SvIpm)
    await interaction.response.send_message(f"{SvIpLm}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="moderator-only") #,file=discord.File('gifBoasVindas')
    if channel:
        await channel.send(f"Bem-vindo ao servidor, {member.mention}!")

bot.run(TOKEN)
