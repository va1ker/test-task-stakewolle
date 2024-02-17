import random
import string


async def generate_referal():
    characters = string.ascii_uppercase + string.digits

    referal_code = "".join(random.choice(characters) for _ in range(12))

    return referal_code
