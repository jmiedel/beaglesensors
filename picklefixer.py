import pickle
import os

print "changes review date"
filename = raw_input('Enter a 3 digit file number: ')
filename = "00"+filename+".pickle"
dir = os.path.dirname(__file__)
filename = os.path.join(dir, filename)
form = pickle.load( open( filename, "rb" ))
if("screviewdate" in form):
    print "review date:",(form["screviewdate"])
print "submit date:",(form["fordate"])
newDate = raw_input('newreviewdate: ')
form["screviewdate"] = newDate
pickle.dump( form, open( filename, "wb" ) )