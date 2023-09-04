# pikpak2aliyun
转存PikPak到阿里云盘   
视频演示:https://youtu.be/6ll5GhxFcWs   

# 在阿里云备份盘建立要上传到的文件夹   
默认是PikPak,加密文件夹为PikPak-encrypt  
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
