from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import discord
from responses import get_response, ping
from time import sleep

pingSpam = True

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# STEP 1L BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True 
client: Client= Client(intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    global pingSpam
    pingSpam = True
    if not user_message:
        print('(Message was empty bcuz intents were not enabled probably)')
        return

    if user_message[0] == '+':
        user_message = user_message[1:]
        try: # <----- shit happen from here
            if 'ping' in user_message:
                if 'stop' in user_message:
                    pingSpam = False
                    await message.reply('ping stopped')
                else:
                    user_ping = ping(user_message)
                    if user_ping == 'no user found':
                        await message.channel.send(user_ping)
                        return
                    
                    try:
                        times = int(user_message.rsplit(' ', 1)[1])
                        if times >100: await message.channel.send('no tagging more than 100 times') 
                        elif times <1: times = 1
                    except:
                        times = 1
                        
                    for i in range(times):
                        if not pingSpam: 
                            break
                        await message.channel.send(f'{i+1}/{times} {user_ping}')
            else:
                response: str = get_response(user_message)
                await message.reply(response)

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