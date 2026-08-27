person = ["My dog", "An alien", "A ninja", "My evil twin", "Batman"]
action = ["ate", "stole", "blew up", "hid", "teleported"]
object = ["my homework.", "my car keys.", "my alarm clock.", "my shoes.", "the internet."]
import random
excuse1=random.choice(person)
excuse2=random.choice(action)
excuse3=random.choice(object)
print(f"{excuse1} {excuse2} {excuse3}")
