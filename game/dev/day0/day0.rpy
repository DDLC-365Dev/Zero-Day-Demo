
label day0_main:
    
    scene bg citystreet with Dissolve(2)
    
    "Our car starts down long winding residential roads. We sit in silence for a while, but as we ride onto the highway Jett begins making small talk."
    
    scene bg road with Dissolve(2)
    
    j "So, [player], you're going to be moving to a new place. One where I can't take care of you or be with you all the time."
    j "I really wish that you will be safe, especially in enemy territory. Don't think that means I won't come to visit you from time to time!"
    j "I still see you as the weak and hungry child on the streets. You're still important to me, [player]."
    j "Do you have any plans for when my contract is up? You won't have to do any more of these dangerous missions again."
    mc "I don't really have anything planned. As I see it, once I'm done, I'll have all that I need to live by myself."
    j "What about college?"
    mc "What {i}about{/i} college?"
    mc "It's kind of pointless. After this I'll have a house and enough money to live the rest of my life alone."
    mc "I'm just finishing high school because it's required by law."
    j "I see. But I don't think you're getting my point, [player]... I'm asking because I want you to think about it."
    mc "What's there to think about?"
    j "Well, for one thing, if you ever have a wife, kids, or even just by myself, I don't think you can just expect to live off of what you have."
    j "Things get more expensive all the time. Soon you'll find myself without anything..."
    mc "Jett... I really don't care."
    j "I'm just saying... You should at least get a job after this. All my brothers in the clan have their own businesses. Maybe you could start one."
    mc "Now that's more like it. I don't want to go to some stuffy 'university' just to wind up in debt and without any real skills."
    j "Just keep my mind open. There's a lot you can learn, [player]."
    j "Plus, you aren't gonna be picking up any chicks when you're broke and worthless!"
    mc "Hahahaha."
    
    "Suddenly a brief alert ping comes from the car."
    j "Dammit. We're low on fuel. These smuggled - I mean - {i}refurbished{/i} cars never have gas in them."
    j "Let's stop at a gas station."
    "Jett takes the next exit off the highway and heads to a small gas station."
    mc "Funny that an escort driver has to have an escort."
    j "Hey, they need to get the car back somehow. These things ain't cheap."
    j "What with all this bullet and impact protection they put inside of it."
    j "Hell, I'm surprised these things drive as fast as they do!"
    mc "This is a new model, right?"
    j "Yup. Turbo-charged, and ready to rumble. If you're lucky you can even get the exhaust pops."
    "Jett disengages the clutch and revs up the engine, before dumping the clutch and leaping forward."
    "The exhaust makes a satisfying pop as he makes the right turn into the gas station."
    
    scene black with Dissolve(2)
    
    stop music fadeout 1.0
    j "Hey, I'll even let you take her for a spin after we get filled up."
    mc "Good deal."
    
    "I exit the car while Jett begins filling it with gas. I go to the restroom before getting on the road."
    "I notice another man with tattoos covering his arms and chest while walking to the restroom. Our eyes meet."
    "He's not from our clan... I look away and continue towards the restroom."
    "After having relieved myself, I exit the restroom."
    "Outside is the same man from before..."
    
    "He's... holding a knife!"
    "The man lunges at me."
    
    "Tutorial: Combat. Combat and driving in this game rely on quick decision making, with timed events. The timer will run down twice - the first time is the fast decision, the second is slow."
    "If you don't respond in time, you fail. my performance relies on choosing the correct or 'better' option quickly. Make sure to save before any confrontation or mission."
    "This is a very quick demonstation of combat. It is {b}NOT{/b} representative of final game combat. This is roughly 40% of the content of what an actual combat scene would have."
    "You shall now be returned to the situation."
    
    play music tfight fadein 1.0
    $ renpy.music.set_volume(0.2, 0, 'music')
    $ combat_perf_score = 0

    jump day0_combat_m1

label day0_combat_m1:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_m1a'
    show screen countdown
    menu:
        "Draw Knife":
            hide screen countdown
            "I smoothly draw my switchblade from my pocket, extending the blade. But the man still runs towards me."
            $ combat_perf_score += 10
            jump day0_combat_m2v1
        "Draw Gun":
            hide screen countdown
            "I smoothly draw my Glock-17 from my pocket, disabling the safety. But the man still runs towards me."
            $ combat_perf_score += 10
            jump day0_combat_m2v2

