from desktop_file.Args import Args
import desktop_file
import sys
import os


class Main:
    def __init__(self):
        self.helpText = open(os.path.join(os.path.dirname(desktop_file.__file__), "help.txt")).read()
        self.args = Args(sys.argv[1:])
        self.format = self.args.formatArgs()
        command = None
        workpath = None
        comment = None
        icon = None
        index = 0
        categories = None
        title = None
        for arg in self.format[0]:
            try:
                if arg[0] == "--help":
                    print(self.helpText)
                    self.args.exit()
                if arg[0] == "--exec":
                    command = arg[1][0]
                if arg[0] == "--workpath":
                    workpath = arg[1][0]
                if arg[0] == "--comment":
                    comment = arg[1][0]
                if arg[0] == "--icon":
                    icon = arg[1][0]
                if arg[0] == "--index":
                    index = arg[1][0]
                if arg[0] == "--categories":
                    categories = arg[1][0]
                if arg[0] == "--title":
                    title = arg[1][0]
            except IndexError:
                print("A parameter must be provided for \"" + arg[0] + "\".")
                self.args.exit()
        if len(self.format[0]) == 0:
            print("no arguments given")
            print("Type \"-h\" or \"--help\" for help.")
            self.args.exit()
        elif len(self.format[1]) == 0:
            print("no files given")
            print("Type \"-h\" or \"--help\" for help.")
            self.args.exit()
        elif len(self.format[1]) > 1:
            print("you can only create one file at once")
            self.args.exit()
        elif command != None:
            shortcut = desktop_file.Shortcut(os.path.dirname(self.format[1][0]), os.path.basename(self.format[1][0].replace(".desktop", "").replace(".lnk", "")), command)
            self.setProp(workpath, shortcut.setWorkingDirectory)
            self.setProp(comment, shortcut.setComment)
            self.setProp(categories, shortcut.setCategories)
            self.setProp(title, shortcut.setTitle)
            if icon != None:
                shortcut.setIcon(icon, index)
            shortcut.save()
        else:
            print("you need to specify an exec")

    def setProp(self, prop, function):
        if prop != None:
            function(prop)


if __name__ == "__main__":
    Main()
