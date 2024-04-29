# Fitness_enquiry_chatbot
The chatbot is designed to handle user queries and provide responses based on predefined intents. It utilizes natural language processing techniques to understand user input and generate appropriate answers.<br/>

Key Features:<br/>
Flask Backend: Built with Flask, a lightweight web framework in Python, to create a RESTful API for communication with the chatbot.<br/>
Intent Recognition: Utilizes a predefined set of intents and patterns to recognize user queries and provide relevant responses.<br/>
Scalable Architecture: Designed with scalability in mind, allowing for easy integration with frontend applications or other systems.<br/>
Performance Metrics: Computes precision to evaluate the chatbot's performance based on ground truth data.<br/><br/><br/>

How to run?:<br/>
If u want to train the model run: python training.py<br/>

Start the Flask server by running python server.py.<br/>
Start the client side by running python chatbot_client.py<br/>
Send POST requests to http://localhost:8080/server with a JSON payload containing the user's message.<br/>
Receive JSON responses containing the chatbot's answers.<br/><br/><br/>

Future Improvements:<br/>
Incorporate more advanced natural language processing techniques for better understanding and response generation.<br/>
Implement user authentication and session management for personalized interactions.<br/>
Integrate with third-party APIs for additional functionality, such as fetching real-time data or performing actions on behalf of users.<br/>
