import pywhatkit as pwk

# Specify the recipient's phone number (with country code)
phone_number = "+916374771918"

# Message to be sent
message = "Hello, this is a test message sent using PyWhatKit!"

# Specify the time (24-hour format) when you want to send the message
time_hour = 4  # Example: 2 PM
time_min = 6   # Example: 30 minutes

try:
    # Send the message at the specified time
    pwk.sendwhatmsg(phone_number, message, time_hour, time_min)
    print(f"Message scheduled to be sent to {phone_number} at {time_hour}:{time_min} successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
