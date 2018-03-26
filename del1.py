#!/usr/bin/env python  
#coding: utf-8  
# Filename : address_book.py  
import cPickle as p  
import os  
import sys  
filename='addressbook.data'  
class member:  
          def __init__(self,name,address,tel):  
              self.name=name  
              self.address=address  
              self.tel=tel  
    def update():  
        s=raw_input('Please input similar to jack,jack@ict.ac.cn,13543454567 >>')  
        s1=s.split(',')  
        pp=member(s1[0],s1[1],s1[2])  
        f=file(filename)  
        conlist=p.load(f)  
        conlist[pp.name]=pp.address+','+pp.tel  
        f=file(filename,'w')  
        p.dump(conlist,f)  
        f.close()  
        del conlist  
      
        #print again  
        f=file(filename)  
        conlist=p.load(f)  
        print conlist  
      
    def delete():  
        f=file(filename)  
        conlist=p.load(f)  
        print conlist  
        d=raw_input("Please input the person's name you want to delete>>")  
        del conlist[d]  
        print conlist  
        f=file(filename,'w')  
        p.dump(conlist,f)  
        f.close()  
        del conlist  
      
    def select():  
        f=file(filename)  
        conlist=p.load(f)  
        print conlist  
        s=raw_input('Please enter the name which you want to select>>')  
        print s,':',conlist[s]  
      
    def main():  
        while True:  
              meu=raw_input(''''' 
                     1.查询 
                     2.添加/修改 
                     3.删除 
                     x.退出 
                     ------>''')  
              if   meu=='1':  
                 select()  
              elif meu=='2':  
                 update()  
              elif meu=='3':  
                 delete()  
              elif meu=='x':  
                 sys.exit()  
              else:  
                 print "Don't have this option,please try again!"  
      
    if os.path.exists('addressbook.data'):  
          main()  
    else:  
          f=file('addressbook.data','w')  
          conlist={'jack':'jack@ict.ac.cn,13645654345'}  
          p.dump(conlist,f)  
          f.close()  
          del conlist  
          main()  