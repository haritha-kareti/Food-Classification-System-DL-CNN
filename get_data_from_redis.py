import redis
import json

# ======================================================
# REDIS CONNECTION
# ======================================================

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

# ======================================================
# FUNCTION TO GET NUTRITION DATA
# ======================================================

def get_nutrition_data(food_name):

    nutrition_data = redis_client.get(food_name)

    if nutrition_data:

        return json.loads(nutrition_data)

    return {

        "calories": "N/A",

        "protein": "N/A",

        "carbs": "N/A",

        "fats": "N/A",

        "fiber": "N/A"
    }