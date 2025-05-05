
messages = {}

def store_message(user_id: str, encrypted_msg: str):
    messages.setdefault(user_id, []).append(encrypted_msg)

def get_user_messages(user_id: str):
    return messages.get(user_id, [])
