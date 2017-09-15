#!/usr/bin/python
import spade
import time

class Resolve_Labirinto(spade.Agent.Agent):
    class solve(spade.Behaviour.Behaviour):
        def _process(self):
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
                print "Objetivo encontrado, enviando proposta de caminho"
                #manda proposta de caminho
            elif content[0] == '[' & content[2] == ',':

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

