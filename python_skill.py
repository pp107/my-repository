#git_hub repository建库命令：(在git bash 界面输入以下命令）
'''git config --global user.name "pp107"
   git config --global user.email name@163.com
   git initial #在当前路径建库（空库）
   git add <file> #将file文件添加到仓库
   git commit -m "注释"  #把文件提交到仓库
   
   ####以下为建立空文件夹库命令#####
   $mkdir learngit
   $cd learngit
   $pwd  #显示当前路径命令
   回显>/xx/xx/learngit
'''


# 安装命令：（在PIP目录下，或已将PIP加入系统环境变量）
'''Pip install XXX'''
# 升级:
'''Python -m pip install --upgrade XXX'''

# .py运行方式：
'''1.python xxx.py
   2.Python -m xxx.py
   1直接运行（与sys.path在同一目录）
   2相当于import，当作模块来启动（与sys.path不在同一目录时使用）
'''
#windows当前目录下建虚拟环境命令
'''
python -m venv ll_env
#激活虚拟环境命令
ll_env\Script\activate
'''
