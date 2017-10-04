dict1 = {'Name': 'Cathy', 'Age': 22, 'Country': 'USA', 'FavLang': 'java'}

def printDic(bio):
    # 
    # for data in bio:
    #  print data
    for key,data in bio.iteritems():
     print "My {} is {}".format(key, data)


printDic(dict1)

# #to print all keys
# for data in capitals:
#      print data
# #another way to print all keys
# for key in capitals.iterkeys():
#      print key
# #to print the values
# for val in capitals.itervalues():
#      print val
# #to print all keys and values
# for key,data in capitals.iteritems():
#      print key, " = ", data