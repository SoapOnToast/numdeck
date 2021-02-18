import wx
from win32api import GetSystemMetrics
from pynput import keyboard
from pynput.keyboard import Key, Controller
from win32api import GetKeyState 
from win32con import VK_NUMLOCK
import pydirectinput
import pyautogui

p = pydirectinput
pl = pyautogui

### Get NUMLOCK
numstate = GetKeyState(VK_NUMLOCK)
## get window
width = int(GetSystemMetrics(0))
height = int(GetSystemMetrics(1))
    #print(width,height)

##overlay code
class FancyFrame(wx.Frame):

    def __init__(self):

        self.current_folder = 'main'
        if numstate == 1:
            self.on = True
        else:
            self.on = False

        style = ( wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR |
                  wx.NO_BORDER | wx.FRAME_SHAPED  )
        wx.Frame.__init__(self, None, title='Fancy', style = style)
        self.panel = wx.Panel(self)
        self.SetSize((400, 500))
        self.SetPosition((width/2-200,height/2-250))
        self.SetTransparent(0)
        self.Show(True)

        self.NUMLOCK = wx.StaticBox(self.panel, wx.ID_ANY, "numstate", pos=(0, 0), size=(100,100))
        self.SLASH = wx.StaticBox(self.panel, wx.ID_ANY, "mute", pos=(100, 0), size=(100,100))
        self.ASTRIX = wx.StaticBox(self.panel, wx.ID_ANY, "deafen", pos=(200, 0), size=(100,100))
        self.DASH = wx.StaticBox(self.panel, wx.ID_ANY, "stream", pos=(300, 0), size=(100,100))
        self.DOT = wx.StaticBox(self.panel, wx.ID_ANY, "HIDE", pos=(200, 400), size=(100,100))

        self.SEVEN = wx.StaticBox(self.panel, wx.ID_ANY, "system", pos=(0, 100), size=(100,100))
        self.EIGHT = wx.StaticBox(self.panel, wx.ID_ANY, "discord", pos=(100, 100), size=(100,100))
        self.NINE = wx.StaticBox(self.panel, wx.ID_ANY, "apps", pos=(200, 100), size=(100,100))
        self.FOUR = wx.StaticBox(self.panel, wx.ID_ANY, "files", pos=(0, 200), size=(100,100))
        self.FIVE = wx.StaticBox(self.panel, wx.ID_ANY, "audio devices", pos=(100, 200), size=(100,100))
        self.SIX = wx.StaticBox(self.panel, wx.ID_ANY, "", pos=(200, 200), size=(100,100))
        self.ONE = wx.StaticBox(self.panel, wx.ID_ANY, "", pos=(0, 300), size=(100,100))
        self.TWO = wx.StaticBox(self.panel, wx.ID_ANY, "", pos=(100, 300), size=(100,100))
        self.THREE = wx.StaticBox(self.panel, wx.ID_ANY, "", pos=(200, 300), size=(100,100))
        self.ZERO = wx.StaticBox(self.panel, wx.ID_ANY, "BACK", pos=(0, 400), size=(200,100))
        self.ENTER = wx.StaticBox(self.panel, wx.ID_ANY, "", pos=(300, 300), size=(100,200))
        self.PLUS = wx.StaticBox(self.panel, wx.ID_ANY, "", pos=(300, 100), size=(100,200))

        self.SEVENB = wx.StaticBoxSizer(self.SEVEN)
        self.EIGHTB = wx.StaticBoxSizer(self.EIGHT)
        self.NINEB = wx.StaticBoxSizer(self.NINE)
        self.FOURB = wx.StaticBoxSizer(self.FOUR)
        self.FIVEB = wx.StaticBoxSizer(self.FIVE)
        self.SIXB = wx.StaticBoxSizer(self.SIX)
        self.ONEB = wx.StaticBoxSizer(self.ONE)
        self.TWOB = wx.StaticBoxSizer(self.TWO)
        self.THREEB = wx.StaticBoxSizer(self.THREE)

    def main(self):
        print('main')
        self.current_folder = 'main'
        self.SEVEN.SetLabel('system')
        self.EIGHT.SetLabel('discord')
        self.NINE.SetLabel('apps')
        self.FOUR.SetLabel('files')
        self.FIVE.SetLabel('audio devices')

    def system(self):
        print('system')
        self.current_folder = 'system'
        self.SEVEN.SetLabel('')
        self.EIGHT.SetLabel('')
        self.NINE.SetLabel('')
        self.FOUR.SetLabel('')
        self.FIVE.SetLabel('')
        self.ONE.SetLabel('')
        self.TWO.SetLabel('')
        self.THREE.SetLabel('')

    def discord(self):
        print('discord')
        self.current_folder = 'discord'
        self.SEVEN.SetLabel('mute')
        self.EIGHT.SetLabel('deafen')
        self.NINE.SetLabel('live')
        self.FOUR.SetLabel('streamer mode')
        self.FIVE.SetLabel('disconnect')
        self.ONE.SetLabel('')
        self.TWO.SetLabel('')
        self.THREE.SetLabel('')

    def apps(self):
        print('apps')
        self.current_folder = 'apps'
        self.SEVEN.SetLabel('')
        self.EIGHT.SetLabel('')
        self.NINE.SetLabel('')
        self.FOUR.SetLabel('')
        self.FIVE.SetLabel('')
        self.ONE.SetLabel('')
        self.TWO.SetLabel('')
        self.THREE.SetLabel('')

    def files(self):
        print('files')
        self.current_folder = 'files'
        self.SEVEN.SetLabel('')
        self.EIGHT.SetLabel('')
        self.NINE.SetLabel('')
        self.FOUR.SetLabel('')
        self.FIVE.SetLabel('')
        self.ONE.SetLabel('')
        self.TWO.SetLabel('')
        self.THREE.SetLabel('')

    def audio(self):
        print('audio')
        self.current_folder = 'audio'
        self.SEVEN.SetLabel('')
        self.EIGHT.SetLabel('')
        self.NINE.SetLabel('')
        self.FOUR.SetLabel('')
        self.FIVE.SetLabel('')
        self.ONE.SetLabel('')
        self.TWO.SetLabel('')
        self.THREE.SetLabel('')

    def toggle_onoff(self):
        if self.on:
            self.on = False
            self.SetTransparent(0)
        elif self.on == False:
            self.on = True
            self.SetTransparent(200)

