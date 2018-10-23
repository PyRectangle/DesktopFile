from setuptools import setup
import atexit
import sys
import os

setup(
    name = "desktop_file",
    version = "1.1",
    packages = ["desktop_file"],
    license = "MIT",
    include_package_data = True,
    author = "PyRectangle",
    author_email = "PyRectangle@web.de",
    url = "https://github.com/PyRectangle/DesktopFile",
    scripts = ["desktop-file"],
    description = "desktop-file is a tool to create desktop shortcuts for windows and linux.",
    install_requires=['pypiwin32; platform_system == "Windows"'],
    long_description = open('README.md').read(),
    long_description_content_type='text/markdown'
)
