import os


def getDesktopPath():
    try:
        output = os.path.expanduser("~/output")
        os.system("xdg-user-dir DESKTOP > " + output)
        path = open(output).read()
        os.remove(output)
    except Exception as e:
        print(e)
        path = os.path.expanduser("~/Desktop")
    stringList = list(path)
    while stringList[-1] == "\n":
        del stringList[-1]
        path = ""
        for i in stringList:
            path += i
    if os.path.exists(path):
        return path
    else:
        return None


def getMenuPath():
    path = os.path.expanduser("~/.local/share/applications")
    if os.path.exists(path):
        return path
    else:
        path = "/usr/local/share/applications"
        if os.path.exists(path):
            return path
        else:
            return None


class LinuxShortcut:
    def __init__(self, path, name, execFile):
        self.execFile = execFile
        self.name = name
        self.path = os.path.join(path, name) + ".desktop"
        self.file = open(self.path, "w")
        self.file.write("[Desktop Entry]\nType=Application\nName=" + self.name + "\nExec=" + self.execFile + "\n")
        self.attributes = {"Path": None, "Comment": None, "Icon": None, "Categories": None}
    
    def setWorkingDirectory(self, directory):
        self.attributes["Path"] = directory

    def setComment(self, comment):
        self.attributes["Comment"] = comment

    def setIcon(self, pathToIcon):
        self.attributes["Icon"] = pathToIcon
    
    def setCategories(self, categories):
        self.attributes["Categories"] = categories
    
    def save(self):
        for attrib in self.attributes:
            if self.attributes[attrib] != None:
                self.file.write(attrib + "=" + self.attributes[attrib] + "\n")
        self.file.close()
