class Person:
    def __init__(self, name, age, gender):
        
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Heyy, my name is {self.name} of age {self.age}. I identify as {self.gender}.")
        
        
#create an instance of the person class
person1 = Person("Marie", 25, "female")

#call the introduce method to display the person's information
person1.introduce() 
            
        
        