import requests
import os
import time




name="""
      ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
  ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
  ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌
  ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
   ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
            ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
   ▄▄▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
  ▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
   ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  \n"""



print(name)
print("\n Server discord : https://discord.gg/PVprfDmUpM \n Credit : ")
time.sleep(3)
os.system('cls')



url=input("Copy and paste like this \n\nExample 1FAIpQLSeHfsfui85lWmtjtDvaE1QyRv93DBSBzoXMTR9EcgPQSGou3A :")
urlfinal= "https://docs.google.com/forms/d/e/" + url +"/formResponse"









def spammer():
    data = {
        "entry.2092238618": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4",   
        "entry.1556369182": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4",  
        "entry.899712621": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4", 
        "entry.998395622": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4",   
        "entry.479301265": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4",
        "entry.1753222212": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4",
        "entry.588393791": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4",
        "entry.406023859": "https://cdn.discordapp.com/attachments/945662348021100584/997288630924083230/vidoleo_demande23101.mp4"
    }


    print(data)
    result = requests.post(urlfinal, data)
    print(result)
    
   


n=int(input("How much send ? Recommended 100 MAX "))
for i in range(n):
    spammer()
    
    

# Credit 𝐃𝐚𝐫𝐤#0174