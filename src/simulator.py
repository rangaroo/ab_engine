import random

def generate_user_data(num_users, p_A, p_B):
    data = []
    for i in range(num_users):
        group = "A" if random.random() <= 0.5 else "B"
        user_id = i
        converted = get_conversion_outcome(group, p_A, p_B)
        data.append((user_id, group, converted))

    return data

def get_conversion_outcome(group, p_A, p_B):
    chance = random.random()

    if group == "A":
        converted = 1 if chance <= p_A else 0
    else:
        converted = 1 if chance <= p_B else 0

    return converted
