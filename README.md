# pygame_particles
Python program that contains a class of Particles with customizeable properties such as - shape, color, affected by gravity, lifetime and lots more

to use it just import:<br>
	<i>from Particles import ParticleMaster</i>

and then create the master:<br>
	<i>master = ParticleMaster()</i>

add an update method in the mainloop:<br>
	<i>master.update_effects()</i>
  
then every time you want to add an effect:<br>
	<i>master.add_effect(screen, color, decrease_by, follow_mouse, pos, radius, rect, gravity, gray, speed, litetime, spawn_speed)</i>
  
explanation:
    	screen, is the pygame screen. example - <i>screen = pygame.display.set_mode((500,500)) # will create a 500px by 500px window named screen</i><br>
	color, is the range the colors can be randomized in. example - <i>[[0, 0, 0], [255, 255, 255]] # will allow any color. or black to white</i><br>
	decrease by, is the range of the amount the size of each particle will be randomized to be decreased by at each frame it's also the way particles are being destroyed - when they're too small so be sure it's bigger than 0, example - <i>[0.2, 0.4] # each particle will choose a number between those and will decrease by it at each frame</i><br>
	follow_mouse, is a boolean that is responsable for will the particles will follow the mouse or not. example - <i>True # the particles will be at the mouse position at all time</i><br>
	pos, is the starting position for the particles. it's irelevant if follow_mouse is on. example - <i>[250, 250]</i><br>
	radius, is the range the radius or half the size of each particle will be randomized in, it's got to be a positive number. remember that it will effect the lifetime of each particle. example - <i>[10, 15] # each particle will choose a starting size between 10 and 15</i><br>
	rect, will determine whether or not the particles will be shaped as squares, if not they will be circles. example - <i>True # the particles will be shaped as squares</i><br>
	gravity, the amount of gravity that will be applyed, can be 0 for no gravity and negative for upwards gravity. example - <i>0.05 # a realatively small downwards gravity< will be applyed</i><br>
	gray, will determine whether or not the color range should be gray which means the r, g, b scales will be equal one to each other. example - <i>False # the color can be colorful</i><br>
	speed, the maximum speed that can be applyed to each particle, wiil effect the distance each particle travels. example - <i>3 # the speed of each particle can be up to 3</i><br>
<br>
lifeetime, the lifetime of the particle group as a whole (not of each particle) in seconds. example - <i>10 # the particles will be generating for 10 seconds</i><br>
spawn_speed, the frames that the programm will wait until generating a new particle. example - <i>1 # a new particle will be generated each frame</i><br>
		
full example - <i>master.add_effect(screen, [[0, 0, 0], [255, 255, 255]], [0.2, 0.4], True, [250, 250], [10, 15], True, 0.05, False, 3, 10, 1)</i><br>

the whole script:<br>
