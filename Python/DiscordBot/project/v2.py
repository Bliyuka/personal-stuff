from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from functions import *
import stat
import yt_dlp
import discord
from time import sleep

file_path = 'F:/Coding stuff/personal-stuff/Python/DiscordBot/project'
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)
file_path = 'C:/Users/ADMIN/AppData/Local/Temp'
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)

pingSpamActive = True
mURL = []
mTITLE = []


# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# STEP 1 BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True 
client: Client= Client(intents=intents)

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
            if 'ping' == user_message[:len('ping')]: 
                # await ping(message, user_message, pingSpamActive)
                if 'stop' in user_message:
                    pingSpamActive = False
                    await message.reply('ping stopped')
                    print('print stopped')
                else:
                    user_ping = get_uID(user_message)
                    if user_ping == 'no user found':
                        await message.channel.send(user_ping)
                        return
                    try:
                        times = get_times(user_message)
                        if times >100: await message.channel.send('No tagging more than 100 times')
                        elif times <1: times = 1
                    except: times = 1
                    
                    for i in range(times):
                        if not pingSpamActive: break
                        sleep(0.5)
                        await message.channel.send(f'{i+1}/{times} {user_ping}')

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

            # soundboard
            elif 'sb' == user_message[:len('sb')]: await soundboard(message, user_message)

            # choosing out 1 given options
            elif 'choose' == user_message[:len('choose')]: await choose(message, user_message)


            elif 'p' == user_message[:len('p')]:
                try: os.remove('song.mp3')
                except: pass
                
                options = {
                    'format': 'bestaudio/best',
                    'keepvideo': False,
                    'outtmpl': 'song.mp3',
                    'extract_flat': True,
                    'quiet': True,
                }
                
                # join vc if not in yet
                if not message.guild.voice_client:
                    await joinVC(message, user_message)

                # search using url -> url
                if 'http' in user_message:
                    video_url = message.content.split(' ')[1]

                # search with query -> url
                else:
                    query = message.content[len('p '):]
                    with yt_dlp.YoutubeDL(options) as ydl:
                        video_info = ydl.extract_info(f"ytsearch:{query}", download=False)
                        if 'entries' in video_info:
                            video_url = video_info['entries'][0]['url']

                video_info = yt_dlp.YoutubeDL().extract_info(url=video_url, download=False)
                title = video_info['title']

                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([video_info['webpage_url']])

                song_path = 'F:/Coding stuff/personal-stuff/Python/DiscordBot/project/song.mp3'
                message.guild.voice_client.play(discord.FFmpegPCMAudio(song_path))



            elif 's' == user_message[:len('s')]:
                voice_client = message.guild.voice_client
                print('stop song')
                if voice_client.is_playing():
                    voice_client.stop()



            # help, roll dice and other unrelated stuff
            else: await message.reply(get_response(user_message))

        except Exception as e: print(e)

# -----------------------------------------------------------
# ------------------------MAIN STUFF ABOVE-------------------
# -----------------------------------------------------------

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


