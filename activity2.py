amount=int(input("please enter the amount:"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount % 100)% 50)//10
note_4=((amount % 100)% 50)//1
note_5=((amount % 100)% 50)//0.55
print("notes of 100 rupee",note_1)
print("notes of 50 rupee",note_2)
print("notes of 10 rupee",note_3)
print("notes of 1 rupee",note_4)
print("notes of 0.55 rupee",note_5)