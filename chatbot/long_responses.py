import random

R_Eating = "I don't like eating"


def unknown():
    response = ["Could you please rephrase that?", "...", "What does that mean?"][
        random.randrange(4)
    ]
    return response
