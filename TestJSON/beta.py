import json
import random
import time

def chance():
	with open("dataChance.json", "r") as f:
		return json.load(f)
def pickaxe():
	with open("pickaxe.json", "r") as f:
		return json.load(f)
def loaderSave():
	with open("save_beta.json", "r") as f:
		return json.load(f)
def save(data):
	with open("save_beta.json", "w") as f:
		return json.dump(data, f, indent=4)
def ore():
	with open("data.json", "r") as f:
		return json.load(f)
def loadequip():
	with open("equip.json", "r") as f:
		return json.load(f)
def equipform(data, equip):
	data["equip"] = loadPickaxe[equip]
	return data
def equip(data):
	with open("equip.json", "w") as f:
		json.dump(data, f, indent=4)

print(pickaxe())
selectPickaxe = input(str("Select Pickaxe:"))

selectOre = ore()
loadSave = loaderSave()
loadPickaxe = pickaxe()
loadChance = chance()
equipData = loadequip()
equipData = equipform(equipData, selectPickaxe)
equipPickaxe = equip(equipData)

current_speed = equipData["equip"]["speed"]
current_luck = equipData["equip"]["luck"]
print("your mining speed is =", current_speed, "s/ore")
print("your mining luck is =", current_luck)
time.sleep(2.5)

while True:
	roll = random.random()
	if roll <= 1 / loadChance["secret"] * current_luck:
		got = random.choice(selectOre["secret"])
		loadSave["secret"][got] += 1
		saveOre = save(loadSave)
		print(f"you got secret ore! ({got})")
		
	elif roll <= 1 / loadChance["exotic"] * current_luck:
		got = random.choice(selectOre["exotic"])
		loadSave["exotic"][got] += 1
		saveOre = save(loadSave)
		print(f"you got exotic ore! ({got})")
		
	elif roll <= 1 / loadChance["mythical"] * current_luck:
		got = random.choice(selectOre["mythical"])
		loadSave["mythical"][got] += 1
		saveOre = save(loadSave)
		print(f"you got mythical ore! ({got})")
		
	elif roll <= 1 / loadChance["legendary"] * current_luck:
		got = random.choice(selectOre["legendary"])
		loadSave["legendary"][got] += 1
		saveOre = save(loadSave)
		print(f"you got legendary ore! ({got})")
		
	elif roll <= 1 / loadChance["epic"] * current_luck:
		got = random.choice(selectOre["epic"])
		loadSave["epic"][got] += 1
		saveOre = save(loadSave)
		print(f"you got epic ore ({got})")
		
	elif roll <= 1 / loadChance["rare"] * current_luck:
		got = random.choice(selectOre["rare"])
		loadSave["rare"][got] += 1
		saveOre = save(loadSave)
		print(f"you got rare ore ({got})")
	else:
		got = random.choice(selectOre["uncommon"])
		loadSave["uncommon"][got] += 1
		saveOre = save(loadSave)
		print(f"you got uncommon ore ({got})")
	time.sleep(current_speed)
		
		
