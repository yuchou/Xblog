# xblog
##创建Postgresql数据库
```bash
$ su - postgres
$ psql
$ \l
$ create database blog owner postgres;
```
##测试数据库连接
```bash
(.venv) D:\work\github\xblog>python manage.py shell
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)
] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.db import connection
>>> cursor = connection.cursor
```