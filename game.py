from layouts import *

def update(selected_class, cat_name, games, ends):
    # variabili stringhe formattate
    if selected_class == "knight":
        cl = ["sword and shield", "sword and shield", "sword"]
    elif selected_class == "adv":
        cl = ["bow and arrows", "menacing bow", "bow"]
    elif selected_class == "wiz":
        cl = ["spell book", "spell book", "spell book"]
    else:
        cl = [None, None, None]

    # liste stati
    state1 = [
        "s1",
        f"You come home after a long day working at the king's castle, but something feels off... You don't hear {cat_name} meowing, complaining about how you dared to give them chicken instead of their favorite salmon. (How many times do they have to tell you they *love* salmon but absolutely *hate* chicken?!) Shocked, you realize {cat_name} must have been kidnapped by the enemy kingdom: the Land of Retrievers! What do you do?",
        "1. Look for some clues",
        "s2",
        "2. Pack up for the journey and leave immediately",
        "s3"
    ]
    state2 = [
        "s2",
        f"There are no clues, except for {cat_name}'s bowl, untouched and still full of chicken. Guilt gnaws at you. You'd better hurry!",
        "1. Pack up for the journey and leave",
        "s3"
    ]
    state3 = [
        "s3",
        f"Haste is the best choice! You grab your {cl[0]} and head toward the enemy kingdom. Along the way, your neighbor stops you and says, <They left not long ago and went into the forest. If you're quick, you might catch up!> You run into the woods, but you have no idea where to go from there.",
        "1. Head east, toward the nearest inn",
        "s4",
        "2. Go northwest, straight toward the enemy kingdom",
        "s5"
    ]
    state4 = [
        "s4",
        f"Since night is approaching, you choose to check if the kidnappers stopped by the only inn in the area to rest and have supper. You walk into the building and are met with the delicious aroma of salmon soup... wait... you forgot to bring with you the salmon for {cat_name}! How could you?! But there's no time to dwell on it, the kidnappers aren't here.",
        "1. Forget it, I need to get some salmon!",
        "e1",
        "2. Ask the innkeeper if anyone suspicious passed by",
        "s6"
    ]
    state5 = [
        "s5",
        f"There's no time to waste. You dash toward the Land of Retrievers, running through the woods all night with determination. Wild animals keep their distance, intimidated by your resolve. As dawn breaks, you reach the kingdom's gates, surrounded by people and... dogs. What a nightmare! (...Okay, maybe you secretly love dogs but never had the courage to tell {cat_name}.) You catch a glimpse of a suspicious man with a cage containing a cat, but it's not {cat_name}.",
        f"1. Keep looking for {cat_name}",
        "s7",
        "2. Save that cat!",
        "s8"
    ]
    state6 = [
        "s6",
        f"The innkeeper, intimidated by your {cl[1]}, stammers and reveals that someone with a cat in a cage passed by less than half an hour ago. Enraged, you demand the direction and hurry off",
        "1. Head northwest, straight to the enemy kingdom",
        "s5"
    ]
    state7 = [
        "s7",
        f"WHAT?! You abandon that poor cat?!",
        "1. No, you ABSOLUTELY save the cat!",
        "s8"
    ]
    state8 = [
        "s8",
        f"You confront the sketchy man, who drops the cage and flees terrified by your {cl[2]}. Nobody seems to care about the commotion. You hear a voice from the cage: <Thank you, my savior! Oh, I recognize you! You're {cat_name}'s servant, the one who forgot the salmon! You must be worried... Take me to your house, and I'll tell you where {cat_name} is!>>",
        "1. Well... all right, let's head back.",
        "e2",
        f"2. No way, you leave and keep looking for {cat_name}",
        "s9"
    ]
    state9 = [
        "s9",
        f"REALLY?!",
        "1. No no, I listen to the cat and save her",
        "e2"
    ]
    ending1 = [
        "e1",
        "You got the Salmon Ending!",
        f"You kindly ask the innkeeper for some salmon, explaining your plight. She bursts into laughter and you are furious: <How dare you?!> She quickly explains that {cat_name} is actually in the kitchen, happily eating salmon because you forgot their favorite food in your work-induced haze. You reunite with {cat_name} (after a thorough scolding) and head home. Hopefully, you'll never forget their love for salmon again!",
        cat_name,
        selected_class
    ]
    ending2 = [
        "e2",
        "You got the Fluffy Ending!",
        f"Hours later, you arrive home. The cat in the cage (who introduces herself as Miss Fluffy) looks smug and says, <Well... {cat_name} is actually happily eating salmon at the inn in the woods. They ran away because you gave them chicken. Next time, be more thoughtful! They'll return soon.> Sure enough, a few hours later, {cat_name} returns, grumbling about your ineptitude as a servant. Meanwhile, Miss Fluffy heads home to her equally 'incompetent' owner.",
        cat_name,
        selected_class
    ]

    # update dizionari
    games.update({
        "s1": Choice(*state1),
        "s2": Choice(*state2),
        "s3": Choice(*state3),
        "s4": Choice(*state4),
        "s5": Choice(*state5),
        "s6": Choice(*state6),
        "s7": Choice(*state7),
        "s8": Choice(*state8),
        "s9": Choice(*state9)
    })

    ends.update({
        "e1": Ending(*ending1),
        "e2": Ending(*ending2)
    })