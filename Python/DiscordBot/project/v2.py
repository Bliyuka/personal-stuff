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
async def ping(ctx: Message, uMess) -> None:
    global pingSpamActive
    if 'stop' in uMess:
        pingSpamActive = False
        await ctx.reply('ping stopped')
        print('print stopped')
    else:
        user_ping = get_uID(uMess)
        if user_ping == 'no user found':
            await ctx.channel.send(user_ping)
            return
        try:
            times = get_times(uMess)
            if times >100: await ctx.channel.send('No tagging more than 100 times')
            elif times <1: times = 1
        except: times = 1
        
        for i in range(times):
            if not pingSpamActive: break
            sleep(0.5)
            await ctx.channel.send(f'{i+1}/{times} {user_ping}')

async def remove_messages(ctx:Message, uMess) -> None:
    try: times = get_times(uMess) + 1
    except: times = 2
    await ctx.channel.purge(limit=times)

async def QR_Scanner(ctx: Message, uMess) -> None:
    try:
        response = requests.get(ctx.attachments[0].url)
        img = Image.open(BytesIO(response.content))
        result = decode(img)
        url = result[0].data.decode('utf-8')
        await ctx.reply(url)
    except Exception as e:
        await ctx.reply(f'Cannot scan - {e}')



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
            if 'ping' == user_message[:4]: await ping(message, user_message)
            
            # mass messages removal
            elif 'mremove' == user_message[:7]: await remove_messages(message, user_message)

            # scanning qr code
            elif 'qr scan' in user_message[:7]: await QR_Scanner(message, user_message)

            # help, roll dice and other unrelated stuff
            else: await message.reply(get_response(user_message))

        except Exception as e:
            print(e)


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