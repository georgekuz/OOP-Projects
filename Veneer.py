#I am really enjoying the process of learning Object Oriented Programming and data science on my own
#This is my second OOP Project that utilizes systems of classes, instances, and
#constructors


#Parent Art Class
class Art():
  def __init__(self, artist,title,medium,year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return '%s. "%s". %s. %s. %s, %s.'%(self.artist,self.title,self.medium,self.year, self.owner.name, self.owner.location)

class Marketplace ():
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)

  def show_listings(self):
    for listing in self.listings:
      print(listing)

veneer = Marketplace()
veneer.show_listings()
#Init any new art sellers and its string representation
class Listing:
  def __init__(self,art,price,seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return '%s, %s' %(self.art.title, self.price)

class Client:
  def __init__(self,name,location,is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    self.artwork = artwork
    self.price = price
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
        



edytta = Client('Edytta Halpirt', 'Private Collection', False)

moma = Client('The MOMA', 'New York', True)

george = Art('George Kuzhikat', 'Mundane', 'Oil on canvas', 2020, edytta)

edytta.sell_artwork(george, '$6M USD')


moma.buy_artwork(george)


veneer.show_listings()
