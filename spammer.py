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
print("\n Server discord : https://discord.gg/PVprfDmUpM \n Credit : Darkexitmatrix")
time.sleep(3)
os.system('cls')



url=input("Copy and paste like this \n\nExample 1FAIpQLSeHfsfui85lWmtjtDvaE1QyRv93DBSBzoXMTR9EcgPQSGou3A :")
urlfinal= "https://docs.google.com/forms/d/e/" + url +"/formResponse"








msg=(input("Message ? :"))
#entry=int(input("Number of entry (Check readme):"))
#for i in range(entry)

def spammer():
    data = {
        "entry.2092238618": msg,   
        "entry.1556369182": msg,  
        "entry.899712621": msg, 
        "entry.998395622": msg,   
        "entry.479301265": msg,
        "entry.1753222212":msg,
        "entry.588393791": msg,
        "entry.406023859": msg
    }


    print(data)
    result = requests.post(urlfinal, data)
    print(result)
    
   


n=int(input("How much send ? Recommended 100 MAX "))
for i in range(n):
    spammer()
    
    

# Credit 𝐃𝐚𝐫𝐤#0174
