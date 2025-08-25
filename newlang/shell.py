import non_basic


while True:
    text=input("non-basic >")
    result,error=non_basic.run(text)
    if text.lower()=='quit':
        break
    if error:
        print(error.as_string())
    else:
        print(result)    

    