import math 

class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
      total += item['amount']

    output = title + items + "Total: " + str(total)
    return output

  def deposit(self, amount, description=""):

    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    
    if(self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False 

  def get_balance(self):

    total_cash = 0
    for item in self.ledger:
      total_cash += item["amount"]

    return total_cash

  def transfer(self, amount, category):
  
    if(self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    
    if(self.get_balance() >= amount):
      return True
    return False

def create_spend_chart(categories):
  string = "Percentage spent by category\n"
  accum = 0
  parts = []
  for category in categories:
    accum =accum + category.get_balance()
 
  for category in categories:
    parts.append(category.get_balance() * 100 / accum)
    #parts.append( math.floor(category.get_balance() / accum * 10) * 10)

#  for part in parts:
#    print(part) #debug

  act = 100
  while act >= 0:
    if act == 100:
      string += str(act) + "|"
    elif act > 0:
      string += " " + str(act) + "|"
    else:
      string += "  " + str(act) + "|"

    for part in parts:
      if part >= act:
        string += " o "
      else:
        string += "   "

    act = act - 10
    string += "\n"
  
  string += "    -" + ("---"* len(parts)) + "\n"

  atoms = []
  for category in categories:
    atoms.append(list(category.name))

  atomicity = atoms.copy()
  while len(atomicity) > 0:
    subString = ""
    for atom in atoms:
      subString += " " + atom[0] + " "
      if len(atom) >= 1 and atom[0] != " ":
        atom.remove(atom[0])
        if len(atom) == 0:
          atom.append(" ")
          atomicity.remove(atomicity[0])

    if(len(atomicity) > 0):
      subString += "\n"
    string += "    " + subString

  return string


