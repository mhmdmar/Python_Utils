import os
from Files import Files
from TestEngine import TestEngine
files = Files()


def createDirectoryTest():

    files._createDirectory("./AA/BB/CC")
    return os.path.exists("./AA/BB/CC")


def copyDirectoryTest():
    testPass = False
    try:
        files.copyDirectory("./AA/BB/CC/fff/f.js", "./AA/BB/CC/fff/f.js")
    except FileNotFoundError:
        testPass = True
    finally:
        return testPass


def splitPathTest():
    foldersArr, foldersLen = files._splitPath("AA/BB/CC/ff.js", True)
    return foldersLen == 4 and foldersArr[0] == "AA" and foldersArr[1] == "BB" and foldersArr[2] == "CC" and foldersArr[3] == "ff.js"
    testPass = False


def pathIncludesFileTest1():
    return files._pathIncludesAFile("./AA/BB/CC") == False


def fixSeperatorTets():
    slash = files._fixSeperators("./AA/BB")
    backSlash = files._fixSeperators(".\\AA\\BB")
    return slash == backSlash


def pathIncludesFileTest2():
    return files._pathIncludesAFile("./AA/BB/CC/ff.txt") == True


def appendFileToPathTest():
    result = files._appendFileToPath(
        "./AA/BB/CC/ff.js", "./AA/BB").split(files.seperator)
    return len(result) == 4 and result[3] == "ff.js"


def appendFileToPathTest2():
    testPassed = False
    try:
        files._appendFileToPath("./AA/BB/CC", "./AA/BB").split(files.seperator)
    except ValueError:
        testPassed = True
    finally:
        return testPassed


def appendFileToPathTest3():
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
    testPassed = False
    try:
        files.copyFile("./ff.txt", "./")
    except ValueError:
        testPassed = True
    finally:
        return testPassed


def copyFileTest2():
    # copy to the same directory with diffrent name
    testPassed = False
    try:
        files.copyFile("./ff.txt", "./aa.txt")
        testPassed = os.path.exists("./aa.txt")
    except ValueError:
        testPassed = False
    finally:
        return testPassed


def copyFileTest3():
    # copy to path with the same file name
    try:
        files.copyFile("./ff.txt", "./AA/BB/CC")
        return os.path.exists("./AA/BB/CC/ff.txt")
    except:
        return False


def copyFileTest4():
    # copy to path
    try:
        files.copyFile("./ff.txt", "./AA/BB/CC/aa.txt")
        return os.path.exists("./AA/BB/CC/aa.txt")
    except:
        return False


def copyFileTest5():
    # Source path doens't include a file
    testPassed = False
    try:
        files.copyFile("./AA", "./AA/BB/CC/aa.txt")
    except ValueError:
        testPassed = True
    finally:
        return testPassed


def copyFileTest6():
    # Source file doesn't exists
    testPassed = False
    try:
        files.copyFile("./AA/savsabvsabvabva.txt", "./AA/BB/CC/aa.txt")
    except FileNotFoundError:
        testPassed = True
    finally:
        return testPassed


def preTests():
    if not os.path.exists("./AA/BB/CC"):
        os.makedirs("./AA/BB/CC")
    with open("./ff.txt", "w") as file:
        file.write("")


def postTests():
    files.removeDirectory("./AA")
    os.remove("./ff.txt")
    os.remove("./aa.txt")


def getTests():
    return [createDirectoryTest, copyDirectoryTest, splitPathTest,
            pathIncludesFileTest1, pathIncludesFileTest2, appendFileToPathTest, appendFileToPathTest2, appendFileToPathTest3, fixSeperatorTets, copyFileTest, copyFileTest2, copyFileTest3, copyFileTest4, copyFileTest5, copyFileTest6]


def main():
    testEngine = TestEngine("Files", getTests(), preTests, postTests)
    testEngine.runTests()


main()
