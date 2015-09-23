square = (x)-> x * x
console.log square 2

cube = (x)-> square(x) * x
console.log cube 3

fill = (container, liquid = "coeff")->
  "fill the #{container} with #{liquid}..."
console.log fill "cup"

song = ["do", "re", "mi", "fa", "so"]
singers = {Jagger: "Rock", Elvis: "Roll"}

bitlist = [
  1, 0, 1
  0, 0, 1
  1, 1, 0
]

kids =
  brother:
    name: "Max"
    age: 11
  sister:
    name: "Ida"
    age: 9

outer = 1
changeNumbers = ->
  inner = -1
  outer = 10
inner = changeNumbers()

singing = false
mood = greatlyImproved if singing

friday = true
sue = true
jill = false
date = if friday then sue else jill


gold = silver = rest = "unknown"
awardMedals = (first, second, others...) ->
  gold = first
  silver = second
  rest = others

contenders = [
  "Michael Phelps"
  "Liu Xiang"
  "Yao Ming"
  "Allyson Felix"
  "Shawn Johnson"
  "Roman Sebrle"
  "Guo Jingjing"
  "Tyson Gay"
  "Asafa Powell"
  "Usain Bolt"
]

awardMedals contenders...

console.log "Gold: " + gold
console.log "Silver: " + silver
console.log "The Field: " + rest

eat = (x)->
  console.log "eating #{x}"

eat food for food in ['toast', 'cheese', 'wine']

menu = (x, y)->
  console.log "#{x}...#{y}"

courses = ['greens', 'caviar', 'truffles', 'roast', 'cake']
menu i + 1, dish for dish, i in courses

foods = ['broccoli', 'spinach', 'chocolate']
eat food for food in foods when food isnt 'chocolate'

countdown = [num for num in [10..1]]

yearsOld =
  max: 10, ida: 9, tim: 11
ages = for child, age of yearsOld
  "#{child} is #{age}"

console.log ages


x =5
triple = (x)-> x*=3
triple x
x