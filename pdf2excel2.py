from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   
from selenium.common.exceptions import TimeoutException

def get_col_vlaues():

    key_list = ['Lot', 'Adresse', 'Cadastre(s) et numéro(s) de lot', 'Numéro matricule', 'Utilisation prédominante', 
        "Numéro d'unité de voisinage", 'Nom', "Statut aux fins d'imposition scolaire", 'Adresse postale', 'ville postale',
        "Date d'inscription au rôle", 'Nom2', "Statut aux fins d'imposition scolaire2", 'Adresse postale2', 'ville postale2',
        "Date d'inscription au rôle2", 'Mesure frontale', 'Superficie', 'Zonage agricole', 'Superficie totale', 
        'Superficie en zone agricole', 'Superficie visée par imposition maximale', "Nombre d'étages", 
        'Année de construction', "Aire d'étages", 'Genre de construction ', 'Lien physique', 'Nombre de logements', 
        'Nombre de locaux non résidentiels', 'Nombre de chambres locatives', 'Superficie totale', 
        'Superficie en zone agricole', 'Date de référence au marché', 'Valeur du terrain', 'Valeur du bâtiment', 
        "Valeur de l'immeuble", "Valeur de l'immeuble au rôle antérieur", 
        "Catégorie et classe d'immeuble à des fins d'application des taux variés de taxation", 
        "Valeur imposable de l'immeuble", "Valeur non imposable de l'immeuble", 'Terrain imposable', 
        "Terrain imposable de l'EAE situé dans une zone agricole", 'Bâtiment imposable', 'Immeuble imposable', 
        "Immeuble imposable de l'EAE situé hors d'une zone agricole (cat. imm. agricoles)", 
        "Immeuble imposable de l'EAE situé dans une zone agricole (cat. imm. agricoles)", 'Loi sur le MAPAQ', 
        'Terrain imposable', "Terrain imposable de l'EAE situé dans une zone agricole", 
        "Terrain non imposable de l'EAE", 'Bâtiment imposable', 'Immeuble imposable', 
        'Immeuble non imposable (non compensable)', 'Loi sur le MAPAQ', 'Loi sur la fiscalité municipale']
    
    new_keylist = []
    for item in key_list:
        # encoded_string = item.encode("ascii", "ignore")
        # decode_string = encoded_string.decode()
        new_keylist.append(item + ' :')
    
    exceptions = ["Utilisation prédominante :", "Numéro d'unité de voisinage :"]

    vall = [''] * 54
    for tr in all_tr:
        try:
            text = tr.find_elements(By.TAG_NAME, 'td')
            if text[0].text not in new_keylist and text[0].text not in exceptions:
                continue
            elif text[0].text == "Adresse :":
                vall[0] = (text[1].text)
                continue
            elif text[0].text == new_keylist[2]:
                vall[1] = (text[1].text)
                continue
            elif text[0].text == new_keylist[3]:
                vall[2] = (text[1].text)
                continue
            elif text[0].text == "Utilisation prédominante :":
                vall[3] = (text[1].text)
                continue
            elif text[0].text == "Numéro d'unité de voisinage :":
                vall[4] = (text[1].text)
                continue
            elif text[0].text == new_keylist[6]:
                vall[5] = (text[1].text)
                continue
            elif text[0].text == new_keylist[7]:
                vall[6] = (text[1].text)
                continue
            elif text[0].text == new_keylist[8]:
                out = (text[1].text)
                s_list = out.split(' ')
                qc = s_list[s_list.index('QC,')-1]
                split = (out.index(qc))
                vall[7] = out[0:split]
                vall[8] = out[split:]
                continue
            elif text[0].text == new_keylist[9]:
                vall[9] = (text[1].text)
                continue
            elif text[0].text+'2' == new_keylist[10]:
                vall[10] = (text[1].text)
                continue
            elif text[0].text+'2' == new_keylist[11]:
                vall[11] = (text[1].text)
                continue
            elif text[0].text+'2' == new_keylist[12]:
                out2 = (text[1].text)
                s_list = out2.split(' ')
                qc = s_list[s_list.index('QC,')-1]
                split = (out2.index(qc))
                vall[12] = out2[0:split]
                vall[13] = out2[split:]
                continue
            elif text[0].text+'2' == new_keylist[13]:
                vall[14] = (text[1].text)
                continue
            elif text[0].text == new_keylist[14]:
                vall[15] = (text[1].text).split(' ')[0]
                continue
            elif text[0].text == new_keylist[15]:
                vall[16] = (text[1].text).split(' ')[0]
                continue
            elif text[0].text == new_keylist[16]:
                vall[17] = (text[1].text)
                continue
            elif text[0].text == new_keylist[17]:
                vall[18] = (text[1].text)
                continue
            elif text[0].text == new_keylist[18]:
                vall[19] = (text[1].text)
                continue
            elif text[0].text == new_keylist[19]:
                vall[20] = (text[1].text)
                continue
            elif text[0].text == new_keylist[20]:
                vall[21] = (text[1].text)
                continue
            elif text[0].text == new_keylist[21]:
                vall[22] = (text[1].text)
                continue
            elif text[0].text == new_keylist[22]:
                vall[23] = (text[1].text).split(' ')[0]
                continue
            elif text[0].text == new_keylist[23]:
                vall[24] = (text[1].text)
                continue
            elif text[0].text == new_keylist[24]:
                vall[25] = (text[1].text)
                continue
            elif text[0].text == new_keylist[25]:
                vall[26] = (text[1].text)
                continue
            elif text[0].text == new_keylist[26]:
                vall[27] = (text[1].text)
                continue
            elif text[0].text == new_keylist[27]:
                vall[28] = (text[1].text)
                continue
            elif text[0].text == new_keylist[28]:
                vall[29] = (text[1].text)
                continue
            elif text[0].text == new_keylist[29]:
                vall[30] = (text[1].text)
                continue
            elif text[0].text == new_keylist[30]:
                vall[31] = (text[1].text)
                continue
            elif text[0].text == new_keylist[31]:
                vall[32] = (text[1].text).rsplit(' ', 1)[0]
                continue
            elif text[0].text == new_keylist[32]:
                vall[33] = (text[1].text).rsplit(' ', 1)[0]
                continue
            elif text[0].text == new_keylist[33]:
                vall[34] = (text[1].text).rsplit(' ', 1)[0]
                continue
            elif text[0].text == new_keylist[34]:
                vall[35] = (text[1].text).rsplit(' ', 1)[0]
                continue
            elif text[0].text == new_keylist[35]:
                vall[36] = (text[1].text)
                continue
            elif text[0].text == new_keylist[36]:
                vall[37] = (text[1].text).rsplit(' ', 1)[0]
                continue
            elif text[0].text == new_keylist[37]:
                vall[38] = (text[1].text)
                continue
            elif text[0].text == new_keylist[38]:
                vall[39] = (text[1].text)
                continue
            elif text[0].text == new_keylist[39]:
                vall[40] = (text[1].text)
                continue
            elif text[0].text == new_keylist[40]:
                vall[41] = (text[1].text)
                continue
            elif text[0].text == new_keylist[41]:
                vall[42] = (text[1].text)
                continue
            elif text[0].text == new_keylist[42]:
                vall[43] = (text[1].text)
                continue
            elif text[0].text == new_keylist[43]:
                vall[44] = (text[1].text)
                continue
            elif text[0].text == new_keylist[44]:
                vall[45] = (text[1].text)
                continue
            elif text[0].text == new_keylist[45]:
                vall[46] = (text[1].text)
                continue
            elif text[0].text == new_keylist[46]:
                vall[47] = (text[1].text)
                continue
            elif text[0].text == new_keylist[47]:
                vall[48] = (text[1].text)
                continue
            elif text[0].text == new_keylist[48]:
                vall[49] = (text[1].text)
                continue
            elif text[0].text == new_keylist[49]:
                vall[50] = (text[1].text)
                continue
            elif text[0].text == new_keylist[50]:
                vall[51] = (text[1].text)
                continue
            elif text[0].text == new_keylist[51]:
                vall[52] = (text[1].text)
                continue
            elif text[0].text == new_keylist[52]:
                vall[53] = (text[1].text)
                continue
            else:
                continue
            
        except Exception as e:
            print(e)
            continue
    
    
    # vall = [str(val).split(' ')[0] for val in vall if val.endswith(('m', 'm2', '$'))]
    return vall, key_list