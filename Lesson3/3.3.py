name=input("name:")
age=input("age:")
city=input("city:")
data={"name":name,"age":age,"city":city}
text="hello %(name)s %(age)s %(city)s" %data
print(text)