import random
"""
This is a sample module to simulate an external/third party API
which the program can not control the result of the method return.

This represent a module such as requests module to download files from 
the internet where you try to simulate network time out.
"""

RANDOM_GREET =[ 'Hello', 'Hi', 'Howdy', 'Greeting']
class ExternalGreetingAPI:

    def greeting(self, name):
        random_choice = random.randint(0, 3)
        return "{} {}".format(RANDOM_GREET[random_choice], name)
