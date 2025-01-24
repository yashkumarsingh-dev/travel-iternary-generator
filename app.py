import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define your OpenAI API key (ensure this is set correctly)
with open("key.txt", "r") as file:
    openai.api_key = file.read()

# Function to generate the itinerary prompt
def generate_itinerary_prompt(user_input):
    # Example prompt generation logic
    # You can modify this based on your needs
    return f"Create a travel itinerary based on the following user input: {user_input}"

# Function to call OpenAI API and generate the itinerary
def generate_itinerary(user_input):
    prompt = generate_itinerary_prompt(user_input)

    try:
        # Make a call to OpenAI's new API method for chat completions
        response = openai.ChatCompletion.create(  # Corrected method name
            model="gpt-3.5-turbo",  # Or another model of your choice
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )
        # Return the generated itinerary text from the response
        return response['choices'][0]['message']['content'].strip()

    except openai.OpenAIError as e:  # Handle OpenAI-specific errors
        return f"Error: {e}"

# Route to handle POST request for generating itinerary
@app.route("/generate", methods=["POST"])
def generate():
    # Get JSON data from the request
    data = request.get_json()

    # Extract user input from the data (ensure the key matches the JSON body)
    user_input = data.get("user_input", "")

    # Validate the user input
    if not user_input:
        return jsonify({"error": "User input is required."}), 400

    # Generate the itinerary using the OpenAI API
    itinerary = generate_itinerary(user_input)

    # Return the generated itinerary as a JSON response
    return jsonify({"itinerary": itinerary})

# Main entry point for the Flask app
if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
