import redis
import json

# REDIS CONNECTION

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

# LOAD JSON FILE

with open("food_data.json", "r") as file:
    food_data = json.load(file)

nutrition_list = food_data["nutrition"]

# STORE DATA INTO REDIS

for item in nutrition_list:

    food_name = item["name"]

    redis_client.set(
        food_name,
        json.dumps(item)
    )

print("\n✅ All data stored successfully.")

