class TestEngine:
    def __init__(self, name, tests, preTests=None, postTests=None):
        self.name = name
        self.preTests = preTests
        self.postTests = postTests
        self.tests = tests

    def runTests(self):
        failedTests = 0
        testsNumber = len(self.tests)
        if self.preTests != None:
            self.preTests()
        for test in self.tests:
            if test() == False:
                failedTests += 1
                result = "Fail"
                print("'"+test.__name__+"'", "test", "failed")
        print(self.name + " test passed -",
              testsNumber - failedTests, "/", testsNumber)
        if self.postTests != None:
            self.postTests()

    def addTest(self, test):
        self.tests.append(test)

    def removeTest(self, test):
        for test in self.tests:
            print(test)