label day0_combat_m1a:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    show screen countdown
    menu:
        "Draw Knife":
            hide screen countdown
            $ combat_perf_score += 5
            "I smoothly draw my switchblade from my pocket, extending the blade. But the man still runs towards me."
            jump day0_combat_m2v1
        "Use fists":
            $ combat_perf_score -= 10
            hide screen countdown
            "I hold up my hands and brace for impact"
            jump day0_combat_m2v3

label day0_combat_fail1:
    "I freeze in place and are stabbed in the chest. He twists the knife, shooting excruciating pain through my body, and tearing my heart."
    "He quickly pulls out the blade and blood pools onto the floor as I collapse."
    "Everything goes black. I hear Jett running towards me..."
    "Game Over."
    return
    
label day0_combat_m2v1:
    "I stand there as the man runs towards me, knife drawn. He prepares to strike."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    show screen countdown
    menu:
        "Dodge":
            hide screen countdown
            $ combat_perf_score += 10
            "I dodge the strike, making the man miss. As he moves past me, he runs into the wall. I get a slash on the back of his leg, forcing him to the ground."
            jump day0_combat_m3v1
        
        "Strike":
            hide screen countdown
            $ combat_perf_score += 5
            "I attack first, leaving a large gash in his side. His blade grazes my arm, leaving a small slash."
            "The man jumps back in pain. Now it's my turn to make a move."
            jump day0_combat_m3v1

label day0_combat_m3v1:
    "It's my time to strike! I charge and stab the injured man in the throat, his blood spurting out of his neck."
    "He collapses to the ground and dies."
    jump day0_combat_complete

label day0_combat_m3v2:
    "I steady my aim and pull the trigger one last time. The man falls, with a bullet lodged in his head. He dies instantly."
    jump day0_combat_complete

label day0_combat_m2v2:
    "I stand there as the man runs towards me, gun drawn, my hands are shaking. He prepares to strike."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    show screen countdown
    menu:
        "Begin firing":
            hide screen countdown
            $ combat_perf_score += 10
            "I begin firing at the man, my shaking hands causing a few shots to miss. I do hit him in the leg and arm, causing him to stop his charge."
            "It's my turn to make a move!"
            jump day0_combat_m3v2
            
        "Aim":
            hide screen countdown
            $ combat_perf_score += 15
            "I steady my aim and pull the trigger. One shot rings out, and the man falls, a bullet between his eyes. He instantly dies."
            jump day0_combat_complete

label day0_combat_m2v3:
    "I ready my fists, but realize it won't suffice in a knife fight."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    show screen countdown
    menu:
        "Punch":
            hide screen countdown
            $ combat_perf_score += 5
            "I punch the man in the face, stunning him temporarily. This gives me the chance to draw my..."
            pass
        
        "Dodge":
            hide screen countdown
            $ combat_perf_score += 10
            "I dodge, giving you time to draw my..."
            pass
    
    
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    menu:
        "Knife":
            hide screen countdown
            $ combat_perf_score += 5
            "You draw my knife. The man turns to you and charges again."
            jump day0_combat_m2v1
        "Gun":
            hide screen countdown
            $ combat_perf_score += 5
            "You draw my Glock 18. The man turns to you and charges again."
            jump day0_combat_m2v2

label day0_combat_complete:
    $ combat_perf_score += 15
    jump day0_main2

label day0_main2:
    "The dead man lays on the floor, I begin sprinting towards the car."
    mc "Jett! Let's get the hell out of here!"
    "As I shout, Jett looks at my bloodied shirt, his eyes widen."
    mc "Get in the passenger side!"
    "He obeys, putting the gasoline pump back and entering the passenger side."
    "I jump into the driver's seat and floor it out of the gas station."
    scene bg citystreet with Dissolve(2)
    
    "As I race through city streets, Jett turns to me."
    j "What the hell happened!?"
    mc "Another Yakuza charged me with a knife! I had no choice but to neutralize the target."
    j "He wasn't our clan?"
    mc "No. Let's hope that there aren't others tailing us."
    j "Give me my Glock, just in case I need to fire."
    "I pull the gun from its back holster and toss it to Jett."
    "I check my mirrors, noticing 2 black motorcycles and 3 black cars tailing us, trying to catch up."
    mc "Dammit Jett! They're coming from behind."
    j "You know the drill! Let's get these fuckers."
    "Jett lowers his window and begins spraying shots at an approaching motorcyclist."
    "One shot hits the wheel, causing a burst that sends the bike - and therefore the rider - out of control, tossing them to the side of the road."
    "An intersection approaches with a yellow light as one of the black cars races up to my blind spot."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_vehicle_fail1'
    show screen countdown
    
    menu:
        "Drift the corner.":
            hide screen countdown
            $ combat_perf_score += 10
            jump day0_vehicle_m1v1
        "Speed through.":
            hide screen countdown
            $ combat_perf_score += 15
            jump day0_vehicle_m1v2

