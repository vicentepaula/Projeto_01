import pyautogui
import FunAuxiliar
import time
import os
import cv2
import ConectaBD
import RepositorioDAO
import FunAuxiliar
import pygetwindow as gw

if __name__  == '__main__':
    print('EXECUTANDO TESTE01...!!!')
   # exec = FunAuxiliar.Funcao_Apoio()
   # exec.GetScreenShot("C:\\Projetos_Python\\FISCAL\\Img\\screenshots_definitiva\\")
   # pyautogui.click(911,555) 

    varFuncao = FunAuxiliar.Funcao_Apoio()
    varFuncao.GetScreenShot("C:\\Projetos_Python_new\\FISCAL_SEMANAL\\Img\\screenshots_definitiva\\", "loja12") 
    #dia_anterior  = varFuncao.data_dia_anterior()
   # print(dia_anterior.strftime('%Y-%m-%d'))
   
                
  
    
    time.sleep(10000)
   
    janelas_abertas = gw.getAllTitles()

    # Exibe os nomes das janelas
    for janela in janelas_abertas:
        print(janela)
    
    time.sleep(10000)
    


    time.sleep(2)
    coordenadas = pyautogui.position()
    print(coordenadas)

    
   
    exec.insertData("26/02/2024", "03/03/2024")

    time.sleep(100000)

    varFuncao = FunAuxiliar.Funcao_Apoio()
    varFuncao.AguardaAberturaJanela("Fiscal")

    