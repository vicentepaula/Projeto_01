from subprocess import Popen
from pywinauto import Application
import pyautogui
import FunAuxiliar
import time
import os
import cv2
import ConectaBD
import RepositorioDAO
import FunAuxiliar
#from FunAuxiliar import Funcao_Apoio

if __name__  == '__main__':
  print('EXECUTANDO TESTE...!!!')


  

  appDlgOk2 = Application().connect(title_re=".*Fiscal.*")
  window = appDlgOk2.Dialog
  window.Wait('ready')
  button = window[u'&Sim']
  button.click_input()

  pyautogui.sleep(100000)
  appDlgOk = Application().connect(title_re=".*Fiscal.*")
  window = appDlgOk.Dialog
  window.Wait('ready')
  button = window[u'&OK']
  button.click_input()


  pyautogui.sleep(100000)
  appDlg = Application().connect(title_re=".*Fiscal.*")
  window = appDlg.Dialog
  window.Wait('ready')
  button = window[u'&Sim']
  button.click_input()


  

  app2 = Application().connect(title_re=".*Fiscal.*")
  time.sleep(1)
  dlg = app2.window(title_re=".*Fiscal.*")
  time.sleep(5)

  dlg[u'Contabilizar Definitivo'].click_input()
           


  pyautogui.sleep(10000)

   # print(pyautogui.KEYBOARD_KEYS)
  time.sleep(5)

  app = Application().connect(title_re=".*Fiscal.*")
  guptamdiframe = app.window(class_name='Gupta:MDIFrame') 
  guptamdiframe.Wait('ready')
  selecao = guptamdiframe.ComboBox
 # combobox = guptamdiframe['']
  #combobox.Select(u'Hoje')

  selecao.click()
  selecao.select("Intervalo")

  guptamdiframe[u'Edit1'].type_keys("15/05/2024")
  guptamdiframe[u'Edit2'].type_keys("18/05/2024")

  listbox = guptamdiframe.ListBox
  listbox.select(1).click_input() # Colocando o foco no componente
  listbox.click_input(button="right")
  pyautogui.press("UP", presses=2, interval=0.35) #Desmarcando os itens desnecessários
  pyautogui.press("enter")

  pyautogui.sleep(1) 
  listbox.select(25) #Selecionando loja 987
  pyautogui.press("space")

  selecao.print_control_identifiers()

 # guptamdiframe.menu_select("Processos -> Contabilização")

  #main_window = app.top_window()
  #window_title = main_window.window_text()
  
  #print("O título da janela é:", window_title)
  #guptamdiframe.print_control_identifiers()
  ##guptamdiframe.window_title.menu_select('Processos -> Contabilização')




  #profuiscontrolbar = guptamdiframe[u'4']
 # profuiscontrolbar.ClickInput()

 # pyautogui.click(263,418)
  time.sleep(10000000)

  x, y = pyautogui.position()
  print(x,y)

  time.sleep(10000000)
  
    

  varExecuteDAO = RepositorioDAO.DAO()
  varLojas=varExecuteDAO.executaQuery("select nroempresa, empresa from CONSINCO.dim_empresa where nroempresa not in (99, 800, 986, 989, 999, 10, 13, 20, 25,29) order by NROEMPRESA")
  varFuncao = FunAuxiliar.Funcao_Apoio()
  
 # pyautogui.hotkey("ctrl","shift","t")
  time.sleep(2)
  for row in varLojas:
    lj=row[0]
    nm=row[1]
    strLoja = str(lj)

    caminho ="C:\\Projetos_Python\\FISCAL\\Img\\screenshots_auxiliar\\"

    varFuncao.GetScreenShot(caminho, nm)
    time.sleep(2)
    print(f"Nro_Loja:{strLoja} Nome Loja: {nm}" )






  

  print('CONCLUIDO')

                                        