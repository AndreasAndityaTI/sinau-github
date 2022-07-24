subnet_biner=[]
prefix=int(input("Masukkan prefix : "))
subnet_biner_=""
for i in range(prefix+1):
    subnet_biner+="1"
    if len(subnet_biner)%9==0:
        subnet_biner+="."
    
while len(subnet_biner)<36:
    subnet_biner+="0"
#

subnet_biner.remove(subnet_biner[0])



for x in subnet_biner:
    subnet_biner_+=x
# print(len(subnet_biner))
subnet_list=subnet_biner_.split(".")
# print(subnet_list[0])
desimal_1=int(subnet_list[0],2)
desimal_2=int(subnet_list[1],2)
desimal_3=int(subnet_list[2],2)
desimal_4=int(subnet_list[3],2)
# desimal=0
# for g in range (len(subnet_list[0])):
#     if g[0]=="1":
#         desimal+=256
# print(desimal)

print((subnet_biner_))
print(subnet_list)
print("{}.{}.{}.{}".format(desimal_1,desimal_2,desimal_3,desimal_4))
print(len(subnet_biner_))