label day0_vehicle_m1v1:
    "I drift through the corner, throwing off the approaching car, which doesn't make the corner and smashes into a building."
    "The other two barely make the corner, with the remaining motorcyclist speeding up towards Jett's side."
    "Another intersection is coming up."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_vehicle_fail2'
    show screen countdown
    menu:
        "Stay steady for Jett.":
            hide screen countdown
            $ combat_perf_score += 5
            jump day0_vehicle_m2v1
        "Take another turn.":
            hide screen countdown
            $ combat_perf_score += 5
            jump day0_vehicle_m2v2

label day0_vehicle_m1v2:
    "I speed through, a crossing vehicle takes down the car, with the other motorcyclist going down."
    "As I look in the mirror 2 cars continuing through the smoke and debris towards my car."
    "Both try to overtake, blocking me in the middle, another intersection with a red light is ahead."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_vehicle_fail2'
    show screen countdown
    menu:
        "Slow down.":
            hide screen countdown
            $ combat_perf_score += 10
            "My car stops quickly, but my opponents do not."
            "They slam directly into the intersection, their cars being totalled instantly."
            jump day0_vehicle_complete
        "Speed up.":
            hide screen countdown
            $ combat_perf_score += 10
            "My car slips through the oncoming traffic, but my opponents do not."
            "You speed off as a cloud of smoke and fire rise."
            jump day0_vehicle_complete

label day0_vehicle_m2v1:
    "Jett takes a shot, the motorcyclist swerving and tumbling under the black car behind it, leaving one left."
    "The remaining car speeds up, and you do the same, but he gains on you and is approaching my side."
    "Another intersection approaches."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_vehicle_fail2'
    show screen countdown
    menu:
        "Slow down.":
            hide screen countdown
            $ combat_perf_score += 10
            "My car stops quickly, but my opponents do not."
            "It slams directly into the intersection, the car being totalled instantly."
            jump day0_vehicle_complete
        "Speed up.":
            hide screen countdown
            $ combat_perf_score += 10
            "My car slips through the oncoming traffic, but my opponent does not."
            "You speed off as a cloud of smoke and fire rise."
            jump day0_vehicle_complete

label day0_vehicle_m2v2:
    "The motorcyclist slams into an oncoming car, with the car behind it crashing as well."
    "The last remnant follows my tail closely."
    "Another intersection approaches."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_vehicle_fail2'
    show screen countdown
    menu:
        "Slow down.":
            hide screen countdown
            $ combat_perf_score += 10
            "My car stops quickly, but my opponents do not."
            "It slams directly into the intersection, the car being totalled instantly."
            jump day0_vehicle_complete
        "Speed up.":
            hide screen countdown
            $ combat_perf_score += 10
            "My car slips through the oncoming traffic, but my opponent does not."
            "I speed off as a cloud of smoke and fire rise."
            jump day0_vehicle_complete

label day0_vehicle_complete:
    $ combat_perf_score += 15
    "I begin speeding away and get on the highway as quickly as possible, making sure nobody else tails me."
    scene bg road with Dissolve(2)
    stop music fadeout 1.0
    play music tcar2 fadein 1.0
    $ renpy.music.set_volume(1.0, 0, 'music')
    
    mdd "Alright, you have completed the combat demo."
    mdd "Your score was [combat_perf_score]!"
    mdd "Nice job."
    mdd "This is the end of the mechanics test, but you may enjoy the (beta) story for today!"
    
    jump day0_main3
    return
    

