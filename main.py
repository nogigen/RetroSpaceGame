import pygame
import random
import math
import time
from Bullet import Bullet
from Enemy import Enemy

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load('background.png')

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

# scoreboard
font = pygame.font.Font("freesansbold.ttf",32)
scoreX = 10
scoreY = 10

def show_score(x, y , currentScore):
	score = font.render("Score : " + str(currentScore), True, (255,255,255))
	screen.blit(score, (x,y))

# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('enemy.png')


# bullet
bulletImg = pygame.image.load('bullet.png')

def player(x, y):
	screen.blit(playerImg, (x,y))

# if a bullet hits to an enemy, enemy dies and bullet disappears
# enemyList and bulletList will be updated accordingly.
def isCollision(enemyList, bulletList,numberOfHits):
	enemyCounter = 0
	hits = numberOfHits
	while enemyCounter < len(enemyList):
		bulletCounter = 0
		while bulletCounter < len(bulletList):
			distance = math.sqrt(math.pow(enemyList[enemyCounter].getEnemyX() - bulletList[bulletCounter].getX(), 2) + math.pow(enemyList[enemyCounter].getEnemyY() - bulletList[bulletCounter].getY(), 2))
			
			if distance < 27:
				enemyList.pop(enemyCounter)
				bulletList.pop(bulletCounter)
				enemyCounter -= 1
				bulletCounter -= 1
				hits += 1
				break
			bulletCounter += 1			

		enemyCounter += 1
	return hits


# game loop
newEnemiesInSeconds = 2
bullets = []
enemies = []
enemies.append(Enemy())
hits = 0
lastTime = round(time.time())
running = True
gameOver = False

while running:

	if not gameOver:		

		# background image
		screen.blit(background,(0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			# check if keystroke is pressed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					playerX_change = -5		
			
				if event.key == pygame.K_RIGHT:
					playerX_change = 5

				if event.key == pygame.K_SPACE:
					newBullet = Bullet(playerX)
					bullets.append(newBullet)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					playerX_change = 0

		# check if enemy reached the ship.
		# if it is, game should end
		for enemy in enemies:
			if enemy.getEnemyY() + 64 >= 480:
				gameOver = True
				break

		# add a new enemy each second
		currentTime = round(time.time())
		if currentTime - lastTime == newEnemiesInSeconds:
			enemies.append(Enemy())
			lastTime = currentTime

		# update player
		playerX += playerX_change
		if playerX <= 0:
			playerX = 0
		if playerX >= 736:
			playerX = 736

		# update enemies's position
		for enemy in enemies:
			enemy.update()


		# check if a bullet hits to an enemy, this function will update lists accordingly.
		hits = isCollision(enemies,bullets,hits)

		# bullet movement (position)
		for bullet in bullets:
			bullet.fire_bullet(screen, bulletImg)
			bullet.update()

		# delete unnecessary bullets
		i = 0
		while i < len(bullets):
			if bullets[i].getY() <= 0:
				bullets.pop(i)
				i -= 1
			i += 1

		player(playerX,playerY)

		for enemy in enemies:
			enemy.drawEnemy(screen, enemyImg)

		show_score(scoreX, scoreY, hits)
		pygame.display.update()
	
	elif gameOver:
		screen.fill((0,0,0)) # is fill have to be here? can it be outside loop.		

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		# restart button
		if 200 + 100 > mouse[0] > 200 and 320 + 30 > mouse[1] > 320:
			pygame.draw.rect(screen, (0,200,0), (200,320,100,30))
		else:
			pygame.draw.rect(screen, (0,255,0), (200,320,100,30))

		
		# quit button
		if 500 + 100 > mouse[0] > 500 and 320 + 30 > mouse[1] > 320:
			pygame.draw.rect(screen, (100,0,110), (500,320,100,30))
		else:
			pygame.draw.rect(screen, (200,0,200), (500,320,100,30))

		# small text
		smallText = pygame.font.Font("freesansbold.ttf",16)

		# restart text
		restartText = smallText.render("Restart", True, (255,255,255))
		screen.blit(restartText, (221,327))


		# quit text
		quitText = smallText.render("Quit", True, (255,255,255))
		screen.blit(quitText, (531,327))

		# game over label
		displayGameOver = font.render("Game Over", True, (255,255,255))
		screen.blit(displayGameOver, (312,260))
		pygame.display.update()

		if click[0] == 1 and 200 + 100 > mouse[0] > 200 and 320 + 30 > mouse[1] > 320:
			# restart the data.
			bullets = []
			enemies = []
			enemies.append(Enemy())
			hits = 0
			lastTime = round(time.time())
			gameOver = False

		elif click[0] == 1 and 500 + 100 > mouse[0] > 500 and 320 + 30 > mouse[1] > 320:
			running = False
			break
		# exit protocol, without this program will crash.
		# also the X thing on the window.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				break

