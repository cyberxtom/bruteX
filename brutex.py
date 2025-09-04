import argparse
import requests
import os
import pyfiglet
import sys
from datetime import datetime
red = '\033[91m'
green = '\033[32m'
reset = '\033[0m'
purple = '\033[95m'
blue = '\033[34m'
if os.name == 'nt':    
    lin = os.system('cls')
else:  
    lin = os.system('clear')
def header(text: str = "BRUTE X", font: str = "big") -> str:
    
    ascii_art = pyfiglet.figlet_format(text, font=font)

    
    colors = ["\033[91m", "\033[93m", "\033[92m",
              "\033[96m", "\033[94m", "\033[95m"]
    reset = "\033[0m"

    
    colored_lines = []
    for i, line in enumerate(ascii_art.splitlines()):
        if line.strip():
            color = colors[i % len(colors)]
            colored_lines.append(color + line + reset)
        else:
            colored_lines.append(line)

    
    width = max(len(line) for line in ascii_art.splitlines())
    border = "+" + "-" * (width + 2) + "+"
    framed = [border] + [f"| {line.ljust(width)} |" for line in colored_lines] + [border]

    return "\n".join(framed)
print(header())    

parser = argparse.ArgumentParser(description="directory brute force tool")
parser.add_argument('-u', '--url', help='Target URL or IP Address', required=True)
parser.add_argument('-d', '--dir',  help='Directories file (.txt) ' , required=True)
arg = parser.parse_args()
url = arg.url
directory = arg.dir
dirs = open(directory, 'r').read().splitlines()
print(f"{purple}#"*50,reset)
print(f"{red} \n[@] Developed by XTOM\033[0m")
print(f"\n{blue}[*] Scan started on Target: {url} {reset}\n") 
print(f"{blue}[*] Scan started at: {str(datetime.now())}{reset}\n")
print(f"{purple}#"*50,reset)
print("\n\n")
Dir = []

def generate_html_report(full_url,url):
     rows = ''.join([f'<tr><td><a href="{full_url}">{dir}</a> </td></tr>' for dir in Dir])
     html_content = f"""
    
     <html>
     <head>
          <title>Directories {url}</title>
          <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: Arial, sans-serif; background: rgb(21, 24, 20); height: 100%;width: 100%;}}
                h2 {{ color: #7e7e7edc; }}
                div {{ text-align: center; margin: 3vh 20vw;}}
                h1 {{ color: #00d107; background-color: rgb(21, 24, 20); padding: 15px; border-radius: 10px; border-style: none; }}
                table {{ border-collapse: collapse; width: 50%; margin: 20px auto;  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); border-radius: 20px; overflow: hidden; border-style: none;}}
                th, td,tr {{ border: none; padding: 8px; text-align: center; }}
                th {{ background: #00d107; color: white; }}
                tr{{border-bottom: 1px solid black;}}
                a{{text-decoration: none;}}
                td,tr {{height: 20px; background-color: rgb(85, 85, 85) ;  font-weight: 900; font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; }}
                span {{ border-radius: 20px;overflow: hidden; border-style: none; background: #ffffff; padding: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }}
          </style>
     </head>
     <body>
          <div>
               <h1>Brute-X Report</h1>
          <h2>{url}</h2>
     </div><span> 
<table>
                <tr><th><h1>Directories</h1></th></tr>
                {rows}
            
          </table>
     </span>
          
     </body>
     </html>
     
     """
     with open("brutex.html", "w") as html_file:
          html_file.write(html_content)
   
def brute(dirs):
     try:
       for dir in dirs:
        full_url = f"{url}/{dir}"
        response = requests.get(full_url)
        if response.status_code == 200:
            
            print(f"{green}[+] Found: {full_url}{reset}")
            Dir.append(full_url)
            
       generate_html_report(full_url,url)   
     except requests.exceptions.RequestException as e:
       print(f"[-] Error: {e}")
       sys.exit()
   
print(f"{purple}="*50,)
brute(dirs)
print(f"{purple}="*50,)



print("\n\n")
print(f"{purple}#"*50,reset)
print(f"\n{blue}[*] Scan completed at: {str(datetime.now())}{reset}\n")
print(f"{blue}[*] Html report generated: brutex.html {reset}\n")
print(f"{purple}#"*50,reset)
