import unittest
import HTMLTestRunner

if __name__ == "__main__":
    suit = unittest.TestSuite()
    tests = unittest.defaultTestLoader.discover(".", "test_*.py")
    for test in tests:
        suit.addTest(test)

    with open("HTMLReport.html", "w") as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f, verbosity=2, title="MailNotification Test Report", description="generated by HTMLTestRunner")
        runner.run(suit)