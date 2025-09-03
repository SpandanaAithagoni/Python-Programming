#currentbill
Cno=int(input("Consumer number: "))
Cname=input("Consumer name: ")
pmr=int(input("Present month reading: "))
lmr=int(input("Last month reading: "))
tu=pmr-lmr
cbill=tu*3.80
print("Consumer number: ",Cno,"\n Consumer name: ",Cname,"\nPresent month reading: ",pmr,"\nLast month reading: ",lmr,"\nTotal units consumed: ",tu,"\nCurrent bill: ",cbill)