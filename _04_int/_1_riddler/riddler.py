"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    u_score=0


    q1 = simpledialog.askstring(title='1?', prompt="What question can you never answer yes to?")
    q2 = simpledialog.askstring(title='2?', prompt="What is always in front of you but can’t be seen?")
    q3 = simpledialog.askstring(title='3?', prompt="I can start a war or end one, I can give you the strength of heroes or leave you powerless. I may be snared with a glance but no force can compel me to stay. What am I?")
    q4 = simpledialog.askstring(title='4?', prompt="A nightmare for some. For others, a savior I come. My hand's cold and bleak. It's the warm hearts they seek")
    q5 = simpledialog.askstring(title='5?', prompt="What do a dead man, a cruise ship and emu have in common?")
    q6 = simpledialog.askstring(title='6?', prompt="strong as a rock, but a word can destroy me. What am I?")
    q7 = simpledialog.askstring(title='7?', prompt="What's strong enough to smash ships but still fears the sun?")
    q8 = simpledialog.askstring(title='8?', prompt="the poor have, the rich need, and if you eat it you'll die.")
    q9 = simpledialog.askstring(title='9?', prompt="The more you cut me the bigger I grow. What am I?")
    q10 = simpledialog.askstring(title='10?', prompt="What's green and then red?")


    
    if (q1=="are you asleep yet"):
        u_score+=1
    if (q2=="The future"):
        u_score+=1
    if (q3=="love"):
        u_score+=1
    if (q4=="Death"):
        u_score+=1
    if (q5=="nothing"):
        u_score+=1
    if (q6=="Silence"):
        u_score+=1
    if (q7=="ice"):
        u_score+=1
    if (q8=="nothing"):
        u_score+=1
    if (q9=="a hole"):
        u_score+=1
    if (q10=="frogs in a blender"):
        u_score+=1


    messagebox.showinfo(message=str(u_score))
