tuple1=(1,2.2,4.3,5,"something")
print(tuple1)

tuple2=(1,2,3,4,5,6,7,8,9)
print(tuple2)

tuple3=tuple2+(10,11)
print(tuple3)

#tuples are inmutable so add more you have to do concatanation
tuple4=(3,6,9,12,15,18,21,24,27,30,33,3,3,3,3,3,3,3,3,)
print(tuple4.count(3))


#slicing
print(tuple2[2:8])