def domain_name(url: str):
    if "//www" in url or "www" in url:
        startdomain = url.find(".")
        finaldomain = url.rfind(".")
        substring = url[startdomain+1:finaldomain]
    elif "http://" in url or "https://":
        startdomain = url.find("//")
        #print(startdomain)
        if startdomain == -1:
            startdomain = url.find("//")
            finaldomain = url.find(".")
            substring = url[startdomain+2:finaldomain]
            #print(substring)
            return substring
        else:
            finaldomain = url.find(".")
            substring = url[startdomain+2:finaldomain]
    else:
        finaldomain = url.rfind(".")
        substring = url[:finaldomain]
    #print(substring)
    return substring
domain_name("https://youtube.com")