
# CodinNinja - https://www.codingninjas.com/studio/problems/sorted-array_6613259?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM&count=25&page=1&search=&sort_entity=order&sort_order=ASC
# Complexity - O(n1+n2) Space = O(1)
# Brute Force solution:
#    Use Set where you insert all the elements for wach array one by one into a singel set and return the final set
#    Complexity: O(n1logn +n2logn) + O(n1+n2)(to return)    
# Optimal Solution

def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    p1 = 0
    p2 = 0
    n1 = len(a)
    n2 = len(b)
    union_list = []
    if a[p1]< b[p2]:
        union_list.append(a[p1])
        p1 += 1
    else:
        union_list.append(b[p2])
        p2 += 1
    while (p1 < n1 and p2 < n2):
        if a[p1] < b[p2]:
            if union_list[-1] != a[p1]:
                union_list.append(a[p1])
            p1 += 1
        elif a[p1] > b[p2]:
            if union_list[-1] != b[p2]:
                union_list.append(b[p2])
            p2 += 1
        else:
            if union_list[-1] != a[p1]:
                union_list.append(a[p1])
            p1 += 1
            p2 += 1

    while p1 < n1:
        if union_list[-1] != a[p1]:
            union_list.append(a[p1])
        p1 += 1

    while p2 < n2:
        if union_list[-1] != b[p2]:
            union_list.append(b[p2])
        p2 += 1
    return union_list
