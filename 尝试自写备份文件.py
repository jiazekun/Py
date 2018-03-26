import os
import time
source=['D:\\一加手机相册\知乎','D:\\Code']
target_dir='D:\\Backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today=target_dir+os.sep+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')
comment=input('Enter your comment--?>')
if len(comment)==0:
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+'_'+\
    comment.replace(' ','_')+'.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('成功创建文件',today)
zip_command="zip -r {0} {1}".format(target,' '.join(source))
print('zip_command is')
print(zip_command)
print('running')
if os.system(zip_command)==0:
    print('备份成功')
else:
    print('备份失败！')
    
    
    
    
