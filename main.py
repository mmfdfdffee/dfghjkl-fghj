import json
import requests
import time
import hashlib
import urllib.parse
import os
import urllib3
import linecache
import sys
import shutil
import base64
from json import loads , dumps
from bs4 import BeautifulSoup as s
import string
import os
import pymongo
import re
import random
import timeit
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import timedelta
import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random,string

#point users
client2user = pymongo.MongoClient("mongodb+srv://aa:bb@cluster0.salso.mongodb.net/a?retryWrites=true&w=majority")
mydb= client2user["a"]

mycol = mydb["users"]
allgive="0"



linkapi=["https://myccount-3.bdbbdbbzbsb.repl.co/p?tagId=",

"https://co-1.coockis.repl.co/p?tagId=",
"https://co-2.coockis.repl.co/p?tagId=",
"https://co-3.coockis.repl.co/p?tagId=",
"https://co-4.coockis.repl.co/p?tagId="


]



myaccounts=["dadadrgfg444fefef@hotmail.com",

"aysqkkmsqsdy@fexpost.com",
"spvvtgnkzcve@fexpost.com",
"rbmhyhzjyjed@fexpost.com",
"lvcrwobzxdcw@fexpost.com"
]



list = ["655049808","1150981021","655049808",'924741529','724400620']
listgrop = ["655049808","1150981021","-1001486013009","-1001265599800","-454571674","-1001267395473"]
payload={}
emalss = loads(open('emails.json' , 'r').read())
counturls = loads(open('counturl.json' , 'r').read())




TOKEN = "1878915210:AAHV9C5kIxaVTLp9utoYWtWQbdCzGrWm23Y"

URL = "https://api.telegram.org/bot{}/".format(TOKEN)
hh1 = ''' <html>
                                                                                                             <head> 
                                                                                                            <meta charset="utf-8"/>        
                                                                                                             <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
                                                                                                                    </head>



                                                                                                                            <body    '''

hh2 = '''</body>
                                                                                                         </html>   '''

class ParseMode(object):
    MARKDOWN = 'Markdown'
    MARKDOWN_V2 = 'MarkdownV2'
    HTML = 'HTML'

def get_url(url):
    try:
        response = requests.get(url)
        content = response.content.decode("utf-8")
        return (content)
    except:
        pass

def post_url(urll , data, file=None):
    try:
        if file is not None:
            response = requests.post(urll, files=file , data=data)
            return json.loads(response.content.decode())
        else:
            response = requests.post(urll , data=data)
            return json.loads(response.content.decode())
    except:
        pass

def get_updates(offset=None):
    try:
        url = URL + "getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset)
        content = get_url(url)
        js = json.loads(content)
        return js
    except:
        pass

def get_last_update_id(updates):
    try:
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)
    except:
        pass


def countss():
    try:
        backaaa=counturls[str("id")]
        df=int(backaaa)
        if df > 25 :
            print("oh need chnge email")
            t=changemlls()
            counturls["id"] = str("0")
            file = open('counturl.json' , 'w')
            file.write(dumps(counturls))
            file.close()
        else:
            print("oh my emalss is good")
            totot=df+1
            counturls["id"] = str(totot)
            file = open('counturl.json' , 'w')
            file.write(dumps(counturls))
            file.close()
    except:
        pass
