from datetime import datetime
from decimal import Decimal

with open("postavy.txt", "r", encoding="utf-8") as soubor, \
     open("oblibene-postavy.txt", "w", encoding="utf-8") as vystup:
    
    for radek in soubor:
        udaje = radek.strip().split("#")
        
        jmeno = udaje[0]
        vek = int(udaje[1])
        pohlavi = udaje[2]
        zvire = udaje[3] == "ano"
        datum = datetime.strptime(udaje[4], '%Y-%m-%d')
        oblibenost = Decimal(udaje[5])
        
        if oblibenost > Decimal("2.5"):
        
            print(f"Jméno: {jmeno}")
            print(f"Věk: {vek}")
            print(f"Pohlaví: {pohlavi}")
        
            print(f"Zvíře: {zvire}")
            print(f"Poslední promítání: {datum.strftime('%Y-%m-%d')}")
            print(f"Oblíbenost u diváků: {oblibenost}")
            print("---------------------------------------------------")
            
            vystup.write(f"{jmeno}\t{vek}\t{pohlavi}\t{zvire}\t{datum.strftime('%Y-%m-%d')}\t{oblibenost}\n")