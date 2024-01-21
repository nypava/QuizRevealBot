import re

def link_filter(link):
    regex = r"^(https://t.me/?)"
    
    return re.match(regex, link) != None

