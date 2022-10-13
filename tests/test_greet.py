import unittest
#from unittest.mock import patch, Mock

# allow for python2 and 3 compatible
try:
    import unittest.mock
except ImportError:
    import mock
    unittest.mock = mock


from src.greet import Greeting


class MockExternalGreetingAPI:
    """
    Creating a mock class to handle external API Call where 
    we can not control the output
    """
    def __init__(self):
        self.RANDOM_GREET =[ 'Hello', 'Hi', 'Howdy', 'Greeting']

    def greeting(self, name):
        greet=self.RANDOM_GREET.pop(0)
        return "{} {}".format(greet, name)


class GreetingTest(unittest.TestCase):

    def setUp(self):
        """This get run before every test case run"""
        self.greet = Greeting()

    def tearDown(self):
        """This get run after every test case run"""
        pass

    def test_greeting_creation(self):
        """Testing the greeting object creation"""
        self.assertTrue(isinstance(self.greet, Greeting))

    def test_greeting_func_no_argument(self):
        """Checking greeting function return the correct value when run with no argument"""
        exp ='Hello World'
        self.assertEqual(exp, self.greet.greeting())
    
    def test_greeting_func_with_argument(self):
        """Checking greeting function return the correct value when run with argument"""
        exp ='Hello John'
        self.assertEqual(exp, self.greet.greeting('John'))

    def test_greeting_repeat_one_time(self):
        """Testing the greeting with repeat function return correct list"""
        exp = ['Hello John']
        actual = self.greet.greeting_repeat(name='John', repeat=1)
        self.assertEqual(exp, actual)

    def test_greeting_repeat_three_time(self):
        """Testing the greeting with repeat function"""
        exp = ['Hello John', 'Hello John', 'Hello John']
        actual = self.greet.greeting_repeat(name='John', repeat=3)
        self.assertEqual(exp, actual)

    def test_greeting_repeat_zero_time(self):
        """Testing the greeting with repeat function"""
        exp = []
        actual = self.greet.greeting_repeat(name='John', repeat=0)
        self.assertEqual(exp, actual)

    def test_greeting_repeat_negative_time(self):
        """Testing the greeting with repeat function negative repeat number raises exception"""
        with self.assertRaises(ValueError, msg='repeat time must be zero or positive number'):
            self.greet.greeting_repeat(name='John', repeat=-1)

    # UNCOMMENT THIS SECTION IF YOU WANT TO SEE TEST FAILED
    # def test_greeting_via_external_api(self):
    #     """This test should randomly fail as we do not know the result of the third party api"""
    #     exp ='Hello John'
    #     self.assertEqual(exp, self.greet.greeting_via_external_api('John'))

    @unittest.mock.patch('src.greet.ExternalGreetingAPI.greeting')
    def test_greeting_via_external_api_via_mock_return_value(self, mock_api):
        """
        Sometime we can not control the result of third party API such as network timeout
        or HTTP 404 errors. Here we use mock method to control the return of the third party
        API to test different behaviour
        """
        exp ='Hello John'
        mock_api.return_value = 'Hello John'
        self.assertEqual(exp, self.greet.greeting_via_external_api('John'))

    @unittest.mock.patch('src.greet.ExternalGreetingAPI.greeting')
    def test_greeting_via_external_api_via_mock_side_effect(self, mock_api):
        """
        We can not control the external return from the third party API
        and therefore use mock method to control the return of the third party
        API via side effect as the function return different result when called
        """
        mock_api.side_effect = MockExternalGreetingAPI().greeting
        self.assertEqual('Hello John', self.greet.greeting_via_external_api('John'))
        self.assertEqual('Hi John', self.greet.greeting_via_external_api('John'))
        self.assertEqual('Howdy John', self.greet.greeting_via_external_api('John'))
        self.assertEqual('Greeting John', self.greet.greeting_via_external_api('John'))

    def test_greeting_via_dependency_injection(self):
        """Test method via dependency injection"""
        injector_class = MockExternalGreetingAPI()
        self.assertEqual('Hello World', self.greet.greeting_via_dependency_injection(injector_class))


    def test_greeting_via_dependency_injection_with_mock(self):
        """Testing the method dependency inject using mock object"""
        mock_obj = unittest.mock.Mock()
        self.greet.greeting_via_dependency_injection(mock_obj, 'John')
        mock_obj.greeting.assert_called_with('John')

    def test_greeting_via_dependency_injection_with_mock_call_multi_times(self):
        """Testing the method dependency inject using mock object calling 2 times"""
        mock_obj = unittest.mock.Mock()
        self.greet.greeting_via_dependency_injection(mock_obj, 'John')
        self.greet.greeting_via_dependency_injection(mock_obj, 'Peter')
        self.assertEqual(mock_obj.greeting.call_count, 2)


# if __name__ == '__main__':
#     unittest.main()