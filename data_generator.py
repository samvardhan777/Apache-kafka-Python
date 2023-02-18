import random
import string

user_ids = list(range(1,101))
recipient_ids = list(range(1,101))

def generate_message () -> dict : 
    randon_user_id = random.choice(user_ids)

    recipient_ids_copy = recipient_ids.copy()

    recipient_ids_copy.remove(randon_user_id)

    randon_recipient_ids = random.choice(recipient_ids_copy)

    msg = ''.join(random.choice(string.ascii_letters) for i in range (32))

    return {
        'user_id': randon_user_id,
        'recipient_ids': randon_recipient_ids,
        'message': msg
     }

#Testing
if __name__ == '__main__':
    print(generate_message())

