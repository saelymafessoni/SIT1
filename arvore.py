#!/usr/bin/python

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
	def visitado(self):
		visitado = visitado +1
	def getVisitado(self):
		return self.visitado
	'''
	def buscaLargura(self, objetivo):
		fifo = []
		fifo.append(self)
		i=0
		while len(fifo)>0:
			#print fifo[i].objetivo
			if (fifo[i].dado == objetivo):
				return fifo[i]
			if fifo[i].getLeft()!=None:
				fifo.append(fifo[i].getLeft())
			if fifo[i].getLeft()!=None:
				fifo.append(fifo[i].getRight())
			fifo.pop(0)
	def buscaProfundidade(self, objetivo):
		print self.dado
		if self.dado == objetivo:
			return self
		if self.getLeft() != None:
			obj = self.getLeft().buscaProfundidade(objetivo)
			if obj != None:
				return obj
		if self.getRight() != None:
			obj = self.getRight().buscaProfundidade(objetivo)
			if obj != None:
				return obj
		return None
	'''

n = [None,None,None,None]
root = no(0,n,None,0,1)
n1 = no(0,n,root,0,1)
n2 = no(0,n,root,0,1)
n3 = no(0,n,root,1,1)
n4 = no(0,n,root,0,1)
s = [n1, n2, n3 , n4]
root.setSucessores(s)
s1 = root.getSucessores()
print root.getObjetivo()
#print ""
print s1[0].getObjetivo() , " ", s1[1].getObjetivo(), " ", s1[2].getObjetivo() ," ", s1[3].getObjetivo(), " " 
print "n3 folha? ", s1[2].folha
print "n3 objetivo? ", s1[2].getObjetivo()
print "n3 visitado ", s1[2].getVisitado() , " vezes"
#print root.buscaLargura()
#print root.buscaProfundidade()