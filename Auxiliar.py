from subprocess import Popen
from pywinauto import Application
import pyautogui
import FunAuxiliar
import os
import cv2
import time
import RepositorioDAO
from subprocess import Popen
from pywinauto import Application


class Auxiliar:
  

    def geraAuxliar(self):
        
        #Endereços 
        varscrennshot ="C:\\Projetos_Python\\FISCAL_SEMANAL\\Img\\screenshots_auxiliar\\"
        #Instancias gerais
        varFuncao = FunAuxiliar.Funcao_Apoio()
        #QueryBanco
        varExecuteDAO = RepositorioDAO.DAO()
        
        #As datas inicial e final, sempre corresponderá a um período de de uma semana
        dtaInicial = varExecuteDAO.executaQuery("SELECT TO_CHAR(SYSDATE - 7, 'DD/MM/YYYY') AS data_dia_anterior FROM dual")
        dtaFinal = varExecuteDAO.executaQuery("SELECT TO_CHAR(SYSDATE - 1, 'DD/MM/YYYY') AS data_dia_anterior FROM dual")
        
        #Variavel da imagens janelas
        varImgJanelaEmpresa="C:\\Projetos_Python\\FISCAL_SEMANAL\\Img\\Janelas\\empresas.png"
        varJanela_Auxiliar="C:\\Projetos_Python\\FISCAL_SEMANAL\\Img\\Janelas\\jn_auxiliar.png"
        #VariaveisQuerys
        varQueryLojas ="SELECT nroempresa, empresa FROM CONSINCO.dim_empresa WHERE nroempresa NOT IN (99, 800, 986, 989, 999, 10, 13, 20, 25, 29) ORDER BY CASE WHEN nroempresa = 987 THEN 0  ELSE 1  END, nroempresa"
      #  varQueryLojas ="select nroempresa, empresa from CONSINCO.dim_empresa where nroempresa not in (99, 800, 986, 989, 999, 10, 13, 20, 25,29, 987) and nroempresa > 28 order by NROEMPRESA"
                     
        pyautogui.press("ctrl")
        #Abrindo A janela Quitação de Título
        #pyautogui.sleep(2)
        pyautogui.press("alt")
        pyautogui.sleep(0.21)
        pyautogui.press("r")
        pyautogui.sleep(0.21)
        pyautogui.press("left", interval=0.069)
        pyautogui.sleep(0.21)
        pyautogui.press("down", presses=13, interval=0.069)
        pyautogui.press("right", interval=0.069)
        pyautogui.press("enter")
                    
        pyautogui.sleep(0.25)
        varLojas=varExecuteDAO.executaQuery(varQueryLojas)
    
        for row in varLojas:
            lj=row[0]
            strLoja = str(lj)
            nm_lj = row[1]

            nroloja = str(lj)

           # time.sleep(1)
            pyautogui.hotkey("ctrl","shift","t")
            varFuncao.AguardaAberturaJanela("Empresas")
           
            #Conectando em empresas administradoras
            appEmpre = Application().connect(title_re=".*Empresas.*", class_name="Gupta:Dialog") 
            dlgEmpresas = appEmpre.window(class_name="Gupta:Dialog")

            dlgEmpresas['Edit0'].click_input() # Clicando na data do campo numeroLoja
            pyautogui.sleep(0.21)
            pyautogui.keyDown("ctrl") #Selecionando a informacao
            pyautogui.keyDown("a")
            pyautogui.keyDown("a")
            pyautogui.keyDown("ctrl")
            dlgEmpresas['Edit0'].type_keys("{DELETE}")
            dlgEmpresas['Edit0'].type_keys(nroloja)
            dlgEmpresas['Button0'].click_input()
          
            varFuncao.esperar_fechamento_janela("Empresas")
                                                                         
            varFuncao.aguardar_janela_por_imagem(varJanela_Auxiliar, "Janela Auxiliar") 
            time.sleep(1)
            
            #Conectando na janela Auxiliar
            app1 = Application().connect(title_re=".*Fiscal.*")
            guptamdiframe = app1.window(class_name='Gupta:MDIFrame') 
            guptamdiframe.Wait('ready')
            selecao = guptamdiframe.ComboBox
            selecao.click()
            selecao.select("Intervalo") #Selecionando a opcao intervalo
            guptamdiframe[u'Edit1'].type_keys(dtaInicial)
            guptamdiframe[u'Edit2'].type_keys(dtaFinal)
               
            time.sleep(1)

            if nroloja == "987":                                                     
              listbox = guptamdiframe.ListBox
              listbox.select(1).click_input() # Colocando o foco no componente
              listbox.click_input(button="right")
              pyautogui.press("UP", presses=2, interval=0.35) #Desmarcando os itens desnecessários
              pyautogui.press("enter")
              pyautogui.sleep(1) 
              listbox.select(25) #Selecionando loja 987
              pyautogui.press("space")
            
            guptamdiframe[u'Button3'].click_input() #Clicando no botão que executa o processo
          
            time.sleep(2)
             
            # O click no botão executar auxiliar por padrão não chama esse janela de confirmação irei manter o codigo, apenas por precaução. 
            varExiste=varFuncao.check_window_exists("Atenção")
            if varExiste is False:
               pyautogui.click(82,96)  
                     

            varFuncao.AguardaAberturaentreduasJanelas("Atenção") 
                                                                                         
            time.sleep(1)

            app2 = Application().connect(title_re=".*Atenção.*")
            time.sleep(1)
            dlg = app2.window(title_re=".*Atenção.*")
            time.sleep(5)
           

            try:
              
             varFuncao.GetScreenShot(varscrennshot, nm_lj)
             time.sleep(1)
                      
            except:
              print("Falha ao retirar o print")
              
            dlg['&OKButton'].click_input()

            varExiste=varFuncao.check_window_exists("Atenção")
            if varExiste is True:
               pyautogui.click(962,746)   

        #Fechando a janela Auxiliar  
        appSair = Application().connect(title_re=".*Fiscal.*")
        sair = appSair.window(class_name='Gupta:MDIFrame') 
        sair[u'Button1'].click_input()
        

   

  



   
        
        

    
