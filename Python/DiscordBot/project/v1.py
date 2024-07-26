from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import discord
from responses import get_response
import re

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
    if not user_message:
        print('(Message was empty bcuz intents were not enabled probably)')
        return

    # is_private = user_message[0]
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    if user_message[0] == '+':
        user_message = user_message[1:]
        try:
            if 'ping' in user_message:
                match = re.search(r'<@(.*?)>', user_message)
                if match:
                    user = match.group(1)
                    user = '<@' + str(user) + '>'
                    print(user)
                else:
                    print('no id found')
                    await message.channel.send("no id found")
                    return
                try:
                    times = user_message.rsplit(' ', 1)[1]
                    times = int(times)
                    print(times)
                except:
                    times = 1
                if user is None:
                    print("User not found")
                else: 
                    for i in range(times):
                        await message.channel.send(f"{i+1}/{times} {user}")
            else:
                response: str = get_response(user_message)
                await message.author.send(response) if is_private else await message.channel.send(response) 

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