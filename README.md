# pikpak2aliyun
转存PikPak到阿里云盘

# 所需secrets:   
ALIYUN_REFRESH_TOKEN: 阿里云刷新token,获取方法:https://github.com/messense/aliyundrive-webdav
DETA_PROJECT_ID: deta.space的项目ID,用来指定项目的数据库,获取方法:稍后更新   
DETA_API_KEY: 访问deta.space数据库的token,获取方法:稍后更新   
ALIST_ENCRYPT_PASSWORD: 文件的加密密码   



## 删除旧的workflow需要修改actions权限
```
Settings > Actions > General > Workflow permissions
把Read repository contents permission 改成 Read and write permissions
```
