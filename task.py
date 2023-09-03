import sys
import os
import argparse
import json
import requests

parser = argparse.ArgumentParser(description='下载任务管理')
parser.add_argument("--act", help="操作类型：download,del", default="download")
parser.add_argument("--projet", help="deta.space的project_id", default="")
parser.add_argument("--apikey", help="deta.space的x_api_key", default="")
parser.add_argument("--taskkey", help="要删除的任务key", default="")

args = parser.parse_args()


DETA_DATAKEY=args.apikey
DETA_PROJECT_ID=args.projet

QUERY_URL=f"https://database.deta.sh/v1/{DETA_PROJECT_ID}/pikpak_task/query"
DELETE_URL=f"https://database.deta.sh/v1/{DETA_PROJECT_ID}/pikpak_task/items/{args.taskkey}"
UPDATE_URL=f"https://database.deta.sh/v1/{DETA_PROJECT_ID}/pikpak_task/items/"

deta_headers = {
    'X-API-Key':DETA_DATAKEY,
    'Content-Type':'application/json'
}

if args.act=="del":
    requests.delete(DELETE_URL,headers=deta_headers,verify=False)
    quit()


if args.act=="download":
    payload = json.dumps({
      "query": [{"isnow": 1}],
      "limit": 1
    })
    tasks_req = requests.post(QUERY_URL,headers=deta_headers,data=payload,verify=False)
    tasks=json.loads(tasks_req.text)
    if len(tasks['items']) < 1:
        quit()
    task=tasks['items'][0]
    urlinfo = task['url'].split("##");
    streamurl = urlinfo[0]
    cmd = "aria2c --conf aria2.conf --seed-time=0 -o "+urlinfo[1]+" -d downloads -c \""+streamurl+"\""
    os.system(cmd)
    # 更新下载状态
    putpayload = json.dumps({
      "set" : {
            "isnow": 10,
        }
    })
    testupdateurl=UPDATE_URL+task["key"]
    put_req = requests.patch(UPDATE_URL+task["key"],headers=deta_headers,data=putpayload,verify=False)
    #os.system('cls' if os.name == 'nt' else 'clear')
    #print(f'::set-output name=taskkey::{task["key"]}')
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'taskkey={task["key"]}', file=fh)
    quit()


