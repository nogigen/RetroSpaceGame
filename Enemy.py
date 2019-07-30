import random
class Enemy:
	def __init__(self):
		self.__enemyX = random.randint(0,800)
		self.__enemyY = 50
		self.__enemyXchange = 4
		self.__enemyYchange = 40

	def update(self):
		self.__enemyX += self.__enemyXchange
		if self.__enemyX <= 0:
			self.__enemyXchange = 4
			self.__enemyY += self.__enemyYchange			

		elif self.__enemyX >= 736:
			self.__enemyXchange = -4
			self.__enemyY += self.__enemyYchange			


	def drawEnemy(self, screen, enemyImg):
		screen.blit(enemyImg, (self.__enemyX,self.__enemyY))

	def getEnemyX(self):
		return self.__enemyX

	def getEnemyY(self):
		return self.__enemyY