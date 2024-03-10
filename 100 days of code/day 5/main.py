print("the 90's rapper/group akinator")
print(" ")

black = str(input("is your rapper black? "))
if black == "yes":
  side = str(input("is your rapper from east or west coast? "))
  if side == "east":
    group = str(input("is that a group? "))
    if group == "yes":
      clan = str(input("were they a clan? "))
      if clan == "yes":
        print("that's wu-tang clan")
      if clan == "no":
        gangster = str(input("they did gangster rap? "))
        if gangster == "yes":
          print("that's mobb deep, good one!")
        if gangster == "no":
          tribe = str(input("they were a tribe? "))
          if tribe == "yes":
            print("that's a tribe called quest")
          if tribe == "no":
            print("that's de la soul")
    if group == "no":
      print("nah, nigga. now i'm lazy to do the non group part. you can make a pull request if you want solo rappers")
  if side == "west":
    print("nah, nigga. now i'm lazy to do the west part. you can make a pull request if you want west rappers")
            
        
    
if black == "no":
  group = str(input("is that a group? "))
  if group == "yes":
    print("it's beastie boys, funny one!")
  if group == "no":
    print("that's eminem")