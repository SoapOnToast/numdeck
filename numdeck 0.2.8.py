#GOALS
##switch for folder--
##clone for the main file--
##disable keyboard presses while blah blah blah
##config switch | set decimal to edit mode
##combine path/hotkey
###brought back config
###setup github---

import wx
import os
import subprocess
import pydirectinput
import pyautogui
import keyboard as kb
from win32api import GetSystemMetrics
from pynput import keyboard
from pynput.keyboard import Controller
from win32api import GetKeyState
from win32con import VK_NUMLOCK
from pathlib import Path
from configparser import ConfigParser
from tkinter import *
from tkinter.messagebox import *

p = pydirectinput
pl = pyautogui
numstate = GetKeyState(VK_NUMLOCK)
width = int(GetSystemMetrics(0)-450)
height = int(GetSystemMetrics(1)-550)
dirs = ['NUM7','NUM8','NUM9','NUM4','NUM5','NUM6','NUM1','NUM2','NUM3','NUM_DIVIDE','NUM_MULTIPLY','NUM_SUBTRACT','NUM_ADD','NUM_DECIMAL','NUM_ENTER','NUM0']

class setup():
	current_folder = [os.getcwd()+'\\MAIN']
	edit_mode = False
	def path(path_path):
		exists = os.path.exists(path_path)
		return exists
	def iniSetup(folder):
		configfile = open(f'{setup.current_folder[-1]}\\{folder}.ini', 'x')
		config = ConfigParser()
		for a in dirs:
			config.add_section(a)
			config.set(a, 'FOLDER', 'FALSE')
			if 'NUM0' in a:
				config.set(a, 'LABEL', 'BACK')
			elif "NUM_SUBTRACT" in a:
				config.set(a, 'LABEL', 'CWD')
			elif "NUM_DECIMAL" in a:
				config.set(a, 'LABEL', 'EDIT')
			else:
				config.set(a, 'LABEL', '')
			config.set(a, 'HOTKEY', '')
			config.set(a, 'PATH', '')
			if folder == 'MAIN':
				config.set(a, 'CLONE', 'FALSE')
		config.write(configfile)
		configfile.close()
	def fts():
		if setup.path('MAIN')==False:
			os.makedirs(f'{setup.current_folder[-1]}')
			setup.iniSetup('MAIN')
	def iniPath(folder):
		setup.current_folder.append(setup.current_folder[-1]+"\\"+folder)
		os.makedirs(f'{setup.current_folder[-1]}')
		return folder
	def get_name(folder, num):
		config = ConfigParser()
		file = os.listdir(folder)
		config.read("MAIN\\MAIN.ini")
		clone = config.get(num,"CLONE")
		if clone == 'TRUE':
			return config.get(num,"LABEL")
		else:
			for a in file:
				if ".ini" in a:
					config.read(folder+f"\\{a}")
					return config.get(num,"LABEL")
	def popUp(file,num):
		main = Tk()
		main.title(num)
		Label(main, text = "FOLDER =").grid(row=0,pady=5,padx=(5,0),sticky=E)
		Label(main, text = "LABEL =").grid(row=1,pady=5,padx=(5,0),sticky=E)
		Label(main, text = "HOTKEY =").grid(row=2,pady=5,padx=(5,0),sticky=E)
		Label(main, text = "PATH =").grid(row=3,pady=5,padx=(5,0),sticky=E)
		config = ConfigParser()
		_main = False
		if 'MAIN.ini' in file:
			_main = True
		def toggle():
		    if FOLDER.config('text')[-1] == 'TRUE':
		        FOLDER.config(text='FALSE')
		    else:
		        FOLDER.config(text='TRUE')
		        if _main:
		        	CLONE.config(text='FALSE')
		def toggleC():
		    if CLONE.config('text')[-1] == 'TRUE':
		        CLONE.config(text='FALSE')
		    else:
		        CLONE.config(text='TRUE')
		        FOLDER.config(text='FALSE')
		FOLDER = Button(main, text='', command=toggle)
		LABEL = Entry(main)
		HOTKEY = Entry(main)
		PATH = Entry(main)
		if ".ini" in file:
			buttonr= 4
			config.read(file)
			if config.get(num,"FOLDER") == 'TRUE':
				FOLDER.config(text='TRUE')
			else:
				FOLDER.config(text='FALSE')
			if _main:
				buttonr=5
				Label(main, text = "CLONE =").grid(row=4,pady=5,padx=(5,0),sticky=E)
				CLONE = Button(main, text='', command=toggleC)
				if config.get(num,"CLONE") == 'TRUE':
					CLONE.config(text='TRUE')
				else:
					CLONE.config(text='FALSE')
			LABEL.insert(0,config.get(num,"LABEL"))
			HOTKEY.insert(0,config.get(num,"HOTKEY"))
			PATH.insert(0,config.get(num,"PATH"))
		FOLDER.grid(row=0, column=1,pady=5,padx=(0,10),sticky=W)
		LABEL.grid(row=1, column=1,pady=5,padx=(0,10))
		HOTKEY.grid(row=2, column=1,pady=5,padx=(0,10))
		PATH.grid(row=3, column=1,pady=5,padx=(0,10))
		if _main:
			CLONE.grid(row=4, column=1,pady=5,padx=(0,10),sticky=W)
		def setdata():
			config = ConfigParser()
			config.read(file)
			config.set(num, 'FOLDER',FOLDER.cget('text'))
			config.set(num, 'LABEL', LABEL.get())
			config.set(num, 'HOTKEY', HOTKEY.get())
			config.set(num, 'PATH', PATH.get())
			if _main:
				config.set(num, 'CLONE',CLONE.cget('text'))
			with open(file, 'w') as configfile:
   				config.write(configfile)
		Button(main, text='SET', command=setdata).grid(row=buttonr, column=0, sticky=E, pady=5,padx=5)
		Button(main, text='CLOSE', command=main.destroy).grid(row=buttonr, column=1, sticky=W, pady=5,padx=5)
		mainloop()
