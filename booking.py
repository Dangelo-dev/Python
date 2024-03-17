import pyautogui
import threading
import time
import keyboard

# Function to continuously monitor the "q" key press
def check_q_key():
    global stop_flag
    while True:
        if keyboard.is_pressed('q'):
            stop_flag = True
            break

# Start the thread for monitoring the "q" key press
stop_flag = False
q_thread = threading.Thread(target=check_q_key)
q_thread.start()

# Main loop for mouse movements and clicks
while not stop_flag:
    x, y = pyautogui.position()
    print("Coordenadas:", x, y)
    
    pyautogui.moveTo(x=1025, y=964)
    pyautogui.click(clicks=1, interval=3)
    
    time.sleep(0.1)  # Add a small delay to reduce CPU usage

# Wait for the "q" thread to finish
q_thread.join()

print("Program stopped by pressing 'q' key.")