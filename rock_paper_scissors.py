
black_durag= "5.99"
green_durag = "7.80"
yellow_durag = "3.90"

lion_test= (input("yo whats ur durag colour: ")).lower()

if lion_test == "black":
  durag_cost = black_durag
elif  lion_test == "green":
  durag_cost = green_durag 
elif  lion_test == "yellow":
  durag_cost = yellow_durag 
else:
    durag_cost = None
    print("Wrong input try again!")

if durag_cost:
  print("Aight so ur durag cost", durag_cost)



