import os
from Files import *


def createDirectoryTest():
    files = File()
    files._createDirectory("./AA/BB/CC")
    return os.path.exists("./AA/BB/CC")


def copyDirectoryTest():
    files = File()
    testPass = False
    try:
        files.copyDirectory("./AA/BB/CC/fff/f.js", "./AA/BB/CC/fff/f.js")
    except FileNotFoundError:
        testPass = True
    finally:
        return testPass


def splitPathTest():
    files = File()
    foldersArr, foldersLen = files._splitPath("AA/BB/CC/ff.js", True)
    return foldersLen == 4 and foldersArr[0] == "AA" and foldersArr[1] == "BB" and foldersArr[2] == "CC" and foldersArr[3] == "ff.js"
    testPass = False


def pathIncludesFileTest1():
    files = File()
    return files._pathIncludesAFile("./AA/BB/CC") == False


def fixSeperatorTets():
    files = File()
    slash = files._fixSeperators("./AA/BB")
    backSlash = files._fixSeperators(".\\AA\\BB")
    return slash == backSlash


def pathIncludesFileTest2():
    files = File()
    return files._pathIncludesAFile("./AA/BB/CC/ff.txt") == True


def appendFileToPathTest():
    files = File()
    result = files._appendFileToPath(
        "./AA/BB/CC/ff.js", "./AA/BB").split(files.seperator)
    return len(result) == 4 and result[3] == "ff.js"


def appendFileToPathTest2():
    files = File()
    testPassed = False
    try:
        files._appendFileToPath("./AA/BB/CC", "./AA/BB").split(files.seperator)
    except ValueError:
        testPassed = True
    finally:
        return testPassed


def appendFileToPathTest3():
    files = File()
    testPassed = False
    try:
        files._appendFileToPath(
            "./AA/BB/CC/ff.js", "./AA/BB/ff.js").split(files.seperator)
    except ValueError:
        testPassed = True
    finally:
        return testPassed


def copyFileTest():
    # copy to the same directory with the same name error
    files = File()
    testPassed = False
    try:
        files.copyFile("./ff.txt", "./")
    except ValueError:
        testPassed = True
    finally:
        return testPassed


def copyFileTest2():
    # copy to the same directory with diffrent name
    files = File()
    try:
        files.copyFile("./ff.txt", "./aa.txt")
        return os.path.exists("./aa.txt")
    except ValueError:
        return False


def copyFileTest3():
    # copy to path with the same file name
    files = File()
    try:
        files.copyFile("./ff.txt", "./AA/BB/CC")
        return os.path.exists("./AA/BB/CC/ff.txt")
    except:
        return False


def copyFileTest4():
    # copy to path
    files = File()
    try:
        files.copyFile("./ff.txt", "./AA/BB/CC/aa.txt")
        return os.path.exists("./AA/BB/CC/aa.txt")
    except:
        return False


def copyFileTest5():
    # Source path doens't include a file
    files = File()
    testPassed = False
    try:
        files.copyFile("./AA", "./AA/BB/CC/aa.txt")
    except ValueError:
        testPassed = True
    finally:
        return testPassed


def copyFileTest6():
    # Source file doesn't exists
    files = File()
    testPassed = False
    try:
        files.copyFile("./AA/savsabvsabvabva.txt", "./AA/BB/CC/aa.txt")
    except FileNotFoundError:
        testPassed = True
    finally:
        return testPassed


tests = [createDirectoryTest, copyDirectoryTest, splitPathTest,
         pathIncludesFileTest1, pathIncludesFileTest2, appendFileToPathTest, appendFileToPathTest2, appendFileToPathTest3, fixSeperatorTets, copyFileTest, copyFileTest2, copyFileTest3, copyFileTest4, copyFileTest5, copyFileTest6]


def runTests():
    failedTests = 0
    for test in tests:
        if test() == False:
            failedTests += 1
            result = "Fail"
            print("'"+test.__name__+"'", "test", "failed")
    return failedTests


def main():
    length = len(tests)
    failedTestsCount = runTests()
    testsPassedCount = length - failedTestsCount
    print("Test passed -", testsPassedCount, "/", length)


main()
