from os import walk
from os import path
import os

"""
将 summary.md 和 navigation.md => SUMMARY.md 和 NAVIGATION.md
"""

def getAllFile(dir):
    """string -> list of tuple(fileDir, fileName)"""
    fileList = []
    for (dirpath, dirnames, filenames) in walk("."):
        curDirFileList = map(lambda fileName: (dirpath, fileName), filenames)
        fileList.extend(curDirFileList)
    return fileList


def filterRule(fileName):
    """string -> boolean"""
    return fileName == "summary.md" or fileName == "navigation.md"

def renameRule(originalName):
    """string -> string"""
    (fileNameWithoutExt, ext) = path.splitext(originalName)
    return fileNameWithoutExt.upper() + ext

def renameFiles(rule, files):
    """(string -> string) -> list of string -> None"""
    def renameFile(originalFile):
        originalName = originalFile[1]
        newName = rule(originalName)
        originalFileFullPath = path.join(originalFile[0], originalName)
        newFileFullPath = path.join(originalFile[0], newName)
        os.rename(originalFileFullPath, newFileFullPath)
        return (originalFile[0], newName)
    return map(renameFile, files)

if __name__ == "__main__":
    fileSet = getAllFile(".")
    matchFiles = filter(lambda x: filterRule(x[1]), fileSet)
    newfiles = renameFiles(renameRule, matchFiles)
    for file in newfiles:
        print(file)