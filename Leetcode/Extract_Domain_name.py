def domain_name(url):
    startdomain = url.find(".")
    finaldomain = url.rfind(".")
    substring = url[startdomain+1:finaldomain]



    """
    if startdomain == -1:
        startdomain = url.find(".")
        print(startdomain)
        finaldomain = url.rfind(".")
        print(finaldomain)
        substring = url[startdomain+1:finaldomain]
    else:
        finaldomain = url.find(".")
        substring = url[startdomain+2:finaldomain]

    print(substring)
    #return substring
    """
    print(substring)
domain_name("http://www.codewars.com/kata/")