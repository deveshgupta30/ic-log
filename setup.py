from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ICLog.pyw", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ICLog",
    options = options,
    version = "3.0.1",
    description = 'Component Management System',
    executables = executables
)
