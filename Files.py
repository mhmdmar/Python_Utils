import os
import shutil


class File():
    def __init__(self):
        self.seperator = os.path.sep

    def copyDirectory(self, source, dest):
        if not os.path.exists(source):
            raise FileNotFoundError("Source directory doesn't' exists")
        self._copyDirectory(source, dest)

    def _copyDirectory(self, source, dest):
        if not os.path.exists(dest):
            os.makedirs(dest)
        for file in os.listdir(source):
            s = os.path.join(source, file)
            d = os.path.join(dest, file)
            if os.path.isdir(s):
                copyDirectory(s, d)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copyfile(s, d)
        self._copyDirectory(source, dest)

    def _fixSeperators(self, path):
        ### Return the path with seperator changed to the current OS seperator ###
        return path.replace("\\", self.seperator).replace(
            "/", self.seperator)

    def _splitPath(self, path, includeFile=True):
        foldersArr = self._fixSeperators(path).split(self.seperator)
        foldersLen = len(foldersArr)
        # ignore the last part of the path if it represents a file
        if includeFile == False and self._pathIncludesAFile(path) == True:
            foldersLen -= 1
        return foldersArr, foldersLen

    def _createDirectory(self, path):
        ### Create all missing folders direcotries in the path ###
        foldersArr, foldersLen = self._splitPath(path, False)
        newPath = ""
        for i in range(foldersLen):
            newPath += (foldersArr[i]+"\\")
            if not os.path.exists(newPath):
                os.makedirs(newPath)

    def _pathIncludesAFile(self, path):
        path = self._fixSeperators(path)
        foldersArr, foldersLen = self._splitPath(path)
        return foldersArr[foldersLen-1].find(".") != -1

    def _appendFileToPath(self, source, dest):
        if self._pathIncludesAFile(dest) == True:
            raise ValueError(
                "Destination path already includes a file")
        if self._pathIncludesAFile(source) == False:
            raise ValueError(
                "Source doesn't include a file to append to dest argumnet")
        foldersArr, foldersLen = self._splitPath(source, True)
        dest = self._fixSeperators(dest)
        if not (dest[len(dest)-1] == self.seperator):
            dest += self.seperator
        dest += foldersArr[foldersLen-1]
        return dest

    def copyFile(self, source, dest):
        source = self._fixSeperators(source)
        dest = self._fixSeperators(dest)
        if self._pathIncludesAFile(source) == False:
            raise ValueError(
                "Source doesn't include a file to copy, use copyDirectory instead")
        if not os.path.exists(source):
            raise FileNotFoundError("Source file doesn't exists")
        if self._pathIncludesAFile(dest) == False:
            dest = self._appendFileToPath(source, dest)
            if source == dest:  # make sure we dont copy the file to the same directory with the same name
                raise ValueError(
                    "Copying the file with the same name to the same directory!")
        self._createDirectory(dest)
        shutil.copyfile(source, dest)
