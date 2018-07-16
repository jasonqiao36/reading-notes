# 目录与路径
## 目录相关命令
- `mkdir`
```
mkdir -p :创建多级目录
mkdir -m :指定权限
```

可执行文件路径的变量PATH
- 查看：`echo $PATH`
- 增加：`PATH="${PATH}:/new_path`

## 文件与目录管理
- 查看：ls
- 复制：cp
```
参数：
-i ：若目标文件已经存在时，在覆盖时会先询问动作的进行
-a ：相当于 -dr --preserve=all 的意思，至于 dr 请参考下列说明
-p ：连同文件的属性（ 权限、用户、时间） 一起复制过去，而非使用默认属性（ 备份常用）
-u ：destination 比 source 旧才更新 destination，或 destination 不存在的情况下才复制
-r ：递回持续复制，用于目录的复制行为；（ 常用）
```
- 移动：mv
- 删除：rm（小心！。-i 进入交互模式）

- 获取文件名：basename path
- 获取目录名：dirname path
- 修改文件时间或创建文件：touch 
```
mtime: 文件内容变更时更新。 ls -l 默认
ctime: 状态变更（权限、属性）时更新。--time=ctime
atime: 内容被取用时（cat）更新。--time=atime
touch file 修改时间为当前。创建文件 。
```

## 默认权限与隐藏权限
文件默认权限：umask
```
umask 查看（一般用户为0002）
umask -S 查看符号类型
如何计算？
文件：-rw-rw-rw- 减去 002 = -rw-rw-r-- 
目录：drwxrwxrwx 减去 002 = drwxrwxr-x
```
隐藏权限: chattr
```
chattr +i filename 

i ：文件“不能被删除、改名、设置链接也无法写入或新增数据！”只有 root 能设置此属性
a ：文件将只能增加数据，而不能删除也不能修改数据，只有root 才能设置这属性
```

## 指令与文件搜寻
- 寻找可执行文件： which
- 查找文件名
```
whereis: 快，只查找特定目录
whereis filename
whereis -l :列出查询的目录

locate: 快，查找位置多。要更新db
-i ：忽略大小写的差异；
-r ：后面可接正则表达式的显示方式
updatedb： 更新db
```
