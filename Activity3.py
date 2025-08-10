tuple1=(1,0,0,0,0,1,1)
suny=0
rainy=0
for i in range(7):
    if tuple1[i]==0:
        rainy=rainy+1
    else:
        suny=suny+1
if suny>rainy:
    print("good weather")
else:
    print("bad weather")