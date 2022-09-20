from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   
from selenium.common.exceptions import TimeoutException
import re

def get_col_vlaues(all_tr, driver):

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
    for ind, item in enumerate(key_list):
        # encoded_string = item.encode("ascii", "ignore")
        # decode_string = encoded_string.decode()
        if ind < 40:
            new_keylist.append(item + ' :')
        else:
            new_keylist.append(item)    
    
    exceptions = ["Utilisation prédominante :", "Numéro d'unité de voisinage :", "Date d'inscription au rôle :"]

    vall = [''] * 54
    for ind, tr in enumerate(all_tr[18:]):
        try:
            text = tr.find_elements(By.TAG_NAME, 'td')
            # if ind+18 > 90:
            #     print(text[0].text, '+++' ,text[1].text)
            if text[0].text not in new_keylist and text[0].text not in exceptions:
                # pdf_text.append(text[0].text)
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
            # elif text[0].text == new_keylist[6]:
            #     vall[5] = (text[1].text)
            #     continue
            # elif text[0].text == new_keylist[7]:
            #     vall[6] = (text[1].text)
            #     continue
            # elif text[0].text == new_keylist[8]:
            #     out = (text[1].text)
            #     s_list = out.split(' ')
            #     qc = s_list[s_list.index('QC,')-1]
            #     split = (out.index(qc))
            #     vall[7] = out[0:split]
            #     vall[8] = out[split:]
            #     continue
            # elif "Date d'inscription au rôle :" in text[0].text:
            #     print(text[0].text)
            #     vall[9] = (text[1].text)
            #     continue
            # elif text[0].text[:-2]+'2' == new_keylist[11][:-2]:
            #     print(text[0].text[:-2]+'2', new_keylist[11][:-2])
            #     vall[10] = (text[1].text)
            #     continue
            # elif text[0].text[:-2]+'2' == new_keylist[12][:-2]:
            #     vall[11] = (text[1].text)
            #     continue
            # elif text[0].text[:-2]+'2' == new_keylist[13][:-2]:
            #     out2 = (text[1].text)
            #     s_list = out2.split(' ')
            #     qc = s_list[s_list.index('QC,')-1]
            #     split = (out2.index(qc))
            #     vall[12] = out2[0:split]
            #     vall[13] = out2[split:]
            #     continue
            # elif text[0].text[:-2]+'2' == new_keylist[15][:-2]:
            #     vall[14] = (text[1].text)
            #     continue
            elif text[0].text == new_keylist[16]:
                vall[15] = (text[1].text)
                continue
            elif text[0].text == new_keylist[17]:
                vall[16] = (text[1].text)
                continue
            elif text[0].text == new_keylist[18]:
                vall[17] = (text[1].text)
                continue
            elif text[0].text == new_keylist[19]:
                vall[18] = (text[1].text)
                continue
            elif text[0].text == new_keylist[20]:
                vall[19] = (text[1].text)
                continue
            elif text[0].text == new_keylist[21]:
                vall[20] = (text[1].text)
                continue
            elif text[0].text == new_keylist[22]:
                vall[21] = (text[1].text)
                continue
            elif text[0].text == new_keylist[23]:
                vall[22] = (text[1].text)
                continue
            elif text[0].text == new_keylist[24]:
                vall[23] = (text[1].text)
                continue
            # elif text[0].text == new_keylist[25]:
            #     vall[24] = (text[1].text)
                # continue
            elif text[0].text == new_keylist[26]:
                vall[25] = (text[1].text)
                continue
            elif text[0].text == new_keylist[27]:
                vall[26] = (text[1].text)
                continue
            elif text[0].text == new_keylist[28]:
                vall[27] = (text[1].text)
                continue
            elif text[0].text == new_keylist[29]:
                vall[28] = (text[1].text)
                continue
            elif text[0].text == new_keylist[30]:
                vall[29] = (text[1].text)
                continue
            elif text[0].text == new_keylist[31]:
                vall[30] = (text[1].text)
                continue
            elif text[0].text == new_keylist[32]:
                vall[31] = (text[1].text)
                continue
            elif text[0].text == new_keylist[33]:
                vall[32] = (text[1].text)
                continue
            elif text[0].text == new_keylist[34]:
                vall[33] = (text[1].text)
                continue
            elif text[0].text == new_keylist[35]:
                vall[34] = (text[1].text)
                continue
            elif text[0].text == new_keylist[36]:
                vall[35] = (text[1].text)
                continue
            elif text[0].text == new_keylist[37]:
                vall[36] = (text[1].text)
                continue
            elif text[0].text == new_keylist[38]:
                vall[37] = (text[1].text)
                continue
            elif text[0].text == new_keylist[39]:
                vall[38] = (text[1].text)
                continue
            elif text[0].text == "Terrain imposable":
                vall[39] = (text[1].text)
                continue
            elif text[0].text == "Terrain imposable de l'EAE situé dans une zone agricole":
                vall[40] = (text[1].text)
                continue
            elif text[0].text == "Bâtiment imposable":
                vall[41] = (text[1].text)
                continue
            elif text[0].text == "Immeuble imposable":
                vall[42] = (text[1].text)
                continue
            elif text[0].text == "Immeuble imposable de l'EAE situé hors d'une zone agricole (cat. imm. agricoles)":
                vall[43] = (text[1].text)
                continue
            elif text[0].text == "Immeuble imposable de l'EAE situé dans une zone agricole (cat. imm. agricoles)":
                vall[44] = (text[1].text)
                continue
            elif text[0].text == "Loi sur le MAPAQ":
                vall[45] = (text[1].text)
                continue
            elif text[0].text == "Terrain imposable":
                vall[46] = (text[1].text)
                continue
            elif text[0].text == "Terrain imposable de l'EAE situé dans une zone agricole":
                vall[47] = (text[1].text)
                continue
            elif text[0].text == "Terrain non imposable de l'EAE":
                vall[48] = (text[1].text)
                continue
            elif text[0].text == "Bâtiment imposable":
                vall[49] = (text[1].text)
                continue
            elif text[0].text == "Immeuble imposable":
                vall[50] = (text[1].text)
                continue
            elif text[0].text == "Immeuble non imposable (non compensable)":
                
                vall[51] = (text[1].text)
                continue
            elif text[0].text == "Loi sur le MAPAQ":
                vall[52] = (text[1].text)
                continue
            elif text[0].text == new_keylist[54]:
                vall[53] = (text[1].text)
                continue
            else:
                continue     
        except Exception as e:
            continue
    try:
        vall[5] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/div').text
    except:
        pass
    try:
        vall[6] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/div').text
    except:
        pass
    try:
        out = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/div').text
        sep = ['(qc)', 'qc', '(quebec)', 'quebec']
        for sep in sep:
            if sep in out.lower():
                s_list = out.lower().split(' ')
                try:
                    qc = s_list[s_list.index(sep)-1]
                except:
                    qc = s_list[s_list.index(sep+',')-1]
                split = (out.lower().index(qc))
                vall[7] = (out[0:split])
                vall[8] = (out[split:])
                break
        else:
            split = (out.split(','))
            try:
                vall[7] = split[0]
                vall[8] = split[1]
            except:
                pass
    except:
        pass
    try:
        vall[9] = driver.find_element(By.XPATH, '//*[@id="__bookmark_3"]/tbody/tr[4]/td[2]/div').text
    except:
        pass
    try:
        vall[10] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[4]/td/table/tbody/tr[6]/td[2]/div').text
    except:
        pass
    try:
        vall[11] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[4]/td/table/tbody/tr[7]/td[2]/div').text
    except:
        pass
    try:
        out2 = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[4]/td/table/tbody/tr[8]/td[2]/div').text
        sep = ['(qc)', 'qc', '(quebec)', 'quebec']
        for sep in sep:
            if sep in out2.lower():
                s_list = out2.lower().split(' ')
                try:
                    qc = s_list[s_list.index(sep)-1]
                except:
                    qc = s_list[s_list.index(sep+',')-1]
                split = (out2.lower().index(qc))
                vall[12] = (out2[0:split])
                vall[13] = (out2[split:])
                break
        else:
            split = (out2.split(','))
            try:
                vall[12] = split[0]
                vall[13] = split[1]
            except:
                pass
    except:
        pass
    try:
        vall[14] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[4]/td/table/tbody/tr[9]/td[2]/div').text
    except:
        pass
    try:
        vall[24] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr[7]/td/table/tbody/tr[2]/td[3]/table/tbody/tr[4]/td[2]/div').text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_85')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_85_6a2f5187-80da-4836-83d9-3308757aae3b")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[40] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_89')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_89_289c1d12-58d3-4f97-88a9-3c4f9aace253")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[41] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_91')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_91_d6b3d882-6bc3-4136-b613-3111bc9ae962")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[42] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_93')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_93_fbb70e6c-4b95-406a-969c-353c8ee23715")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[44] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_86')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_86_467add3f-06ce-4886-b464-955a6d4271cd")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[45] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_106')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_106_13f913a3-1639-4324-9bf9-e8dd090c7b4b")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[46] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_104')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_104_bf16667e-0136-4212-902f-2879a611559d")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[47] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_108')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_108_6ad71329-f461-4976-a75f-5d6d687b8e3d2")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[48] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_110')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_110_38bb10ef-de6b-4a9d-9b77-0af9748a9827")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[49] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_112')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_112_7bf33b3a-aed8-4970-a4ca-75950cc50b42")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[50] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_114')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_114")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[51] = data[1].text
    except:
        pass
    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_105')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_105_ade76dfa-2a58-42bb-a129-8904a87a105a")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[52] = data[1].text
    except:
        pass

    try:
        table = driver.find_element(By.XPATH, "//table[starts-with(@id, 'AUTOGENBOOKMARK_109')]")
        # table = driver.find_element(By.ID, "AUTOGENBOOKMARK_109_7d1a8d1a-b1b4-4651-b2b4-54b062cc8b50")
        data = table.find_elements(By.TAG_NAME, 'td')
        # vall[52] = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/div').text
        vall[53] = data[1].text
    except:
        pass


    non_decimal = re.compile(r'[^\d.]+')
    for i, val in enumerate(vall):
        if val.endswith(('m', 'm2', '$')):
            # vall[i] = val.rsplit(' ', 1)[0]
            if ',' in val:
                val = val.replace(',', '.')
            vall[i] = float(non_decimal.sub('', val.rsplit(' ', 1)[0]))

    # vall = [val.rsplit(' ', 1)[0] for i, val in enumerate(vall) if val.endswith(('m', 'm2', '$'))]
    return vall, key_list