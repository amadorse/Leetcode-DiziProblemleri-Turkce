"""
2 listeyi birleştir ve grubun medyanini bul 
"""

nums1 = [1,2]
nums2 = [3,4]

nums1.extend(nums2) # "for döngüsü açmadan" extend metodu ile nums2 listesindeki elemanları nums1 listesine ekledik
nums1.sort()

n = len(nums1)

if n % 2 != 0:
    print(nums1[int(n/2)])

else:
    print((nums1[int(n/2)] + nums1[int(n/2) -1 ]) / 2)


'''
burada önemli olan "extend" 

'''
