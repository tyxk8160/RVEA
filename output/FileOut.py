#/usr/bin/python

class FileOut(object):
    def __init__(self,filepath,key = 'cv0'):
        self.fp = open(filepath,'w')
        self.key = key
    def display(self,pop,*arg,**karg):
        '''
        save
        '''
        self.fp.write(str([pop_tmp[self.key] for pop_tmp in pop]))
        self.fp.write('\r\n')
        self.fp.write('='*80)
        self.fp.write('\r\n')
    def close(self):
        self.fp.close()
        
