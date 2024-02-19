def outer():
    name = "Bibhuti"
    
    def inner():
        nonlocal name
        print(name)
        name = "Biswas"
    
    inner()
    print(name)
    
outer()
     