[TOC]

## 在阿里云部署Flask环境

#### 参考文档

+ [通过Gunicorn部署flask应用（阿里云服务器：Ubuntu 16.04）](<https://juejin.im/post/5a5a1408518825733060e232#heading-6>)

#### 注意事项

+ ```python
   app.run(host='0.0.0.0',port=5000)   # 设置外部访问限制，本例表示所有ip均可访问，端口为5000
  ```

+ 导出的`requirements.txt` 

  + 导出方法 `pip freeze > requirements.txt` 
  + 安装方法 `pip install -r requirement.txt`

  ```python
  alembic==1.0.9
  Babel==2.6.0
  blinker==1.4
  Click==7.0
  coverage==4.5.3
  decorator==4.4.0
  defusedxml==0.6.0
  dominate==2.3.5
  Flask==1.0.2
  Flask-Babel==0.12.2
  Flask-Bootstrap==3.3.7.1
  Flask-Login==0.4.1
  Flask-Mail==0.9.1
  Flask-Migrate==2.4.0
  Flask-OpenID==1.2.5
  Flask-SQLAlchemy==2.3.2
  Flask-WhooshAlchemy==0.56
  Flask-WTF==0.14.2
  flipflop==1.0
  guess-language==0.2
  itsdangerous==1.1.0
  Jinja2==2.10.1
  Mako==1.0.9
  MarkupSafe==1.1.1
  pbr==5.1.3
  python-dateutil==2.8.0
  python-editor==1.0.4
  python3-openid==3.1.0
  pytz==2019.1
  six==1.12.0
  SQLAlchemy==1.3.3
  sqlalchemy-migrate==0.12.0
  sqlparse==0.3.0
  Tempita==0.5.2
  visitor==0.1.3
  Werkzeug==0.15.2
  Whoosh==2.7.4
  WTForms==2.2.1
  ```

+ `gunicorn` 设置启动参数 部署到服务器上时 **'127.0.0.1' 改为你的服务器的私有IP**，**并在服务器上设置相关端口（如5000）的安全组  test改为项目运行入口 如run** 

  ```
  gunicorn -w 4 -b 172.19.172.207:5000 run:app
  ```

+ 安装和配置Nginx

  ```
  # file_name=default
  server {
      listen 80;
      server_name example.org; # 这是HOST机器的外部域名，用地址也行
  
      location / {
          proxy_pass http://your.私有IP:5000; # 指向 gunicorn host 的服务地址，注意，这里填我们服务器的私有IP
          proxy_set_header Host $host;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      }
    }
  ```

用xshell将项目的文件传到服务器上（不用传在本地建的虚拟环境中使用的包）

至此，理论上在浏览器中输入公有的ip地址，就可以访问项目

+ 有关`gunicorn`的相关操作

  + ```shell
    pkill gunicorn  //关闭gunicorn
    ```

  + ```shell
    pstree -ap|grep gunicorn
    ```



## 阿里云配置MongoDB

#### 参考文档

+ [[Linux下MongoDB安装和配置详解](https://www.cnblogs.com/pfnie/articles/6759105.html)](<https://www.cnblogs.com/pfnie/articles/6759105.html>)

#### 注意事项

+ 先开启服务器Mongod，在使用Mongo操作数据库

  ```shell
  #必须在mongod的目录下
  ./mongod --config /usr/local/mongoDB/mongodbserver/etc/mongodb.conf
  #如果已经添加到了系统路径，可以直接
  mongod --config /usr/local/mongoDB/mongodbserver/etc/mongodb.conf
  ```

+ 错误`./mongod: error while loading shared libraries: libcurl.so.4: cannot open shared object file: No such file or directory`

  解决办法：`apt-get install libcurl4-openssl-dev`
  
+ 将mongod路径添加到系统路径中，方便随处执行mongod命令

  ```shell
  export PATH=$PATH:/usr/local/mongoDB/mongodbserver/bin
  source /etc/profil  使系统环境变量立即生效
  ```



## 上传MongoDB数据到服务器

#### 参考资料

+ [MongoDB日常运维操作命令小结](https://www.cnblogs.com/kevingrace/p/8184087.html)

  

## 存在的问题

1. MongoDB没有添加访问权限

2. MongoDB没有开机自启

3. 配置原理不熟悉

   

## 相关参考资料

1. [新手的Flask+uwsgi+Nginx+Ubuntu部署过程 - 简书](https://www.jianshu.com/p/5b73444eb47d?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)
2. [阿里云部署Flask+WSGI+Nginx 详解 - 简书](https://www.jianshu.com/p/9293cc21a571)
3. [Linux如何查看进程、杀死进程、启动进程等常用命令 - wojiaopanpan - CSDN博客](https://blog.csdn.net/wojiaopanpan/article/details/7286430)
4. [MongoDB日常运维操作命令小结 - 散尽浮华 - 博客园](https://www.cnblogs.com/kevingrace/p/8184087.html)
5. [Linux下MongoDB安装和配置详解 - pfnie - 博客园](https://www.cnblogs.com/pfnie/articles/6759105.html)
6. [Ubuntu 16.04 mongodb enterprise 3.4 安装中遇到的错误 - 简书](https://www.jianshu.com/p/00bd136b4165)
7. [通过Gunicorn部署flask应用（阿里云服务器：Ubuntu 16.04） - 掘金](https://juejin.im/post/5a5a1408518825733060e232)



![sojson.com](.\sojson.com.png)