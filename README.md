# 重要更新：
## 由于之前的方法需要开启开发者模式 比较麻烦现在对代码进行更新，使用更方便

## 安装PikPak下载列表管理工具(之前安装过的请更新):   
https://deta.space/discovery/@pikpak/pikpak

## deta.space后台获取两个信息：
- 安装后的网址：添加secrets:DETA_PROJECT_URL
- 在项目设置的Keys里添加APP KEY（第二个）:添加secrets:DETA_APP_KEY
完成设置  运行Actions:PikPak转存Aliyun APP KEY  
   
## 添加secrets：ALIYUN_REFRESH_TOKEN: 阿里云刷新token    
获取方法:https://github.com/messense/aliyundrive-webdav    

That's ALL   
***  
***




# Tip：注册deta.space的时候要开启才可以使用api_key 开启方法看这里https://deta.space/docs/en/build/space-kit
# pikpak2aliyun
转存PikPak到阿里云盘   
视频演示:https://youtu.be/6ll5GhxFcWs   

# 在阿里云备份盘建立要上传到的文件夹   
默认是PikPak,加密文件夹为PikPak-encrypt 【注意区分大小写】  
# PikPak下载列表管理工具:   
https://deta.space/discovery/@pikpak/pikpak

# 所需secrets:   
ALIYUN_REFRESH_TOKEN: 阿里云刷新token,获取方法:https://github.com/messense/aliyundrive-webdav      
DETA_PROJECT_ID: deta.space的项目ID,用来指定项目的数据库,获取方法:视频中      
DETA_API_KEY: 访问deta.space数据库的token,获取方法:视频中      
ALIST_ENCRYPT_PASSWORD: 文件的加密密码   


## 删除旧的workflow需要修改actions权限
```
Settings > Actions > General > Workflow permissions
把Read repository contents permission 改成 Read and write permissions
```


### github actions的linux主机在加密文件时有些会加密失败，可以换成macos主机可以避免
### 20230813加入文件混淆后缀，解密不影响使用
