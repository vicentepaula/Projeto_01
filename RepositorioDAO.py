import ConectaBD
#from ConnectionBD import Connect_BD

class DAO:

        def __init__(self):
                self.con = ConectaBD.ConexaoOracle
            

        def executaQuery(self, query):
                conexao = self.con.conectar(self)
                resultados = []

                # Verifica se a conexão foi bem-sucedida
                if conexao is not None:
                        try:
                                cursor = conexao.cursor()

                                # Executa a consulta
                                for row in cursor.execute(query):
                                        resultados.append(row)

                                # Fecha o cursor
                                cursor.close()

                        except Exception as e:
                         print(f"Erro ao executar a consulta: {e}")

                        finally:
                        # Sempre desconecta, mesmo em caso de exceção
                         self.con.desconectar(self)
                         

                else:
                        print("Falha ao conectar ao banco de dados. CONEXAO É NULL.")

                return resultados
        

        
             
             
             
                
                
                    

        
                     