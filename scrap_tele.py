from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

myprofile = webdriver.FirefoxProfile(r'C:\Users\Aloysius\AppData\Roaming\Mozilla\Firefox\Profiles\fcbei8vp.teleScrape')
PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)

target = 100
Saham = ['AALI', 'ABBA', 'ABDA', 'ABMM', 'ACES', 'ACST', 'ADES', 'ADHI', 'ADMF', 'ADMG', 'ADRO', 'AGAR', 'AGII', 'AGRO', 'AGRS', 'AHAP', 'AIMS', 'AISA', 'AKKU', 'AKPI', 'AKRA', 'AKSI', 'ALDO', 'ALKA', 'ALMI', 'ALTO', 'AMAG', 'AMAN', 'AMAR', 'AMFG', 'AMIN', 'AMOR', 'AMRT', 'ANDI', 'ANJT', 'ANTM', 'APEX', 'APIC', 'APII', 'APLI', 'APLN', 'ARGO', 'ARII', 'ARKA', 'ARMY', 'ARNA', 'ARTA', 'ARTI', 'ARTO', 'ASBI', 'ASDM', 'ASGR', 'ASII', 'ASJT', 'ASMI', 'ASPI', 'ASRI', 'ASRM', 'ASSA', 'ATAP', 'ATIC', 'AUTO', 'AYLS', 'BABP', 'BACA', 'BAJA', 'BALI', 'BANK', 'BAPA', 'BAPI', 'BATA', 'BAYU', 'BBCA', 'BBHI', 'BBKP', 'BBLD', 'BBMD', 'BBNI', 'BBRI', 'BBRM', 'BBSI', 'BBSS', 'BBTN', 'BBYB', 'BCAP', 'BCIC', 'BCIP', 'BDMN', 'BEBS', 'BEEF', 'BEKS', 'BELL', 'BESS', 'BEST', 'BFIN', 'BGTG', 'BHAT', 'BHIT', 'BIKA', 'BIMA', 'BINA', 'BIPI', 'BIPP', 'BIRD', 'BISI', 'BJBR', 'BJTM', 'BKDP', 'BKSL', 'BKSW', 'BLTA', 'BLTZ', 'BLUE', 'BMAS', 'BMRI', 'BMSR', 'BMTR', 'BNBA', 'BNBR', 'BNGA', 'BNII', 'BNLI', 'BOGA', 'BOLA', 'BOLT', 'BOSS', 'BPFI', 'BPII', 'BPTR', 'BRAM', 'BRIS', 'BRMS', 'BRNA', 'BRPT', 'BSDE', 'BSIM', 'BSSR', 'BSWD', 'BTEK', 'BTEL', 'BTON', 'BTPN', 'BTPS', 'BUDI', 'BUKK', 'BULL', 'BUMI', 'BUVA', 'BVIC', 'BWPT', 'BYAN', 'CAKK', 'CAMP', 'CANI', 'CARE', 'CARS', 'CASA', 'CASH', 'CASS', 'CBMF', 'CCSI', 'CEKA', 'CENT', 'CFIN', 'CINT', 'CITA', 'CITY', 'CLAY', 'CLEO', 'CLPI', 'CMNP', 'CMPP', 'CNKO', 'CNTX', 'COCO', 'COWL', 'CPIN', 'CPRI', 'CPRO', 'CSAP', 'CSIS', 'CSMI', 'CSRA', 'CTBN', 'CTRA', 'CTTH', 'DADA', 'DART', 'DAYA', 'DCII', 'DEAL', 'DEFI', 'DEWA', 'DFAM', 'DGIK', 'DGNS', 'DIGI', 'DILD', 'DIVA', 'DKFT', 'DLTA', 'DMAS', 'DMMX', 'DMND', 'DNAR', 'DNET', 'DOID', 'DPNS', 'DPUM', 'DSFI', 'DSNG', 'DSSA', 'DUCK', 'DUTI', 'DVLA', 'DWGL', 'DYAN', 'EAST', 'ECII', 'EDGE', 'EKAD', 'ELSA', 'ELTY', 'EMDE', 'EMTK', 'ENRG', 'ENVY', 'ENZO', 'EPAC', 'EPMT', 'ERAA', 'ERTX', 'ESIP', 'ESSA', 'ESTA', 'ESTI', 'ETWA', 'EXCL', 'FAPA', 'FAST', 'FASW', 'FILM', 'FINN', 'FIRE', 'FISH', 'FITT', 'FMII', 'FOOD', 'FORU', 'FORZ', 'FPNI', 'FREN', 'FUJI', 'GAMA', 'GDST', 'GDYR', 'GEMA', 'GEMS', 'GGRM', 'GGRP', 'GHON', 'GIAA', 'GJTL', 'GLOB', 'GLVA', 'GMFI', 'GMTD', 'GOLD', 'GOLL', 'GOOD', 'GPRA', 'GSMF', 'GTBO', 'GWSA', 'GZCO', 'HADE', 'HDFA', 'HDIT', 'HDTX', 'HEAL', 'HELI', 'HERO', 'HEXA', 'HITS', 'HKMU', 'HMSP', 'HOKI', 'HOME', 'HOMI', 'HOTL', 'HRME', 'HRTA', 'HRUM', 'IATA', 'IBFN', 'IBST', 'ICBP', 'ICON', 'IDPR', 'IFII', 'IFSH', 'IGAR', 'IIKP', 'IKAI', 'IKAN', 'IKBI', 'IMAS', 'IMJS', 'IMPC', 'INAF', 'INAI', 'INCF', 'INCI', 'INCO', 'INDF', 'INDO', 'INDR', 'INDS', 'INDX', 'INDY', 'INKP', 'INOV', 'INPC', 'INPP', 'INPS', 'INRU', 'INTA', 'INTD', 'INTP', 'IPCC', 'IPCM', 'IPOL', 'IPTV', 'IRRA', 'ISAT', 'ISSP', 'ITIC', 'ITMA', 'ITMG', 'JAST', 'JAWA', 'JAYA', 'JECC', 'JGLE', 'JIHD', 'JKON', 'JKSW', 'JMAS', 'JPFA', 'JRPT', 'JSKY', 'JSMR', 'JSPT', 'JTPE', 'KAEF', 'KARW', 'KAYU', 'KBAG', 'KBLI', 'KBLM', 'KBLV', 'KBRI', 'KDSI', 'KEEN', 'KEJU', 'KIAS', 'KICI', 'KIJA', 'KINO', 'KIOS', 'KJEN', 'KKGI', 'KLBF', 'KMDS', 'KMTR', 'KOBX', 'KOIN', 'KONI', 'KOPI', 'KOTA', 'KPAL', 'KPAS', 'KPIG', 'KRAH', 'KRAS', 'KREN', 'LAND', 'LAPD', 'LCGP', 'LCKM', 'LEAD', 'LIFE', 'LINK', 'LION', 'LMAS', 'LMPI', 'LMSH', 'LPCK', 'LPGI', 'LPIN', 'LPKR', 'LPLI', 'LPPF', 'LPPS', 'LRNA', 'LSIP', 'LTLS', 'LUCK', 'MABA', 'MAGP', 'MAIN', 'MAMI', 'MAPA', 'MAPB', 'MAPI', 'MARI', 'MARK', 'MASA', 'MAYA', 'MBAP', 'MBSS', 'MBTO', 'MCAS', 'MCOR', 'MDIA', 'MDKA', 'MDKI', 'MDLN', 'MDRN', 'MEDC', 'MEGA', 'MERK', 'META', 'MFIN', 'MFMI', 'MGNA', 'MGRO', 'MICE', 'MIDI', 'MIKA', 'MINA', 'MIRA', 'MITI', 'MKNT', 'MKPI', 'MLBI', 'MLIA', 'MLPL', 'MLPT', 'MMLP', 'MNCN', 'MOLI', 'MPMX', 'MPOW', 'MPPA', 'MPRO', 'MRAT', 'MREI', 'MSIN', 'MSKY', 'MTDL', 'MTFN', 'MTLA', 'MTPS', 'MTRA', 'MTSM', 'MTWI', 'MYOH', 'MYOR', 'MYRX', 'MYTX', 'NASA', 'NATO', 'NELY', 'NFCX', 'NICK', 'NIKL', 'NIPS', 'NIRO', 'NISP', 'NOBU', 'NRCA', 'NUSA', 'NZIA', 'OASA', 'OCAP', 'OKAS', 'OMRE', 'OPMS', 'PADI', 'PALM', 'PAMG', 'PANI', 'PANR', 'PANS', 'PBID', 'PBRX', 'PBSA', 'PCAR', 'PDES', 'PEGE', 'PEHA', 'PGAS', 'PGJO', 'PGLI', 'PGUN', 'PICO', 'PJAA', 'PKPK', 'PLAN', 'PLAS', 'PLIN', 'PMJS', 'PMMP', 'PNBN', 'PNBS', 'PNGO', 'PNIN', 'PNLF', 'PNSE', 'POLA', 'POLI', 'POLL', 'POLU', 'POLY', 'POOL', 'PORT', 'POSA', 'POWR', 'PPGL', 'PPRE', 'PPRO', 'PRAS', 'PRDA', 'PRIM', 'PSAB', 'PSDN', 'PSGO', 'PSKT', 'PSSI', 'PTBA', 'PTDU', 'PTIS', 'PTPP', 'PTPW', 'PTRO', 'PTSN', 'PTSP', 'PUDP', 'PURA', 'PURE', 'PURI', 'PWON', 'PYFA', 'PZZA', 'RAJA', 'RALS', 'RANC', 'RBMS', 'RDTX', 'REAL', 'RELI', 'RICY', 'RIGS', 'RIMO', 'RISE', 'RMBA', 'ROCK', 'RODA', 'RONY', 'ROTI', 'RUIS', 'SAFE', 'SAME', 'SAMF', 'SAPX', 'SATU', 'SBAT', 'SCCO', 'SCMA', 'SCNP', 'SCPI', 'SDMU', 'SDPC', 'SDRA', 'SFAN', 'SGER', 'SGRO', 'SHID', 'SHIP', 'SIDO', 'SILO', 'SIMA', 'SIMP', 'SINI', 'SIPD', 'SKBM', 'SKLT', 'SKRN', 'SKYB', 'SLIS', 'SMAR', 'SMBR', 'SMCB', 'SMDM', 'SMDR', 'SMGR', 'SMKL', 'SMMA', 'SMMT', 'SMRA', 'SMRU', 'SMSM', 'SOCI', 'SOFA', 'SOHO', 'SONA', 'SOSS', 'SOTS', 'SPMA', 'SPTO', 'SQMI', 'SRAJ', 'SRIL', 'SRSN', 'SRTG', 'SSIA', 'SSMS', 'SSTM', 'STAR', 'STTP', 'SUGI', 'SULI', 'SUPR', 'SURE', 'SWAT', 'TALF', 'TAMA', 'TAMU', 'TARA', 'TAXI', 'TBIG', 'TBLA', 'TBMS', 'TCID', 'TCPI', 'TDPM', 'TEBE', 'TECH', 'TELE', 'TFAS', 'TFCO', 'TGKA', 'TGRA', 'TIFA', 'TINS', 'TIRA', 'TIRT', 'TKIM', 'TLKM', 'TMAS', 'TMPO', 'TNCA', 'TOBA', 'TOPS', 'TOTL', 'TOTO', 'TOWR', 'TOYS', 'TPIA', 'TPMA', 'TRAM', 'TRIL', 'TRIM', 'TRIN', 'TRIO', 'TRIS', 'TRJA', 'TRST', 'TRUK', 'TRUS', 'TSPC', 'TUGU', 'TURI', 'UANG', 'UCID', 'UFOE', 'ULTJ', 'UNIC', 'UNIQ', 'UNIT', 'UNSP', 'UNTR', 'UNVR', 'URBN', 'VICI', 'VICO', 'VINS', 'VIVA', 'VOKS', 'VRNA', 'WAPO', 'WEGE', 'WEHA', 'WICO', 'WIFI', 'WIIM', 'WIKA', 'WINS', 'WMUU', 'WOMF', 'WOOD', 'WOWS', 'WSBP', 'WSKT', 'WTON', 'YELO', 'YPAS', 'YULE', 'ZBRA', 'ZINC', 'ZONE', 'TAHAN', 'HOLD', 'HALT', 'EIDO', 'IHSG']
# Saham = ['ADHI', 'ADRO', 'AKRA', 'ANTM', 'ASII', 'ASRI', 'BBCA', 'BBNI', 'BBRI', 'BBTN', 'BKSL', 'BMRI', 'BSDE', 'CPIN', 'ELSA', 'EXCL', 'GGRM', 'HMSP', 'ICBP', 'INCO', 'INDF', 'INDY', 'INKP', 'INTP', 'ITMG', 'JSMR', 'KLBF', 'LPKR', 'LPPF', 'MEDC', 'MNCN', 'PGAS', 'PTBA', 'PTPP', 'SCMA', 'SMGR', 'SRIL', 'SSMS', 'TLKM', 'TPIA', 'UNTR', 'UNVR', 'WIKA', 'WSBP', 'WSKT']

