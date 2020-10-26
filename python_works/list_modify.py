#addition,deletion,modification
Guest=['gaby','paula','lucy','mayira','allyn']
print("Hello "+Guest[0]+", you are invited for dia del muertos dinner")
print("Hello "+Guest[1]+", you are invited for dia del muertos dinner")
print("beacuse of travel restrictions paula cannot make it")
Guest[1]='viri'
print("new list: "+str(Guest))
del Guest[1] # Is used only when you don't want to use the deleted item 
print(Guest)
print("sorry, i cannot invite "+Guest.pop())
print(Guest)
Guest.pop(1)
print(Guest)
Guest.remove('mayira') #remove is used by value 
print(Guest)
print("but you have more chairs")
Guest.append('veda')
Guest.insert(0,'roopa')
Guest.insert(2,'priyanka')
print(Guest)
print("Hello "+Guest[0].title()+", you are invited for dia del muertos dinner")
print("Hello "+Guest[2].upper()+", you are invited for dia del muertos dinner")