
# mysql 操作


```python
#查看库
SHOW database;
#使用哪一个库
USE Database;
#删除数据库
DROP database;
#查看表
show tables;
#创建数据库
CREATE DATABASE a CHARACTER SET utf8 COLLATE utf_general_ci;
```

### mysql数据引擎


```python
#存储引擎以插件的形式被MYSQL数据库引入
#查看数据库引擎
SHOW ENGINES;(SHOW ENGINES \G)
#查询支持的存储引擎
SHOW VARIABLES LIKE 'have%';
#查看默认的存储引擎
SHOW VARIABLES LIKE 'storage_engine%';
```

* 三种存储引擎：
* MyISAM 不支持事务安全，没有数据缓存，不支持外键，表锁机制，访问速度快
* InnoDB 不支持数据压缩，行锁机制,占磁盘空间比较大，对事物完整性要求高
* MEMORY 不支持外键，表锁机制，适合数据少，快速访问


```python
#数据表导出 txt格式
select * from 表 INTO OUTFILE 'secure_file_priv/filename';
#secure_file_priv 设置在/etc/my.cnfz里面设置，设置完重启mysql.server
#新建的数据库一般包含几个表：
imformation_schema:主要储存数据库信息
performance_schema:主要储存数据库服务器性能参数
MySQL：主要储存用户权限信息
test:自动创建的测试数据库
```


```python
# mysql 中所有的sql语句中的DDL和DML(不包含select)执行后都会显示“Query OK”
# create table table_name( 属性名 数据类型（长度），。。。);
# 查看表结构
DESCRIBE table-name;
# 查看表的详细信息 ,结尾可以用 ； \g  \G表示，但是方彪用户看，用\G好一点
SHOW CREATE TABLE table-name;
# 修改表名字
ALTER TABLE old-name RENAME new-name;
# 检验数据表是否存在
DESC table-name;
# 在表中最后增加一个字段
ALTER TABLE table-name ADD 属性名 类型（长度）；
# 在表最开始增加一个字段
ALTER TABLE table-name ADD 属性名 类型（长度） FIRST；
# 在表指定字段之后增加字段
ALTER TABLE table-name ADD 属性名 类型（长度） AFTER 属性名；
# 在表删除某个字段
ALTER TABLE table-name Drop 属性名；
# 在表修改字段数据类型
ALTER TABLE table-name MODIFY 属性名 类型（长度）；
# 在表修改字段名字
ALTER TABLE table-name CHANGE 旧属性名 新属性名 旧数据类型（长度）；
```

## 操作表的约束
* NOT NULL 不为空
* DEFAULT 默认值
* UK 约束字段为唯一值
* PK 主键
* AUTO_INCREMENT 自增
* FK 外键


```python
# 创建表
CREATE TABLE a(
    b int NOT NULL,
    c VARCHAR(20) DEFAULT '-',
    #单主键
    id int PRIMARY KEY AUTO_INCREMENT,
    #多字段主键
    #CONSTRAINT 约束名 PRIMARY KEY(属性名1，属性名2，。。。),
    #外键
    CONSTRAINT 约束名 FOREIGN KEY(属性名3) REFERENCES 数据库（表3）
);
```

## 数据库的索引

### 索引可以分为B型树 和  哈希索引
* 存储引擎 InnoDB和MyISAM存储引擎支持BTREE类型索引，MEMORY支持HASH类型索引。
* mysql支持6种索引
    * 普通索引
    * 唯一索引
    * 全文索引
    * 单列索引
    * 多列索引
    * 空间索引
* 一般创建索引的情况
    * 经常被查询的字段，在Where中出现的字段
    * 在分组的字段，groupBY中出现的字段
    * 存在关联的子父联表查询，主键或者外键
* 一般不适合创建索引的情况
    * 在查询中很少被使用的字段
    * 拥有很多重复字段


```python
#创建表创建索引
CREATE TABLE table_name(
  属性名 数据类型，
    #demo INDEX suoyin(id) ASC正序，DESC倒倒序
  INDEX|KEY [索引名] （属性名 【长度】 【ASC|DESC】）
);

#在已有的表上创建索引
CREATE INDEX 索引名 ON 表名（属性名【长度】【ASC|DESC】）

#通过sql语句ALERT TABLE 创建普通索引
ALERT TABLE table_name ADD INDEX|KEY 索引名（属性名【长度】【asc|DESC】）

#创建表创建唯一索引
UNION INDEX|KEY [索引名]（属性名【长度】【ASC|DESC】）

#检验索引是否被使用，我们这边使用
EXPLAIN SELECT * FROM table WHERE indexname='' \G
```

## 创建视图


```python
#step1:创建视图
create view view_name AS 查询语句 ;
#step2:查看视图
SELECT * FROM view_name;

# 查看视图
SHOW TABLES STATUS 【from db_name】【like 'pattern'】

# 删除视图
DROP VIEW view_name 【view-name】
```

## 触发器


```python
#触发语句
DELETE \ INSERT \UPDATE

#创建一个触发
create trigger trigger_name#触发器名字
    BEFORE|AFTER trigger_event#（DELETE,INSERT,UPDATE）
        ON TABLE_NAME FOR EACH ROW trigger_STMT#（触发后执行的语句）;
        
#创建多个触发
create trigger trigger_name#触发器名字
    BEFORE|AFTER trigger_event#（DELETE,INSERT,UPDATE）
        ON TABLE_NAME FOR EACH ROW 
            BEGIN
            trigger_STMT,
            ...#（触发后执行的语句）;
            END
            
#查看触发器
SHOW TRIGGERS \G


```

## 查询


```python
# 避免重复DISTINCT
SELECT DISTINCT ....FROM table_name

#连接结果
SELECT CONCAT(a,b,c) AS sometab FROM table

#查询匹配
_ 通配符，能匹配单个字符
% 通配符，可以匹配任意长度的字符串
```

## 多表数据查询
