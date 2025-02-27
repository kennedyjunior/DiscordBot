import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import asyncio


intents = discord.Intents.default()
client = discord.Client(intents=intents)
load_dotenv("access.env")
BEARERt = os.getenv("BEARER_TOKEN")
URLa = os.getenv("URL_API")
TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
guild = client.get_guild(GUILD_ID)
if guild:
        print("\n🔹 Lista de canais disponíveis:")
        for channel in guild.channels:
            print(f"📌 {channel.name} - ID: {channel.id}")
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
    channel = discord.utils.get(member.guild.channels, name="moderator-only")
    if channel:
        embed = discord.Embed(
            title="Seja Bem-vindo à Logikoz Network!",
            description=f"Não esqueça de dar uma olhada nas <#1343596540366688409>, {member.mention}! Esperamos que você se divirta aqui! 🚀",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    
        embed.set_image(url="https://mc.logikoz.net/uploads/template_banners/66a8fdb2e93b51.54145097_kejgfplhiqnom.png")

        embed.set_footer(text=f"ID do usuário: {member.id}")


        await channel.send(embed=embed)



@bot.command()
async def status(ctx):
    mensagens = [
        " :pick:Minecraft: STATUS",
        " :fire:Pipa Raiz: STATUS",
        " :boom:Pipa Combate: STATUS ",
        " :man_zombie:Zombie Plague: STATUS",
        " :man_running:Zombie Escape: STATUS",
        " :art:PaintBal: STATUS"
    ]
    for mensagem in mensagens:
        await ctx.send(mensagem)

async def editar_msg_api():
    channel = client.get_channel(1344131381974011954)
    message = await channel.fetch_message[1344153674091462677]


        

bot.run(TOKEN)
