def student_info(name, age, grade, *args, **kwargs):
    print("Name:", name)
    print("Age:", age)
    print("Grade:", grade)

    if args:
        print("Additional Info (args):", args)

    if kwargs:
        print("Additional Details (kwargs):")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

    
    
    
    
    
    
    
    
    
    
    
    