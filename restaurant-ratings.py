#create a dictionary for resturant ratings
restaurant_ratings = {}
restaurant_file = open("scores.txt")

#for resturant_rating_pair_text:
for line in restaurant_file:
    #dictionaryname[resturant_name] = rating
    stripped = line.rstrip()
    both_keys = stripped.split(":")
    restaurant_name = both_keys[0]
    restaurant_rating = both_keys[1]

    restaurant_ratings[restaurant_name] = restaurant_rating
    # print restaurant_ratings
# print restaurant_ratings
for restaurant_name, restaurant_rating in restaurant_ratings.items():
    print "{name} is rated at {rate}.".format(name = restaurant_name, 
                                            rate = restaurant_rating)
