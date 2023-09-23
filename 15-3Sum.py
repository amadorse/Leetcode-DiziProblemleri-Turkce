def three_sum(nums):
    nums.sort()  # Dizi sıralama
    result = []  # Sonuçları tutacak boş liste
    
    for i in range(len(nums) - 2):  # Ana döngü


        #----1 !!!!!!!!!!Tekrar Bak
        if i > 0 and nums[i] == nums[i - 1]:  # Tekrarlanan üçlü kombinasyonları engellemek
            continue
        #----1  


        left, right = i + 1, len(nums) - 1  # İki işaretçi yöntemi için sol ve sağ işaretçiler
        
        while left < right:  # İşaretçiler birbirine yaklaşıncaya kadar devam eden döngü
            total = nums[i] + nums[left] + nums[right]  # Üç elemanın toplamını hesapla 




           #----2
           # Örnek olarak nums = [0,1,1,1,2,3,4,4] olsun ve left = 1 olsun (burada left üzerinden gideceğim)
           # aşağıda while loop yerine if kontrolcüsü açsaydık 
           # left +1 olucaktı fakat nums[left+2]= nums[left]  eşit olduğundan dolayı yine aynı elemanda kalıcaktık 
           # Bizim burada while açmamızın sebebi nums[left]' in değişmesini istememiz  

            if total == 0:  # Toplam 0'a eşitse, üçlü kombinasyonu bulduk
                result.append([nums[i], nums[left], nums[right]])  # Sonuca ekle
                
                # Tekrarlanan ikinci ve üçüncü elemanları engellemek için işaretçileri hareket ettir
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
           #----2


            elif total < 0:  # Toplam 0'dan küçükse, sol işaretçiyi sağa hareket ettir
                left += 1

            else:  # Toplam 0'dan büyükse, sağ işaretçiyi sola hareket ettir
                right -= 1
    
    return result  # Tüm üçlü kombinasyonları içeren sonuç listesini döndür

# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 1, 1]))              # Output: []
print(three_sum([0, 0, 0]))              # Output: [[0, 0, 0]]
