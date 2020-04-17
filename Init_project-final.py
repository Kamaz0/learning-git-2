zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]}

for sklep, lista in zakupy.items():
   str2 = [towar.capitalize() for towar in lista]
   print(f"Pierwsza jest {sklep.capitalize()}, kupuję tu następujące rzeczy: {str2}")

ctr = sum(map(len, zakupy.values()))
print(f"W sumie kupuję {ctr} produktów")