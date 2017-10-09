import spade
import time

class tabuleiro(spade.Agent.Agent):
    mapa = []
    posObjetivo = []
    players = []
            
    def criaMapa(self): #-2 livre | -1 parede | -3 objetivo
        tam = 6
        
        #cria uma matrix quadrada de ordem tam
        mapa = [0] * tam
        for i in range(tam):
            mapa[i] = [0] * tam
            
        mapa = [[-1, -1, -1, -1, -1, -1],
                [-1, -2, -1, -1, -3, -1],
                [-1, -2, -2, -2, -2, -1],
                [-1, -2, -1, -2, -1, -1],
                [-1, -2, -1, -2, -1, -1],
                [-1, -1, -1, -1, -1, -1]]
        
        #define ponto final
        posObjetivo = [1,4]
        
        for i in range(tam):
            print mapa[i][:]
            
        print posObjetivo
                   
        return mapa, posObjetivo
                          
    class player():
        def __init__(self, nome):
            global mapa
            import random
            tam = len(mapa)
            #define ponto inicial do player
            x = 4
            y = 1
            while mapa[x][y] == -3:
                x = random.randint(tam/2,tam-2)
                y = random.randint(tam/2,tam-2)
            #mapa[x][y] = 0
            self.posicaoInicial = [x,y]
            self.posicaoAtual   = [x,y]
            self.nome           = nome
            print self.posicaoInicial
            print self.posicaoAtual

        def acao(self, direcao):
            global mapa
            #for i in range(len(mapa)):
            #    print mapa[i][:]
            print 'Direcao:', direcao, 'vindo de', self.posicaoAtual
            x,y = self.posicaoAtual
            if direcao == 'esq': 
                if mapa[x][y-1] != -1: #para ESQUERDA esta livre
                    self.posicaoAtual = [x, y-1]
                    return True
                else:
                    return False
            elif direcao == 'dir':
                if mapa[x][y+1] != -1: #para DIREITA esta livre
                    self.posicaoAtual = [x, y+1]
                    return True
                else:
                    return False
            elif direcao == 'cima':
                if mapa[x-1][y] != -1:  #para CIMA esta livre
                    self.posicaoAtual = [x-1, y]
                    return True
                else:
                    return False
            elif direcao == 'baixo': 
                if mapa[x+1][y] != -1: #para BAIXO esta livre
                    self.posicaoAtual = [x+1, y]
                    return True
                else:
                    return False
            else:
                return False
            
    class cria(spade.Behaviour.Behaviour):             
        def _process(self):
            msg = self._receive(True)          
            #print 'Players', tabuleiro.players
            
            if len(msg.getSender().getName()) > 0:
                print 'CRIAR recebeu mensagem de', msg.getSender().getName(), msg.getSender().getAddresses()
                print 'Conteudo da mensagem:', msg.getContent()
                #adiciona na lista de agentes existentes
                tabuleiro.players.append(tabuleiro.player(msg.getSender().getName()))
               
                #avisa que a criacao ocorreu
                msg2 = spade.ACLMessage.ACLMessage()
                msg2.addReceiver(msg.getSender())             
                msg2.setPerformative("inform")
                resposta = 'criar'
                msg2.setContent(resposta)
                self.myAgent.send(msg2) 
                print "Agente registrado:", msg.getSender().getName()

    class objetivo(spade.Behaviour.Behaviour):             
        def _process(self):
            msg = self._receive(True)

            if len(msg.getSender().getName()) > 0:
                print 'OBJ recebeu mensagem de', msg.getSender().getName(), msg.getSender().getAddresses()
                print 'Conteudo da mensagem:', msg.getContent()
                
                msg2 = spade.ACLMessage.ACLMessage()
                msg2.addReceiver(msg.getSender())  
                msg2.setPerformative("inform")
                
                for i in range(len(tabuleiro.players)):
                    if tabuleiro.players[i].nome == msg.getSender().getName():
                        break
                print 'indice', i, tabuleiro.players[i].nome, tabuleiro.players[i].posicaoAtual 
    
                global mapa
                x,y = tabuleiro.players[i].posicaoAtual
                if mapa[x][y] == -3: #posicao objetivo
                    resposta = 'true'
                else:
                    resposta = 'false'
                print "Resposta de objetivo enviada para", msg.getSender().getName(), "com", resposta
                    
                msg2.setContent(resposta)
                self.myAgent.send(msg2) 
                                            
    class sucessores(spade.Behaviour.Behaviour):             
        def _process(self):
            msg = self._receive(True)
            #print 'Players', tabuleiro.players

            if len(msg.getSender().getName()) > 0:
                print 'SUS recebeu mensagem de', msg.getSender().getName(), msg.getSender().getAddresses()
                print 'Conteudo da mensagem:', msg.getContent()
            
                for i in range(len(tabuleiro.players)):
                    if tabuleiro.players[i].nome == msg.getSender().getName():
                        break
                print 'indice', i, tabuleiro.players[i].nome, tabuleiro.players[i].posicaoAtual 
    
                x,y = tabuleiro.players[i].posicaoAtual 
                global mapa
                acoes = []
                if mapa[x-1][y] != -1: #para CIMA esta livre
                    print 'pode ir para cima'
                    acoes.append(1)
                else:
                    acoes.append(0) 
                if mapa[x][y+1] != -1: #para DIREITA esta livre
                    print 'pode ir para direita'
                    acoes.append(1)
                else:
                    acoes.append(0) 
                if mapa[x+1][y] != -1: #para BAIXO esta livre
                    print 'pode ir para baixo'
                    acoes.append(1)
                else:
                    acoes.append(0) 
                if mapa[x][y-1] != -1: #para ESQUERDA esta livre
                    print 'pode ir para esquerda'
                    acoes.append(1)
                else:
                    acoes.append(0)
                    
                msg2 = spade.ACLMessage.ACLMessage()
                msg2.addReceiver(msg.getSender())   
                                
                msg2.setPerformative("inform")
                resposta = acoes
                print "Responde sucessores para", msg.getSender().getName(), "com", resposta
                
                msg2.setContent(resposta)
                self.myAgent.send(msg2) 

    class acao(spade.Behaviour.Behaviour):             
        def _process(self):
            msg = self._receive(True)
            #print 'Players', tabuleiro.players

            if len(msg.getSender().getName()) > 0:
                print 'ACAO recebeu mensagem de', msg.getSender().getName(), 'com pedido de ', msg.getContent()
            
                msg2 = spade.ACLMessage.ACLMessage()
                msg2.addReceiver(msg.getSender())

                for i in range(len(tabuleiro.players)):
                    if tabuleiro.players[i].nome == msg.getSender().getName():
                        break
                print 'indice,nome,posicao:', i, tabuleiro.players[i].nome, tabuleiro.players[i].posicaoAtual 
    
                acoes = msg.getContent().split('|')
                resposta = 'done'
                msg2.setPerformative("done")                   
                for acao in acoes:
                    print 'Pedido de ir para: ', acao
                    if not tabuleiro.players[i].acao(acao): #se conseguir fazer a acao solicitada
                        resposta = 'failure'
                        msg2.setPerformative("failure")
                        break
                    print 'Chegou em', tabuleiro.players[i].posicaoAtual 
                    
                print "Responde acao de", msg.getSender().getName(), 'para', msg.getContent(), "com", resposta
                
                msg2.setContent(msg.getContent())
                self.myAgent.send(msg2) 

    class solucao(spade.Behaviour.Behaviour):             
        def _process(self):
            msg = self._receive(True)
            print 'proposta recebida', msg.getContent()
            
            if len(msg.getSender().getName()) > 0:
                msg2 = spade.ACLMessage.ACLMessage()
                msg2.addReceiver(msg.getSender())

                for i in range(len(tabuleiro.players)):
                    if tabuleiro.players[i].nome == msg.getSender().getName():
                        break
                print 'indice,nome,posicao:', i, tabuleiro.players[i].nome, tabuleiro.players[i].posicaoInicial 
    
                acoes = msg.getContent().split('|')               
                print 'Pedidos cima:', acoes.count('cima')
                print 'Pedidos dir:', acoes.count('dir')
                print 'Pedidos baixo:', acoes.count('baixo')
                print 'Pedidos esq:', acoes.count('esq')
                movimentoX = acoes.count('baixo') - acoes.count('cima')
                movimentoY = acoes.count('esq') - acoes.count('dir')
                
                global mapa
                x,y = tabuleiro.players[i].posicaoInicial
                
                if mapa[x+movimentoX][y-movimentoY] == -3: #posicao objetivo
                    print 'Chega no objetivo'
                    resposta = 'accept-proposal'
                    msg2.setPerformative("accept-proposal")  
                else:
                    print 'Nao chega no objetivo'
                    resposta = 'failure'
                    msg2.setPerformative("failure")                      
                
                print 'Posicao alcancada: ', [x+movimentoX, y-movimentoY]
                print "Responde path ", msg.getSender().getName(), 'para', msg.getContent(), "com", resposta
                
                msg2.setContent(msg.getContent())
                self.myAgent.send(msg2) 
                                      
    def _setup(self):  
        global mapa
        global posObjetivo
        mapa, posObjetivo = self.criaMapa()

        template = spade.Behaviour.ACLTemplate()
        template.setPerformative("request")
        template.setContent("criar")
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.cria(),t)    

        template2 = spade.Behaviour.ACLTemplate()
        template2.setPerformative("request")
        template2.setContent("obj")
        t2 = spade.Behaviour.MessageTemplate(template2)
        self.addBehaviour(self.objetivo(),t2) 

        template3 = spade.Behaviour.ACLTemplate()
        template3.setPerformative("request")      
        template3.setContent("sucessores")
        t3 = spade.Behaviour.MessageTemplate(template3)
        self.addBehaviour(self.sucessores(),t3)   

        template4 = spade.Behaviour.ACLTemplate()
        template4.setPerformative("subscribe")
        t4 = spade.Behaviour.MessageTemplate(template4)
        self.addBehaviour(self.acao(),t4)

        template5 = spade.Behaviour.ACLTemplate()
        template5.setPerformative("propose")
        t5 = spade.Behaviour.MessageTemplate(template5)
        self.addBehaviour(self.solucao(),t5)
                      
ip = '127.0.0.1'
teste = tabuleiro("tabuleiro@"+ip, "secret") 
teste.start()

time.sleep(600)

teste.stop()
