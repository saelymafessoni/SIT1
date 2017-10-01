#!/usr/bin/python
import spade
import time
from random import randint

class mapa(object):
    """docstring for mapa"""
    def __init__(self, ordem):
        self.lugarx = 4
        self.lugary = 4
        self.caminho = ""
        self.matriz = [[0 for j in range(ordem)] for i in range(ordem)]
        for i in range(0,ordem):
            for j in range(0, ordem):
                self.matriz[i][j] = 0
        '''for i in range(0,ordem):
            for j in range(0, ordem):
                print str(i) + " "+ str(j)'''

    def proximo(self, cima, direita, baixo, esquerda):
        l = [cima, direita, baixo, esquerda]
        aux = randint(0, 3)
        while (l[aux] == 0):
            aux = randint(0,3)
        print aux
        return aux
        '''
        lista = [999,999,999,999]
        print "proximo(" + str(cima) + "," + str(direita) + "," + str(baixo) + "," + str(esquerda) + ")" 
        if cima==1 :
            lista[0] = self.matriz[self.lugarx][self.lugary+1]
            print "lista[0]: " + str(lista[0])
        if direita==1 :
            lista[1] = self.matriz[self.lugarx+1][self.lugary]
            print "lista[1]: " + str(lista[1])
        if baixo==1 :
            lista[2] = self.matriz[self.lugarx][self.lugary-1]
            print "lista[2]: " + str(lista[2])
        if esquerda==1 :
            lista[3] = self.matriz[self.lugarx-1][self.lugary]
            print "lista[3]: " + str(lista[3])
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
        return aux


    def getCaminho(self):
        print "getcaminho"
        return self.caminho

m = mapa(10)

class Resolve_Labirinto(spade.Agent.Agent):
    class solve(spade.Behaviour.Behaviour):
        def _process(self):
            global m
            msg = self._receive(True)
            content  = msg.getContent()
            performative = msg.getPerformative()
            print "mensagem recebida"
            print content
            print performative
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
                print "entrou no true"
                caminho = m.getCaminho()
                print caminho
                caminho = caminho[:-1]
                print caminho
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("propose")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent(caminho)
                self.myAgent.send(msg)
                print "Objetivo encontrado, enviando proposta de caminho"
                #salva o caminho e o numero de passos dados
                #se for a melhor resposta, manda proposta de caminho
            elif (content[0] == '[' and content[-1] == ']'):

                cima =  int(content[1])
                direita = int(content[4])
                baixo = int(content[7])
                esquerda = int(content[10])

                print cima
                print esquerda
                print baixo
                print direita

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
                    msg.setContent("baixo")
                else:
                    msg.setContent("esq")
                self.myAgent.send(msg)
                print "acao enviada"
            elif content=="done":
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
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





agente = Resolve_Labirinto("jogador@127.0.0.1", "secret")

agente.start()


time.sleep(60)


