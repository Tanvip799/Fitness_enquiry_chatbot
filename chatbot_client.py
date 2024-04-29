import requests

def main():
    while True:
        message = input("You: ")

        if message.lower() == 'quit':
            print("Exiting...")
            break

        response = send_message_to_chatbot(message)
        print("Chatbot:", response)


def send_message_to_chatbot(message):
    url = "http://127.0.0.1:8080/chatbot"
    payload = {"message": message}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()["answer"]
    except requests.exceptions.RequestException as e:
        print("Error communicating with the chatbot server:", e)
        return "Sorry, there was an error."


if __name__ == "__main__":
    main()
