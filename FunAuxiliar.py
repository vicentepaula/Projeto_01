import pygetwindow as gw
import cv2
import pyautogui
import time
import datetime
#from datetime import datetime, timedelta


class Funcao_Apoio:

  
    #Retorna o título da Janela Ativa
    def GetScreenShot(self,caminhoArquivo, nmLoja):
        screenshot = pyautogui.screenshot()
        data_hora_atual = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        nome_arquivo = f'{nmLoja}_{data_hora_atual}.png'

        #screenshot.save(f"C:\\Projetos_Python\\FISCAL\\Img\\screenshots_auxiliar\\{nome_arquivo}")
        screenshot.save(f"{caminhoArquivo}{nome_arquivo}")
        
     

    # Aguarda até a janela abrir.
    def AguardaAberturaJanela(self, janela_alvo):

     # Nome da janela que estou está esperando abrir
       
           # Loop para verificar continuamente se a janela alvo foi aberta
        while True:
            # Obtém todas as janelas ativas
            janelas = gw.getAllWindows()

            # Verifica se a janela alvo está entre as janelas ativas
            if any(janela_alvo in janela.title for janela in janelas):
                print("Janela alvo foi aberta!:")
                break  # Sai do loop quando a janela alvo for encontrada

            # Pausa por um curto período de tempo antes de verificar novamente
            time.sleep(1)  # Importe time se você ai

    #
    def AguardaAberturaentreduasJanelas(self, janela_alvo):

        #Nome da janela que estou está esperando abrir
       
           # Loop para verificar continuamente se a janela alvo foi aberta
        while True:
            # Obtém todas as janelas ativas
            janelas = gw.getAllWindows()

            # Verifica se a janela alvo está entre as janelas ativas
            if any(janela_alvo in janela.title for janela in janelas):
                print("Janela alvo foi aberta!:")
                break  # Sai do loop quando a janela alvo for encontrada
            else:
                if any("Atenção" in janela.title for janela in janelas):
                    pyautogui.click(977,560, duration=0.25)
                    break
                
            # Pausa por um curto período de tempo antes de verificar novamente
            time.sleep(1)  # Importe time se você ai

       
               
   
     # Testa se a janela existe baseado em imagens
    def aguardar_janela_por_imagem(self,imagem_janela, mensagem): # Passar o endereço da imagem salvo no computador
        
        while True:

            try:
                posicao = pyautogui.locateCenterOnScreen(imagem_janela, confidence=0.2)
                if posicao is not None:
                   return 0
          
            except Exception as e:
                print(f'Aguardando {mensagem}...', e)

    
    def esperar_fechamento_janela(self, janela_alvo):
                
        #Loop para verificar continuamente se a janela alvo foi aberta
        while True:
            # Obtém todas as janelas ativas
            janelas = gw.getAllWindows()

            # Verifica se a janela alvo está entre as janelas ativas
            if any(janela_alvo in janela.title for janela in janelas):
                print("Janela alvo foi aberta!")
            else:
                print("Janela alvo não existe mais. Encerrando o script.")
                break  # Sai do loop quando a janela alvo não existe mais

            # Pausa por um curto período de tempo antes de verificar novamente
            time.sleep(1)  # Importe time se você ainda não o fez
        
        
    def check_window_exists(self, window_name):
        time.sleep(2)
        # Obtém todas as janelas ativas
        windows = gw.getWindowsWithTitle(window_name)
        
        # Verifica se a lista de janelas não está vazia
        if windows:
            return True
        else:
            return False
    
    #SEM USO
    #Retorna o título da Janela Ativa
    def GetTituloJanelaAtiva(self):
        janela_ativa = gw.getActiveWindow().title
        return janela_ativa

    


            
                
                 