create database if not exists login;
use login;

-- 创建用户表
drop table user;
create table if not exists user(
    id int auto_increment,
    name varchar(120),
    age int(120),
    primary key(id)
);