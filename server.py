
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_functiont import process_query
from ddtrace.runtime import RuntimeMetrics


RuntimeMetrics.enable()


# Create a new instance of Flask.
app = Flask(__name__)
CORS(app)


# Create Flask route with a POST method for sending the message to our frontend.
@app.post('/chatbot')
def chatbot():
    # Retrieve message from user.
    message_from_user = request.get_json().get('message')
    print(f'[message_from_user:\t{message_from_user}]')

    # Process message_from_user by sending it to our chatbot_assistant.py.
    response = process_query(message_from_user)

    # Format response to be JSON friendly.
    response_formatted = {'answer': response}
    print(f'[response_formatted:\t{response_formatted}]')

    # Return a jsonify version of the response.
    return jsonify(response_formatted)


# Run Flask app.
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True) 

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from chatbot_functiont import process_query
# from ddtrace.runtime import RuntimeMetrics
# from sklearn.metrics import precision_score, recall_score, f1_score

# RuntimeMetrics.enable()

# # Create a new instance of Flask.
# app = Flask(__name__)
# CORS(app)

# # Define the expected labels for the responses
# expected_labels = {
#     "add-new-client": "clients",
#     "client-list": "clients",
#     "remove-client-from-class": "clients",
#     "current-classes": "classes",
#     "name-class": "classes",
#     "add-class-at-time-and-or-date": "classes",
#     "add-client-to-class": "classes"
# }

# # Create Flask route with a POST method for sending the message to our frontend.
# @app.post('/chatbot')
# def chatbot():
#     # Retrieve message from user.
#     message_from_user = request.get_json().get('message')
#     print(f'[message_from_user:\t{message_from_user}]')

#     # Process message_from_user by sending it to our chatbot_assistant.py.
#     response = process_query(message_from_user)

#     # Format response to be JSON friendly.
#     response_formatted = {'answer': response}
#     print(f'[response_formatted:\t{response_formatted}]')

#     # Calculate precision, recall, and F1-score
#     predicted_label = response['tag']
#     expected_label = expected_labels.get(predicted_label, None)
#     if expected_label:
#         precision = int(predicted_label == expected_label)
#         recall = precision
#         f1 = precision
#     else:
#         precision, recall, f1 = 0, 0, 0

#     # Print precision, recall, and F1-score
#     print(f'Precision: {precision}, Recall: {recall}, F1-score: {f1}')

#     # Return a jsonify version of the response.
#     return jsonify(response_formatted)

# # Run Flask app.
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True)
