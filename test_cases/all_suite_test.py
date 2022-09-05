import unittest

from unittest.loader import makeSuite

from test_cases.fill_search_box import TestSearchBox
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.adding_a_player_to_the_database import TestAddingAPlayerToTheDatabase
from test_cases.change_language import TestChangeLanguage
from test_cases.login_in_with_invalid_data import TestLoginPageInvalidDate
from test_cases.sign_out import TestLoginPageSignOut


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestSearchBox))
    test_suite.addTest(makeSuite(Test))
    test_suite.addTest(makeSuite(TestAddingAPlayerToTheDatabase))
    test_suite.addTest(makeSuite(TestChangeLanguage))
    test_suite.addTest(makeSuite(TestLoginPageInvalidDate))
    test_suite.addTest(makeSuite(TestLoginPageSignOut))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())