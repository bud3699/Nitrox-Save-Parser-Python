import json
import re

with open('PlayerData.json') as f:
    data = json.load(f)
f.close()
Name_Count = 0
#print (json.dumps(data, indent=4))
print ('''Users In this world:
''')

def CapitalSpace(str1):
    try:
        str2 = str1.replace("HUD", "Hud")
    except:
        str2 = str1
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str2)


while True:

    try:
        print ("Name          : ", data['Players'][Name_Count]['Name'])
        print ("Permision     : ", data['Players'][Name_Count]['Permissions'])
        print ("Nitrox Id     : ", data['Players'][Name_Count]['NitroxId'])
        PermaDead = (data['Players'][Name_Count]['IsPermaDeath'])
        if 'False' in str(PermaDead):
            PermaDead = "Still Alive"
        else:
            PermaDead = "Dead"
        print ("HardcoreDead  : ", str(PermaDead))
        Oxygen = int(data['Players'][Name_Count]['CurrentStats']['Oxygen'])
        MaxOxygen = int(data['Players'][Name_Count]['CurrentStats']['MaxOxygen'])
        Health = int(data['Players'][Name_Count]['CurrentStats']['Health'])
        Food = int(data['Players'][Name_Count]['CurrentStats']['Food'])
        Water = int(data['Players'][Name_Count]['CurrentStats']['Water'])
        InfectionAmount = float(data['Players'][Name_Count]['CurrentStats']['InfectionAmount'])
        print('''Player Stats  :
                Oxygen          :''', str(Oxygen), '''
                Tank Capacity   :''', str(MaxOxygen), '''
                Health          :''', str(Health), '''
                Food            :''', str(Food), '''
                Water           :''', str(Water), '''
                Infection Amount:''', str(InfectionAmount))
        X = int(data['Players'][Name_Count]['SpawnPosition']['X'])
        Y = int(data['Players'][Name_Count]['SpawnPosition']['Y'])
        Z = int(data['Players'][Name_Count]['SpawnPosition']['Z'])
        print('''Player Location:
                X = ''', str(X),'''
                Y = ''', str(Y),'''
                Z = ''', str(Z))
        print ("Equipped Items:" )
        EICount = 0
        while True:
            try:
                TechType = (data['Players'][Name_Count]['EquippedItems'][EICount]['TechType'])
                TechType = (CapitalSpace(TechType))
                print ("               ", str(TechType))
                EICount = EICount + 1 
            except:
                break
    
        print ("")
        Name_Count = Name_Count + 1
    except:
        break

