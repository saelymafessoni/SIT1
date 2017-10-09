#!/usr/bin/python
import spade
import time
from random import randint

tamanho = 30
debug = False


class no():
    def __init__(self, folha, sucessores, pai, objetivo, visitado):
        self.folha = folha 
        self.sucessores = [sucessores[0], sucessores[1], sucessores[2], sucessores[3]]
        self.pai = pai
        self.objetivo = objetivo
        self.visitado = visitado
    def folha(self):
        if (self.sucessores[0] == None and self.sucessores[1] == None and self.sucessores[2] == None and self.sucessores[3] == None ): 
            self.setFolha(True)
            return True
        else:
            self.setFolha(False)
            return False
    def setFolha(self, f):
        self.folha = f
    def setSucessores(self, s):
        self.sucessores[0] = s[0]
        self.sucessores[1] = s[1]
        self.sucessores[2] = s[2]
        self.sucessores[3] = s[3]
    def getSucessores(self):
        return self.sucessores
    def setObjetivo(self, obj):
        self.objetivo = obj
    def getObjetivo(self):
        return self.objetivo
    def getPai(self):
        return self.pai
    def setPai(self, i):
        if self.pai == 5:
            self.pai = i
    def setVisitado(self, i):
        self.visitado = i
    def getVisitado(self):
        return self.visitado
    def buscaLargura(self):
        numeros = []
        direction = []
        fifo = []
        fifo.append(self)
        numeros.append(0)
        direction.append(4)
        i=0
        print "busca largura"
        while (1):
            #print fifo[i].getObjetivo()
            print len(fifo)
            if (fifo[i].getObjetivo() == True):
                result = []
                while direction[i]!=4:
                    result.append(direction[i])
                    i = numeros[i]
                for i in result:
                    print i,
                reverse = []
                for i in result:
                    reverse.insert(0, i)
                for i in reverse:
                    print i,    
                caminho = ""
                for i in reverse:
                    if i == 0:
                        caminho += "cima|"
                    elif i == 1:
                        caminho += "dir|"
                    elif i == 2:
                        caminho += "baixo|"
                    else:
                        caminho += "esq|"
                caminho=caminho[0:-1]
                print caminho
                return caminho
                
            l = fifo[i].getSucessores()
            if direction[i]==0:
                pai = 2
            elif direction[i]==1:
                pai = 3
            elif direction[i]==2:
                pai = 0
            else:
                pai = 1

            for j in range(4):
                if l[j]!=None and j!=pai:
                    fifo.append(l[j])
                    numeros.append(i)
                    direction.append(j)
            i+=1

class mapa():
    """docstring for mapa"""
    def __init__(self, ordem):
        self.lugarx = tamanho/2
        self.lugary = tamanho/2
        self.root = None
        self.caminho = ""
        self.matriz = [[0 for j in range(ordem)] for i in range(ordem)]
        for i in range(0,ordem):
            for j in range(0, ordem):
                self.matriz[i][j] = no(False, [None, None, None, None], 5, False, False)
        '''for i in range(0,ordem):
            for j in range(0, ordem):
                print str(i) + " "+ str(j)'''
    def getNo(self, i):
        if i==0:
            no = self.matriz[self.lugarx][self.lugary+1]
        elif i==1:
            no = self.matriz[self.lugarx+1][self.lugary]
        elif i==2:
            no = self.matriz[self.lugarx][self.lugary-1]
        elif i==3:
            no = self.matriz[self.lugarx-1][self.lugary]
        else:
            no = self.matriz[self.lugarx][self.lugary]
        return no
    def getRoot(self):
        #print "a"
        return self.root
    def setRoot(self, r):
        #print "a"
        self.root = r        
    def proximo(self, lsucessores):
        
        if lsucessores[0]==1 and self.matriz[self.lugarx][self.lugary+1].getVisitado()==False :
            prox = 0
        elif lsucessores[1]==1 and self.matriz[self.lugarx+1][self.lugary].getVisitado()==False :
            prox = 1
        elif lsucessores[2]==1 and self.matriz[self.lugarx][self.lugary-1].getVisitado()==False :
            prox = 2
        elif lsucessores[3]==1 and self.matriz[self.lugarx-1][self.lugary].getVisitado()==False :
            prox = 3
        else:
            print "MOVER PARA O PAI: ",
            print self.matriz[self.lugarx][self.lugary].getPai()
            prox = self.matriz[self.lugarx][self.lugary].getPai()
        print "prox: ", prox
        return prox

        '''aux = randint(0, 3)
        while (l[aux] == 0):
            aux = randint(0,3)
        print aux
        return aux'''

    def andar(self, direcao):
        #sleep(1)
        
        print "self.lugarx: ",
        print self.lugarx
        print "self.lugary: ",
        print self.lugary
        #aux = self.matriz[self.lugarx][self.lugary] 
        #print aux
        #self.matriz[self.lugarx][self.lugary] = aux + 1
        if direcao=="esq" :
            self.lugarx = self.lugarx - 1
            self.matriz[self.lugarx][self.lugary].setPai(1)
        if direcao=="dir" :
            self.lugarx = self.lugarx + 1
            self.matriz[self.lugarx][self.lugary].setPai(3)
        if direcao=="cima" :
            self.lugary = self.lugary +1
            self.matriz[self.lugarx][self.lugary].setPai(2)
        if direcao=="baixo" :
            self.lugary = self.lugary -1
            self.matriz[self.lugarx][self.lugary].setPai(0)
        print self.lugarx
        print self.lugary
        
        self.caminho = self.caminho + direcao + "|"
        print self.caminho
        print self.matriz[self.lugarx][self.lugary].getPai()
        m.printMatriz()
        
        return self.matriz[self.lugarx][self.lugary]

    def getCaminho(self):
        print "getcaminho"
        return self.caminho
    def printMatriz(self):
        for i in range(tamanho):
            for j in range(tamanho):
                if (j)==self.lugarx and (tamanho-1-i)==self.lugary:
                    print "2",
                elif self.matriz[j][tamanho-1-i].getObjetivo() == True:
                    print "3",
                else:
                    print int(self.matriz[j][tamanho-1-i].getVisitado()),
                print " ",
            print " "
    def printNo(self):
        print "Pai: ",
        print self.matriz[self.lugarx][self.lugary].getPai()
        print "Visitado: ",
        print self.matriz[self.lugarx][self.lugary].getVisitado()
        print "Sucessores: ",
        l = self.matriz[self.lugarx][self.lugary].getSucessores()
        print "[ ",
        for i in l:
            print str(i) + " ,",
        print "] "


