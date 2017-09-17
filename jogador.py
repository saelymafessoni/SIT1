#!/usr/bin/python
import spade
import time

class mapa(object):
    """docstring for mapa"""
    def __init__(self, ordem):
        lugarx = 4
        lugary = 4
        matriz = [[0 for j in range(ordem)] for i in range(ordem)]
        for i in range(0,ordem):
            for j in range(0, ordem):
                matriz[i][j] = 0
        '''for i in range(0,ordem):
            for j in range(0, ordem):
                print str(i) + " "+ str(j)'''
    def print2(self):
        print "batata"
    def proximo(self, cima, direita, baixo, esquerda):
        print "min10"
        '''lista = []
        lista.apend(999)
        lista.apend(999)
        lista.apend(999)
        lista.apend(999)'''
        print "w"
        print matriz[lugarx][lugary+1]
        if cima==1 :
            print "min2"
            lista[0] = matriz[lugarx][lugary+1]
        if direita==1 :
            print "min3"
            lista[1] = matriz[lugarx+1][lugary]
        if baixo==1 :
            print "min4"
            lista[2] = matriz[lugarx+1][lugary]
        if esquerda==1 :
            print "min5"
            lista[3] = matriz[lugarx+1][lugary]
        aux = 0
        min = lista[0]
        if min > lista[1]:
            min = lista[1]
            aux = 1
        if min > lista[2]:
            min = lista[2]
            aux =2
        if min > lista[3]:
            min = lista[3]
            aux = 3
        print "aux"
        return aux




class Resolve_Labirinto(spade.Agent.Agent):
    class solve(spade.Behaviour.Behaviour):
        def _process(self):
            m = mapa(10)
            msg = self._receive(True)
            content  = msg.getContent()
            if content == 'Start':
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent('criar')
                self.myAgent.send(msg)
                print "Criar enviado!"
            elif content == 'criar':
                print "criar recebido"
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent('obj')
                self.myAgent.send(msg)
                print "Obj enviado!"
            elif content == 'false':
                print "Objetivo nao encontrado, continuar procurando solucao"
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent('sucessores')
                self.myAgent.send(msg)
                print "Requisicao de sucessores enviada"
            elif content == 'true':
<<<<<<< HEAD
                print "true"
                #salva o caminho e o numero de passos dados
                #se for a melhor resposta, manda proposta de caminho
            elif (content[0] == '[' and content[-1] == ']'):

                cima =  int(content[1])
                esquerda = int(content[4])
                baixo = int(content[7])
                direita = int(content[10])

                print cima
                print esquerda
                print baixo
                print direita

                print isinstance( cima, int )

                prox=0
                prox = m.proximo(cima, direita, baixo, esquerda)
                print prox
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("subscribe")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                if prox == 0:
                    msg.setContent("cima")
                elif prox == 1:
                    msg.setContent("dir")
                elif prox == 2:
                    msg.setContent("esq")
                else:
                    msg.setContent("baixo")
                self.myAgent.send(msg)
                print "acao enviada"
            elif content=="done":
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent('obj')
                self.myAgent.send(msg)
                print "Obj enviado!2"
=======
                print "Objetivo encontrado, enviando proposta de caminho"
                #manda proposta de caminho
            elif content[0] == '[' & content[2] == ',':

>>>>>>> 1036efc70bbc14abba50ac1e58cfe29082064a46
            else:
                #toma decisao de caminhada pelo labirinto
                print "Sucessores: ", content


    def _setup(self):

        template1 = spade.Behaviour.ACLTemplate()
        #template1.setPerformative("request")
        t1 = spade.Behaviour.MessageTemplate(template1)
        self.addBehaviour(self.solve(),t1)




agente = Resolve_Labirinto("jogador@127.0.0.1", "secret")

agente.start()


time.sleep(60)

#teste.stop()

