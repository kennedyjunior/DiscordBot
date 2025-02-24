
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} online!')

@bot.command()
async def servidores(ctx):
    await ctx.send('Quer conhecer nossos servidores? Então me diz ai, qual o seu game')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="【ωєℓcσмє】") #,file=discord.File('gifBoasVindas')
    if channel:
        await channel.send(f"Bem-vindo ao servidor, {member.mention}!")

bot.run('')