m = mapa(tamanho)
objetivo_encontrado = False
no = m.getNo(4)
m.setRoot(no)
no.setPai(4)

class Resolve_Labirinto(spade.Agent.Agent):
    class solve(spade.Behaviour.Behaviour):
        def _process(self):
            global m
            global objetivo_encontrado
            global no
            msg = self._receive(True)
            content  = msg.getContent()
            performative = msg.getPerformative()
            print "mensagem recebida"
            print content
            print performative
            if content == 'Start':
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@"+ip,["xmpp://tabuleiro@"+ip]))
                msg.setContent('criar')
                self.myAgent.send(msg)
                print "Criar enviado!"
            elif content == 'criar':
                print "criar recebido"
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@"+ip,["xmpp://tabuleiro@"+ip]))
                msg.setContent('obj')
                self.myAgent.send(msg)
                print "Obj enviado!"
            elif content == 'false':
                print "Objetivo nao encontrado, continuar procurando solucao"
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@"+ip,["xmpp://tabuleiro@"+ip]))
                msg.setContent('sucessores')
                if (debug==True):
                    time.sleep(3)
                self.myAgent.send(msg)
                print "Requisicao de sucessores enviada"
            elif content == 'true':
                print "entrou no true"
                #caminho = m.getCaminho()
                #print caminho
                #caminho = caminho[:-1]
                #print caminho
                m.getNo(4).setObjetivo(True)
                '''msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("propose")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent(caminho)
                self.myAgent.send(msg)'''
                print "Objetivo encontrado, continuar mapeando"
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@"+ip,["xmpp://tabuleiro@"+ip]))
                msg.setContent('sucessores')
                if (debug==True):
                    time.sleep(3)
                self.myAgent.send(msg)
                print "Requisicao de sucessores enviada"
                #salva o caminho e o numero de passos dados
                #se for a melhor resposta, manda proposta de caminho
            elif (content[0] == '[' and content[-1] == ']'):

                
                '''print "getNo: "
                print m.getNo(4).getVisitado()
                print "no: "
                print no.getVisitado()'''
                

                cima =  int(content[1])
                direita = int(content[4])
                baixo = int(content[7])
                esquerda = int(content[10])

                print cima
                print esquerda
                print baixo
                print direita

                lsucessores = [cima, direita, baixo, esquerda]
                prox=0
                prox = m.proximo(lsucessores)
                
                if (not m.getNo(4).getVisitado()):
                    for i in range(4):
                        if lsucessores[i] == 1:
                            lsucessores[i] = m.getNo(i)
                            '''if i==0 :
                                lsucessores[i].setPai(2)
                            elif i==1:
                                lsucessores[i].setPai(3)
                            elif i==2:
                                lsucessores[i].setPai(0)
                            elif i==3:
                                lsucessores[i].setPai(1)
                            else:
                                print "EXPLODE"                        
                                exit()'''
                        else:
                            lsucessores[i] = None
                    m.getNo(4).setSucessores(lsucessores)
                m.getNo(4).setVisitado(True)

                m.printNo()

                
                print prox
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("subscribe")
                msg.addReceiver(spade.AID.aid("tabuleiro@"+ip,["xmpp://tabuleiro@"+ip]))    
                if prox == 0:
                    msg.setContent("cima")
                elif prox == 1:
                    msg.setContent("dir")
                elif prox == 2:
                    msg.setContent("baixo")
                else:
                    msg.setContent("esq")
                if prox == 4:
                    print "mapeamento completo"
                    caminho = m.getRoot().buscaLargura()
                    print "batata"                    
                    msg = spade.ACLMessage.ACLMessage()
                    msg.setPerformative("propose")
                    msg.addReceiver(spade.AID.aid("tabuleiro@"+ip,["xmpp://tabuleiro@"+ip]))
                    msg.setContent(caminho)
                    self.myAgent.send(msg)

                else:
                    self.myAgent.send(msg)
                print "acao enviada"
            elif (content=="esq" or content=="dir" or content=="cima" or content=="baixo") and performative=="done":
                print "entrou"
                print content
                m.andar(content)
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@"+ip,["xmpp://tabuleiro@"+ip]))
                msg.setContent('obj')
                self.myAgent.send(msg)
                print "Obj enviado!"
                #manda proposta de caminho
            elif performative =="failure":
                print "Failed to perform action"
            elif performative == "accept-proposal":
                print "SUCESSO"
            else:
                print "else: ", content
            



    def _setup(self):

        template1 = spade.Behaviour.ACLTemplate()
        #template1.setPerformative("request")
        t1 = spade.Behaviour.MessageTemplate(template1)
        self.addBehaviour(self.solve(),t1)




ip = '127.0.0.1'
agente = Resolve_Labirinto("brenosaely@"+ip, "secret")

agente.start()


time.sleep(60)


