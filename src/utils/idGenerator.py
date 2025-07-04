import uuid

#128 bit / 16 byte ids
#String format
#36 char (counting hyphens)
def new_id() -> str:
    '''
    Returns unique 36 char id
    '''
    return str(uuid.uuid4())

