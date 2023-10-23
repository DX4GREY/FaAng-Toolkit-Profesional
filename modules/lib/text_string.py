from colorama import Fore

wrap = 60

def desc():
    help_desc = "The features within this menu offer a range of powerful and diverse DDoS methods, designed to test and identify vulnerabilities and resilience of networks and servers. This menu encompasses attacks on both layer 4 and layer 7, including various attack types such as UDP, TCP, HTTP, and more. These attack methods enable users to simulate real-world scenarios, providing deeper insights into the defense capabilities of their systems against such attacks. Ranging from request-based attacks to protocol-based ones, this menu covers a broad spectrum of options to identify and mitigate DDoS risks effectively."
    return help_desc
    
def menus():
    menu = [
        "UDP       layer4 => UDP Attack", 
        "TCP       layer4 => TCP Attack", 
        "FiveM     layer4 => Fivem Server Attack", 
        "MC        layer4 => Minecraft Bedrock or Java Server Attack", 
        "", 
        "GET       layer7 => 'Requests GET' Attack", 
        "POS       layer7 => 'Requests POST' Attack", 
        "SOC       layer7 => Socket Attack" , 
        "HTTP2     layer7 => HTTP 2.0 Request Attack", 
        "SPOOF     layer7 => HTTP Spoof Socket Attack  ", 
        "HEAD     layer7 => Head Request Attack", 
        "SKY      layer7 => Sky method", 
        "CFREQ    layer7 => Bypass CF UAM, CAPTCHA, BFM (request)", 
        "CFSOC    layer7 => Bypass CF UAM, CAPTCHA, BFM (socket)", 
        "CFB      layer7 => Bypass CF Attack", 
        "SLOW     layer7 => Slowloris method attack", 
        "MBP      layer7 => Send large megabyte payload method attack", 
        "RUDY     layer7 => Send large content for attack"
    ]
    return menu

def word_wrapper(text, line_length):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if len(current_line) + 1 + len(word) <= line_length:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return "\n".join(lines)

def logos():
    logo = f"""
{Fore.MAGENTA} █████▒▄▄▄          ▄▄▄       ███▄    █   ▄████ 
▓██   ▒▒████▄       ▒████▄     ██ ▀█   █  ██▒ ▀█▒
▒████ ░▒██  ▀█▄     ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░
{Fore.RESET}░▓█▒  ░░██▄▄▄▄██    ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓
░▒█░    ▓█   ▓██▒    ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒
 ▒ ░    ▒▒   ▓▒█░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ 
 ░       ▒   ▒▒ ░     ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░ ░     ░   ▒        ░   ▒      ░   ░ ░ ░ ░   ░ 
             ░  ░         ░  ░         ░       ░ 
                                                 
{word_wrapper(f"THE OWNER OF THESE TOOLS (Dx4) WILL NOT BE RESPONSIBLE FOR ANY DAMAGE CAUSED BY THE USER OWN THEREFORE, USE THESE TOOLS ONLY TO TEST YOUR OWN SITE FOR {Fore.GREEN}VULNERABILITIES {Fore.RESET}ATTACKING SITES OWNED BY OTHERS, {Fore.YELLOW}FAANG SHOULD NOT BE USED FOR ILLEGAL ACTIVITIES{Fore.RESET}, BY USING THIS SOFTWARE, {Fore.RED}YOU MUST AGREE TO BE FULLY RESPONSIBLE FOR DAMAGE CAUSED BY FAANG IN ANY WAY TO YOUR OWN{Fore.RESET}. THE CREATORS DO NOT WANT PEOPLE TO USE FAANG IF THEY HAVE NO EXPERIENCE WITH ATTACKS INCLUDING. ANY ATTACK WILL CAUSE TEMPORARY DAMAGE, BUT {Fore.YELLOW}LONG TERM DAMAGE{Fore.RESET} IS POSSIBLE. FAANG SHOULD NOT ADVISE PEOPLE TO DO {Fore.RED}ILLEGAL ACTIVITIES{Fore.RESET}.", wrap)}
"""
    return logo