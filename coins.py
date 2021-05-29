import amino, json, os

client = amino.Client()
x = 0

try:
    with open("/storage/emulated/0/adro_gantiam/accounts/emails.txt") as json_file:
        emails = json.load(json_file)
except:
    print("Error")
    exit()

print(len(emails))

os.system("cd /storage/emulated/0/adro_gantiam/ && mkdir 'coins'")

try:
    try: id = open("/storage/emulated/0/adro_gantiam/coins/id.txt", "r").read()
    except:
        try:
            id = client.get_from_code(input("Link on your blog: ")).objectId
            open("/storage/emulated/0/adro_gantiam/coins/id.txt", "w").write(id)
        except: print("Error")

    print(id) 

    while int(len(emails)/30) >= x + 1:
        try:   
            if len(emails) >= 0:
                try:
                    open("/storage/emulated/0/adro_gantiam/coins/" + str(x)) 
                except:
                    os.system("cd /storage/emulated/0/adro_gantiam/coins && mkdir " + str(x))
                    open("/storage/emulated/0/adro_gantiam/coins/" + str(x) + "/py.py", "w").write("import amino, json\namino.lib.util.helpers.generate_device_info()\nwith open('/storage/emulated/0/adro_gantiam/accounts/emails.txt') as json_file:\n        emails = json.load(json_file)\nid = open('/storage/emulated/0/adro_gantiam/coins/id.txt', 'r').read()\nclient = amino.Client()\ndef collect(data):\n    x = " + str(x * 30) + "\n    while True:\n        client.login(data[x]['email'], data[x]['password'])\n        client.join_community('188117165', None)\n        sub_client = amino.SubClient('188117165', profile = client.profile)\n        send = 1\n        sub_client.lottery()\n        while send == 1:\n            try:\n                sub_client.send_coins(int(client.get_wallet_info().totalCoins), id)\n                print('+')\n            except:\n                send = 0\n        x += 1\n        print(x)\ndata = []\ncollect(emails)")
                x += 1
        except:
            pass
    if int(len(emails)/30) <= x + 1:
        print("Мало аккаунтов")
except:
    os.system("cd /storage/emulated/0/adro_gantiam/ && mkdir 'coins'")
    os.system("python coins.py")