driver.get('https://web.telegram.org/#/im?p=@TheTradersGroup')
time.sleep(5)

wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
print(len(chat))
jumlah = 0

while len(chat) < target:
    html = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]')
    wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
    if(jumlah!=len(chat)):
        print(len(chat))
        jumlah = len(chat)
        driver.execute_script("arguments[0].scrollTop = 0", html)
penulis = ""
pesan2 = []
jam = ""
time.sleep(2)
tanggal = []
tanggal2 = []
n = 0
# f = open("scrapeCoba.txt","w+")
for i in reversed(range(1,len(chat)+21)):
    masuk = False
    if (len(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(i)+"]")) > 0):
        time.sleep(0.25)
        pesan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(i)+"]")
        driver.execute_script("arguments[0].scrollIntoView(true);", pesan)
        try:
            if (len(pesan.find_elements_by_xpath(".//a[@class='im_message_photo_thumb']")) > 0) :
                # print('ini adalah foto')
                penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                gambar = pesan.find_element_by_xpath(".//img[@class='im_message_photo_thumb']").get_attribute('src')
                pesan2.insert(0,"Gambar : "+gambar)
                if (len(pesan.find_elements_by_xpath(".//div[@class='im_message_photo_caption']")) > 0):
                    pesan2.insert(0, pesan.find_element_by_xpath(".//div[@class='im_message_photo_caption']").text)
                jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
                urllib.request.urlretrieve(gambar, str(i)+'.jpg')
            elif (len(pesan.find_elements_by_xpath(".//span[@ng-switch-when='messageActionChatJoined']")) > 0):
                # print('seseorang join')
                penulis = pesan.find_element_by_xpath(".//div[@class='im_service_message']").text
                pesan2 = []
                jam = ''
            elif (len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_split_text']")) > 0):
                if((len(pesan.find_elements_by_xpath(".//div[@class='im_message_date_split im_service_message_wrap' and @style='display: none;']")) > 0)):
                    penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                    pesan2.insert(0, pesan.find_element_by_xpath(".//div[@class='im_message_text']").text)
                    jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
                else :
                    print("ini adalah tanggal")
                    print("Div : " + str(i))
                    tgl = pesan.find_element_by_xpath(".//span[@class='im_message_date_split_text']").text
                    print(tgl)
                    for k in range(len(tanggal2)):
                        tanggal2[k]['Tanggal'] = tgl
                    tanggal.extend(tanggal2)
                    tanggal2 = []
            else :
                # print('ini adalah pesan biasa')
                penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
                pesan2.insert(0, pesan.find_element_by_xpath(".//div[@class='im_message_text']").text)
                if(len(pesan.find_elements_by_xpath(".//span[@my-short-message='replyMessage']"))>0):
                    balas = pesan.find_element_by_xpath(".//span[@my-short-message='replyMessage']").text
                    balas = "Membalas : " + balas
                    pesan2.insert(0,balas)

        except:
            penulis = "Error"
            pesan2 = "Error"
        # print("Div : "+str(i))
        pesan2 = "\n".join(pesan2)
        if any(word in pesan2.upper().split() for word in Saham):
            masuk = True
        if(penulis != ""):
            if((penulis == 'Hendro Masori' or penulis == 'Hauw' or penulis == 'Michael Yeoh') or masuk):
                print("Div : "+str(i))
                print("user : "+penulis)
                try:
                    # f.write("User : "+ penulis +"\n"+pesan2+"\nJam : "+jam+"\n==========================\n")
                    print(pesan2)
                except:
                    print("Tidak bisa menampilkan pesan")
                print("jam : " + jam)
                print('=======================================================')
                item = {
                    'User' : penulis,
                    'Pesan' : pesan2,
                    'Jam' : jam
                }
                tanggal2.append(item)

            penulis = ""
            pesan2 = []
        jam = ""
# f.close()
df = pd.DataFrame(tanggal)
# df.to_csv('coba.csv')