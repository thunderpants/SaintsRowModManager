from cx_Freeze import setup, Executable
 
exe = Executable(
    script="main.py",
    base="Win32GUI",
    targetName = "SR3ModInstaller.exe",
    icon = "Icon.ico"
    )

setup(
    name = "Saints Row The Third Mod Installer",
    version = "1.0",
    description = "An simple Saints Row The Third Mod Installer",
    executables = [exe]
    )
