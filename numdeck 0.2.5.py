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

p = pydirectinput
pl = pyautogui
numstate = GetKeyState(VK_NUMLOCK)
width = int(GetSystemMetrics(0)-450)
height = int(GetSystemMetrics(1)-550)
dirs = [
	'NUM7','NUM8','NUM9',
	'NUM4','NUM5','NUM6',
	'NUM1','NUM2','NUM3',
	'NUM_DIVIDE','NUM_MULTIPLY','NUM_SUBTRACT',
	'NUM_ADD','NUM_DECIMAL','NUM_ENTER',
	'NUM0']
class setup():
	current_folder = [os.getcwd()+'\\MAIN']
	def path(path_path):
		exists = os.path.exists(path_path)
		return exists
	def read(file):
		return open(file).read()
	def folder(path):
		folder = open(path)
		folder = folder.read()
		return folder
	def folder_structure(path):
		for a in dirs:
			os.makedirs(path+a)
			if a == 'NUM0':
				folder = open(path+a+'/FOLDER.txt', 'x')
				folder.write('FALSE')
				name = open(path+a+'/'+a+'_LABEL.txt', 'x')
				name.write('BACK')
				action = open(path+a+'/'+a+'_ACTION.txt', 'x')
				action.write('[BACK]')
			elif a == 'NUM_SUBTRACT':
				folder = open(path+a+'/FOLDER.txt', 'x')
				folder.write('FALSE')
				name = open(path+a+'/'+a+'_LABEL.txt', 'x')
				name.write('OPEN CWD')
				action = open(path+a+'/'+a+'_ACTION.txt', 'x')
				action.write('[CWD]')
			else:
				folder = open(path+a+'/FOLDER.txt', 'x')
				folder.write('FALSE')
				name = open(path+a+'/'+a+'_LABEL.txt', 'x')
				name.write('')
				action = open(path+a+'/'+a+'_ACTION.txt', 'x')
				action.write('[NONE]')
	def make_folders():
		if setup.path('MAIN') == False:
			os.mkdir('MAIN')
			folder = open('MAIN/FOLDER.txt', 'x')
			folder.write('TRUE')
			_help = open('MAIN/HELP.txt', 'x')
			_help.write("ACTIONS: [BACK] - navigate backwards through the folder directory\n\n"
						"[HOTKEY] - utilizes the https://pypi.org/project/keyboard/ module to send key presses\n"
						"eg. win+d\n\n"
						"[PATH] - Run path\n"
						R"eg. C:\users\user\Desktop\app.exe")
		files = []
		for r, d, f in os.walk(os.getcwd()):
			for file in f:
				files.append(os.path.join(r, file))
		for d in files:
			if "FOLDER.txt" in d:
				dfile = open(d)
				if dfile.read() == 'TRUE':
					path = str(d[:-11]+"\\")
					if setup.path(path+'\\FOLDER_NAME.txt'):
						pass
					else:
						folder_name = open(path+'FOLDER_NAME.txt', 'x')
						folder_name.write('NONE')
					if setup.path(path+'NUM7') == False:
						setup.folder_structure(path)
					else:
						pass
			else:
				pass
	def get_name(folder, num):
		name = []
		for r, d, f in os.walk(folder):
			for file in f:
				name.append(os.path.join(r, file))
		for d in name:
			if d.endswith(folder+'\\'+num+'\\'+num+'_LABEL.txt'):
				dlabel = open(d)
				dlabel = dlabel.read()
				return dlabel
			else:
				pass
