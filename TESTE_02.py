import pyautogui
import FunAuxiliar
import time
import os
import cv2
import ConectaBD
import RepositorioDAO
import FunAuxiliar
from subprocess import Popen
from pywinauto import Application
import uuid

#from FunAuxiliar import Funcao_Apoio

if __name__  == '__main__':
  print('EXECUTANDO TESTE 2...!!!')

  print(uuid.uuid4())
  pyautogui.sleep(100000)

  pyautogui.click(387,67)
  pyautogui.press("alt")
  pyautogui.sleep(0.21)
  pyautogui.press("a")   
  pyautogui.press("down", presses=4, interval=0.069)
  pyautogui.press("enter")      
  time.sleep(10000)

  app = Application().connect(title_re=".*Fiscal.*")
  time.sleep(1)
  dlg = app.window(title_re=".*Fiscal.*")
  time.sleep(5)
      
  #dlg['&OKButton'].click_input()

  dlg.print_control_identifiers()
 # time.sleep(10000)

   # print(pyautogui.KEYBOARD_KEYS)
  #time.sleep(3)
  #pyautogui.doubleClick(pyautogui.locateCenterOnScreen("C:\\Projetos_Python\\FISCAL\\Img\\campos_janela_exclusao\\btn_exclusao.png", confidence=0.90), duration=0.35)
                                      
 # pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Projetos_Python\\FISCAL\\Img\\campos_janela_exclusao\\btn_ok_jn_exclucao.png",confidence=0.4, grayscale=True), duration=0.15)
  #pyautogui.leftClick(pyautogui.locateCenterOnScreen("C:\\Projetos_Python\\FISCAL\\Img\\campos_janela_exclusao\\btn_exclusao.png", confidence=0.88), duration=0.15)

  x, y = pyautogui.position()
  print(x,y)
  time.sleep(10000)
  
  for nro in range(1):
       pyautogui.leftClick(pyautogui.locateCenterOnScreen("C:\\Projetos_Python\\FISCAL\\Img\\campos_jn_definitiva\\tx_data_def.png",confidence=0.71), duration=0.15) 
       time.sleep(2)
       pyautogui.hotkey("ctrl","a") 
       time.sleep(2)
       pyautogui.typewrite("07/03/2024")
       time.sleep(2)
       pyautogui.hotkey("ctrl","shift","t") 
       time.sleep(2)
       pyautogui.doubleClick(77,122)
       time.sleep(1)
       pyautogui.typewrite("987"+"\n",interval=0.15)

       #varFuncao = FunAuxiliar.Funcao_Apoio()
       #varFuncao.Trt_lj987()
       