label day0_vehicle_fail2:
    "I hear the sound of breaking glass and a blinding white light."
    "A stray bullet shatters my skull, and everything goes black"
    "Game Over."
    return

label day0_vehicle_fail1:
    "A car rams into us, making me lose control and slam into a building."
    "I feel my head smack the steering wheel, and everything goes black."
    "Game Over."
    return

label day0_main3:
    "Our tensions calm slightly. It's not uncommon for violence to go down like this. The police won't even bother to bring charges to anyone."
    "The clans and the police have a somewhat grudging friendship. They can never take us to jail, usually due to evidence."
    "And we'll never get rid of them. So the two have practically called a truce."
    "Feeling brighter, Jett looks in the mirror begins to pipe up."
    j "Well I'll be damned. You didn't even get a scratch!"
    mc "There's a reason I'm the finest transport driver in the Yamaguchi clan."
    j "Hahaha, don't get too ahead of yourself kid. You're still just human."
    mc "For now."
    j "What's that supposed to mean? You're no better than anybody else."
    mc "Just a joke. Lighten up old man."
    j "Ahh, I'm old now. At least you don't call me a 'boomer'"
    mc "What the hell is a 'boomer'?"
    j "Beats me."
    "The two of us continue chit-chatting as a green sign with the name 'Tokyo' points us to our destination."
    "After following Jett's guidance, I pull into a small residential neighborhood."
    scene bg residential_day
    stop music fadeout 1.0
    play music t8 fadein 1.0

    "I get out of the car, still shaken up, but getting over it now."
    j "Let me see here... this smudgy handwriting is hard to read..."
    j "Ah! Right down the street, house 402! That's your assigned house [player]!"
    mc "Right. Well Jett, it's been good spending time with you again."
    j "It's been fun spending time with you too, kiddo. Be careful."
    "The older man takes me into a strong embrace. We hug it out for a few seconds before parting."
    j "I'll come by and visit from time to time, alright kiddo?"
    mc "Sounds good. You know my number."
    j "Hahah. See you soon."
    "With that, Jett gets in the car and drives off."
    "I head down the street, noticing the usual activities and what's going on."
    "This neighborhood is rather peaceful and quiet, with minimal activity. Knowing your surroundings is always important, especially if you're going to be living there!"
    "I notice a plaque on the side of the fencing."
    "It reads '402'."
    "But which one... It's smack-dab in the middle of two houses!"
    "Guessing, I walk over to the one to my right. I pull out the keys Jett gave me and try to slot them in."
    "I struggle a bit to get them inserted and try turning. It doesn't turn."
    "Ah shit, this must be the wrong house."
    "As I withdraw the keys, I hear a voice come from behind me."
    $ s_name = "???"
    s "Hello... are you lost?"
    "I turn around to see a girl with coral pink hair and red bow. She has mesmerizing blue eyes, and an innocent look on her face."
    show sayori 1b at leftin zorder 2
    mc "I'm sorry! I'm new here and I'm supposed to move into house 402?"
    "I become painfully aware that I'm a rather large man and she's so small and vulnerable. Let alone that I'm creeping around her house! This is bad!"
    mc "You live here right? Could you help me?"
    "Oh she's gonna think I'm a creep now! You're such an idiot [player]!"
    "I must look really nervous."
    s 1a "Oh, you're moving into 402? That's actually the house back one. This is 403."
    mc "I see. My apologies. I don't want you to think that I'm trying to intrude or anything!"
    s 1r "Why would I think that, silly? But you're also my new neighbor!"
    "She laughs gently. The sound of her laughter is calming."
    $ s_name = "Sayori"
    s 1a "I'm Sayori. What's your name?"
    mc "I'm [player]. It's nice to meet you... uh, neighbor."
    s 1c "I'm a student at the local high school. Are you also a student, [player]?"
    mc "Well yes, I will be attending tomorrow."
    s 1x "Ah! So I'll see you in the morning!"
    mc "It would appear so."
    s 1a "I can show you the way if you don't mind waiting for me."
    mc "Um. Sure! That would be fine."
    s 1q "Alrighty! I'll see you then. Goodbye, [player]!"
    mc "You too, Sayori!"
    "I hurry out of her yard, as she smiles at me and waves. I wave back."
    hide sayori at thide
    "So she's my neighbor. She seems nice enough."