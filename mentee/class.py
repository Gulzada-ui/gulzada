class Human:
    def __init__(self,name,age,nation):
        self.name = name
        self.age = age
        self.nation = nation
    def __str__(self):
        return f'My name is {self.name}'
    def study(self):
        return f'I am {self.nation}'

class Men(Human):
    def __init__(self,name,age,nation,university,hobby,height):
        super().__init__(name,age,nation)
        self.university = university 
        self.hobby = hobby 
        self.height = height 
    
    def __str__(self):
        return f'I am {self.age} years old'

    def study(self):
        return f'I study at {self.university}'

    def free(self):
        return f'I like {self.hobby}'

class Women(Human):
    def __init__(self,name,age,nation,college,weight,fav_music):
        super().__init__(name,age,nation)
        self.college = college
        self.weight = weight
        self.fav_music = fav_music 

    def study(self):
        return f'I go to {self.college}'

    def listen(self):
        return f'I listen to {self.fav_music}'
#maybe add 'if'
arman = Men('Arman', 23, 'american', 'standford', 'football', 175)
aidana = Women('Aidana', 21, 'french', 'Colby', 56, 'rock')

#print(arman.__dict__)
print(aidana.study())
print(arman)
print(aidana.listen())
print(arman.study())
print(arman.free())