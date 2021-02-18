#GOALS
##GET RID OF ACTION--
##GUI EDITOR--
##MAIN MEMORY--

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
				config.set(a, 'LABEL', 'CONFG')
			else:
				config.set(a, 'LABEL', '')
			config.set(a, 'HOTKEY', '')
			config.set(a, 'PATH', '')
			if folder == 'MAIN':
				config.set(a, 'CLONE', 'FALSE')
		config.write(configfile)
		configfile.close()
	def fts():
		folder = 'MAIN'
		if setup.path(folder)==False:
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
		FOLDER = Entry(main)
		LABEL = Entry(main)
		HOTKEY = Entry(main)
		PATH = Entry(main)
		a = file
		if ".ini" in a:
			config.read(a)
			FOLDER.insert(0,config.get(num,"FOLDER"))
			LABEL.insert(0,config.get(num,"LABEL"))
			HOTKEY.insert(0,config.get(num,"HOTKEY"))
			PATH.insert(0,config.get(num,"PATH"))
		FOLDER.grid(row=0, column=1,pady=5,padx=(0,10))
		LABEL.grid(row=1, column=1,pady=5,padx=(0,10))
		HOTKEY.grid(row=2, column=1,pady=5,padx=(0,10))
		PATH.grid(row=3, column=1,pady=5,padx=(0,10))
		def setdata():
			config = ConfigParser()
			config.read(a)
			config.set(num, 'FOLDER',FOLDER.get())
			config.set(num, 'LABEL', LABEL.get())
			config.set(num, 'HOTKEY', HOTKEY.get())
			config.set(num, 'PATH', PATH.get())
			with open(a, 'w') as configfile:
   				config.write(configfile)
		Button(main, text='SET', command=setdata).grid(row=4, column=0, sticky=E, pady=5,padx=5)
		Button(main, text='CLOSE', command=main.destroy).grid(row=4, column=1, sticky=W, pady=5,padx=5)
		mainloop()

class overlay_class(wx.Frame, setup):
	def __init__(self):
		if numstate == 1:
			self.on = True
		else:
			self.on = False
		style = ( wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.NO_BORDER | wx.FRAME_SHAPED  )
		wx.Frame.__init__(self, None, title="deckn't", style = style)
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
	def action(self,num,label,hotkey,path,file):
		if 'BACK' in label:
			if len(setup.current_folder) > 1:
				del setup.current_folder[-1]
				f.set_label()
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
		for a in file:
			config.read("MAIN\\MAIN.ini")
			clone = config.get(num,"CLONE")
			label = config.get(num,"LABEL")
			hotkey = config.get(num,"HOTKEY")
			path = config.get(num,"PATH")
			if clone == 'TRUE':
				f.action(label,hotkey,path,"MAIN\\MAIN.ini")
			else:
				if ".ini" in a:
					config.read(folder+f"\\{a}")
					label = config.get(num,"LABEL")
					folder = config.get(num,"FOLDER")
					hotkey = config.get(num,"HOTKEY")
					path = config.get(num,"PATH")
					if folder == "TRUE":
						if num in file:
							setup.current_folder.append(setup.current_folder[-1]+'\\'+num)
							f.set_label()
						else:
							setup.iniSetup(setup.iniPath(num))
					else:
						f.action(num,label,hotkey,path,setup.current_folder[-1]+'\\'+a)
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