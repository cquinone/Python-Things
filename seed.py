import random


def draw(stage):
	if stage <= 6:
		print "_____________"
		print "      o      "
		print ""
	if stage > 6 and stage <= 20:
		print "______^______"
		print ""
	if stage > 20 and stage <= 30:
		print "      Y      "
		print "______|______"
		print ""
	if stage > 30 and stage <= 50:
		print "      Y      "
		print "      |/     "
		print "      Y      "   
		print "______|______"
		print ""
	if stage > 50 and stage <= 80:
		print "      ^      "
		print "     / \     "
		print "    /___\    "
		print "      |      "
		print"_______|______"

def pick(fruit, prune):
	if prune == 0:
		print  "No fruit to gather"
	if prune > 0 and prune <= 4:
		pickings = random.randint(1,3)
		fruit = fruit + pickings
		print "You gathered " + str(pickings) + "" + "fruits!"

	if prune > 4 and prune <= 8:
		pickings = random.randint(3,12)
		fruit = fruit + pickings
		print "You gathered " + str(pickings) + "" + "fruits!"
	
	if prune > 8:
		pickings = random.randint(6,20)
		fruit = fruit + pickings
		print "You gathered " + str(pickings) + "" + "fruits!"
	
	return fruit

def main():
	print "Planting seed ......"
	print "-------------"
	print "      o      "
	print ""
	day = 0
	stage = 0
	hydration = 3
	heat = 0
	prune = 10
	fruit = 0
	stages = ["seed"]
	while True:
		if day > 0:
			print "Heat:		", heat
			print "Hydration:	", hydration
			print "Fruits:		", fruit
			print "Prune:		", prune
		
		print "DAY: ", day
		print "what would you like to do?"
		print "Commands: water, prune, sunbathe, check, store"
		cmd = raw_input(": ")
		if cmd == "sunbathe":
			print "    \|/"
			print "    -O-"
			print "    /|\ "
			print ""
			draw(stage)
			print "The sun is high in the sky"
			print ""
			heat = heat + 4
			stage = stage + 2
		
		if cmd == "water":
			print "   (     )"
			print "    | | |"
			print ""
			draw(stage)
			print "The rainclouds are high in the sky"
			print ""
			hydration = hydration + 2
			stage = stage + 1
		
		if cmd == "prune":
			if stage == 0:
				print "Gardner Andy says: You cant prune a seed!"
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
				prune = prune - 3
				if prune < 0:
					prune = 0
				
				if stage > 30:
					fruit = pick(fruit, prune)
 
			if prune == 0:
				print "your plant is barren"
				print ""

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
			print "growth stone (20 fruit), ultra shears (30 fruit), gasoline (5 fruit), lottery ticket (10 fruit)"
			buy = raw_input(":")
			if buy == "lottery ticket":
				if fruit < 10:
					print "You dont have enough fruit!"


		if cmd == "check":
			print "Here it is:"
			draw(stage)
			print "looking dandy"
			print ""
			

			
		if hydration <= 0:
			print "your plant is dead."
			print "you didnt water it enough."
			print "you failed."
			print "----------------------------"
			print "GAME OVER"
			quit()

		if hydration > 6:
			print "your plant flooded."
			print "you watered it too much."
			print "you failed."
			print "---------------------------"
			print "GAME OVER"

		if heat >= 10:
			print "you burnt your plant."
			print "you sunbathed too much."
			print "you failed"
			print "----------------------------"
			print "GAME OVER"
			quit()

		day = day  + 1
		hydration = hydration - 1
		if heat > 0:
			heat = heat - 1 
			

		if stage > 6:
			if stage <= 20:
				if "bud" not in stages:
					for i in range(50):
						print ""
					print "Your plant has made it to the BUD stage"
					print "0    0        0      0        0        0"
					print "(    (        )      (        )        ("
					print ")    )       (        )      (          )"
					print ""
					print "Here it is: "
					draw(stage)
					stages.append("bud")

			if stage > 20  and stage <= 30:
				if "sapling" not in stages:
					for i in range(50):
						print ""
					print "Your plant has made it to the SAPLING stage"
					print "0    0        0      0        0        0"
					print "(    (        )      (        )        ("
					print ")    )       (        )      (          )"
					print ""
					print "Here it is: "
					print ""
					draw(stage)
					stages.append("sapling")

			if stage > 30 and stage <= 50:
				if "super sapling" not in stages:
					for i in range(50):
						print ""
					print "Your plant has made it to the SUPER SAPLING stage"
					print "0    0        0      0        0        0"
					print "(    (        )      (        )        ("
					print ")    )       (        )      (          )"
					print ""
					print "Here it is: "
					print ""
					draw(stage)
					stages.append("super sapling")
			
			if stage > 50 and stage <= 80:
				if "tree" not in stages:
					for i in range(50):
						print ""
					print "Your plant has made it to the TREE stage"
					print "0    0        0      0        0        0"
					print "(    (        )      (        )        ("
					print ")    )       (        )      (          )"
					print ""
					print "Here it is: "
					print ""
					draw(stage)
					stages.append("tree")

		prune  = prune + 1
		stage = stage + .5
		raw_input("Next Day?")
		for i in range(100):
			print ""
		print  "----------------------------------------------------------------"


while True:
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

