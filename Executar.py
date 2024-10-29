from subprocess import Popen
from pywinauto import Application
import pyautogui
import Auxiliar
import os
import cv2
import time


if __name__  == '__main__':
    print('EXECUTANDO')

    pyautogui.PAUSE=1.5
    pyautogui.FAILSAFE=False

    #Modulo Fiscal
    varModuloOperador ="C:\\C5Client\\Fiscal\\Fiscal.EXE \n"
 
    #Variaveis de atenticacao c5
    varNome="automacao"
    varSenha="automacaocd99"
    
    #Variaveis dos modulos
    varMd_auxiliar = Auxiliar.Auxiliar()
       
    pyautogui.hotkey("win","r")
    pyautogui.sleep(2)
    pyautogui.typewrite(varModuloOperador,interval=0.015)
    pyautogui.sleep(5)

    #iniciando aplicativo da consinco
    app = Application().connect(class_name="Gupta:Dialog")
    pyautogui.sleep(2)
    #O formulário em questão não tem título, sendo assim foi identificado desta forma.
    dlg = app.window() 

    #Digitando os dados no formulário de login
    dlg['Edit4'].click_input() # Caixa de texto usuário
    dlg['Edit4'].type_keys("Vicentelj08") #Escrevendo na caixa de texto usuário
    pyautogui.sleep(1)
    dlg['Edit5'].click_input() # Click dentro da caixa de texto senha
    dlg['Edit5'].type_keys("1209") #Escrevendo na caixa de texto senha
    dlg['Button0'].click_input() # Click no butão entrar

   # varMd_exclusao.geraExclusao()
    pyautogui.sleep(1) 
    varMd_auxiliar.geraAuxliar()
    pyautogui.sleep(1)
   
                                                                            
print("CONCLUIDO")
    
    

   
   
  