# Write code to
#
# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# Have sonny greet jordan using the greet method.
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan.
# Add a method 2
#
# Go back to the Person class. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person. You will use it thus:
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __repr__(self):
        return "%s's info: %s %s" % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1

    def print_contact_info(self):
        print "%s's email: %s %s's phone# %s:" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print "\n%s has %d friends" % (self.name, len(self.friends))



sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordon = Person('Jordon', 'jordon@aol.com', '495-586-3456')


sonny.greet(jordon)
jordon.greet(sonny)

print "%s's contact info is: %s, %s" % (sonny.name, sonny.phone, sonny.email)
print "%s's contact info is: %s, %s" % (jordon.name, jordon.phone, jordon.email)

sonny.print_contact_info()

sonny.add_friend(jordon)
# Add an instance variable (attribute)
#
# Add a friends instance variable (attribute) to the Person class. You will initialize it to an empty list within the constructor (__init__). Once you've done this you should be able to add a friend to a person using list's append method:
jordon.add_friend(sonny)
# Add a num_friends method
#
# Similarly, to get the number of friends a person has, we'd like to hide the implementation detail that there is a friends attribute which is a list. Implement a num_friends method which returns the number of friends the person currently has:
sonny.num_friends()
