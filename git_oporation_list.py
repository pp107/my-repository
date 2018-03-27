'''
Home repository

版本查询
$ git log

版本回退
$ git reset --hard commit id(前几位即可）

既往log查询（后悔药）
$ git reflog

回撤到最后一次修改前(用版本库里的版本替换工作区版本）
$ git checkout <file>

删除文件
$ rm <file> #仅工作区删除（本地删除）
$ git rm <file> #版本库删除（本地+工作区）
$ git commit -m "注释“（更新版本库）

添加远程库
$ git remote add origin git@github.com:pp107/my-repository.git  (与远程库建立链接）
$ git push -u origin master (把本地推送至远程，第一次使用加”-u“建立关联）
$ git push origin master (以后直接推送）

SSH keys认证
$ ssh-keygen -t rsa -C "email"

id_rsa.pub 内容复制到setting ->SSH and GPG keys中

'''
