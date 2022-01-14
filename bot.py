import configparser
import discord
from discord.ext import commands
import random
config = configparser.ConfigParser()
config.read('config.ini')
key = config["DISCORD"]
token = key["BOT_TOKEN"]

intents= discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='bot')

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)}ms")
    return

@client.command()
async def add(ctx, num1, num2):
    sum = float(num1) + float(num2)
    await ctx.send(sum)

@client.command()
async def slap(ctx):
    user = random.choice(ctx.message.channel.guild.members)
    slapper = ctx.author.mention
    await ctx.send(f"Ouch! {slapper} slapped {user.mention}.")

client.run(token)