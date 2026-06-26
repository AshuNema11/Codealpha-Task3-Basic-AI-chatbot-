import urllib.request
import urllib.parse
import json
import time

class Colors:
    BOT = '\033[96m'  # Cyan
    USER = '\033[92m' # Green
    SYS = '\033[93m'  # Yellow
    RESET = '\033[0m'

class ZeroPipBot:
    def __init__(self):
        self.api_url = "https://html.duckduckgo.com/html/"
        
    def type_effect(self, text: str, delay: float = 0.005):
        print(f"\n{Colors.BOT}Assistant 🎙️: {Colors.RESET}{Colors.BOT}", end="")
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print(f"{Colors.RESET}")

    def ask_ai(self, query: str) -> str:
        try:
            # Preparing web request to fetch answers directly
            data = urllib.parse.urlencode({'q': query}).encode('utf-8')
            req = urllib.request.Request(
                self.api_url, 
                data=data, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8')
                
                # HTML parse karke best snippet nikalna (Built-in regex/string functions)
                links = html.split('<td class="result-snippet">')
                if len(links) > 1:
                    ans = links[1].split('</td>')[0]
                    # Clean HTML tags from the result
                    ans = ans.replace('<b>', '').replace('</b>', '').strip()
                    return ans
                
            return "Mujhe is baare mein abhi clear data nahi mila. Sahi spelling use karein."
        except:
            return "Network slow hai ya connection nahi ho paa raha hai."

    def start(self):
        print(f"{Colors.SYS}--- ZERO-PIP WEB ASSISTANT (NO INSTALL REQUIRED) ---{Colors.RESET}")
        self.type_effect("System fully active! Main bina pip ke chal raha hoon aur mere paas internet ki jankari hai. Type 'exit' to quit.")
        
        while True:
            user_input = input(f"\n{Colors.USER}You: {Colors.RESET}").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ['exit', 'quit', 'bye']:
                self.type_effect("Alvida! Apna dhyan rakhiyega. 👋")
                break
                
            print(f"{Colors.SYS}Searching database...{Colors.RESET}", end="\r")
            answer = self.ask_ai(user_input)
            
            # Clear text
            print(" " * 25, end="\r")
            self.type_effect(answer)

if __name__ == '__main__':
    bot = ZeroPipBot()
    bot.start()
