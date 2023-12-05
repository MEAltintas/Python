def quick(array):
    if(len(array)<=1):
        return array
    else:
        pivot=array[len(array)//2]
        left=[i for i in array if i<pivot]
        middle=[i for i in array if i==pivot]
        right=[i for i in array if i>pivot]
        return quick(left)+middle+quick(right)

dizi1=[1,5,7,9,2,4,3]
print(quick(dizi1))