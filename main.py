
from Tkinter import *
import tkFileDialog,tkMessageBox,shutil,os
root = Tk()
root.title("Superstepa's Saints Row Mod Manager")
try:
	root.wm_iconbitmap('Icon.ico')
except TclError:
	print "Error: Icon not found"

mods = []
modlabels = []
vppmods = []
numberofmods = 0
try:
	f = open ("directory.cfg", "r")
	DIRECTORY = f.read()
	if(DIRECTORY == ""):
		raise IOError
	f.close()
except IOError:
	f = open("directory.cfg", "w")
	DIRECTORY = tkFileDialog.askdirectory(title = "Please choose your 'Saints Row The Third' installation directory",initialdir = "C://Program Files/Steam/Steamapps/common/saints row the third")
	f.write(DIRECTORY)
	f.close()

VPPDIRECTORY = DIRECTORY + "/packfiles/pc/cache/"
BACKUPDIRECTORY = os.getcwd() +"\\backup\\"
print BACKUPDIRECTORY
print "The game installation directory is " + DIRECTORY

def ChooseMod():
	global mods

	mod = tkFileDialog.askopenfilenames(title = "Please choose the mod files", filetypes = [('All', '.*'),('Vpp_pc', '.vpp_pc'), ('Lua', '.lua'), ("Str2_pc" ,'str2_pc'), ('Xtbl', '.xtbl'), ('Asm_pc', '.asm_pc')])
	mod = root.splitlist(mod)
	for x in mod:
		print x
		mods.append(x)
		modlabel = Label(labelframe,text = x)
		modlabel.pack()
		modlabels.append(modlabel)
		if ('.vpp_pc' in x):
				vppmods.append(x)
	
		
def ChangeDirectory():
	f = open("directory.cfg", 'w')
	DIRECTORY = tkFileDialog.askdirectory(title = "Please choose your 'Saints Row The Third' installation directory ", initialdir = "C://Program Files/Steam/Steamapps/common/saints row the third")
	f.write(DIRECTORY)
	f.close()
	print "Directory changed to " + DIRECTORY



def InstallVpp(file):
	os.system('cls')
	print "Installing " + file
	shutil.copy(file,VPPDIRECTORY)


def InstallOther(file):
	os.system('cls')
	print "Installing " + file
	shutil.copy(file,DIRECTORY)
	os.system('cls')
	print "Sucessfully installed "

if ("steam" not in DIRECTORY.lower()):
	tkMessageBox.showwarning("Error","You a dirty pirate!") 

def StartInstall():
	global mods,numberofmods
	for x in mods:
		if ('.vpp_pc' in x):
				InstallVpp(x)
				numberofmods+=1
		elif ('.lua' in x) or ('.str2_pc' in x) or ('.asm_pc' in x) or ('.xtbl' in x):
				InstallOther(x)
				numberofmods+=1
		else:
				print x + " Is Not A Mod"
	ClearModList()
	print "Sucessfully installed " + str(numberofmods) + " mods"

def ClearModList():
	global mods,modlabels
	os.system('cls')
	mods = []
	for x in modlabels:
		x.forget()
	modlabels = []

def Backup():
	global vppmods
	if not os.path.exists(BACKUPDIRECTORY):
		print "Error: Backup directory not found, creating it now"
		os.makedirs(BACKUPDIRECTORY)

	for x in vppmods:
		vpp = x
		vpporiginal = VPPDIRECTORY + os.path.basename(x)
		try:
			shutil.copy(vpporiginal,BACKUPDIRECTORY)
			print "Sucessfully backed up " + vpporiginal
		except IOError:
			tkMessageBox.showwarning("Error","Not Found")


def Uninstall():
	global BACKUPDIRECTORY
	os.system('cls')
	print "Restoring vpp mods from backup"
	backups = os.listdir(BACKUPDIRECTORY)
	for x in backups:
		try:
			shutil.copy(BACKUPDIRECTORY + x,VPPDIRECTORY)
			print "Sucessfully restored " + x
		except IOError:
			print "Couldn't restore " + x

	print "Uninstalling loose mods"

	loosemods = os.listdir(DIRECTORY)
	for x in loosemods:
		if ('.lua' in x) or ('.str2_pc' in x) or ('.asm_pc' in x) or ('.xtbl' in x):
			print "Removing " + x
			os.remove(DIRECTORY +"/" + x)
	ClearModList()
	print "Removed all mods"


frame = Frame(root)
frame2 = Frame(root)

ChooseModButton = Button(frame, text="Choose Mods", command=ChooseMod)
ChooseModButton.pack(side=LEFT, padx = 100)
ChangeDirectoryButton = Button(frame, text = "Change the installation directory", command = ChangeDirectory)
ChangeDirectoryButton.pack(side = RIGHT, padx = 100)
InstallButton = Button(frame,text = "Install the mods (Backup first)", command = StartInstall)
InstallButton.pack(side = TOP,pady = 10)
ClearModsButton = Button(frame,text = "Clear The Mod List", command = ClearModList)
ClearModsButton.pack(side = LEFT,padx = 10)
BackupButton = Button(frame, text = "Backup packfiles", command = Backup)
BackupButton.pack(side = RIGHT, padx = 10)
RestoreButton = Button(frame, text = "Uninstall all mods", command = Uninstall)
RestoreButton.pack(side = TOP)
labelframe = LabelFrame(frame2, text="Mods:")
labelframe.pack(fill="both", expand="yes")
  


frame.pack()
frame2.pack()
root.mainloop()