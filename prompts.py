# Generate prompt to gather user input and produce itinerary
def generate_itinerary_prompt(user_input):
    system_prompt = (
        "You are an AI assistant helping to plan a personalized travel itinerary. "
        "Use the details provided by the user to suggest a day-by-day travel plan."
    )
    
    user_prompt = (
        f"User Input: {user_input}\n"
        "Please create an itinerary based on the user’s preferences, including daily activities, "
        "accommodation suggestions, and other relevant travel tips."
    )
    
    return f"{system_prompt}\n\n{user_prompt}"
