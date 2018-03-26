import os
import time
source=['"D:\刘俊的承诺.aac"','D:\\Code']
target_dir='D:\\Backup'

target=target_dir+os.sep+\
        time.strftime('%Y%m%d%H%M%S')+'.zip'
        
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    
zip_command='zip -r {0} {1}'.format(target,
                                    ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')