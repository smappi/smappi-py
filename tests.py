import unittest


class TestGotoUrl(unittest.TestCase):
    def test_helper(self):
        from smappi import smappi

        self.assertEqual(
            smappi('adw0rd/example').greeting(name='friend'),
            'Hello, friend!'
        )
        
    def test_full(self):
        import smappi

        self.assertEqual(
            smappi.Request('adw0rd/example', 'json').calculator(digits=[42, 42, 42]),
            126
        )
            
            
if __name__ == '__main__':
    unittest.main()
    
# To run the test suite
# python tests.py
