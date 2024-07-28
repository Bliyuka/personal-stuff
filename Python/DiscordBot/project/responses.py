from random import choice, randint
import re

def get_response(user_input: str) -> str:
    # raise NotImplementedError('code is missing...')
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Well, you\'re awfully silent...'
    
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

def ping(user_input: str) -> str:
    lowered: str = user_input.lower()
    match = re.search(r'<@(.*?)>', lowered)
    if match:
        user = match.group(1)
        user = '<@' + str(user) + '>'
        print(user)
        return user
    else:
        return 'no user found'