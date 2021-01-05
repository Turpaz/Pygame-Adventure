# pygame_particles
Python program that contains a class of Particles with customizeable properties such as - shape, color, affected by gravity, lifetime and lots more

to use it just import:<br>
	<i>from Particles import ParticleMaster</i>

and then create the master:<br>
	<i>master = ParticleMaster()</i><br><br>

add an update method in the mainloop:<br>
	<i>master.update_effects()</i><br><br>
  
then every time you want to add an effect:<br>
	<i>master.add_effect(screen, color, decrease_by, follow_mouse, pos, radius, rect, gravity, gray, speed, litetime, spawn_speed)</i><br><br>
  
explanation:<br>
    	<b>screen</b>, is the pygame screen. example - <i>screen = pygame.display.set_mode((500,500)) # will create a 500px by 500px window named screen</i><br><br>
	<b>color</b>, is the range the colors can be randomized in. example - <i>[[0, 0, 0], [255, 255, 255]] # will allow any color. or black to white</i><br><br>
	<b>decrease by</b>, is the range of the amount the size of each particle will be randomized to be decreased by at each frame it's also the way particles are being destroyed - when they're too small so be sure it's bigger than 0, example - <i>[0.2, 0.4] # each particle will choose a number between those and will decrease by it at each frame</i><br><br>
	<b>follow_mouse</b>, is a boolean that is responsable for will the particles will follow the mouse or not. example - <i>True # the particles will be at the mouse position at all time</i><br><br>
	<b>pos</b>, is the starting position for the particles. it's irelevant if follow_mouse is on. example - <i>[250, 250]</i><br><br>
	<b>radius</b>, is the range the radius or half the size of each particle will be randomized in, it's got to be a positive number. remember that it will effect the lifetime of each particle. example - <i>[5, 10] # each particle will choose a starting size between 10 and 15</i><br><br>
	<b>rect</b>, will determine whether or not the particles will be shaped as squares, if not they will be circles. example - <i>True # the particles will be shaped as squares</i><br><br>
	<b>gravity</b>, the amount of gravity that will be applyed, can be 0 for no gravity and negative for upwards gravity. example - <i>0.05 # a realatively small downwards gravity< will be applyed</i><br><br>
	<b>gray</b>, will determine whether or not the color range should be gray which means the r, g, b scales will be equal one to each other. example - <i>False # the color can be colorful</i><br><br>
	<b>speed</b>, the maximum speed that can be applyed to each particle, wiil effect the distance each particle travels. example - <i>3 # the speed of each particle can be up to 3</i><br><br>
<br>
<b>lifeetime</b>, the lifetime of the particle group as a whole (not of each particle) in seconds. example - <i>10 # the particles will be generating for 10 seconds</i><br><br>
<b>spawn_speed</b>, the frames that the programm will wait until generating a new particle. example - <i>1 # a new particle will be generated each frame</i><br><br>
		
<b>full example</b> - master.add_effect(screen, [[0, 0, 0], [255, 255, 255]], [0.2, 0.4], True, [250, 250], [10, 15], True, 0.05, False, 3, 10, 1)<br><br>

<img src=>

the whole script:<br>
```python
import pygame
from particles import ParticleMaster

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

master = ParticleMaster()

master.add_effect(screen, [[0, 0, 0], [255, 255, 255]], [0.2, 0.4], True, [250, 250], [5, 10], True, 0.05, False, 3, 10, 1)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.fill((30,30,30))
	
	master.update_effects()
	
	pygame.display.update()
	clock.tick(60)
```
