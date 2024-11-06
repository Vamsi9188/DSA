# Find The minimum distance between stalls when cows are moved using Binary Search

def aggCows(stalls,cows):
    stalls.sort()
    l=0
    r=stalls[-1]
    minDist=None
    while l<=r:
        mid=(l+r)//2
        if check(stalls,cows,mid):
            minDist=mid
            l=mid+1
        else:
            r=mid-1
    return minDist
def check(stalls,cows,minDist):
    last_stall_used=stalls[0]
    cows -=1
    for stall in stalls:
        if stall-last_stall_used>=minDist:
            cows -= 1
            last_stall_used = stall
            if cows == 0:
                return True
    return  False
stalls = [1,2,8,4,9]
cows=3
print("The minimum distance between stalls is",aggCows(stalls,cows))