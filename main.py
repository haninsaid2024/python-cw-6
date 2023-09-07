person = {
    "name": "haneen",
    "age": 15,
    "hobbies":['reeding' , 'cooking' , 'playing_games']   

}

print(person["name"])
print(person['age'])
person["age"] = 16 
print(person['age'])
person['country']='Egypet'
print(person)
person["hobbies"].append("skating")
print(person)
len(person)
print(len(person))

def check_hobbies(person):
  if len(person)["hobiies"] > 3:
     print('wow you are ama')
  else:  
      print('Falus')
check_hobbies(person)









