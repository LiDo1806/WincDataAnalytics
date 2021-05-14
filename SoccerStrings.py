# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Wie scoorde in deze wedstrijd.
scorer_name1 = "Ruud Gullit"
scorer_name2 = "Marco van Basten"

#In welke minuut werd er gescoord.
goal_0 = 32
goal_1 = 54

#Wie heeft er gescoord en wanneer.
scorers = (scorer_name1)+ ' ' + str(goal_0) + ', '+ (scorer_name2)+ ' ' + str(goal_1)
print(scorers)

#In zinvorm.
report = (f"{scorer_name1} scored in the {goal_0}nd minute and \n{scorer_name2} scored in the {goal_1}th minute")
print(report)

#Hier probeer ik een cheer te maken voor een speler. 
player = "Jan Wouters"
first_name = player[0:player.find(' ')]
print(first_name)
last_name_len = len(player[player.find(' ')+1:len(player)])
print(last_name_len)
name_short = player[0:1]+'. ' + player[player.find(' ')+1:len(player)]
print(name_short)
chant = ((player[0:player.find(' ')]+ '! ') * len(player[0:player.find(' ')]))[:-1]
print(chant)
good_chant = (' ' !=chant.strip()[-1])
print(good_chant)

                