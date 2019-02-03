import json
import base64
import requests
import subprocess

process = subprocess.Popen(['php', 'app.php'], stdout=subprocess.PIPE)
out, _ = process.communicate()
data = json.loads(out.decode(), encoding='utf-8')

for player in data['players']['sample']:
    print(player)
    url = f"https://api.mojang.com/users/profiles/minecraft/{player['name']}"
    result = requests.get(url).text.strip()
    if result:
        uuid = json.loads(result)['id']
        url = f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
        result = requests.get(url).text.strip()
        profile = json.loads(result)['properties'][0]['value']
        profile = json.loads(base64.b64decode(profile).decode())
        print(profile['textures']['SKIN']['url'])
