from Tkinter import *
import math

master = Tk()

criteria = ["Cheesiness", "Cowbellness", "Coolness", "Likability"]
ideas = ["Cheese", "Cowbell", "Stephen Colbert", "Ricky Gervais"]
bios = ["Man's never hot", "According to all known laws of aviation", "There is no reason a bee should be able to fly", "The bee of course flies anyway because bees don't care what people think"]
j = 0

def leave_event(event, wind, bind):
    wind.withdraw()
##    j=0
##    for i in ideas:
##        bind[j].bind("<Enter>", lambda event, q=j: enter_event(event, q))
##        j += 1

bio_win = []
def enter_event(event, q):
    bio = Tk()
    bio.deiconify()
    bio_win.append(Label(bio, text=bios[q]))
    bio_win[q].bind("<Leave>", lambda event, wind=bio, bind=bio_win: leave_event(event, wind, bind))
    bio_win[q].grid(row=0,column=0,rowspan=5,columnspan=3)
    bio.mainloop()

idea_win = []


for i in ideas:
    idea_win = [0 for k in range(len(ideas))]
    idea_win[j] = Label(master, text=i) #.append(Label(master, text=i))
    idea_win[j].bind("<Enter>", lambda event, q=j: enter_event(event, q))
    idea_win[j].grid(row=j+1,column=0)
    j += 1

j=0
for i in criteria:
    Label(master, text=i).grid(row=0,column=j+1)
    j += 1

crit_num = []
for i in range(len(criteria)):
    crit_num.append(str(i+1))

variable = {}
w = {}
values = {}
totals = {}


for i in range(len(ideas)*len(criteria)):
    #for j in range(len(criteria)):
        #variable = [[0 for x in range(len(ideas))] for y in range(len(criteria))]
        variable.update({i: StringVar(master)})
        variable[i].set(crit_num[0]) # default value

        #w = [[0 for x in range(len(ideas))] for y in range(len(criteria))]
        w.update({i: apply(OptionMenu, (master, variable[i]) + tuple(crit_num))})
        w[i].grid(row=(i%len(ideas))+1, column=(i/len(criteria))+1)


def submit_action():
    for i in range(len(ideas)*len(criteria)):
        #for j in range(len(criteria)):
            values.setdefault(criteria[(i/len(criteria))], [])
            values[criteria[(i/len(criteria))]].append(ideas[(i%len(ideas))] + "=" + str(variable[i].get()))
            totals.setdefault(ideas[(i%len(ideas))], [])
            totals[ideas[(i%len(ideas))]].append(int(variable[i].get()))
             #Look at this. It is broken. Think about it. Solve it. You are so close.
    for i in range(len(ideas)):
        totals[ideas[i]] = sum(totals[ideas[i]][0:len(totals[ideas[i]])])
    with open('submit.txt','a') as file:
        for item in values:
            print>>file, item, values[item]
        for item in totals:
            print>>file, item, totals[item]
    #bio.destory()
    master.destroy()
    print range(len(ideas))
    print range(len(criteria))
    print values
    print totals
    
    

submit = Button(master, text="Submit", width=10, command=submit_action).grid(row=len(ideas)+1,column=int(math.ceil(len(criteria)/2)),columnspan=2)


#master.after(500, idea)
master.mainloop()
