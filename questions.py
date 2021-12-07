
from random import choice
from time import sleep

class questions:

        def popup_question(self):
                rand = self.random_qn()
                qchoice = choice(list(rand.keys()))
                qn = rand[qchoice]
                qview = qn["question"]
                rand.pop(qchoice)
                print(f"""===================================
POP-UP QUESTION: a test to your whole existence
 """)
                while True:
                        print(f"""{qview}
===================================""")
                        ans = input("Your choice: ")   
                        if ans.lower() == 'a':
                                print(f"""===================================
{qn["outcome_a"]}""")
                                input("Press ENTER to continue")
                                break
                        elif ans.lower() == 'b':
                                
                                print(f"""===================================
{qn["outcome_b"]}""")
                                print("\nYOU DIED")
                                exit()
                        else: 
                                print("You have entered an invalid action!")
                                continue


        def popup_question2(self):
                rand2 = self.random_qn2()
                qchoice2 = choice(list(rand2.keys()))
                qn2 = rand2[qchoice2]
                qview2 = qn2["question"]
                rand2.pop(qchoice2)
                print(f"""===================================
POP-UP QUESTION: another test
""")
                while True:
                        print(f"""{qview2}
===================================""")
                        ans = input("Your choice: ")   
                        if ans.lower() == 'a':
                                print(f"""===================================
{qn2["outcome_a"]}""")
                                input("Press ENTER to continue")
                                break
                        elif ans.lower() == 'b':
                                
                                print(f"""===================================
{qn2["outcome_b"]}""")
                                print("===================================")
                                print("GAME OVER")
                                sleep(3)
                                print("Just kidding that is just how society wants us to think")
                                input("Press ENTER to continue")
                                break
                        else: 
                                print("You have entered an invalid action!")
                                continue


        def game_qn(self):
                question = {1:"""You've got homework and assignments due the next day and your friend asked you to hang out together with her. Would you ...

[ [ ]a ] join her because of peer pressure.
[ [ ]b ] decline politely and said you would join next time.
[ [ ]c ] None of the above""", 

2:"""Upon hearing negative comments about yourself from others, how would you react?

[ [ ]a ] Self-blame and self-hate.
[ [ ]b ] Take it with a pinch of salt.
[ [ ]c ] None of the above""", 

3:"""You see your friends post stories of them having fun hanging out with other groups of friends, you...

[ [ ]a ] wonder why you do not have as many friends as them.
[ b ] feel happy for them.
[ c ] None of the above""", 

4:"""Your group members are experienced in the topic for your school assignment, but you are completely new to the topic. You...

[ a ] feel bad about yourself for not knowing as much as them and cannot contribute much to the project.
[ b ] see it as an opportunity to learn from your group mates and improve yourself.
[ c ] None of the above""", 

5:"""You are out with your friends for dinner and they suggest to go for a few drinks. Based on past experience, it never stops at a few. Your friends are all trying to convince you but you have an important meeting tomorrow that could greatly affect your life. What will you do?

[ a ] YOLO join them and get completely wasted! A little alcohol in your body will increase confidence during the meeting.
[ b ] Reject their bad influence and get new friends.
[ c ] None of the above.""", 

6:"""Which statement describes you the best?

[ a ] You copy other people's lifestyle that you see on Instagram to validate yourself.
[ b ] You accept yourself as who you are.
[ c ] None of the above""", 

7:"""You don't have enough money but you are tempted to buy branded items because you saw some of your friends buying them recently. You will...

[ a ] ask your parents for money unconsiderately.
[ b ] write it down as a motivation to work harder so that you can buy it by your own money.
[ c ] None of the above""", 

8:"""You recently started dating someone. Your partner has been telling you that you should stop meeting with your close friends as he/she does not like them. You...

[ a ] stop seeing your close friends as you are scared he/she will leave you.
[ b ] explain to your partner that your friends are really important to you, and that you cannot forget them.
[ c ] None of the above""", 

9:"""Which statement describes you the best?

[ a ] You demand for people to understand you as you feel more vulnerable than others.
[ b ] You try to understand others' situation even if you are feeling down.
[ c ] None of the above""", 

10:"""You wanted to make new friends in university. You will...

[ a ] join a group of toxic friends despite being used all the time because you are scared you won't have friends at all.
[ b ] approach your classmates and engage in a small talk with them.
[ c ] None of the above"""}
                return question
        

        def random_qn(self):
                question = {1:{"question":"""Your parents wish to go on a month long vacation, should they go?    

[ a ] Yes
[ b ] No""", "outcome_a":"""Congratulations You are alive! You were conceived during the vacation so you would not have existed without it. Have fun!""", "outcome_b":"""As a result of not going for the vacation where you were conceived, you no longer exist. """},

2:{"question":"""You are running late for class and the pedestrian crossing light is about to turn red. Should you make a run for it or wait for the next one?   

[ a ] Wait as a good citizen should
[ b ] I am the Flash """, "outcome_a":"""A traffic accident occurs at the crossing, you shudder at thought of what might have happened if you dashed accross...""", "outcome_b":"""Truck-kun comes along and hits you"""},

3:{"question":"""Do you support getting Vaccinated against COVID-19?

[ a ] Vaccines are okay...got mine so I can eat out 
[ b ] Vaccines are a cospiracy created by big pharma and Governments, I will never yield my freedom!!""" , "outcome_a":"""There is Omicron but the vaccines are still effective. """, "outcome_b":"""Beep...beep...beep....beep.................That's the sound of your vital signs monitor flatlining after contracting COVID-19"""}
}
                return question
        

        def random_qn2(self):
                question = {1:{"question":"""Finals are next week and you have not started studying, but your friends have just invited you to go for supper. You...    

[ a ] Decline and spend the night studying
[ b ] Join them, you can always start tomorrow right?""", "outcome_a":"""You have passed your finals due to your hard work""", "outcome_b":"""You are now 30 and sweep the streets for a living. You often wonder what your life would be like if you didn't slack off so much..."""},

2:{"question":"""You are grocery shopping with your friends when you see one of them secretly slip a bottle of alcohol into their bag. What do you do?

[ a ] Confront them and convince them to pay for it
[ b ] Snitches get stitches. You pretend not to have seen anything""", "outcome_a":"""Life goes on as usual...""", "outcome_b":"""Your friend gets caught red-handed and you are all arrested. You now have a criminal record that will follow you the rest of your life..."""}
}
                return question
        