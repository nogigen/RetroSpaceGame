class Bullet:

	def __init__(self, coordinateX):
		self.__coordinateY = 480
		self.__coordinateX = coordinateX
		self.__bulletChange = 10

	def update(self):
		self.__coordinateY -= self.__bulletChange

	def fire_bullet(self, screen, bulletImg):
		screen.blit(bulletImg,(self.__coordinateX+16,self.__coordinateY+10))

	def getY(self):
		return self.__coordinateY

	def getX(self):
		return self.__coordinateX