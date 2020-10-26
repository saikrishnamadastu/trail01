# Organizing a list involves sorting techniques
Anime=['one piece','naruto','death note','bakuman','boruto','unlucky & undead']
print(Anime)
# to temporarily sort a list use sorted function
print("here is the sorted List: ")
print(sorted(Anime))
print("here is the original List:")
print(Anime)
print("the reverse of the List:")
Anime.reverse() # it simply reverses the order from the original 
print(Anime)
Anime.reverse() # reverse is a method of list 
print(Anime)
Anime.sort() # changes of Methods on Lisr is Permanent
print(Anime)
Anime.sort(reverse=1) # sorting with reverse alphabetical order
print(Anime)
# Len() is the function used to determine the length 
# which returns a integer value
print("the length of the Anime List is: "+str(len(Anime)))


