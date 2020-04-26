import pygame
import random
import math
from pygame import mixer


# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background image. Call this variable in the loop for continuity
background = pygame.image.load("space.png")

# Background sound. -1 is to play the music continuously
mixer.music.load("background.wav")
mixer.music.play(-1)

# Title and Icon from flaticon.com
pygame.display.set_caption("Space Invaders by Kits")

icon = pygame.image.load("project.png")
pygame.display.set_icon(icon)

# Player The image size is 64x64
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 20

for e in range(num_of_enemies):
	enemyImg.append(pygame.image.load("battleship.png"))
	enemyX.append(random.randint(0, 734))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(4)
	enemyY_change.append(40)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over font
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# Bullet

# Ready - Bullet not displayed
# Fire - Bullet moving

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480 # Same as playerY
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Functions

def show_score(x, y):
	global score
	score = font.render("Score : " + str(score_value), True, (255, 255, 255))
	screen.blit(score, (x, y))

def game_over_text(x, y):
	over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
	screen.blit(over_text, (200, 250))

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y, e):
	screen.blit(enemyImg[e], (x, y))

def bullet_fire(x, y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg, (x + 16, y + 10))

# Distance between two points = square root of (x2 - x1)^2 + (y2 - y1)^2
def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt((math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2))))
	if distance <= 27:
		return True
	else:
		return False

# Game Loop. Everything that needs to be persistent on the screen should be in this loop

running = True

while running:

	# Background color. RGB - Red, Green nad Blue
	screen.fill((0, 0, 128))

	# Background image
	screen.blit(background, (0,0))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# If keystrokes are pressed

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -10

			if event.key == pygame.K_RIGHT:
				playerX_change = 10

			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					bullet_sound = mixer.Sound("laser.wav")
					bullet_sound.play()

					# Get the X coordinate of the spaceship
					bulletX = playerX
					bullet_fire(bulletX, bulletY)


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	# Set boundaries

	playerX += playerX_change


	if playerX <= 0:
		playerX = 0

	elif playerX >= 735:
		playerX = 735


	# Enemies movement

	for e in range(num_of_enemies):

		# Game Over
		if enemyY[e] > 410:
			bulletY = -10000
			for j in range(num_of_enemies):
				enemyY[j] = 2000
			game_over_text(200, 250)
			break

		enemyX[e] += enemyX_change[e]
		if enemyX[e] <= 0:
			enemyX_change[e] = 3
			enemyY[e] += enemyY_change[e]

		elif enemyX[e] >= 735:
			enemyX_change[e] = -3
			enemyY[e] += enemyY_change[e]

		# Collision

		collision = isCollision(enemyX[e], enemyY[e], bulletX, bulletY)

		if collision:
			collision_sound = mixer.Sound("explosion.wav")
			collision_sound.play()
			bulletY = 480
			bullet_state = "ready"
			score_value += 1
			enemyX[e] = random.randint(0, 734)
			enemyY[e] = random.randint(50, 150)

		# Call the enemy function
		enemy(enemyX[e], enemyY[e], e)

	# Bullet movement

	if bulletY <= 0:
		bulletY = 480
		bullet_state = "ready"

	if bullet_state == "fire":
		bullet_fire(bulletX, bulletY)
		bulletY -= bulletY_change

	


	# Calling functions

	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update() # Updating the display





