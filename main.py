from datetime import datetime, date

def kunlar_soni(sana1, sana2):
    sana1 = datetime.strptime(sana1, "%Y-%m-%d")
    sana2 = datetime.strptime(sana2, "%Y-%m-%d")
    farq = sana2 - sana1
    return farq.days

sana1 = "2020-01-01"
sana2 = "2022-01-01"
print(kunlar_soni(sana1, sana2))
