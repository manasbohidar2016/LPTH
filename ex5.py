name = 'Manas Bohidar'
Age = 35 #bit of a lie
height = 165 #cms
weight = 85 #kgs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He is %d cms tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofee." % teeth

# this line is tricky, try to get it exactly right

print "if I add %d, %d and %d I get %d." % (Age, height, weight, Age + height + weight)
print "I am trying to print %f" % round(7.43)