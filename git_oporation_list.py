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
$ git remote rm origin (删除本地git/config中注册的远程库）

添加远程库
$ git remote add origin https://github.com/pp107/my-repository.git  (与远程库建立链接）
$ git push -u origin master (把本地推送至远程，第一次使用加”-u“建立关联）
$ git push origin master (以后直接推送）


SSH keys认证
$ ssh-keygen -t rsa -C "email/username"  #依据邮箱或用户名生成SSH KEYGEN，保存路径可重选。
$ clip < ~/.ssh/id_sra.pub  #剪切id_rsa.pub内容并复制到github.com->setting ->SSH and GPG keys中
'''
#在GNU-SHELL界面与远程库建立SSH通信前，需启动ssh-agent服务/进程，并将本地SSH私钥添加到SSH_AGENT
'''
$ eval $(ssh-agent -s)
$ ssh-add~/.ssh/id_rsa

'''  '''
克隆远程库
$ git clone https://github.com/pp107/my-repository.git （克隆master分支）

分支操作
$ git branch  （列出本地分支）
$ git branch -r (列出远程分支）
$ git branch -a (列出本地分支和远程分支）
$ git clone -b masterTest <版本库的网址>  （克隆masterTest分支）

'''
