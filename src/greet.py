from .external_greeting_api import ExternalGreetingAPI


class Greeting:
    """Greeting object for hello world or hello [name]"""

    def greeting(self, name='World'):
        """Return Hello World"""
        return 'Hello ' + name

    def greeting_repeat(self, name, repeat):
        """Return greeting string repeatedly in a list"""
        repeat_list = []
        if repeat < 0:
            raise ValueError("repeat time must be zero or positive number")
        for i in range(repeat):
            repeat_list.append(self.greeting(name))
        return repeat_list

    def greeting_via_external_api(self, name='World'):
        """Return Hello String via the use of external API"""
        return ExternalGreetingAPI().greeting(name)

    def  greeting_via_dependency_injection(self, dependency_class, name='World'):
        """Return Hello String via the use of external API"""
        return dependency_class.greeting(name)
       
