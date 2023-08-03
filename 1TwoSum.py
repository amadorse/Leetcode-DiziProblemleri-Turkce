# Buradaki tek olay 2 tane for döngüsünü iç içe kullanmak 

# nums listesinde toplamı "target" a eşit olan 2 tane elemanın index lerini yazdır 

nums = [2,7,11,15] # örnek = 0,1 
target = 9


for i in range(len(nums)):
    
    for j in range(i+1, len(nums)): 
        # range(-->i+1<--, len(nums)) yazarak  sırası gelen index'i ve sonraki indexleri almamızı sağlıyor
        # yani yanlışlıkla index 1  ile index 1 'i toplamıyoruz  
        
        if nums[i] + nums[j] == target:
            print(f"{i}, {j}")


"""
"range" nasil kullanilir??

range(başlangiç sayisi, bitiş sayisi, ardişik atlanacak sayi)



"""