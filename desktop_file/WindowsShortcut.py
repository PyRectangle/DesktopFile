from win32com.shell import shell, shellcon
import pythoncom
import os


def getDesktopPath():
    path = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, 0, 0)
    if os.path.exists(path):
        return path
    else:
        return None


def getMenuPath():
    path = shell.SHGetSpecialFolderPath(0, shellcon.CSIDL_STARTMENU)
    if os.path.exists(path):
        return path
    else:
        return None


class WindowsShortcut:
    def __init__(self, path, name, execFile):
        self.execFile = execFile
        self.name = name
        self.path = os.path.join(path, name) + ".lnk"
        self.file = pythoncom.CoCreateInstance(shell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
        if os.path.exists(self.execFile):
            self.file.SetPath(self.execFile)
        self.working = None
    
    def setWorkingDirectory(self, directory):
        self.file.SetWorkingDirectory(directory)
        self.working = directory

    def setComment(self, comment):
        self.file.SetDescription(comment)

    def setIcon(self, pathToIcon, index = 0):
        self.file.SetIconLocation(pathToIcon, index)
    
    def setCategories(self, categories):
        pass

    def setTitle(self, title):
        pass
    
    def save(self):
        if not os.path.exists(self.execFile):
            if self.working != None:
                path = self.working
            else:
                path = "."
            path = os.path.join(path, self.name + ".bat")
            count = 0
            while os.path.exists(path):
                count += 1
                path = os.path.join(os.path.dirname(path), self.name + str(count) + ".bat")
            file = open(path, "w")
            file.write(self.execFile)
            file.close()
            self.file.SetPath(path)
        file = self.file.QueryInterface(pythoncom.IID_IPersistFile)
        file.Save(self.path, 0)
