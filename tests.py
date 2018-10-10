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
        self.assertEqual(
            smappi.Request('adw0rd/example', 'json').calculator(digits='42,42,42'),
            126
        )

    def test_errors(self):
        import smappi

        try:
            resp = smappi.Request('adw0rd/example', 'json').calculator()
        except smappi.SmappiAPIError as e:
            self.assertEqual(str(e.kwargs.get('code')), '1501')
            self.assertEqual(str(e), 'No specified argument "digits" for "calculator". Please check Log tab for this API. (code: 1501)')

            
if __name__ == '__main__':
    unittest.main()
    
# To run the test suite
# python tests.py
