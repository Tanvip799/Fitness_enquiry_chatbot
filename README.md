# Fitness_enquiry_chatbot
The chatbot is designed to handle user queries and provide responses based on predefined intents. It utilizes natural language processing techniques to understand user input and generate appropriate answers.

Key Features:
Flask Backend: Built with Flask, a lightweight web framework in Python, to create a RESTful API for communication with the chatbot.
Intent Recognition: Utilizes a predefined set of intents and patterns to recognize user queries and provide relevant responses.
Scalable Architecture: Designed with scalability in mind, allowing for easy integration with frontend applications or other systems.
Performance Metrics: Computes precision to evaluate the chatbot's performance based on ground truth data.

How to run?:
If u want to train the model run: python training.py
Start the Flask server by running python server.py.
Start the client side by running python chatbot_client.py
Send POST requests to http://localhost:8080/server with a JSON payload containing the user's message.
Receive JSON responses containing the chatbot's answers.

Future Improvements:
Incorporate more advanced natural language processing techniques for better understanding and response generation.
Implement user authentication and session management for personalized interactions.
Integrate with third-party APIs for additional functionality, such as fetching real-time data or performing actions on behalf of users.
