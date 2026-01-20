def student_info(name, age, grade, *middle_last,**subjects):
    print("Name:", name,middle_last)
    print("Age:", age)
    print("Grade:", grade)
    print("subjects",subjects)



    if middle_last:
        print("Additional Info (middle last):", middle_last)

    if subjects:
        print("Additional Details (subjects):")
        for key, value in subjects.items():
            print(f"  {key}: {value}")

student_info("loreen",20,"A","Lyimo","jay",AI="a",P="b")
    
    
    
    
    
    
    
    
    
    

    
