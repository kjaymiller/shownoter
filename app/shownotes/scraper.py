def link_detect(chat):
    return re.findall(r'^#.*|\b\S+\.\S+', chat, re.M)
    