class overlay_class(wx.Frame,wx.FocusEvent, setup):
	def __init__(self):
		if numstate == 1:
			self.on = True
		else:
			self.on = False
		style = ( wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.NO_BORDER | wx.FRAME_SHAPED )
		wx.Frame.__init__(self, None, title="deckn't", style = style)
		wx.FocusEvent.__init__(self, eventType=wxEVT_SET_FOCUS, id=0)
		self.panel = wx.Panel(self)
		self.SetSize((400, 500))
		self.SetPosition((width, height))
		self.SetTransparent(0)
		self.Show(True)
		self.NUMLOCK = wx.Button(self.panel, wx.ID_ANY, "HIDE", pos=(0, 0), size=(100,100))
		self.DIVIDE = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], 'NUM_DIVIDE'), pos=(100, 0), size=(100,100))
		self.MULTIPLY = wx.Button(self.panel, wx.ID_ANY,setup.get_name(setup.current_folder[-1], "NUM_MULTIPLY"), pos=(200, 0), size=(100,100))
		self.SUBTRACT = wx.Button(self.panel, wx.ID_ANY,setup.get_name(setup.current_folder[-1], "NUM_SUBTRACT"), pos=(300, 0), size=(100,100))
		self.DECIMAL = wx.Button(self.panel, wx.ID_ANY,setup.get_name(setup.current_folder[-1], "NUM_DECIMAL"), pos=(200, 400), size=(100,100))
		self.PLUS = wx.Button(self.panel, wx.ID_ANY,setup.get_name(setup.current_folder[-1], "NUM_ADD"), pos=(300, 100), size=(100,200))
		self.ENTER = wx.Button(self.panel, wx.ID_ANY,setup.get_name(setup.current_folder[-1], "NUM_ENTER"), pos=(300, 300), size=(100,200))
		self.SEVEN =wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM7"), pos=(0, 100), size=(100,100))
		self.EIGHT = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM8"), pos=(100, 100), size=(100,100))
		self.NINE = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM9"), pos=(200, 100), size=(100,100))
		self.FOUR = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM4"), pos=(0, 200), size=(100,100))
		self.FIVE = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM5"), pos=(100, 200), size=(100,100))
		self.SIX = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM6"), pos=(200, 200), size=(100,100))
		self.ONE = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM1"), pos=(0, 300), size=(100,100))
		self.TWO = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM2"), pos=(100, 300), size=(100,100))
		self.THREE = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM3"), pos=(200, 300), size=(100,100))
		self.ZERO = wx.Button(self.panel, wx.ID_ANY, setup.get_name(setup.current_folder[-1], "NUM0"), pos=(0, 400), size=(200,100))
		self.buttonVars = [(self.DIVIDE,'NUM_DIVIDE',(100,0)),(self.MULTIPLY, "NUM_MULTIPLY",(200,0)),(self.SUBTRACT, "NUM_SUBTRACT",(300,0)),(self.DECIMAL,"NUM_DECIMAL",(200, 400)),(self.PLUS, "NUM_ADD",(300,100)),(self.ENTER,"NUM_ENTER",(300,300)),(self.SEVEN, "NUM7",(0,100)),(self.EIGHT, "NUM8",(100,100)),(self.NINE, "NUM9",(200, 100)),(self.FOUR, "NUM4",(0, 200)),(self.FIVE, "NUM5",(100, 200)),(self.SIX, "NUM6",(200,200)),(self.ONE, "NUM1",(0,300)),(self.TWO, "NUM2",(100,300)),(self.THREE, "NUM3",(200,300)),(self.ZERO, "NUM0",(0,400))]

	def set_label(self):
		for a,b,c in self.buttonVars:
			a.SetLabel(setup.get_name(setup.current_folder[-1], b))
	def action(self,folder,num,label,hotkey,path,file,_dir):
		if 'EDIT' in label:
			if setup.edit_mode== True:
				setup.edit_mode = False
			else:
				setup.edit_mode = True
		elif setup.edit_mode:
			setup.popUp(file,num)
		elif 'TRUE' in folder:
			print(num)
			print(_dir)
			if num in _dir:
				setup.current_folder.append(setup.current_folder[-1]+'\\'+num)
				f.set_label()
			else:
				setup.iniSetup(setup.iniPath(num))
		elif 'BACK' in label:
			if len(setup.current_folder) > 1:
				del setup.current_folder[-1]
				f.set_label()
		elif 'CWD' in label:
			cwd = Path(setup.current_folder[-1])
			path = subprocess.Popen(f'C:\\windows\\explorer.exe "{file}"')
		elif '' == label:
			setup.popUp(file,num)
		elif path != '':
			cwd = Path(path)
			path = subprocess.Popen(f'C:\\windows\\explorer.exe "{cwd}"')
		elif hotkey != '':
			kb.press_and_release(hotkey)
	def navigation(num):
		config = ConfigParser()
		file = os.listdir(setup.current_folder[-1])
		folder = setup.current_folder[-1]
		config.read("MAIN\\MAIN.ini")
		clone = config.get(num,"CLONE")
		label = config.get(num,"LABEL")
		hotkey = config.get(num,"HOTKEY")
		path = config.get(num,"PATH")
		if clone == 'TRUE':
			f.action(folder,num,label,hotkey,path,"MAIN\\MAIN.ini",file)
		else:
			for a in file:
				if ".ini" in a:
					config.read(folder+f"\\{a}")
					label = config.get(num,"LABEL")
					folder = config.get(num,"FOLDER")
					hotkey = config.get(num,"HOTKEY")
					path = config.get(num,"PATH")
					f.action(folder,num,label,hotkey,path,setup.current_folder[-1]+'\\'+a,file)
	def numpad_handler(num):
		keyboard = Controller()
		overlay_class.navigation(num)
		f.set_label()
	def toggle_onoff(self):
		if self.on:
			self.on = False
			self.SetTransparent(0)
		elif self.on == False:
			self.on = True
			self.SetTransparent(200)
		overlay_class.set_label(self)
		overlay_class.set_label(self)
	def on_press(key):
		num = '{0}'.format(key)[1:-1]
		NUM_DICT = {'103':'NUM7','104':'NUM8','105':'NUM9','100':'NUM4','101':'NUM5','102':'NUM6','97':'NUM1','98':'NUM2','99':'NUM3','/':'NUM_DIVIDE','*':'NUM_MULTIPLY','-':'NUM_SUBTRACT','+':'NUM_ADD','110':'NUM_DECIMAL','14':'NUM_ENTER','96':'NUM0'}
		if '{0}'.format(key) == 'Key.num_lock':
			f.toggle_onoff()
		if f.on == True:
			if num in NUM_DICT:
				overlay_class.numpad_handler(NUM_DICT[num])
listener = keyboard.Listener(on_press=overlay_class.on_press)
listener.start()
app = wx.App()
setup.fts()
s = setup()
f = overlay_class()
app.MainLoop()
