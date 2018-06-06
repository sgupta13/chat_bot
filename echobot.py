bot_template = "BOT: {0}"
user_template = "USER: {0}"

# Function that responds to a user's message: respond
def respond(message):
    bot_message = "I can hear you! You said: " + message
    return bot_message

# Function that sends a message to the bot: send_message

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

send_message("hello")
