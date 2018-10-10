import sys

if sys.platform == "linux":
    from desktop_file.LinuxShortcut import LinuxShortcut as Shortcut
    from desktop_file.LinuxShortcut import getMenuPath, getDesktopPath
if sys.platform == "win32":
    from desktop_file.WindowsShortcut import WindowsShortcut as Shortcut
    from desktop_file.WindowsShortcut import getMenuPath, getDesktopPath
