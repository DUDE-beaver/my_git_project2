while True:
    try:
        size=int(input("To'plamning hajmini kiriting: "))
    except ValueError:
        print("Xato. Hajmi butun son bo'lishi zarur. Boshqatdan kiriting.\n")
    else:
        break

print()
external_list=[]
for steps1 in range(size):
    internal_list=[]
    for steps2 in range(3):
        while True:
            value=input("Qiymat kiriting: ")
            if value=="":
                try: 
                    raise NameError("Ichiga qiymat kiritmadingiz. Iltimos kiritib qo'ying.\n")
                except NameError as exc:
                    print(exc)
                else:
                    break
            else:
                break
        internal_list.append(value)
    print()
    external_list.append(internal_list)    

print()
print(f"Kirish: {external_list}")
print()
diction=dict()
for value in external_list:
    key=value[0]
    value.pop(0)
    diction[key]=value
print(f"Chiqish: {diction}")