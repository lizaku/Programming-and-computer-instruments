import os
def main():
    num = int(input('Введите число: '))    
    for i in range(num):        
        dirname = str(i+1)        
        if not os.path.exists(dirname):            
            os.mkdir(dirname)            
            t = 'file{}.txt'            
            for fnum in range(1, i+1):                
                fname = os.path.join(dirname, t.format(fnum))                
                with open(fname, 'w', encoding='utf-8') as f:                    
                    f.write('..')
main()
