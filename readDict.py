dict1 = {'Name': 'Cathy', 'Age': 22, 'Country': 'USA', 'FavLang': 'java'}

def printDic(bio):
    # 
    # for data in bio:
    #  print data
    for key,data in bio.iteritems():
     print "My {} is {}".format(key, data)


printDic(dict1)