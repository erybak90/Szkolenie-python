from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])


testdata = [Contact(Firstname="", Lastname="",address="", homephone="", mobilephone="",
                workphone="", secondaryphone="", email="", email2="", email3="")] + [
        Contact(Firstname=random_string("first", 4), Lastname=random_string("last", 4),
                address=random_string("address", 4),
                homephone=random_string("92", 6), mobilephone=random_string("666", 6),
                workphone=random_string("0", 6), secondaryphone=random_string("0000", 5), email=random_string("abc", 5),
                email2=random_string("zxc", 6), email3=random_string("ghjk", 6)) for i in range (5)


    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))