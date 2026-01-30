# # class emloyee:
# #     def __init__(self,name,salary):
# #         self.name=name
# #         self.salary=salary
# #     @property
# #     def first_name(self):
# #         l=self.name.split(" ")
# #         return l[0]
    
# #     @first_name.setter
# #     def first_name(self,first):
# #         l=self.name.split(" ")
# #         new_name=f"{first} {l[1]}"
# #         self.name=new_name

# # e=emloyee("yash patil",55000)
# # # print(e.first_name())
# # # e.set_new_name("john")
# # # print(e.name)

# # print(e.first_name)
# # e.first_name="diksha"
# # print(e.name)


# # class employee:
# #     def __init__(self,name,salary):
# #         self.name=name
# #         self.salary=salary
# #     @property
# #     def first_name(self):
# #         l=self.name.split(" ")
# #         return l[0]
# #     @first_name.setter 
# #     def first_name(self,first):
# #         l=self.name.split(" ")
# #         new_name=f"{first} {l[1]}"
# #         self.name=new_name

        
    

# # e=employee("yash patil",50000)
# # print(e.first_name)
# # e.first_name="diksha"
# # print(e.name)



# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @property
#     def first_name(self):
#         l=self.name.split(" ")
#         return l[0]
#     @first_name.setter
#     def first_name(self,first):
#         l=self.name.split(" ")
#         new_name=f"{first} {l[1]}"
#         self.name=new_name
        
# e=employee("Yash Patil",50000)
# print(e.first_name)
# e.first_name="Dikshu"
# print(e.name)



class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @property
    def first_name(self):
        l=self.name.split(" ")
        return l[0]
    
    @first_name.setter
    def first_name(self,first):
        l=self.name.split(" ")
        new_name=f"{first} {l[1]}"
        self.name=new_name


e=employee("Yash patil",50000)
print(e.first_name)
e.first_name="Dikshu"
print(e.name)
