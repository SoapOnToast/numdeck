#GOALS
##CONVERT TO INI FILES
##COMPRESS SET LABEL
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
				config.set(a, 'ACTION', 'BACK')
			elif "NUM_SUBTRACT" in a:
				config.set(a, 'LABEL', 'CONFG')
				config.set(a, 'ACTION', '')
			else:
				config.set(a, 'LABEL', '')
				config.set(a, 'ACTION', '')
			config.set(a, 'HOTKEY', '')
			config.set(a, 'PATH', '')
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
		file =os.listdir(folder)
		for a in file:
			if ".ini" in a:
				config.read(folder+f"\\{a}")
				return config.get(num,"LABEL")
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
	def action(self,action,hotkey,path,file):
		if 'BACK' in action:
			if len(setup.current_folder) > 1:
				del setup.current_folder[-1]
				f.set_label()
		elif '' == action:
			cwd = Path(file)
			path = subprocess.Popen(f'C:\\windows\\explorer.exe "{cwd}"')
		elif 'PATH' in action:
			cwd = Path(path)
			path = subprocess.Popen(f'C:\\windows\\explorer.exe "{cwd}"')
		elif 'HOTKEY' in action:
			print(hotkey)
			kb.press_and_release(hotkey)
	def navigation(num):
		config = ConfigParser()
		file = os.listdir(setup.current_folder[-1])
		folder = setup.current_folder[-1]
		for a in file:
			if ".ini" in a:
				config.read(folder+f"\\{a}")
				folder = config.get(num,"FOLDER")
				action = config.get(num,"ACTION")
				hotkey = config.get(num,"HOTKEY")
				path = config.get(num,"PATH")
				if folder == "TRUE":
					if num in file:
						setup.current_folder.append(setup.current_folder[-1]+'\\'+num)
						f.set_label()
					else:
						setup.iniSetup(setup.iniPath(num))
				else:
					f.action(action,hotkey,path,setup.current_folder[-1]+'\\'+a)
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