def out3(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele+'\n==================\n'  
    
    # return string  
    return str1
def an():
    try:
        f=emalss[str("id")]
        print(f)
        for d in range(len(linkapi)):
            print(linkapi[int(f)])
            return str(linkapi[int(f)])
            break
    except:
        pass

def changemlls():
    try:
        f=emalss[str("id")]
        print(f)
        tot=int(f)+1
        remme=len(linkapi)-1
        if tot > remme :
            print("is out format")
            emalss["id"] = str("0")
            file = open('emails.json' , 'w')
            file.write(dumps(emalss))
            file.close()
        else:
            print("is in list")
            emalss["id"] = str(tot)
            file = open('emails.json' , 'w')
            file.write(dumps(emalss))
            file.close()
    except :
        pass


def send_msgr(txt,chat_id,message_id):
   token = "your_token"
   txt="🔰لا تتوفر لديك نقاط للاشتراك\nتواصل⬇️\n🔰 من العراق 🔰\n@eng2028\n📍You have no points.To subscribe, contact\n"
   chat_id = str(chat_id)
   url_req = "https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + txt +'&reply_to_message_id='+str(message_id)+'&parse_mode=Markdown'+'&reply_markup={"inline_keyboard": [[{"text": "from Iraq", "url": "https://t.me/eng2080/67"}],[{"text": "from India", "url": "https://t.me/mohdUsama99_vip/3"}]]}'
   results = requests.get(url_req)
   print(results.json())
#check is url is chegg or not


def get_id(qu_url):
    qu_url = qu_url.split('?')[0]
    qu_url = qu_url.split('&')[0]
    qu_url = qu_url.split('#')[0]
    qu_url = qu_url.split('%')[0]
    qid = ''
    ty = ''
    if ('solution' in qu_url) and ('chapter' in qu_url):  # and ('problem' in qu_url):
        if '-exc' in qu_url:
            exc = qu_url.rindex('-exc')
            if exc > 100:
                qu_url = qu_url[:exc]
            else:
                pass
        qid = qu_url[qu_url.rindex('help/') + 5:]
        ty = 't'
    elif '-q' in qu_url:
        try:
            qid = qu_url[qu_url.rindex('-q'):]
            ty = 'q'
        except Exception as e:
            if 'not found' in str(e):
                return 'Please make sure the link is correct 🤔😕'

    else:
        return 'Please make sure the link is correct 🤔😕'

    return [qid, ty]

#

def zro(repy_id):
    try:
        mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
        print(mydoc2)
        print("is sub grube")
        g=[mydoc2]
        oldadd=int(g[0]['point'])
        newadd=int(g[0]['point'])
        clc=oldadd-newadd
        print("is clc sub  :"+str(clc))
        mydict77 = {  str(repy_id):str(repy_id), "point": str(clc) }
        mydict4 = { "$set":mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass

#sub grupe
def sub_point(user_id):
    try:
        mydoc2 = mycol.find_one({ str(user_id):str(user_id)})
        print(mydoc2)
        print("is sub ")
        g=[mydoc2]
        oldadd=int(g[0]['point'])
        newadd=int("1")
        clc=oldadd-newadd
        print("is clc sub  :"+str(clc))
        mydict77 = {  str(user_id):str(user_id), "point": str(clc) }
        mydict4 = { "$set":mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass



#add points
def add_point(repy_id ,add):
    try:
        #print("id group points :"+str(chat_id)+"and add point :"+str(add_point))
        mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
        print(mydoc2)
        if  str(repy_id)  not in str(mydoc2):
            mydict = {  str(repy_id):str(repy_id), "point": str(add) }
            x = mycol.insert_one(mydict)
            return str(add)
        else:
            print("is old grupe")
            g=[mydoc2]
            oldadd=int(g[0]['point'])
            newadd=int(add)
            clc=oldadd+newadd
            print("is clc :"+str(clc))
            mydict77 = {  str(repy_id):str(repy_id), "point": str(clc) }
            mydict4 = { "$set":mydict77}
            mycol.update_one(mydoc2, mydict4)
            return str(clc)
    except:
        pass



#chuck point
def get_point(user_id):
    try:
        print("id  points :"+str(user_id))
        mydoc2 = mycol.find_one({ str(user_id):str(user_id)})
        print(mydoc2)
        if  str(user_id)  not in str(mydoc2):
            mydict = {  str(user_id):str(user_id), "point": allgive }
            x = mycol.insert_one(mydict)
            return allgive
        else:
            g=[mydoc2]
            print("user is old in file time :"+str(g[0]['point']))
            return str(g[0]['point'])
    except:
        pass



def Check(update):
    try:
        if not 'callback_query' in str(update) and not 'channel_post' in str(update):
            
            user_id = update["message"]["from"]["id"]
            chat_id = update["message"]["chat"]["id"]
            chat_type= update["message"]["chat"]["type"]
            message_text = update['message']['text']
            try:
                first_name = update["message"]["from"]["first_name"]
            except:
                first_name = ''
            try:
                last_name = update["message"]["from"]["last_name"]
            except:
                last_name = ''
            try:
                username = update["message"]["from"]["username"]
            except:
                username = ''
            
            message_id = update["message"]["message_id"]
            if message_text=='/get':
                pi=get_point(user_id)
                send_message('💠Number of points :'+str(pi),chat_id,message_id)
            elif message_text.startswith('/ch-')  and str(user_id) in list:
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[0])
                remme=len(linkapi)-1
                if int(result[0]) > remme :
                    send_message("Wrong email number :"+str(result[0]), chat_id, message_id)
                else:
                    emalss["id"] = str(result[0])
                    file = open('emails.json' , 'w')
                    file.write(dumps(emalss))
                    file.close()
                    send_message("An account has been changed to a number :"+str(result[0]), chat_id, message_id)
            elif message_text==('/emails')  and str(user_id) in list:
                g=[]
                t=-1
                for s in myaccounts:
                    t=t+1
                    g.append(str(t)+" :"+s)
                print(g)
                remil=out3(g)
                send_message(str(remil) , chat_id, message_id)
            elif message_text==('/show')  and str(user_id) in list:
                print("is show")
                backa=emalss[str("id")]
                send_message("Email is now working in a bot :"+str(backa) , chat_id, message_id)
            elif message_text.startswith('/add-') and update["message"]['reply_to_message'] and str(user_id) in list:
                repy_id = update["message"]['reply_to_message']['from']['id']
                repy_msg_id= update["message"]['reply_to_message']['message_id']
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result)
                add=str(result[0])
                asd=add_point(repy_id ,add)
                send_message('🔰Points have been added to you 🔰   '+str(asd)+'🔰',chat_id,repy_msg_id)
            elif message_text=="/zero"  and update["message"]['reply_to_message'] and str(user_id) in list:
                repy_id = update["message"]['reply_to_message']['from']['id']
                zz=zro(repy_id)
                print(str(zz))
                send_message("Total points have been deleted",chat_id,message_id)
            elif message_text=="/id" :
                send_message("id :"+str(user_id)+"\n"+str(chat_id),chat_id,message_id)
            elif message_text=="/info"  :
                send_message( 'The number of database  :'+str(mycol.count()) , chat_id, message_id)

              

            elif 'text' in update['message'].keys():
                if message_text=='/start':
                    send_message('🔰You can subscribe to Chegg to get more answers ⬇️'+'\n\n🔰 يمكنك الاشتراك بموقع Chegg للحصول اجابات اكثر ⬇️'+'\n\n https://t.me/eng2080/67\nhttps://t.me/mohdUsama99_vip/3',chat_id)
                    return True


                if 'entities' in update['message'].keys():
                    qu_url = ''
                    for entiti in update['message']['entities']:
                        if (entiti['type']=='url' or entiti['type']=='text_link'):
                            offset = entiti['offset']
                            length = entiti['length']
                            qu_url = message_text[offset: offset + length]
                    
                    if  qu_url and str(chat_id) in listgrop:
                        print("Question : ",qu_url)
                        cc=get_id(qu_url)
                        print(cc)
                        time.sleep(20)
                        if "Please make sure the link is correct" in  cc:
                            print("url is not chegg")
                        elif cc[0].startswith('-q'):
                            print("url is from Q and A")
                            pi=get_point(user_id)
                            print(pi)
                            ress=int(pi)
                            if ress==0 or ress<0:
                                txt="s"
                                snd=send_msgr(txt,chat_id,message_id)
                                #send_message('تم انتهاء نقاط \npoints expired\n\nMore points contact ',chat_id,message_id)
                            else:
                                resl =send_req(qu_url)
                                se = str(resl)
                                if se.startswith('here is your answer'):
                                    su=sub_point(user_id)
                                    i = open('./Answer.html', 'rb')
                                    url876 = ("https://api.telegram.org/bot"+TOKEN+"/sendDocument?chat_id="+str(chat_id)+'&caption='+str('💠 This is your answer 🌚\n'+'\n✅ Remaining points:'+str(su)+"\n✅ Join channel :"+'&reply_to_message_id='+str(message_id))+'&parse_mode=Markdown'+'&reply_markup={"inline_keyboard": [[{"text": "from Iraq", "url": "https://t.me/eng2080/67"}],[{"text": "from India", "url": "https://t.me/mohdUsama99_vip/3"}]]}')
                                    url_txt = requests.post(url876, files={'document': i})
                                else:
                                    send_message(resl, chat_id, message_id)
                        else:
                            print("now l can get answer")
                            pi=get_point(user_id)
                            print(pi)
                            ress=int(pi)
                            if ress==0 or ress<0:
                                txt="s"
                                snd=send_msgr(txt,chat_id,message_id)
                                #send_message('🔰لا تتوفر لديك نقاط للاشتراك\nتواصل⬇️\n🔰 من العراق 🔰\n@eng2028\n📍You have no points.To subscribe, contact\n🔰From India and Pakistan\n⬇️\n@MohdUsama99',chat_id,message_id)
                            else:
                                print("l am sore but not answer")
                                resl = ans_book(qu_url)
                                se = str(resl)
                                if se.startswith('here is your answer'):
                                    su=sub_point(user_id)
                                    i = open('./Answer.html', 'rb')
                                    url876 = ("https://api.telegram.org/bot"+TOKEN+"/sendDocument?chat_id="+str(chat_id)+'&caption='+str('💠 This is your answer 🌚\n'+'\n✅ Remaining points:'+str(su)+"\n✅ Join channel :"+'&reply_to_message_id='+str(message_id))+'&parse_mode=Markdown'+'&reply_markup={"inline_keyboard": [[{"text": "from Iraq", "url": "https://t.me/eng2080/67"}],[{"text": "from India", "url": "https://t.me/mohdUsama99_vip/3"}]]}')
                                    url_txt = requests.post(url876, files={'document': i})
                                else:
                                    send_message(resl, chat_id, message_id)

    except:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('Error EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
    return True





chuk = {
         "User-Agent":"PostmanRuntime/7.28.0",
        "Accept": "*/*",
 "Cache-Control":"no-cache",
 "Postman-Token": "04d2a2c9-63ab-43bf-bfcb-e7f38a92beb4",
 "Host":"www.chegg.com",
 "Accept-Encoding":"gzip, deflate, br",
 "Connection": "keep-alive",
 "Cookie": "C=0;CSessionID=6f7a55cd-cf95-485c-ba1c-e3b122cd1d7b;O=0; PHPSESSID=837161d45166559ee95dfa1bdde1e371; U=0; V=ba35049ebce8516446423128043519ce6074891676d8c5.51631027; exp=A184A%7CA311C%7CA803B%7CC024A%7CA560B; expkey=BEE682351558F2E82EA91564D646A8A1; user_geo_location=%7B%22country_iso_code%22%3A%22US%22%2C%22country_name%22%3A%22United+States%22%2C%22region%22%3A%22VA%22%2C%22region_full%22%3A%22Virginia%22%2C%22city_name%22%3A%22Ashburn%22%2C%22postal_code%22%3A%2220149%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22en-US%22%5D%7D%7D"

}
# ans urls chegg book
def ans_book(qu_url):
    try:
        urk = str(qu_url)
        while True:

            ############
            r = requests.get(str(urk), headers=chuk)
            print(r)
            soup = s(r.content, 'html.parser')
            images4 = soup.find_all("script")
            cc = str(images4)
            zx = cc.find("isbn13")
            print(zx)
            print((cc[zx:(zx + 34)]))
            text = str(soup)
            start = text.find('''chapterData''') + 1
            end = text.find('''chapterMap''')
            cut_text = text[start:end].strip()
            print(cut_text)
            ###############################
            text = str(cut_text)
            start = text.find("problemId") + 1
            end = text.find('''''')
            cut_text3 = text[start:].strip()
            print(cut_text3)
            ####################
            text = str(cut_text)
            start = text.find('''chapterId''') + 1
            end = text.find('''problemData''')
            cut_text2 = text[start:end].strip()
            print(cut_text2)
            if zx == -1:
                continue
            else:
                # import requests
                import json
                import re
                # print((take[x:(x+20)]))
                # print((take[x2:(x2+26)]))
                # print((take[x3:(x3+22)]))
                string = str(cut_text2)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[0])
                z1 = result[0]
                ######
                string = (cc[zx:(zx + 34)])
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[1])
                z2 = result[1]
                ##########
                string = str(cut_text3)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[0])
                z3 = result[0]
                ##################
                url = "https://www.chegg.com/study/_ajax/persistquerygraphql"

                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
                    'Accept': 'application/json',
                    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                    'Referer': urk,
                    'Content-Type': 'application/json',
                    # 'Origin': 'https://www.chegg.com',
                    # 'Connection': 'keep-alive',
                    'Cookie': "C=0; O=0; U=53a315e8b624e8113d0fedd2b5279e2e; V=53ea3d09ffac4987552099cbc650c3f1600572af6bd005.67201889; exp=A184B%7CA311C%7CA803B%7CC024A%7CA560B%7CA259B%7CA294C%7CA207A%7CA735A%7CA209A%7CA212A%7CA239A%7CA448A%7CA966F%7CA270C%7CA278C%7CA935B%7CA890H; expkey=39A7192252E6B4DCE4A2E85538D5D002; usprivacy=1YNY; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jun+10+2021+22%3A24%3A43+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.10.0&hosts=&consentId=42e3d1d6-5eb1-4651-a397-7228e2e5bcee&interactionCount=1&landingPath=NotLandingPage&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1&AwaitingReconsent=false; _scid=51cbd642-6298-4f9a-8e63-5340c7f5b568; s_ecid=MCMID%7C29037934875219248102115392500229927675; _ga=GA1.2.969290114.1610969786; _sctr=1|1613336400000; LPVID=ZlNmM0ZDg4NTU4YWJjOGMw; _omappvp=YtbBWN9Rej9YSk5amzwlEYQyTNkY6oTNrZIYwl4RF5JVI56dJGs6uCNmIpSG0gvbkyDtbbJAgVYtagiZq0SJiYCFZvZfsBCm; OneTrustWPCCPAGoogleOptOut=false; sbm_mcid=29037934875219248102115392500229927675; _pxvid=d3c11c77-5981-11eb-bafc-0242ac12000d; sbm_sbm_id=0100007F73730560340052BB0268C817; sbm_country=IQ; sbm_dma=0; __gads=ID=c3186b246bf23f05-22271f3b95b90052:T=1610969972:S=ALNI_MapCo18UIZ8skSlOzbQtftyHuJz0Q; sbm_gaid=969290114.1610969786; csrftoken=HHEsWsklgxBaSlQB2Ol8gmn1n47E3Fdi0hbDHEu2x1g79xX8UoaQpBFE9Iip5rh0; al_cell=main-1-control; optimizelyEndUserId=oeu1612370560880r0.845804414318425; _cs_c=1; __CT_Data=gpv=405&ckp=tld&dm=chegg.com&apv_79_www33=405&cpv_79_www33=405&rpv_79_www33=35; _cs_id=80a89d96-4877-abd3-99ac-9b25fd169509.1612370628.121.1622554936.1622554936.1.1646534628095.Lax.0; WRUID=3150646956556611; bc.visitor_token=6762772580509515776; _vid=O5syefnm0OgfgfmYsRF6; DFID=web|O5syefnm0OgfgfmYsRF6; _ym_uid=1612534492191791627; _ym_d=1612534492; chgcsdmtoken=%7B%22user_uuid%22%3A%229df80428-1ac9-438f-9867-7871293da6dd%22%2C%22created_date%22%3A%222021-06-09T14%3A02%3A53.784Z%22%2C%22account_sharing_device_management%22%3A1%7D; al_cell=main-1-control; chgcsdetaintoken=1; chgcsastoken=nZ6bB9cr0hHlUqFGqCVcnqbEoLL7iMETmoU19VJp3vxZBhCTAPRjdbGWQc0PiVlCBV0WMY3WfyoAhI1X4SkI5_hZIw0ugq77pMXKCoc1aj-ORRZ5-GUzoyh-WTgcEACv; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%203896d4d5-2705-45f7-b84d-6af53501c2f7%2C%20%22created_date%22%20%3D%3E%202021-06-10T19%3A22%3A42.831Z%20%5D; _CT_RS_=Recording; gid=1; gidr=MA; forterToken=0f35933ac63146f883ddfdab379135da_1623352940631_9547_dUAL9_13ck; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCMID%7C29037934875219248102115392500229927675%7CMCIDTS%7C18788%7CMCAID%7CNONE%7CMCOPTOUT-1623360275s%7CNONE%7CvVersion%7C4.6.0; s_pers=%20buFirstVisit%3Dcore%252Ccs%7C1781013730607%3B%20gpv_v6%3Dchegg%257Cweb%257Ccs%257Cchegg%2520study%2520homepage%7C1623354875856%3B; intlPaQExitIntentModal=hide; user_geo_location=%7B%22country_iso_code%22%3A%22IQ%22%2C%22country_name%22%3A%22Iraq%22%2C%22region%22%3A%22DQ%22%2C%22region_full%22%3A%22Dhi+Qar%22%2C%22city_name%22%3A%22Nasiriyah%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22ar-IQ%22%5D%7D%7D; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; _sdsat_authState=Hard%20Logged%20In; s_sess=%20buVisited%3Dcs%252Ccore%3B%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccs%2525257Cqa%2525257Cquestion%25252520page%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.chegg.com%2525252Fstudy%252526ot%25253DA%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D69A878A07D217B5F-7A05833F2887BE16%3B%20s_ptc%3D0.00%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E3.42%255E%255E0.00%255E%255E10.72%255E%255E0.12%255E%255E14.28%3B; mcid=29037934875219248102115392500229927675; CVID=016059f3-1d47-45e5-ad17-aef3f86d921f; _sdsat_cheggUserUUID=3896d4d5-2705-45f7-b84d-6af53501c2f7; BIBSESSID=f2e1a1d4-e1b4-4253-880a-bd1042b441f2; tpudsa=tpudsa; userRole=mybibpro; _gd1623345814358=1; opt-user-profile=53ea3d09ffac4987552099cbc650c3f1600572af6bd005.67201889%252C19944471923%253A19963683656; _gd1623345823394=1; _sdsat_highestContentConfidence={%22course_uuid%22:%224b278621-1ff4-4f47-afcf-c613047a1553%22%2C%22course_name%22:%22intermediate-algebra%22%2C%22confidence%22:0.1501%2C%22year_in_school%22:%22college-year-1%22%2C%22subject%22:[{%22uuid%22:%220cf46127-71ed-41c6-bea0-67b85e0d3bc6%22%2C%22name%22:%22algebra%22}]}; _gd1623349134304=1; CSID=1623351669693; schoolapi=39d1a707-b142-40d6-b4ba-3f5833b3e904|0.9; _gd1623351875188=1; sbm_sbm_session_id_2=476cf8cd-c71c-4732-8039-4382dac4a3ee; _gd1623351880248=1; 188796f5-ba98-4284-b4c0-5b9a1bca9d2a_TMXCookie=true; PHPSESSID=54iqjp2cpn0piojfuinvgt5cm2; CSessionID=ad67d3a4-2cd3-419f-a6de-a534dd6169a1; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzODk2ZDRkNS0yNzA1LTQ1ZjctYjg0ZC02YWY1MzUwMWMyZjciLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTYzOTEyMjk4OCwiaWF0IjoxNjIzMzUyOTg4LCJlbWFpbCI6InRoaXNncmVhdDI3ODlAb3V0bG9vay5jb20ifQ.q5mgNw-REGfxxJJLHy3dT2j2oehyEcQ33MwzCqMp0NaIbWx6DcMRO7wIk7VSigFDJMYNHmZOqTKThpdFjoAT8G79hp76EciZP9oGDMY0UL6z0PjSol6HUztQXO4vnSGQCLyZZcBVYoweV6fOj-BOEmnz3wzmL5VwErsd_SN17yg8eC1TfIJ2izYrqneQkYzUIvhikyehlkt0nnc67wBxSWUZs52TDZ_YjppsA5K69nc2RKZva8yUCCIjQOOnklT79WnmOH9Vf9ltJ5Jr6Lie52xEj5Ec5n0i75s21nxjFQvH5gi7naX52FYfAGpjDN6zrFYP5sWsMRNbdVrNuRyJ_w; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhUTkU0cWwxNTRxekZieTBBakxDdSJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8Mzg5NmQ0ZDUtMjcwNS00NWY3LWI4NGQtNmFmNTM1MDFjMmY3IiwiYXVkIjpbImNoZWdnLW9pZGMiLCJodHRwczovL2NoZWdnLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMzM1Mjk4OCwiZXhwIjoxNjIzMzU0NDI4LCJhenAiOiIzVFpiaGZzWndkZUhiaG9WTXhPdlpHYjM3TWN2YzBvOCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgYWRkcmVzcyBwaG9uZSBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.nRjqpJEb_q34sO3ArQVD9xYq_nxMaAIt9uDQEx6kN3LO-Yi_E7cAYKWFThVfpSbHwP8GlEmWicKRun9uyv926aHmoyej2cMNyZHMWnrDcHcKv08xRoFLNPms0RvxtCUkhg6Sa1lJcqvW7SvTYHzIy0SDLpiV8rgqwMvXHtyIDYOOC8cUr9BbFQJdwUjfy49mzf91Zbhm4JAWekivf6uUqJqp48_cHXDkVgDE81galo4zawNNw1zJK1r5kg7Bb1af2C2UZUrdAu4zF-dnGvNQe_Qp6AytlNg2jVMlWsMDVJVgbeqXWPr87zYLopbd_UXoWFRKu5KuRclW6GsgnX5SgA; access_token_expires_at=1623354429; refresh_token=ext.a0.t00.v1.MfD8CsB6Yuv2YvxarMRuoAlUqybErbe8crwz6e_1ZZEX37JIsDjBL15pp4ahGLv7JasY3ayLvvKmB4hPuk8kI8g; SU=pGr6KkF3t6UtsWRRg0w9juaHmCFkmiGGNIyJBGzAu4r7hsIpKyUNv6GXQ9eabGdG8RQD9kyoHhXOhAW3hchkesgAhFMKOoK-5lbjnHAKgwiOF5k1HFjlZBmuZwadum1Z; _gd1623353011761=1; sbm_a_b_test=1-control; _uetsid=14bd7b70ca0e11ebbed60def281bf8bf; _uetvid=6439cf50598111eb8b57b3883813738a; exp=A184B%7CA311C%7CA803B%7CC024A; expkey=E6003A675A636A34AE07AF56A498B086",
                    # 'Sec-GPC': '1',
                    # 'TE': 'Trailers'
                }

                r = requests.get(str("https://www.chegg.com/homework-help/follow-prob-7-39-students-measure-aerodynamic-drag-model-sub-chapter-7-problem-41p-solution-9780077295462-exc"),headers=headers, data=payload)
                soup = s(r.content, 'html.parser')

                f = open("nn2.txt", "w")
                f.write(str(soup))
                f.close
                f2 = open("./nn2.txt", "r")
                # f2.read()
                # print(f2.read())

                #############
                text = str(f2.read())
                start = text.find('''prod","token"''') + 1
                end = text.find('''userUuid''')
                cut_text2 = text[start:end].strip()
                print(cut_text2)
                vv = cut_text2.replace('''rod","token":"''', "")
                vv2 = vv.replace('''","''', "")
                print(str(vv2))
                ##################

                payload2 = json.dumps({
                    "query": {
                        "operationName": "getSolutionDetails",
                        "variables": {
                            "isbn13": z2,
                            "chapterId": z1,
                            "problemId": z3
                        }
                    },
                    "token": str(vv2)
                })
                response = requests.request("POST", url, headers=headers, data=payload2)
                print(response)
                if "problemHtml" not in str(response.text):
                    print("is can not get ans book")
                    return 'Something is wrong with the book getting resolved'
                else:
                    print("now l can get ans book")
                    # print(response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]["problemHtml"])
                    xx = response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0]["totalSteps"]
                    xx2 = response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]["problemHtml"]
                    for i in range(xx):
                        # print(response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0]['steps'][i]["html"])
                        # v="\n"+response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0]['steps'][i]["html"]
                        # print(str(v))
                        f = open('DD.html', 'a')
                        f.write("""<H3> <p style="color:RED;">""" + "Step " + str(i + 1) + " of " + str(
                            xx) + ":) </H3> </p>" + "\n" + str(
                            response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0][
                                'steps'][i]["html"]))
                        f.close()
                    # os.remove("DD.html")
                    f2 = open('DD.html', 'r')
                    f = open('Answer.html', 'w')
                    f.write(str(hh1) + """<H1> <p style="color:#2E97A6;">""" + " All Step " + str(
                        xx) + ":) </H1> </p> " + "\n" + str(xx2) + "\n" + f2.read() + str(hh2))
                    f.close()
                    os.remove("DD.html")
                    i = open('./Answer.html', 'rb')
                    # imgkit.from_file('Answer.html', 'Answer.jpg')
                    # i2 = open('./Answer.jpg', 'rb')
                    #########up file
                    url = "https://siasky.net/skynet/skyfile"

                    files = [
                        ('', ('Answer.html', open('./Answer.html', 'rb'), 'text/html'))
                    ]
                    headers7 = {
                        'referrer': 'https://siasky.net/'
                    }
                    #response = requests.request("POST", url, headers=headers7, data=payload, files=files)
                    #print(response.text)
                    if 'skylink' not in str("oooooo"):
                        return 'here is your answer :\n'
                    else:
                        #print(response.json()["skylink"])
                        #linkup = "https://siasky.net/" + response.json()["skylink"]
                        return 'here is your answer :\n' 
                    #i2 = open('./clients.json', 'rb')
                    #markdown = """✅ This is your answer 🌚\n✅ Join channel : @Chegg6\n✅ Remaining : 🔓""" + r + """🔓 """ + "\n✅ Time ⏱ : """ + str( mma) + "\n✅ Solution link: " + str(linkup) + """"""

                break




    except:
        pass

