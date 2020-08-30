import random
import math
import time

# possible upgrades to increase sun / hydration limit in store?

# shoudl pruning advance day? maybe not, so you can prune and then hit the store

# or, item to doulbe water in one day going forward?
# would need variable for water addition, and maybe according limit increase?
# not sure^

# should there be alternate plant progressions?
# algo that adds branches to base designs, either randomly, or based on
# how you have treated your plant over time (keep track of overall water / sun, or ...)
# possible mutation item in store?

def setup(curr_stage):
	for i in range(50):
		print ""
	print "Your plant has made it to the " +curr_stage+" stage"
	print "0    0        0      0        0        0"
	print "(    (        )      (        )        ("
	print ")    )       (        )      (          )"
	print ""
	print "Here it is: "
	print ""
	draw(curr_stage)

def draw(curr_stage):
	if curr_stage == "seed":
		print "_____________"
		print "      o      "
		print ""
	if curr_stage == "bud":
		print "______^______"
		print ""
	if curr_stage == "sapling":
		print "      Y      "
		print "______|______"
		print ""
	if curr_stage == "super sapling":
		print "      Y      "
		print "      |/     "
		print "      Y      "   
		print "______|______"
		print ""
	if curr_stage == "tree":
		print "      ^      "
		print "     / \     "
		print "    /___\    "
		print "      |      "
		print"_______|______"

def pick(fruit, prune):
	# should actual rand ints for fruit found be based on current heat / hyrdation?
	# current is just how long youve waited, but should matter how plant is doing
	# high values, or ratio? ratio --> well kept, high vals of each, near limits ("plant bursting"?)

	if prune == 0:
		print  "No fruit to gather"
		return 0

	if prune > 0 and prune <= 4:
		pickings = random.randint(1,3)

	if prune > 4 and prune <= 8:
		pickings = random.randint(3,12)
	
	if prune > 8:
		pickings = random.randint(6,20)

	print "You gathered " + str(pickings) + " " + "fruits!"	
	fruit = fruit + pickings
	return fruit

