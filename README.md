monarch
## Burp - First Token Launched By Burp

1. Install Python 3.11 from [here](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe).
2. Clone the repository.
3. Install all requirements: `pip install -r requirements.txt`.
4. Use the `.lnk` shortcut file to launch Chrome. Close all Chrome instances before launching.
   - You can manually create a shortcut with the following additional data:
     ```
     "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
     ```
5. Ensure that the page opens correctly: [http://localhost:9222/json](http://localhost:9222/json).
6. The `.env` file contains information about the token to create.
7. Run the script: `python main.py`.
8. After loading the script, wait for the message: "Recording...".
9. BURP