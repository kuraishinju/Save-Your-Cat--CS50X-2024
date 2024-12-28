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
        f"You come back home from a long work day at the king's castle when... you don't hear {cat_name} meowing, complaining that you didn't give them their favorite food but some chicken (how many times do they have to tell you that they love salmon but absolutely despise chicken?!) You are in shock, {cat_name} definetly has been kidnapped by the enemy kingdom: the Land of Retrievers! What do you do?",
        "1. You look for some clues",
        "s2",
        "2. You pack up for the journey and leave at once",
        "s3"
    ]
    state2 = [
        "s2",
        f"There are no clues apart from {cat_name}'s bowl being untouched and still full of chicken. Your remorse haunts you, you'd better hurry!",
        "1. You pack up for the journey and leave",
        "s3"
    ]
    state3 = [
        "s3",
        f"Haste is the best choice! You pick up your {cl[0]} and venture to the enemy kingdom. Along the way your neighbour stops you and tells you: <They left not a long time ago and went into the forest, if you're quick enough you might be able to catch up!> You run into the woods, but you have no idea where you are supposed to go from there.",
        "1. East, towards the nearest inn",
        "s4",
        "2. North west, straight towards the enemy kingdom",
        "s5"
    ]
    state4 = [
        "s4",
        f"Since night is approaching, you choose to check if the kidnappers stopped by the only inn in the area to rest and have supper. You walk into the building and are met with the delicious smell of salmon soup... wait... you forgot to bring with you the salmon for {cat_name}! How could you?! But you have no time to spare and need to catch up with the kidnappers (who are not there).",
        "1. Screw it, I need to retrieve some salmon!",
        "e1",
        "2. You ask the inn keeper if someone passed by",
        "s6"
    ]
    state5 = [
        "s5",
        f"You have no time to spare, you rush towards the Land of Retrievers and run through the woods all night, determined to save {cat_name}. No wild animals dare to approach you out of fear. As morning comes you walk through the gates of the kingdom and find yourself surroundedby people and... dogs. What a nightmare! (... You liar, you love dogs, you just never had the courage to tell {cat_name}). You catch a glimpse of a sketchy man with a cage with a cat inside, but no sight of {cat_name}.",
        f"1. You have no time to waste, look for {cat_name}",
        "s7",
        "2. Save that cat!",
        "s8"
    ]
    state6 = [
        "s6",
        f"The inn keeper, intimidated by your {cl[1]}, stutters and tells you that someone stopped by less than half an hour ago and was carrying with them a cat in a cage. Furious with rage you ask them the direction and go...",
        "1. North west, straight towards the enemy kingdom",
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
        f"You approach the sketchy man who, intimidated by your {cl[2]} drops the cage and runs in fear. Nobody seems to care about you and that man. You hear a voice from the cage telling you: <Thank you my saviour! Oh, I recognize you! You are {cat_name}'s servant! The one who forgot about the salmon! You must be so worried about them... Bring me back to your house and I will tell you where {cat_name} is!>",
        "1. Well... all right, let's go back.",
        "e2",
        f"2. No way, you leave and go look for {cat_name}",
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
        f"You approach the inn keeper and kindly ask them for some salmon, explaining your misadventure. She starts laughing at you and you are enraged: <How dare you!> But she quickly tells you that {cat_name}, actually, is in the kitchen eating salmon by themselves because you were so distracted by work that you dared to forget what their favorite food was! You reunite with {cat_name} (after they meow at you all of their complaints) and go straight back home. I hope that from now on you will never forget to give them salmon again!",
        cat_name,
        selected_class
    ]
    ending2 = [
        "e2",
        "You got the Fluffy Ending!",
        f"It takes you a few hours, but eventually you get home in the evening. The cat (whose name is Miss Fluffy, at least that's what she said) looks at you satisfied and tells you: <Well... {cat_name} is actually happily eating salmon at the inn in the woods. They run away from home because you gave them chicken. Maybe next time be more mindful! They will be back soon, don't worry.> A few hours pass and {cat_name} is back home complaining about your ineptitude as a servant, while Pizza already went back home to her's (equally incompetent).",
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