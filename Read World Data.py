import json
import re

with open('WorldData.json') as f:
    data = json.load(f)
f.close()
Count = 0
APC = 0
PlayersCount = 1
while True:
    try:
        #EscapePodData Attempting Parse
        Seed = str(data['Seed'])
        X = int(data['EscapePodData']['EscapePods'][0]['Location']['X'])
        Y = int(data['EscapePodData']['EscapePods'][0]['Location']['Y'])
        Z = int(data['EscapePodData']['EscapePods'][0]['Location']['Z'])
        EscapePodId = str(data['EscapePodData']['EscapePods'][0]['Id'])
        FabricatorId = str(data['EscapePodData']['EscapePods'][0]['FabricatorId'])
        MedicalFabId = str(data['EscapePodData']['EscapePods'][0]['MedicalFabricatorId'])
        StorageId = str(data['EscapePodData']['EscapePods'][0]['StorageContainerId'])
        RadioId = str (data['EscapePodData']['EscapePods'][0]['RadioId'])
        Damaged = (data['EscapePodData']['EscapePods'][0]['Damaged'])
        RadioDamaged = (data['EscapePodData']['EscapePods'][0]['RadioDamaged'])
        if 'False' in str(Damaged):
            Damaged = "Fixed"
        elif 'True' in str(Damaged):
            Damaged = "Broken"
        else:
            Damaged = "Unknown"
        if 'False' in str(RadioDamaged):
            RadioDamaged = "Fixed"
        elif 'True' in str(RadioDamaged):
            RadioDamaged = "Broken"
        else:
            RadioDamaged = "Unknown"
        print('''LifePod Information :
                        Seed           : ''', str(Seed),'''
                        LifePod Status : ''', str(Damaged),'''
                        Radio Status   : ''', str(RadioDamaged), '''
                        Location       :
                                         X = ''', str(X), '''
                                         Y = ''', str(Y), '''
                                         Z = ''', str(Z), '''
                        ID's           :
                                         LifePod Id           : ''', str(EscapePodId),'''
                                         Fabricator Id        : ''', str(FabricatorId),'''
                                         Medical Fabricator Id: ''', str(MedicalFabId),'''
                                         Storage Container Id : ''', str(StorageId), '''
                                         Radio Id             : ''', str(RadioId), '''
                        Players Lifepod:''')
        while True:
            try:
                CurrentPlayer = (data['EscapePodData']['EscapePods'][0]['AssignedPlayers'][APC])
                PlayerCount = APC + 1
                print("                                        ",str(PlayerCount))
                APC = APC + 1 
            except:
                break
        #EscapePodData Parsed
        APC = 0
        while True:
            try:
                VehicleData = (data['VehicleData']['Vehicles'][APC])
                APC = APC + 1 
            except:
                print (str(APC))
                APC = 0
            print("Vehicles Information:")
            while True:
                
                Name = (data['VehicleData']['Vehicles'][APC]['Name'])
                TechType = (data['VehicleData']['Vehicles'][APC]['TechType'])
                Health = (data['VehicleData']['Vehicles'][APC]['Health'])
                try:
                    LightOn = (data['VehicleData']['Vehicles'][APC]['LightOn'])
                    if 'False' in str(LightsOn):
                        LightOn = "Off"
                    elif 'True' in str(LightsOn):
                        LightOn = "On"
                    else:
                        LightOn = "Unknown"
                except:
                    pass
                Id = (data['VehicleData']['Vehicles'][APC]['Id'])
                DockingBayId = (data['VehicleData']['Vehicles'][APC]['DockingBayId']['value'])
                if 'null' in str(DockingBayId):
                    DockingBayId = "No Id (Can't be docked)")
                X = (data['VehicleData']['Vehicles'][APC]['Position']['X'])
                Y = (data['VehicleData']['Vehicles'][APC]['Position']['Y'])
                Z = (data['VehicleData']['Vehicles'][APC]['Position']['Z'])
                RotX = (data['VehicleData']['Vehicles'][APC]['Rotation']['X'])
                RotY = (data['VehicleData']['Vehicles'][APC]['Rotation']['Y'])
                RotZ = (data['VehicleData']['Vehicles'][APC]['Rotation']['Z'])
                RotW = (data['VehicleData']['Vehicles'][APC]['Rotation']['W'])
                Type = (data['VehicleData']['Vehicles'][APC]['$type'])
                try:
                    FloodLightsOn = (data['VehicleData']['Vehicles'][APC]['FloodLightsOn'])
                    InternalLightsOn = (data['VehicleData']['Vehicles'][APC]['InternalLightsOn'])
                    SilentRunningOn = (data['VehicleData']['Vehicles'][APC]['SilentRunningOn'])
                    ShieldOn = (data['VehicleData']['Vehicles'][APC]['ShieldOn'])
                    SonarOn = (data['VehicleData']['Vehicles'][APC]['SonarOn'])
                    EngineState = (data['VehicleData']['Vehicles'][APC]['EngineState'])
                    EngineSpeed = (data['VehicleData']['Vehicles'][APC]['EngineMode'])
                    
                except:
                    pass
                    
                if 'Seamoth' in str(TechType):
                    print ('''              Name  : ''', str(Name), '''
                                        Type    : ''', str(TechType), '''
                                        Health  : ''', str(Health), '''
                                        Lights  : ''', str(LightOn), '''
                                        Position:
                                                    X = ''', str(X),'''
                                                    Y = ''', str(Y),'''
                                                    Z = ''', str(Z),'''
                                        Rotation:
                                                    X = ''', str(RotX),'''
                                                    Y = ''', str(RotY),'''
                                                    Z = ''', str(RotZ),'''
                                                    W = ''', str(RotW),'''
                                        
                                        Docking Id: ''', str(DockingBayId),'''
                                        Id        : ''', str(Id),'''
''')
                    pass
                
                elif 'Cyclops' in str(TechType):
                    pass
                
                elif 'Exosuit' in str (TechType):
                    pass
                else:
                    print ("            No Vehicles Found")
                    
                break

        
        Count = Count + 1
        break
    except:
        break

