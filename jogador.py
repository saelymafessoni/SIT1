#!/usr/bin/python
import spade
import time

class Resolve_Labirinto(spade.Agent.Agent):
    class cria_tabuleiro(spade.Behaviour.Behaviour):
        def _process(self):
            msg = self._receive(True)

            if msg.getContent() == 'Start':
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent('criar')
                self.myAgent.send(msg)
                print "Criar enviado!"

    class requsita_obj(spade.Behaviour.Behaviour):
        def _process(self):
            msg = self._receive(True)
            if msg.getContent() == 'criar':
                print "criar recebido"
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent('obj')
                self.myAgent.send(msg)
                print "Obj enviado!"


    class verifica_posicao(spade.Behaviour.Behaviour):
        def _process(self):
            msg = self._receive(True)
            if msg.getContent() ==  'false':  #Continua prucurando solucao
                print "Objetivo nao encontrado, continuar procurando solucao"
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(spade.AID.aid("tabuleiro@127.0.0.1",["xmpp://tabuleiro@127.0.0.1"]))
                msg.setContent('sucessores')
                self.myAgent.send(msg)

    class envia_solucao_encontrada(spade.Behaviour.Behaviour):
        def _process(self):
            msg = self._receive(True)
            if msg.getContent() == 'true':
                print "Objetivo encontrado, enviando proposta de caminho"
                #manda proposta de caminho

    class caminha_no_labirinto(spade.Behaviour.Behaviour):
        def _process(self):
            msg = self._receive(True)
            print msg.getContent()
            print msg.getSender()



    def _setup(self):
        template1 = spade.Behaviour.ACLTemplate()
        template1.setPerformative("request")
        t1 = spade.Behaviour.MessageTemplate(template1)
        self.addBehaviour(self.cria_tabuleiro(),t1)

        template2 = spade.Behaviour.ACLTemplate()
        template2.setPerformative("inform")
        template2.setContent("criar")
        t2 = spade.Behaviour.MessageTemplate(template2)
        self.addBehaviour(self.requsita_obj(),t2)

        template3 = spade.Behaviour.ACLTemplate()
        template3.setPerformative("inform")
        template3.setContent("false")
        t3 = spade.Behaviour.MessageTemplate(template3)
        self.addBehaviour(self.verifica_posicao(),t3)

        template4 = spade.Behaviour.ACLTemplate()
        template4.setPerformative("inform")
        template4.setContent("true")
        t4 = spade.Behaviour.MessageTemplate(template3)
        self.addBehaviour(self.envia_solucao_encontrada(),t4)

        template5 = spade.Behaviour.ACLTemplate()
        template5.setPerformative("inform")
        t5 = spade.Behaviour.MessageTemplate(template5)
        self.addBehaviour(self.caminha_no_labirinto(),t5)


teste = Resolve_Labirinto("jogador@127.0.0.1", "secret")

teste.start()


time.sleep(60)

teste.stop()

