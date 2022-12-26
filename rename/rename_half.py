from os import walk
from os import path
import os

"""
将 summary.md 和 navigation.md => SUMMARY.md 和 NAVIGATION.md

先变成: summary0.md 和 navigation0.md, 进行git提交

然后再变成: SUMMARY.md 和 NAVIGATION.md, 再进行git提交

git无法直接区分大小写
"""


def upperName(oriName):
    """string -> string"""
    (fileNameWithoutExt, ext) = path.splitext(oriName)
    return fileNameWithoutExt.upper() + ext


rule = {
    "summary.md": lambda name: "summary0.md",
    "navigation.md": lambda name: "navigation0.md",
    "summary0.md": lambda name: "SUMMARY.md",
    "navigation0.md": lambda name: "NAVIGATION.md",
}


def getAllFile(dir):
    """string -> list of tuple(fileDir, fileName)"""
    fileList = []
    for (dirpath, dirnames, filenames) in walk("."):
        curDirFileList = map(lambda fileName: (dirpath, fileName), filenames)
        fileList.extend(curDirFileList)
    return fileList


def filterRule(fileName):
    """string -> boolean"""
    return fileName in rule.keys()


def renameRule(originalName):
    """string -> string"""
    return rule[originalName](originalName)


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
