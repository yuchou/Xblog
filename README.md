# xblog
## 创建Postgresql数据库
```bash
$ su - postgres
$ psql
$ \l
$ create user blog with password 'test123456';
CREATE ROLE
$ create database blog owner blog;
CREATE DATABASE
$ grant all privileges on database blog to blog;
GRANT
```
## 测试数据库连接
```bash
$ netstat -antp | grep 5432
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      6975/postmaster     
tcp6       0      0 ::1:5432                :::*                    LISTEN      6975/postmaster 

$ vi /var/lib/pgsql/9.6/data/postgresql.conf
#------------------------------------------------------------------------------
# CONNECTIONS AND AUTHENTICATION
#------------------------------------------------------------------------------

# - Connection Settings -

listen_addresses = '*'			# what IP address(es) to listen on;

$ vi /var/lib/pgsql/9.6/data/pg_hba.conf
# IPv4 local connections:
host    all             all             0.0.0.0/0            md5
# IPv6 local connections:
host    all             all             ::/0                 	md5
$
$ netstat -antp | grep 5432
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      7427/postmaster     
tcp6       0      0 :::5432                 :::*                    LISTEN      7427/postmaster
$ psql -U blog -d blog -h 127.0.0.1 -p 5432
$ psql -U blog -d blog -h 10.10.68.100 -p 5432
```