import sys
import os
import argparse
import json
import requests

parser = argparse.ArgumentParser(description='下载任务管理')
parser.add_argument("--act", help="操作类型：download,del", default="download")
parser.add_argument("--projet", help="deta.space的网址", default="")
parser.add_argument("--appkey", help="deta.space的X-Space-App-Key", default="")
parser.add_argument("--taskkey", help="要删除的任务key", default="")

args = parser.parse_args()


DETA_APPKEY=args.appkey
DETA_PROJECT_ID=args.projet

API_URL=f"{DETA_PROJECT_ID}/downloads"

deta_headers = {
    'X-Space-App-Key':DETA_APPKEY,
    'Content-Type':'application/json'
}

if args.act=="del":
    payload = json.dumps({"action":"delete","data":args.taskkey})
    requests.post(API_URL,headers=deta_headers,data=payload,verify=False)
    quit()


if args.act=="download":
    payload = json.dumps({"action": "query"})
    tasks_req = requests.post(API_URL,headers=deta_headers,data=payload,verify=False)
    tasks=json.loads(tasks_req.text)
    if len(tasks) < 1:
        quit()
    task=tasks[0]
    urlinfo = task['url'].split("##");
    streamurl = urlinfo[0]
    # 更新下载状态
    putpayload = json.dumps({"action": "update","data":task['key']})
    put_req = requests.post(API_URL,headers=deta_headers,data=putpayload,verify=False)
    cmd = "aria2c --conf aria2.conf --seed-time=0 -o "+urlinfo[1]+" -d downloads -c \""+streamurl+"\""
    os.system(cmd)
    #os.system('cls' if os.name == 'nt' else 'clear')
    #print(f'::set-output name=taskkey::{task["key"]}')
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'taskkey={task["key"]}', file=fh)
    quit()

