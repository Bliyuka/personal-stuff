import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from typing import Final
import re
from time import sleep

pingSpamActive = True

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True 
intents.members = True
client = commands.Bot(command_prefix= '+', intents=intents)

def get_uID(user_input: str) -> str:
    lowered: str = user_input.lower()
    #get user IDs as list
    numbers = re.findall(r'<@(\d+)>', lowered) 
    if numbers:
        IDs = ['<@'+num+'>' for num in numbers]
        user = ' '.join(IDs)
        return user
    
    else:
        return 'no user found'

def get_times(user_input: str) -> int:
    print('user imput: ' + user_input)
    return int(user_input.rsplit(' ', 1)[-1])

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.command()
async def sb(ctx, soundboard):
    if not ctx.voice_client:
        await join(ctx)
    ctx.voice_client.stop()

    folder_path = 'F:/Coding stuff/personal-stuff/Python/DiscordBot/project/soundboard/'

    file_path = folder_path + soundboard + '.mp3'
    print(file_path)

    ctx.voice_client.play(discord.FFmpegPCMAudio(file_path))

    await ctx.reply(f'played: {soundboard}')
    await ctx.channel.purge(limit=2)

@client.command()
async def sbl(ctx):
    folder_path = 'F:/Coding stuff/personal-stuff/Python/DiscordBot/project/soundboard/'
    
    filenames = []
    
    for filename in os.listdir(folder_path):
        file_name_only = filename.split(".")
        filenames.append(file_name_only[0])
    
    filenames_string = " \n".join(filenames)
    await ctx.reply(filenames_string)

@client.command()
async def mremove(ctx, times: int):
    times = times + 1
    await ctx.channel.purge(limit=times)

@client.command()
async def ping(ctx, uMess: str):
    global pingSpamActive
    pingSpamActive = True
    if uMess == 'stop':
        pingSpamActive = False
        await ctx.reply('Ping stopped')
        print('ping stopped')
    else:
        user_ping = get_uID(uMess)
        
        if user_ping == 'no user found':
            await ctx.reply(user_ping)
            return
        
        try:
            print(uMess)
            times = get_times(uMess)
            if times >100: await ctx.reply('No tagging more than 100 times')
            elif times <1: times = 1
        except: times = 1
        
        for i in range(times):
            if not pingSpamActive: break
            sleep(0.5)
            await ctx.channel.send(f'{i+1}/{times} {user_ping}')




@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        return True
    else:
        await ctx.reply('vào voice đi đã r hẵng gọi t thglz')
        return False
        

@client.command(pass_context = True)
async def cuts(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()



@client.command()
async def hello(ctx):
    await ctx.send('Lô con cằc')


@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')

    # await send_message(message, user_message)


client.run(token=TOKEN)
