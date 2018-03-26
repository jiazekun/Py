import os
import time

source=['D:\Py','D:\\Code']
target_dir='D:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today=target_dir+os.sep+time.strftime(\
                                  '%Y%m%d')
now=time.strftime('%H%M%S')
#添加一条来自是用户的注释以创建
#zip文件的文件名
comment=input('Enter a comment -->')
if len(comment)==0:
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+ '_' + \
        comment.replace(' ', '_')+'.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)
#使用zip命令将文件打包成zip格式
zip_command="zip -r {0} {1}".format(target
                                    ,' '.join(source))
                                    
print('zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command)==0:
    print('Successfully backup to',target)
else:
    print('Backup FAILED')