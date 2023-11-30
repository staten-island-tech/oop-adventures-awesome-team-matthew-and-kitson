from merchant import Merchant
from hero import Hero
guy=Merchant("Filler", ["1", "2", "3", "4"])
me=Hero("Me", 500, [])
guy.welcome()

guy.sell("3")
me.buy("3")