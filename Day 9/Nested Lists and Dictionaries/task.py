# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#    },
# }
#
# print(travel_log["Germany"]["cities_visited"][2])

def clear_terminal():
    print(chr(27) + "[2J")

# Example usage
print("Learning Python!")
input("Press Enter to clear the terminal...")
clear_terminal()
print("Terminal cleared!")
