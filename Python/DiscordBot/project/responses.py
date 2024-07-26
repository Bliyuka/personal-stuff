from random import choice, randint

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
        return f'You rolled: {randint(1,6)}'
    else:
        return choice(['huh?',
                       'đ hiểu',
                       'nice yappin',
                       'memaybeo',
                       'why are u gei?'])

