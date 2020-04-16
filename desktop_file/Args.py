from desktop_file.Arg import Arg
import os


class Args:
    def __init__(self, args):
        self.args = args
        self.allArgs = [Arg("-h", "--help", 0),
                        Arg("-e", "--exec", 1),
                        Arg("-w", "--workpath", 1),
                        Arg("-c", "--comment", 1),
                        Arg("-i", "--icon", 1),
                        Arg("-n", "--index", 1),
                        Arg("-t", "--categories", 1),
                        Arg("-s", "--title", 1)]
        self.invalidValue = "invalid rarg rvalue"
        self.invalidArg = "invalid argument rarg"
    
    def formatArgs(self):
        formatedArgs = []
        files = []
        count = 0
        argCount = -1
        for arg in self.args:
            argCount += 1
            if count > 0:
                count -= 1
                continue
            found = False
            for maybeArg in self.allArgs:
                if arg == maybeArg.name or arg == maybeArg.shortName:
                    found = True
                    formatedArg = [maybeArg.name, []]
                    try:
                        for i in range(maybeArg.values):
                            formatedArg[1].append(self.args[argCount + i + 1])
                    except IndexError:
                        pass
                    formatedArgs.append(formatedArg)
                    count = maybeArg.values
            if not found:
                files.append(arg)
        return [formatedArgs, files]
    
    def exit(self):
        exit()
