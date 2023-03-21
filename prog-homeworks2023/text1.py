a=str(input("Введите предложение"))
predlozh=a.split()
n=0
kbukv=0
slovo1=''
slovo2=''
for i in range(0, len(predlozh)):
    if predlozh.count(predlozh[i])>n:
        n=predlozh.count(predlozh[i])
        slovo1=predlozh[i]
    if len(a.split()[i])>kbukv:
        kbukv=len(a.split()[i])
        slovo2=a.split()[i]
print(slovo1, "встречается в тексте", n, "раз,", slovo2, "является самым длинным словом с длиной в", kbukv,"букв")
