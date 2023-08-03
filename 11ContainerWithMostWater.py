'''
SUYUN EN FAZLA KAPLAYABİLECEĞİ ALANI BUL 
'''
nums = [1,8,6,2,5,4,8,3,7]

n = len(nums)
right = n - 1
left = 0 
max_area = 0

while right > left:
    
    # 2 index arasındaki uzunluğu hesapladık
    width = right - left 
    # listede seçilen 2 sayı arasından en küçük olanı aldık çünkü suyun yüksekliği en fazla kısa olan sayı kadar yukarıya çıkabilir
    current_height = min(nums[left], nums[right])

    # area adında bir değişken oluşturuyoruz ve maximum dolabilecek su alanını hesaplıyoruz 
    # degisken = max(degisken, sıradaki alan)
    area = width * current_height # taban * yükseklik
    max_area = max(max_area, area)
    # max_area ve area'yı kıyaslıyor en büyük olanı max_area adına değişkene atıyor 
    # böylelikle sadece area max_area'dan büyükse max_area değişiyor 
    


    if nums[left] < nums[right]:
        # hangi eleman daha küçükse(kısaysa) o elemanı değiştiriyoruz 
        # çünkü alan hesabında (taban * -->yükseklik<--)  
        # değiştirince taban 1 birim azalıyor ancak yüksekliği artırmaya çalıştığımız için
        # yine en yüksek olan alanı bulabiliyoruz  
        left +=1
    else:
        right -=1
print(max_area)