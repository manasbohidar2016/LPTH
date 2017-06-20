#use a %d assignment to a variable
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#pass string to form string which can directly be used in print
y = "Those who know %s and those who know %s." % (binary,do_not)

print x
print y

print "I said: %r." % x
print "I also said %s." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with right side."

#concatenation
print w + e