#usage of string Methods
name="alex baggy"
print(name.title())
print(name.lower())
print(name.upper())

#combinig & concatenating
first_name="ada"
last_name="lovelace"
full_name="\n"+first_name+" "+last_name
print(full_name)

print("Hello,"+full_name.title()+", How are you doing?")

#or you can usage a variable to store combined or concatenation message
message="Hello,"+full_name.lower()+"!, How are you doing?"
print(message)