def main():
	day = 0
	stage = 30
	hydration = 3
	sun = 1
	prune = 0
	fruit = 0
	items = []
	max_hydration = 6.0
	max_sun = 11.0
	death_string = """	
					  _____
					 /     \\
					| () () |
					 \  ^  /
					  |||||
					  |||||"""
	stage_dict = {5: "seed", 19: "bud", 29: "sapling", 49: "super sapling", 79: "tree"}
	price_dict = {"lottery ticket": 10, "growth stone":20, "ultra shears":30, "gasoline":5, "lottery ticket":10}
	# set initial stage
	old_stage = "seed"
	# intro 
	print "Planting seed ......"
	draw(old_stage)
	print ""

	while True:
		if day > 0:
			print "Sun:		", sun
			print "Hydration:	", hydration
			print "Fruits:		", fruit
			print "Prune:		", prune
			print "Fruit:		", fruit
			print  "----------------------------------------------------------------"
		
		print "DAY: ", day
		print "what would you like to do?"
		print "Commands: water, prune, sunbathe, check, stats, store, item, clear"
		print "Enter nothing to skip"
		cmd = raw_input(": ")
		print ""

		if cmd =="item":
			if len(items) == 0:
				print ""
				print "you don't have any items!"
				print ""
				time.sleep(1.8)
				continue
			else:
				item_pick = raw_input("Which item? ")
				if item_pick in items:
					print "stuff"
					# here do action of tiem, then remove from items list
					# should there be items that are reusable?
					items.remove(item_pick)
				else:
					print "you don't have that item!"
					print ""
					time.sleep(1.8)
					continue

		if cmd == "sunbathe":
			print "    \|/"
			print "    -O-"
			print "    /|\ "
			print ""
			draw(old_stage)
			print "The sun is high in the sky"
			print ""
			sun = sun + 4
			exp_stage = 12.0*(1.0/math.exp(max_sun-sun))  # 12 is chosen constant
			stage = stage + max(exp_stage,1.0)
			hydration = hydration - .5
		
		if cmd == "water":
			print "   (     )"
			print "    | | |"
			print ""
			draw(old_stage)
			print "The rainclouds are high in the sky"
			print ""
			hydration = hydration + 2
			exp_stage = 5.0*(1.0/math.exp(max_hydration-hydration))  # 5 is chosen constant
			stage = stage + max(exp_stage,1.0)

		if cmd == "prune":
			if stage == 0:
				print "Gardner Andy says: Your plant is too small to prune!"
				print ""
				print " ? ? ? ? ? ? ? ?"
				draw(stage)
			else:
				print "0 0"
				print " x"
				print "/ \ "
				draw(stage)
				print "Your plant is looking nifty"
				print "Keep it up!"
				prune = prune - 4
				if prune < 0:
					prune = 0
				if stage > 30:
					fruit = pick(fruit, prune)
				if stage <= 30:
					print "No fruit found"

			print ""

		if cmd == "store":
			print "----------------------------------------------------"
			print "|                 GENERAL STORE                    |"
			print "|__________________________________________________|"
			print "   |                                             |" 
			print "   |                                             |" 
			print "   |                                             |"
			print "   |                ----------         _____     |"
			print "   |                |        |         | | |     |"
			print "   |                |        |         |---|     |"
			print "   |                |       o|         |_|_|     |"
			print "   |                |        |                   |" 
			print "   |                |        |                   |"
			print "   |________________----------___________________|"
			print "                    |        |                    "
			print ""      
			print "what would you like to buy?"
			print "growth stone (20 fruit), ultra shears (30 fruit), gasoline (5 fruit), lottery ticket (10 fruit), [MORE TO BE ADDED]"
			buy = raw_input(":")
			if buy in price_dict.keys():
				if fruit < price_dict[buy]:
					print ""
					print "You dont have enough fruit!"
					print ""
					time.sleep(2.2)
					continue
				else:
					print ""
					print "you bought a "+str(buy)+"."
					print ""
					items.append(str(buy))
					fruit = fruit - price_dict[buy]
			else:
				print ""
				print str(buy) +" not available in the store"
				print ""
				time.sleep(2.2)
				continue

		if cmd == "check":
			print "Here it is:"
			draw(old_stage)
			print "Your plant is in the "+old_stage+" stage"
			print ""
			print "looking dandy"
			print ""
			continue
			
		if cmd == "stats":
			print "----------------------------"
			print "Sun:		", sun
			print "Hydration:	", hydration
			print "Fruits:		", fruit
			print "Prune:		", prune
			print "Fruit:		", fruit
			print "----------------------------"
			print ""
			continue

		if cmd == "clear":
			for i in range(100):
				print ""
			continue

	#checking for losses
	# should older plants be able to take more? ( as in, more hydro+ heat, so limits are function of stage)
	# seems so, sapling most fragile
	# makes it easier to advance and possibly more fun?

		if hydration <= 0:
			print death_string
					  
			print "your plant is dead."
			print "you didn't water it enough."
			print "you failed."
			print "----------------------------"
			print "GAME OVER"
			time.sleep(5)
			quit()

		if hydration > max_hydration:
			print death_string

			print "your plant flooded."
			print "you watered it too much."
			print "you failed."
			print "---------------------------"
			print "GAME OVER"
			time.sleep(5)
			quit()

		if sun >= max_sun:
			print death_string
			print "you burnt your plant."
			print "you sunbathed too much."
			print "you failed."
			print "----------------------------"
			print "GAME OVER"
			time.sleep(5)
			quit()

		if prune > 15:
			print "-------------------------------"
			print "Hey! Your plant needs pruning!"
			print "-------------------------------"
			print ""

		#add changes for day, increment day
		day = day  + 1
		hydration = hydration - 1	
		sun = sun - 1
		
		# check for not enough sun
		if sun < 0:
			print death_string
		  
			print "your plant etiolated."
			print "you did't sunbathe enough."
			print "you failed."
			print "----------------------------"
			print "GAME OVER"
			time.sleep(5)
			quit()

		# evolution check
		for key in sorted(stage_dict.keys()):
			if stage <= key:
				curr_stage = stage_dict[key]
				break
		if old_stage != curr_stage:
			setup(curr_stage)
			old_stage = curr_stage

		if stage > 30:
			hydration_diff = max_hydration/2.0 - hydration
			sun_diff = max_sun/2.0 - sun
			# cover (should be hyper rare) case of hydration == max_hydration/2.0
			if hydration_diff == 0:
				hydration_diff = .8
			if sun_diff == 0:
				sun_diff = .8
			# closer to max_hydration / 2.0. max_sun / 2.0  add more prune --> use 1/abs(half val), cut out infin value with min function
			# more prune is more fruit, this is more fruit for better kept plant
			# should add 8 and 8 for any val that takes it over 8, also if exactly on middle values
			prune = prune + min(1.0/abs(hydration_diff) ,6) + min(1.0/abs(sun_diff),6)
		
		stage = stage + .5

		raw_input("The sun sets and rises, as it always does.")
		for i in range(100):
			print ""
		print  "----------------------------------------------------------------"

while True:
	print ""
	print ""
	print "		SEED GAME"
	print "	BY: CHRIS Q and ANDY B"
	print ""
	print "Would you like to plant a seed?"
	ans = raw_input("yes/no: ")
	if ans == "no":
		print "You did nothing"
		print ""
		print "GAME OVER" 
		quit()
	if ans == "yes":
		main()	
	else:
		print "Invalid command"

