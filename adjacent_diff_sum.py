def adjacent_diff_sum(n,arr,position):
    total_sum=0
    for i in range(position,n-1):
        diff = abs(arr[i]-arr[i+1])
        total_sum+=diff
    return total_sum

n=int(input("Enter the no. of element: "))
arr=list(map(int,input().split()))
position = int(input("Enter the position: "))
print(adjacent_diff_sum(n,arr,position))
