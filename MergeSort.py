def MergeSort(My_List):
    if len(My_List) > 1:
        mid=len(My_List)//2
        left=My_List[:mid]
        right=My_List[mid:]

        MergeSort(left)
        MergeSort(right)

        i=0
        j=0

        k=0

        while i< len(left) and j < len(right):
            if left[i] <= right[j]:
               My_List[k] = left[i]
               i += 1
            else:
                My_List[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
            My_List[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            My_List[k]=right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    n=int(input())
    My_List=[]
    for i in range(n):
        My_List.append(int(input()))
    
    MergeSort(My_List)
    print(My_List)

    