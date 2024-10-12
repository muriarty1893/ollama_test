def log_conversation(log_file, current_time, user_input, result, response_time):
    log_file.write(f"Time: {current_time}\n")
    log_file.write(f"User: {user_input}\n")
    log_file.write(f"Bot: {result}\n")
    log_file.write(f"Response Time: {response_time:.2f} seconds\n\n--------new-chat---------\n")
