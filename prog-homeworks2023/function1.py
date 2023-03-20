start=int(input("Введите первое значение"))
end=int(input("Введите второе значение"))
sum=0
if start>end:
    start,end=end,start
def sum_range(start,end,sum):
    while start<end:
        sum+=end
        end-=1
    return sum+start
print(sum_range(start,end,sum))
