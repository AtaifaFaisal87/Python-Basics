print("====WEIGHT CONVERTOR PROGRAM====")

weight=input("ENTER YOUR WEIGHT:")
unit=input("(L)lbs or (K)kgs:")

if unit.upper( )=="L":
    converted=(int(weight))*0.45
    print(f"YOUR WEIGHT IN KILOS IS {converted}")

elif unit.upper()=="K":
     converted=(int(weight))//0.45
     print(f"YOUR WEIGHT IN Lbs IS {converted}")
