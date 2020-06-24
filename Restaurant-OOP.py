"""
06-24-20

I created my first object oriented project that utilized:
- System of classes to organize code
- Constructors 
- Instances, Inheritance, and polymorphism 

"""

#parent class menu for all kinds of menus
class Menu: 
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
#string representation constructor 
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' to ' + str(self.end_time)

#calculate bill method that takes a list of purchased items, retrives key value and totals it to bill
  def calculate_bill(self,purchased_items):
    self.purchased_items = purchased_items
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items.get(item)
    return bill
#Franchise class 
class Franchise():
  def __init__(self,address,menus):
     self.address = address
     self.menus = menus
#String rep that returns address
  def __repr__(self):
    return 'We are located at ' + self.address
#Returns available menus based on time you want to go into restaurant 
  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu 

#Class for new business we want to start that encompasses components of other classes. 
class Business:
  def __init__(name, franchises):
    self.name = name
    self.franchises = franchises


##All objects below

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)


earlybird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

earlybird_menu = Menu('Early Bird', earlybird_items, 1500, 1800)


dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu('Dinner',dinner_items, 1700, 2300)


kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('Kids',kids_items, 1100 , 2100)

print(brunch_menu)

#how to call a method, the object refers to class

print(brunch_menu.calculate_bill(['pancakes','coffee']))

## Now we want to create Franchises

menus = [brunch_menu,earlybird_menu,dinner_menu,kids_menu]

flagship_store = Franchise("1232 West End Road", menus)

new_installment = Franchise("12 East Mulberry Street",menus)

print(flagship_store.available_menus(1700))

##Businesses

newbusiness = Business('Basta Fazoolin with my Heart', [flagship_store,new_installment])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Arepas', arepas_items, 10, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

arepas_business = Business('Take a Arepa', arepas_place)

