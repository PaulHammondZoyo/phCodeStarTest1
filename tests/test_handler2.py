import unittest
import index2


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = index2.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello World2', result['body'])


if __name__ == '__main__':
    unittest.main()
