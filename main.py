class character:
  name = None 
  health = None
  magicPoints = None
  
  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}")

class player(character):
  lives = None
  alive = None
  
  def __init__(self, name, health, magicPoints, lives, alive):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.lives = lives
    self.alive = alive

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nLives: {self.lives}\nAlive: {self.alive}")

class enemy(character):
  type = None
  strength = None
  
  def __init__(self, name, health, magicPoints, type, strength):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}")

class orc(enemy):
  speed = None
  
  def __init__(self, name, health, magicPoints, strength, speed):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = "Orc"
    self.strength = strength
    self.speed = speed

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}")

class vampire(enemy):
  day = None
  
  def __init__(self, name, health, magicPoints, strength, day):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = "Vampire"
    self.strength = strength
    self.day = day

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nDay: {self.day}")

print("🌟Generic RPG🌟")
print()
david = player("David", 100, 50, 3, "Yes")
david.print()
print()
boris = vampire("Boris", 45, 70, 3, "Night")
boris.print()
print()
rishi = vampire("Rishi", 70, 10, 75, "Day")
rishi.print()
print()
bill = orc("Bill", 60, 5, 75, 90)
bill.print()
print()
ted = orc("Ted", 75, 40, 80, 45)
ted.print()
print()
station = orc("Station", 35, 40, 49, 50)
station.print()

  