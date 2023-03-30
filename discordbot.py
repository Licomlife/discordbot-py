from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.environ['TOKEN']

client = discord.Client()

app = commands.Bot(command_prefix='/')
 
@app.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@app.command()
async def hello(ctx):
    await ctx.send('Hello I am Bot!')

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
