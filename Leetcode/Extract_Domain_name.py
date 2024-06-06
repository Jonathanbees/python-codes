def domain_name(url: str):
    if "//www" in url or "www" in url:
        startdomain = url.find(".")
        substringdivide = url[startdomain+1:]
        #print(substringdivide)
        finaldomain = substringdivide.find(".")
        substring = substringdivide[:finaldomain]
        #print("substring con www", substring)
        return substring
    elif "http://" in url or "https://" in url:
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
        finaldomain = url.find(".")
        substring = url[:finaldomain]
    #print(substring)
    return substring
domain_name("http://www.g80antioyawwxnzmdpx0hs.info/index.php")