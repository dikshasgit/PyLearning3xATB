# Tuples -> Values doesn't change - Immutable

API_URLs = ("https://sdet.live/python3x", "https://google.com/images", "https://vwo.com/login")
print(API_URLs[0])
print(API_URLs[1])
# API_URLs[1] = "Mangesh"           # Not allowed
API_URLs = API_URLs + ("https://sdet.live/python3x/intros",)
print(API_URLs)


