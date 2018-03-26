import sys
import time
f=None
try:
    f=open('poem.txt')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line,end='')
        sys.stdout.flush()
        print('Press ctrl+c now')
        time.sleep(2)
except IOError:
    print('could not find file ')
except KeyboardInterrupt:
    print('You cancelled the reading from the file')
finally:
    if f:
        f.close()
    print('(cleaning up:Closed the file)')