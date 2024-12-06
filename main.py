import webview
import os
import subprocess

class API:
    def on_button_pressed(self):
        subprocess.run(["gnome-terminal", "-e", f"bash -c 'neofetch; exec bash'" ])
        
    
    def start_port_scan(self,data):
        hostname = data.get("hostname")
        port = data.get("port")
        print(hostname,port)
        
        if hostname:
            if port:
                command = f"nmap -p {port} {hostname}"
                
            else:
                command = f"nmap {hostname}"
            subprocess.run(["gnome-terminal", "-e", f"bash -c '{command}; exec bash'"])
        else:
            print("hostname is required!")
            
    def start_vuln_scan(self, data):
        print("the button is working")
        hostname = data.get("hostname")
        
        if hostname:
            command = f"nmap --script vuln {hostname}"
        subprocess.run(["gnome-terminal", "-e", f"bash -c '{command}; exec bash'"])
        
        
    
        


current_dir = os.path.abspath(os.path.dirname(__file__))
html_file = os.path.join(current_dir,'static', 'index.html')

api = API()


webview.create_window(
    'portProbe',
    f'file://{html_file}',
    height=700,
    width=1200,
    js_api=api
)
webview.start()