def mute():
    p.keyDown('shift')
    p.keyDown('alt')
    p.keyDown('m')
    p.keyUp('shift')
    p.keyUp('alt')
    p.keyUp('m')
    print('mute')

def deafen():
    p.keyDown('shift')
    p.keyDown('alt')
    p.keyDown('d')
    p.keyUp('shift')
    p.keyUp('alt')
    p.keyUp('d')
    print('deafen')

def live():
    p.keyDown('shift')
    p.keyDown('alt')
    p.keyDown('l')
    p.keyUp('shift')
    p.keyUp('alt')
    p.keyUp('l')
    print('live')

def hide():
    pl.hotkey('winleft','d')

def numpad_handler(num):
    keyboard = Controller()
    if num == '/':
        mute()
    elif num == '*':
        deafen()
    elif num == '-':
        live()
    elif num == '+':
        pass
    elif num == '.':
        hide()
    elif num == 0:
        f.main()

    elif f.current_folder == 'main':
        if num == 7:
            f.system()
        elif num == 8:
            f.discord()
        elif num == 9:
            f.apps()
        elif num == 4:
            f.files()
        elif num == 5:
            f.audio()
        else:
            pass
    elif f.current_folder == 'system':
        if num == 7:
            pass
        elif num == 8:
            pass
        elif num == 9:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 6:
            pass
        elif num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
    elif f.current_folder == 'discord':
        if num == 7:
            mute()
        elif num == 8:
            deafen()
        elif num == 9:
            live()
        elif num == 4:
            #stream()
            pass
        elif num == 5:
            ##disconnect()
            pass
        elif num == 6:
            pass
        elif num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
    elif f.current_folder == 'apps':
        if num == 7:
            pass
        elif num == 8:
            pass
        elif num == 9:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 6:
            pass
        elif num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
    elif f.current_folder == 'files':
        if num == 7:
            pass
        elif num == 8:
            pass
        elif num == 9:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 6:
            pass
        elif num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
    elif f.current_folder == 'audio':
        if num == 7:
            pass
        elif num == 8:
            pass
        elif num == 9:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 6:
            pass
        elif num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass            
    elif f.current_folder == 'system':
        ##SYSTEM CONTROLS
        pass
    elif f.current_folder == 'discord':
        ##DISCORD CONTROLS
        pass
    elif f.current_folder == 'apps':
        ##apps CONTROLS
        pass
    elif f.current_folder == 'files':
        ##file CONTROLS
        pass

def on_press(key):

    #codes
    num = '{0}'.format(key)[1:-1]
    num0 = '96'
    num1 = '97'
    num2 = '98'
    num3 = '99'
    num4 = '100'
    num5 = '101'
    num6 = '102'
    num7 = '103'
    num8 = '104'
    num9 = '105'

    if '{0}'.format(key) == 'Key.num_lock':
        f.toggle_onoff()
    if f.on == True:
        if num == '/':
            numpad_handler('/')
        elif num == '*':
            numpad_handler('*')
        elif num == '-':
            numpad_handler('-')
        elif num == '+':
            numpad_handler('+')
        elif num == '110':
            numpad_handler('.')
        elif num == num0:
            numpad_handler(0)
        elif num == num1:
            numpad_handler(1)
        elif num == num2:
            numpad_handler(2)
        elif num == num3:
            numpad_handler(3)
        elif num == num4:
            numpad_handler(4)
        elif num == num5:
            numpad_handler(5)
        elif num == num6:
            numpad_handler(6)
        elif num == num7:
            numpad_handler(7)
        elif num == num8:
            numpad_handler(8)
        elif num == num9:
            numpad_handler(9)
        else:
            pass
    else:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

app = wx.App()
f = FancyFrame()
app.MainLoop()