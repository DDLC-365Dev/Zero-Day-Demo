
define q = Character("???")
define j = Character("Jett")
define mdd = Character("Mod Dev.")

label script_intro_start:
    stop music fadeout 2.0
    play music tcityscape1
    m "Hey you brought me ba-"
    pause 1.0
    call updateconsole("delete monika.chr","Deleted Monika.")
    pause 2.0
    mdd "Alright. That's taken care of for this demo..."
    call hideconsole()
    
    mdd "Hey, it's Iridescence, or the Mod Dev. Whatever you want to call me."
    mdd "Damn, that chat box doesn't fit Iridescence. Oh well."
    
    if player == "Zero":
        mdd "Oh. I see. Hello, AfroZer0. I've been waiting for you... I have one question... do you actually have an afro?"
        menu:
            "Yes":
                "That's very cool. I enjoy that. Carry on."
                pass
            "No":
                "My disappointment is immeasurable, my day is ruined."
                pass
    
    mdd "This is a VERY short demo of DDLC 365. It's basically just a mechanics test of driving missions, combat, and the affection system."
    mdd "That said, it's pretty cool, and I hope you enjoy the beginnings of the world of DDLC 365."
    mdd "In the full game, your choices will matter, and lead you through this world. Should you fail to keep balance, the world will come crashing down."
    mdd "And yes, 365 means 365 days of content. I might be insane."
    mdd "Oh well..."
    
    $ line = glitchtext(120)
    mdd "[line]"
    
    scene black with Dissolve(2)
    show text "Alley - 2:00PM, Monday 8/21/2017" with Dissolve(2)
    pause 1.0
    scene black with Dissolve(2)
    
    "..."
    "A shirtless man with a large tattoo of a dragon which spans his back and arms approaches me in the alley."
    "The clan had contacted me earlier and stated to meet here. By all accounts, this man appears to be a fellow member, likely a higher-up."
    "I was told to pack up my belongings. I assumed that I will be transported to a different region. My backpack tugs at my shoulders lightly, I only took the essentials."
    
    
    q "Welcome, Red Death."
    q "We've decided to re-assign you to a new region. You are to be moved to Tokyo for your upcoming missions."
    q "I'm glad to see you've been keeping, if not surpassing our expectations. Your contract is still good for one more year, and this relocation is a direct order."
    q "The Kumicho will be happy with your results. You shall attend the local school in your district, and do not, under any circumstance, tell anybody who you work for."
    q "As you are aware, Tokyo is not Yamaguchi territory. The local clan and ours have been rivals for a long time. Do not disobey your orders."
    q "You are to only act against the other clan if necessary during your transport operations. Do not engage unless told."
    q "Is this understood?"
    
    menu:
        "Yes.": 
            pass

    q "Good. We shall transport you immediately. As you are aware, under our contract you shall be provided temporary housing, cleaning services, and adequate funds."
    "The man presses a button on his phone, likely signalling my driver."
    q "Of course, you must maintain a performance score of at least 40 in your missions to maintain this, but you are well aware, I'm sure."
    q "He should be here in a minute."
    
    "We both stand in silence and wait."
    "A glossy black car with chrome highlights pulls up to the two of us. In the drivers seat is an older man with a long gray beard. I recognize him."
    
    j "Good to see you again, [player]. It hasn't been very long, has it? I assume you are carrying all that you need?"
    mc "It's nice to see you as well, Jett. You know me, I'm prepared for anything."
    "I crack a confident grin at the aging man."
    "Jett was the first kind person I met in the streets. He took me in after my parents were murdered, and he has been almost like my father. Not that I can remember my real father..."
    "Jett introduced me to my brothers in the clan, and I'm forever grateful for him. He has given me this opportunity, and taught me all that I know."
    
    q "Remember, be careful out there. You are one of our most valuable transporters, and your talent is irreplacable."
    q "Good luck, Red Death."
    
    mc "Thank you. But before I go... I have a few questions, if you wouldn't mind?"
    q "I'll try the best I can, kid."
    jump intro_question_loop
    
label intro_question_loop:
    menu:
        "What can I expect for missions?":
            jump intro_q1_answer
        "When are my missions scheduled?":
            jump intro_q2_answer
        "When does school start?":
            jump intro_q3_answer
        "Thank you for answering.":
            jump intro_question_end

label intro_q1_answer:
    q "It's pretty much the standard as is here in Kobe. You will be transporting a variety of items like arms, drugs, and other assets."
    q "We may have you escort some of our members across the city, and make sure to defend them on their meetings."
    q "Your top priority is the safety of our assets and officials. You're the best man we have for the job."
    jump intro_question_loop
    
label intro_q2_answer:
    q "You only have 10 missions left in your term, so I believe there should be one per month. That way you have 2 months off at the end."
    q "Of course, it's subject to change, as you are aware. We will make sure to give you as much notice as possible."
    q "Once a date is set, you must make sure to come on that day."
    jump intro_question_loop
    
label intro_q3_answer:
    q "Ah yes, your new school. The officials said it shall be starting tomorrow. Your education will serve you well once you retire."
    q "We have no requirements when it comes to this, but make sure not to stir up trouble. You're free to do as you wish so long as it's not a mission date."
    q "Try to enjoy your last year. It's the last thing you get before the real world."
    jump intro_question_loop
    
label intro_question_end:
    q "I'm glad you are satisfied. Good luck on your journey, brother."
    mc "Thank you, but I do not need luck."
    q "Whatever you say, kid."
    "The man smiles proudly at me, following as I get into the car to ride shotgun with Jett."
    stop music fadeout 1.0
    play music tcar fadein 1.0
    "He bids us a farewell wave and turns as Jett begins to speed out of the alley and onto city streets."
    
    # Here we should jump into the Day Zero script
    call day0_main from _call_day0_main
    
    return