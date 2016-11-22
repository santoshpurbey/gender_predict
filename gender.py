''' this is gender prediction for nepali names only'''
male_name = ['hari','ramu' ]
common_name = ['suman', 'sonu', 'komal', 'laxmi']
female_name = ['i', 'u', 'a',
               'ti','ka','ma','na','nu','ta','ti', 'tu', 'sa','ya',
               'sha',
               'ree',]


def main():
    name = raw_input('Enter your name:')
    result = isfemale(name)
    if result:
        print 'Female'
    elif result=='common name!':
        print 'common name!'
    else:
        print 'Male'
    
def isfemale(name):
    if (name in male_name):
                return False
    elif (name in common_name):
                return 'common name!'
    else:
        for l in female_name:
            if name.endswith(l):
                return True
                break
        else:
            return False
    
if __name__=='__main__':
    while True:
        main()
        
    

        
    
