from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import discord
from responses import get_response, get_uID, get_times
from time import sleep
from PIL import Image
import requests
from io import BytesIO
from pyzbar.pyzbar import decode
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import stat
import yt_dlp

file_path = 'F:/Coding stuff/personal-stuff/Python/DiscordBot/project'
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)
file_path = 'C:/Users/ADMIN/AppData/Local/Temp'
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)

pingSpamActive = True






# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# STEP 1 BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True 
client: Client= Client(intents=intents)



# --------------------------FUNCTIONS--------------------
async def ping(message: Message, uMess) -> None:
    global pingSpamActive
    if 'stop' in uMess:
        pingSpamActive = False
        await message.reply('ping stopped')
        print('print stopped')
    else:
        user_ping = get_uID(uMess)
        if user_ping == 'no user found':
            await message.channel.send(user_ping)
            return
        try:
            times = get_times(uMess)
            if times >100: await message.channel.send('No tagging more than 100 times')
            elif times <1: times = 1
        except: times = 1
        
        for i in range(times):
            if not pingSpamActive: break
            sleep(0.5)
            await message.channel.send(f'{i+1}/{times} {user_ping}')

async def remove_messages(message:Message, uMess) -> None:
    try: times = get_times(uMess) + 1
    except: times = 2
    await message.channel.purge(limit=times)

async def QR_Scanner(message: Message, uMess) -> None:
    try:
        response = requests.get(message.attachments[0].url)
        img = Image.open(BytesIO(response.content))
        result = decode(img)
        url = result[0].data.decode('utf-8')
        await message.reply(url)
    except Exception as e:
        await message.reply(f'Cannot scan - {e}')

async def joinVC(message: Message, uMess) -> None:
    if message.author.voice:
        channel = message.author.voice.channel
        try:
            await message.reply(f"Connected to {channel}")
            await channel.connect()
        except discord.errors.ClientException as e:
            await message.channel.send(f"Error connecting to voice channel: {e}")

    else:
        await message.reply("Vào voice ngồi đi đã r hẵng gọi t thằng lonz")

async def leaveVC(message: Message, uMess) -> None:
    if message.guild.voice_client:
        await message.reply('fuck this im out')
        await message.guild.voice_client.disconnect()
    else:
        await message.reply(f'I\'m not even in a voice chat bruh')

async def TTS(message: Message, uMess) -> None:
    if not message.guild.voice_client:
        await joinVC(message, uMess)


    text = message.content[len('tts '):]
    # if message.content[len('tts '):len('tts ')+2] == 'vn': lang = 'vn'
    # else: lang = 'en'
    tts = gTTS(text)
    tts.save('tts.mp3')


    if message.guild.voice_client:
        message.guild.voice_client.play(discord.FFmpegPCMAudio('tts.mp3'), after=lambda e: print('tts played', e))
        # os.remove('tts.mp3')
    else:
        await message.reply('let me in mtfk')

async def soundboard(message: Message, uMess) -> None:

    if not message.guild.voice_client:
        await joinVC(message, uMess)
    
    # list available soundboards
    if uMess == 'sb':
        folder_path = 'F:/Coding stuff/personal-stuff/Python/DiscordBot/project/soundboard'
        filenames = []
        for filename in os.listdir(folder_path):
            file_name_only = filename.split(".")
            filenames.append(file_name_only[0])
        
        filenames_string = " \n".join(filenames)
        await message.reply(filenames_string)
    
    # play the chosen soundboard
    elif uMess[:len('sb ')] == 'sb ':
        soundboard_name = message.content[len('tts '):]
        soundboard_PATH = 'soundboard/' + soundboard_name + '.mp3'
        
        if message.guild.voice_client:
            message.guild.voice_client.play(discord.FFmpegPCMAudio(soundboard_PATH), after=lambda e: print(f'{soundboard_name} played - {e}'))
            await message.channel.send(f'played {soundboard_name}')
            await message.channel.purge(limit=2)
    
    # chosen soundboard not available
    else:
        await message.reply('Soundboard not available')


# -----------------------------------------------------------
# ------------------------MAIN STUFF HERE--------------------
# -----------------------------------------------------------

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    global pingSpamActive
    pingSpamActive = True
    if not user_message:
        print('(Message was empty bcuz intents were not enabled probably)')
        return

    if user_message[0] == '+': 
        user_message = user_message[1:]
        try: # <----- shit happen from here
            # ping spam command
            # print(user_message)
            if 'ping' == user_message[:len('ping')]: await ping(message, user_message)

            # mass messages removal
            elif 'mremove' == user_message[:len('mremove')]: await remove_messages(message, user_message)

            # scanning qr code
            elif 'qr scan' == user_message[:len('qr scan')]: await QR_Scanner(message, user_message)

            # joining voice channel
            elif 'join' == user_message[:len('join')]: await joinVC(message, user_message)

            # leaving voice channel
            elif 'cuts' == user_message[:len('cuts')]: await leaveVC(message, user_message)

            # text to speech
            elif 'tts' == user_message[:len('tts')]: await TTS(message, user_message)

            elif 'sb' == user_message[:len('sb')]: await soundboard(message, user_message)

            # help, roll dice and other unrelated stuff
            else: await message.reply(get_response(user_message))

        except Exception as e: print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()