#ans url chegg H.w
#linkapi=""
def send_req(qu_url):
    try:
        print(qu_url)
        edsss=countss()
        r = requests.get(str(an()) + qu_url,data=payload)
        print(r)
        soup = s(r.content, 'html.parser')
        print(r)

        if "An expert answer will be posted here" in str(soup):
            return '⚠️ لم يتم الرد على  هذا السؤال بعد • انتظر اجابة الخبير'+"\n⚠️ This question hasn't been answered"
        else:
            x0 = soup.find('div', '</div>', class_="ugc-base question-body-text")
            x1 = soup.find('div', '</div>', class_="answer-given-body ugc-base")
            if 'None' in str(x1):
                gge=changemlls()
                return "Something went wrong, send it at another time"
            else:
                for a in x0.findAll('img'):
                    if "https:" not in a['src']:
                        print("reo https")
                        a['src'] = "https:" + a['src']
                    else:
                        print("noo")
                s1 = str(x0)
                ###################
                for a in x1.findAll('img'):
                    if "https:" not in a['src']:
                        print("reo https")
                        a['src'] = "https:" + a['src']
                    else:
                        print("noo")
                s2 = str(x1)
                ############
                f = open('Answer.html', 'w')
                messagee = str("""

                <html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">
                                        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
                                            <link rel="preconnect" href="https://fonts.gstatic.com">
                                            <link href="https://fonts.googleapis.com/css2?family=Questrial&amp;display=swap" rel="stylesheet">
                                        <link rel="stylesheet" href="style.css">
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">



                                        <style>
                                        h1 {
                                            font-family: 'Questrial', sans-serif;
                                                }

                                        p {
                                    font-family: 'Questrial', sans-serif;
                                            }

                                        td {
                                    font-family: 'Questrial', sans-serif;
                                            }  


                                        .content {
                                            width: 100%;
                                        margin: auto;
                                        background: white;
                                        padding: 10px;
                                            }


                                        img{
                                        max-width: 100%;
                                            }
                                            body {background-color: LightGray;
                                                overflow: scroll;}
                                        h1   {color: red;}

                                            </style>

                                            </head><body><div class="container"><div class="alert alert-danger alert-dismissible" role="alert">
                                            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
                                            <center><strong> <p><a href="https://t.me/eng2080">For All Answers Join channel : @eng2080</a></p></strong> 
                                            </center></div><div class="content" "=""><h1></h1><h1><font size="6"><strong>Q:</strong></font></h1><p></p><div id="mobile-question-style" style="font-family: Roboto; color:#333333; "><p dir="ltr"> """ + str(
                    s1) + """</p>
                </div><p dir="ltr">&nbsp; </p>
                <p></p><hr><h1><font size="6"><strong>A:</strong></font></h1><p></p><p> """ + str(s2) + """ </p><p></p> </div> </div></body></html>










                """)
                f.write(messagee)
                f.close()
                url = "https://siasky.net/skynet/skyfile"
                files = [
                    ('', ('Answer.html', open('./Answer.html', 'rb'), 'text/html'))
                ]
                headers7 = {
                    'referrer': 'https://siasky.net/'
                }
                #response = requests.request("POST", url, headers=headers7, data=payload, files=files)
                #print(response.text)
                if 'skylink' not in str(messagee):
                    return 'here is your answer :\n'
                else:
                    #print(response.json()["skylink"])
                    #linkup = "https://siasky.net/" + response.json()["skylink"]
                    return 'here is your answer :\n'
    except:
        pass


def editMessage(text, chat_id, text_id , inline_keyboard):
    try:
        url = URL + "editMessageText?chat_id={}&message_id={}&parse_mode=&text={} &reply_markup=".format(chat_id,text_id, text) + inline_keyboard
        r = get_url(url)
        return r
    except:
        pass

def deleteMessage(chat_id, message_id):
    try:
        url = URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
        get_url(url)
    except:
        pass

def send_message(text, chat_id, text_id = None,inline_keyboard=None,parse_mode=None):
    try:
        data = {
            'text':text,
            'chat_id':chat_id,
            'reply_to_message_id':text_id,
            'reply_markup':inline_keyboard,
            'disable_web_page_preview':True,
            'parse_mode': parse_mode
        }
        r = post_url(URL + "sendMessage",data)
        return r
    except Exception as e:
        print(e)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        # print(updates)
        try:
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                for i in updates['result']:
                    Check(i)
        except:
            try:
                print(updates['description'])
            except:
                pass




if __name__ == '__main__':
    main()
