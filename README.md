# vulunerabillty check tools.

### requirements
```
# pip install xmltodict
```


```
$ docker pull centos:centos7
$ docker run --privileged -v /Users/ytsukada/Y/develop/Vulnera:/var/www/develop -p 8080:80 -p 8443:443  -p 13306:3306 -it -d --name centos7 centos:centos7 /sbin/init
```

```
$ pip install lambda-uploader
$ pip install python-lambda-local
```