setup.make_folders()
class overlay_class(wx.Frame, setup):
	def __init__(self):
		if numstate == 1:
			self.on = True
		else:
			self.on = False
		style = ( wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR |
				  wx.NO_BORDER | wx.FRAME_SHAPED  )
		wx.Frame.__init__(self, None, title='coc', style = style)
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
	def set_label(self):
		self.DIVIDE.SetLabel(setup.get_name(setup.current_folder[-1], 'NUM_DIVIDE'))
		self.MULTIPLY.SetLabel(setup.get_name(setup.current_folder[-1], "NUM_MULTIPLY"))
		self.SUBTRACT.SetLabel(setup.get_name(setup.current_folder[-1], "NUM_SUBTRACT"))
		self.DECIMAL.SetLabel(setup.get_name(setup.current_folder[-1], "NUM_DECIMAL"))
		self.PLUS.SetLabel(setup.get_name(setup.current_folder[-1], "NUM_ADD"))
		self.ENTER.SetLabel(setup.get_name(setup.current_folder[-1], "NUM_ENTER"))
		self.SEVEN.SetLabel(setup.get_name(setup.current_folder[-1], "NUM7"))
		self.EIGHT.SetLabel(setup.get_name(setup.current_folder[-1], "NUM8"))
		self.NINE.SetLabel(setup.get_name(setup.current_folder[-1], "NUM9"))
		self.FOUR.SetLabel(setup.get_name(setup.current_folder[-1], "NUM4"))
		self.FIVE.SetLabel(setup.get_name(setup.current_folder[-1], "NUM5"))
		self.SIX.SetLabel(setup.get_name(setup.current_folder[-1], "NUM6"))
		self.ONE.SetLabel(setup.get_name(setup.current_folder[-1], "NUM1"))
		self.TWO.SetLabel(setup.get_name(setup.current_folder[-1], "NUM2"))
		self.THREE.SetLabel(setup.get_name(setup.current_folder[-1], "NUM3"))
		self.ZERO.SetLabel(setup.get_name(setup.current_folder[-1], "NUM0"))
	def action(info):
		if '[BACK]' in info:
			if len(setup.current_folder) > 1:
				del setup.current_folder[-1]
				f.set_label()
		elif '[HOTKEY]' in info:
			info = info.strip('[HOTKEY]\n')
			print(info)
			kb.press_and_release(info)
		elif '[OPEN]' in info:
			info = info.strip('[OPEN]\n')
			cwd = r"{}".format(Path(info))
			path = subprocess.Popen(f'C:\\windows\\explorer.exe "{cwd}"')
		elif '[CWD]' in info:
			cwd = Path(setup.current_folder[-1])
			path = subprocess.Popen(f'C:\\windows\\explorer.exe "{cwd}"')
	def navigation(num):
		LS = []
		results = os.listdir(setup.current_folder[-1]+'\\'+num)
		for a in results:
			LS.append(os.path.join(setup.current_folder[-1]+'\\'+num+'\\'+a))
		for a in LS:
			if num+'\\FOLDER.txt' in a:
				if open(a).read() == 'TRUE':
					for b in LS:
						if num+'_LABEL.txt' in b:
							setup.current_folder.append(setup.current_folder[-1]+'\\'+num)
							f.set_label()
				elif open(a).read() == 'FALSE':
					for a in LS:
						if 'ACTION.txt' in a:
							overlay_class.action(setup.read(a))
							if setup.read(a) == "[NONE]":
								for a in LS:
									subprocess.Popen(f'C:\\windows\\explorer.exe "{a}"')
			else:
				pass
	def numpad_handler(num):
		keyboard = Controller()
		overlay_class.navigation(num)   
	def toggle_onoff(self):
		if self.on:
			self.on = False
			self.SetTransparent(0)
		elif self.on == False:
			self.on = True
			self.SetTransparent(200)
		setup.make_folders()
		overlay_class.set_label(self)   
	def on_press(key):
		num = '{0}'.format(key)[1:-1]
		NUM_DICT = {
			'103':'NUM7','104':'NUM8','105':'NUM9',
			'100':'NUM4','101':'NUM5','102':'NUM6',
			'97':'NUM1','98':'NUM2','99':'NUM3',
			'/':'NUM_DIVIDE','*':'NUM_MULTIPLY','-':'NUM_SUBTRACT',
			'+':'NUM_ADD','110':'NUM_DECIMAL','14':'NUM_ENTER',
			'96':'NUM0'}
		if '{0}'.format(key) == 'Key.num_lock':
			f.toggle_onoff()
		if f.on == True:
			if num in NUM_DICT:
				overlay_class.numpad_handler(NUM_DICT[num])
			else:
				pass
		else:
			pass
listener = keyboard.Listener(on_press=overlay_class.on_press)
listener.start()
app = wx.App()
s = setup()
f = overlay_class()
app.MainLoop()