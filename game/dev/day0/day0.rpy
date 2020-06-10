
label day0_main:
    
    scene bg road with Dissolve(2)
    
    "Our car starts down long winding residential roads. We sit in silence for a while, but as we ride onto the highway Jett begins making small talk."
    
    j "So, [player], you're going to be moving to a new place. One where I can't take care of you or be with you all the time."
    j "I really wish that you will be safe, especially in enemy territory. Don't think that means I won't come to visit you from time to time!"
    j "I still see you as the weak and hungry child on the streets. You're still important to me, [player]."
    j "Do you have any plans for when your contract is up? You won't have to do any more of these dangerous missions again."
    mc "I don't really have anything planned. As I see it, once I'm done, I'll have all that I need to live by myself."
    j "What about college?"
    mc "What {i}about{/i} college?"
    mc "It's kind of pointless. After this I'll have a house and enough money to live the rest of my life alone."
    mc "I'm just finishing high school because it's required by law."
    j "I see. But I don't think you're getting my point, [player]... I'm asking because I want you to think about it."
    mc "What's there to think about?"
    j "Well, for one thing, if you ever have a wife, kids, or even just by yourself, I don't think you can just expect to live off of what you have."
    j "Things get more expensive all the time. Soon you'll find yourself without anything..."
    mc "Jett... I really don't care."
    j "I'm just saying... You should at least get a job after this. All your brothers in the clan have their own businesses. Maybe you could start one."
    mc "Now that's more like it. I don't want to go to some stuffy 'university' just to wind up in debt and without any real skills."
    j "Just keep your mind open. There's a lot you can learn, [player]."
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
    "If you don't respond in time, you fail. Your performance relies on choosing the correct or 'better' option quickly. Make sure to save before any confrontation or mission."
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
            "You smoothly draw your switchblade from your pocket, extending the blade. But the man still runs towards you."
            $ combat_perf_score += 10
            jump day0_combat_m2v1
        "Draw Gun":
            hide screen countdown
            "You smoothly draw your Glock-17 from your pocket, disabling the safety. But the man still runs towards you."
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
            "You smoothly draw your switchblade from your pocket, extending the blade. But the man still runs towards you."
            jump day0_combat_m2v1
        "Use fists":
            $ combat_perf_score -= 10
            hide screen countdown
            "You hold up your hands and brace for impact"
            jump day0_combat_m2v3

label day0_combat_fail1:
    "You freeze in place and are stabbed in the chest. He twists the knife, shooting excruciating pain through your body, and tearing your heart."
    "He quickly pulls out the blade and blood pools onto the floor as you collapse."
    "You die quickly, to the sound of Jett running towards you."
    "Game Over."
    return
    
label day0_combat_m2v1:
    "You stand there as the man runs towards you, knife drawn. He prepares to strike."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    show screen countdown
    menu:
        "Dodge":
            hide screen countdown
            $ combat_perf_score += 10
            "You dodge the strike, making the man miss. As he moves past you, he runs into the wall. You get a slash on the back of his leg, forcing him to the ground."
            jump day0_combat_m3v1
        
        "Strike":
            hide screen countdown
            $ combat_perf_score += 5
            "You attack first, leaving a large gash in his side. His blade grazes your arm, leaving a small slash."
            "The man jumps back in pain. Now it's your turn to make a move."
            jump day0_combat_m3v1

label day0_combat_m3v1:
    "It's my time to strike! I charge and stab the injured man in the throat, his blood spurting out of his neck."
    "He collapses to the ground and dies."
    jump day0_combat_complete

label day0_combat_m3v2:
    "I steady my aim and pull the trigger one last time. The man falls, with a bullet lodged in his head. He dies instantly."
    jump day0_combat_complete

label day0_combat_m2v2:
    "You stand there as the man runs towards you, gun drawn, your hands are shaking. He prepares to strike."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    show screen countdown
    menu:
        "Begin firing":
            hide screen countdown
            $ combat_perf_score += 10
            "You begin firing at the man, your shaking hands causing a few shots to miss. You do hit him in the leg and arm, causing him to stop his charge."
            "It's your turn to make a move!"
            jump day0_combat_m3v2
            
        "Aim":
            hide screen countdown
            $ combat_perf_score += 15
            "You steady your aim and pull the trigger. One shot rings out, and the man falls, a bullet between his eyes. He instantly dies."
            jump day0_combat_complete

label day0_combat_m2v3:
    "You ready your fists, but realize it won't suffice in a knife fight."
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    show screen countdown
    menu:
        "Punch":
            $ combat_perf_score += 5
            "You punch the man in the face, stunning him temporarily. This gives you the chance to draw your..."
            pass
        
        "Dodge":
            $ combat_perf_score += 10
            "You dodge, giving you time to draw your..."
            pass
    
    
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'day0_combat_fail1'
    menu:
        "Knife":
            "You draw your knife. The man turns to you and charges again."
            jump day0_combat_m2v1
        "Gun":
            "You draw your Glock 18. The man turns to you and charges again."
            jump day0_combat_m2v2

label day0_combat_complete:
    $ combat_perf_score += 20
    $ combat_perf_score *= 2
    mdd "Good job. This was a successful run of the combat test."
    mdd "Although, this fight was very short, it's just an example of what can be done!"
    mdd "Your performance score was [combat_perf_score]! This is in the Combat category."
    jump day0_main2

label day0_main2:
    "The dead man lays on the floor, I begin sprinting towards the car."
    mc "Jett! Let's get the hell out of here!"
    "As I shout, Jett looks at my bloodied shirt, his eyes widen."
    mc "Get in the passenger side!"
    "He obeys, putting the gasoline pump back and entering the passenger side."
    "I jump into the driver's seat and floor it out of the gas station."
    "As I race through city streets, Jett turns to me."
    j "What the hell happened!?"
    mc "Another Yakuza charged me with a knife! I had no choice but to neutralize the target."
    j "He wasn't our clan?"
    mc "No. Let's hope that there aren't others tailing us."
    j "Give me your Glock, just in case I need to fire."
    "I pull the gun from its back holster and toss it to Jett."
    "I check my mirrors, noticing 2 black motorcycles and 3 black cars tailing us, trying to catch up."
    mc "Dammit Jett! They're coming from behind."
    j "You know the drill! Let's get these fuckers."
    "Jett lowers his window and begins spraying shots at an approaching motorcyclist."
    "One shot hits the wheel, causing a burst that sends the bike - and therefore the rider - out of control, tossing them to the side of the road."
    return