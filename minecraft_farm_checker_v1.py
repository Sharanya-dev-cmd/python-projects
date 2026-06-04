has_hoe = input("do you have a hoe? : ").lower()
if has_hoe == "yes" :
    print("you have a hoe")
elif has_hoe == "no" :
    print("you need a hoe")
else :
    print("invalid input")


has_dirt_blocks = int(input("how many dirt blocks do you have? : "))
if has_dirt_blocks >= 9 :
    print("you can build a 3x3 farm or bigger!")
elif has_dirt_blocks >= 1 and has_dirt_blocks <=8 :
    print("you can have a decent-sized farm")
else :
    print("you need dirt blocks / invalid input")


has_seeds = int(input("how many seeds do you have? : "))
if has_seeds >= has_dirt_blocks :
    print("you have a decent number of seeds")
else :
    print("you need more seeds / invalid input")


has_water_bucket = int(input("how many water buckets do you have? : "))  # ill later add 'u can be near a water source too' in another version
if has_water_bucket >= 1 :   # i shall fix this game lag later
    print("you will be able to irrigate your farm")
else :
    print("you need one or more water buckets / invalid input")


has_light_source = input("do you have a light source? : ").lower()
if has_light_source == "yes" :
    print("you will be able to light up your farm")
elif has_light_source == "no" :
    print("you need a light source to build your farm")
else :
    print("invalid input")


if has_hoe == "yes" and has_dirt_blocks >= 1 and has_seeds >= has_dirt_blocks and has_water_bucket >= 1 and has_light_source == "yes" :
    print("you can build a great farm!")
else :
    print("you need more resources to make your farm functional")

    
# IDEAS FOR FUTURE VERSIONS / NEW PROJECTS
# u can give a final summary of all missing resources instead of many sep. messages
# add bone meal in later version
# add thingies for different crop types (wheat, carrots, potatoes, beetroot)
# check if player can build animal farm
# check if farm is safe from hostile mobs
# check if player has enough resources for starter base
# create a complete farm planner with building and growth advice