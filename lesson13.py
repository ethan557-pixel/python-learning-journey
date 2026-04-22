import requests

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        print("")
        print("Here's a joke for you:")
        print("")
        print(data['setup'])
        print(data['punchline'])
        print("")
    except Exception as e:
        print("couldn't fetch a joke: " + str(e))

keep_going = "yes"

while keep_going.lower() == "yes":
    get_joke()
    keep_going = input("Do you want to hear another joke? (yes/no): ")
print("thanks for the tehes!!")