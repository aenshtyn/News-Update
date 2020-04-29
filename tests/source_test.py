import unittest
from app.models import Source

class Sourcetest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('the-hindu','The Hindy','The Hindu. latest news, analysis, comment,','http://www.thehindu.com/','general', 'en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
