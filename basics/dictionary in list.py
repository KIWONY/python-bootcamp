travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    travel_log.append({"country" : country,
                       "visits" : visits,
                       "cities" : cities
                      })

# 강의 정답 함수
def solution_in_lecture(country, visits, cities):
	new_country = {}
	new_country["country"] = country
	new_country["visits"] = visits
	new_country["cities"] = cities	
	travel_log.append(new_country)
 

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
solution_in_lecture("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)



