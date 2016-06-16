# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('HeartbeatRollCall.pyw', base=base, icon='icon256.ico')
]


setup(
    name="HeartbeatRollCall",
    version="0.1",
    description="心跳点名",
    options=options,
    executables=executables
)

        #,
        # path=['/usr/lib/python3/dist-packages'],targetName='99999',copyDependentFiles=True
