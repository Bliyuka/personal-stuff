from random import choice, randint
import re

def get_response(user_input: str) -> str:
    # raise NotImplementedError('code is missing...')
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Well, you\'re awfully silent...'
    
    elif lowered == 'help':
        return '''+ping <@(user1)> <@(user2)> <times>: spam ping user(s) 
+mremove <times>: quick remove above message(s)
+roll dice: get a random number from 1 to 6 (will update later)'''
    
    elif 'hello' in lowered:
        return 'Lô con cặc'
    
    elif 'how are you' in lowered:
        return 'nhw lon'
    
    elif 'bye' in lowered:
        return 'cuts'
    
    elif 'roll dice' in lowered:
        return f'{randint(1,6)}'
        
    else:
        return choice(['huh?',
                       'đ hiểu',
                       'nice yappin',
                       'memaybeo',
                       'why are u gei?'])

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
    return int(user_input.rsplit(' ', 1)[1])

