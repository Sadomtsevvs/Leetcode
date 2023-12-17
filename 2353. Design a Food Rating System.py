import heapq
from time import time
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_cuisine = dict()
        self.food_ratings = dict()
        self.cuisines = dict()
        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.foods_cuisine[food] = cuisine
            self.food_ratings[food] = rating
            if cuisine not in self.cuisines:
                self.cuisines[cuisine] = []
                heapq.heapify(self.cuisines[cuisine])
            heapq.heappush(self.cuisines[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating
        heapq.heappush(self.cuisines[self.foods_cuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while - self.cuisines[cuisine][0][0] != self.food_ratings[self.cuisines[cuisine][0][1]]:
            heapq.heappop(self.cuisines[cuisine])
        return self.cuisines[cuisine][0][1]


# official solution with SortedSet
#
# from sortedcontainers import SortedSet
#
# class FoodRatings:
#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
#         # Map food with its rating.
#         self.food_rating_map = {}
#         # Map food with cuisine it belongs to.
#         self.food_cuisine_map = {}
#
#         # Store all food of a cuisine in a set (to sort them on ratings/name)
#         # Set element -> Tuple: (-1 * food_rating, food_name)
#         self.cuisine_food_map = defaultdict(SortedSet)
#
#         for i in range(len(foods)):
#             # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map' maps.
#             self.food_rating_map[foods[i]] = ratings[i]
#             self.food_cuisine_map[foods[i]] = cuisines[i]
#             # Insert the '(-1 * rating, name)' element in the current cuisine's set.
#             self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))
#
#     def changeRating(self, food: str, newRating: int) -> None:
#         # Fetch cuisine name for food.
#         cuisine_name = self.food_cuisine_map[food]
#
#         # Find and delete the element from the respective cuisine's set.
#         old_element = (-self.food_rating_map[food], food)
#         self.cuisine_food_map[cuisine_name].remove(old_element)
#
#         # Update food's rating in 'food_rating' map.
#         self.food_rating_map[food] = newRating
#         # Insert the '(-1 * new rating, name)' element in the respective cuisine's set.
#         self.cuisine_food_map[cuisine_name].add((-newRating, food))
#
#     def highestRated(self, cuisine: str) -> str:
#         highest_rated = self.cuisine_food_map[cuisine][0]
#         # Return name of the highest-rated 'food' of 'cuisine'.
#         return highest_rated[1]


start_time = time()

# Example 1:
# Input
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]
#
# Explanation
# FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
# foodRatings.highestRated("korean"); // return "kimchi"
#                                     // "kimchi" is the highest rated korean food with a rating of 9.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // "ramen" is the highest rated japanese food with a rating of 14.
# foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "sushi"
#                                       // "sushi" is the highest rated japanese food with a rating of 16.
# foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // Both "sushi" and "ramen" have a rating of 16.
#                                       // However, "ramen" is lexicographically smaller than "sushi".

# print(Solution().minimumOneBitOperations(_n))

print("--- %s seconds ---" % (time() - start_time))
