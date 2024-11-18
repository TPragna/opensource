class Solution:
    def merge(self, m: List[int], a: int, n: List[int], b: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=0,0
        res=[]
        while i<a and j<b:
            if m[i]<=n[j]:
                res.append(m[i])
                i+=1
            else:
                res.append(n[j])
                j+=1
        while i<a:
            res.append(m[i])
            i+=1
        while j<b:
            res.append(n[j])
            j+=1
        for i in range(0,(a+b)):
            m[i]=res[i]
