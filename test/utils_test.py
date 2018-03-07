import unittest

# from utils.winrm.winrm_session import winrm_session


class TestStringMethods(unittest.TestCase):
    # run = winrm_session('192.168.130.129', '\Marco Mendez', 'Control123')
    # def test_set_execution_policy_to_unrestrict(self):
    #     expect_result = 0
    #     actual_result = self.run.set_execution_policy_to_unrestrict
    #     self.assertEqual(expect_result,actual_result)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()