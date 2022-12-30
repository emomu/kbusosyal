# kbusosyal
karabuk universitesinin sosyal medyası


sitenin demo linki için buyrun siteyi denemeyi unutmayın denedikten sonra hata bulursanız sitenin içerisinden keşfete yazın ben bulurum sizi
[site linki](http://sosyalkbu2.pythonanywhere.com/)


sitenin kodlarını kullanmak mı istiyorsunuz?
ilk önce siteyi indirin ya da git'i indirip komut satırına bu komudu yazın
```
git clone https://github.com/emomu/kbusosyal.git
 ```

 
 
siteyi açmak için ilk bilgisayarınıza sanal makine kurmanız gerekmektedir o da şöyle olur
```
pip install virtualenv
```

sanal makineyi kurmak için şu komudu yazın
```
virtualenv venv
```
 
tebrikler artık sizin bir sanal makineniz var peki nasıl açacaksınız?
```
venv/Scripts/activate
```
 
tamamdır şimdi  gerekli modülleri indirmeniz gerekir
```
pip install django
pip install asgiref==3.6.0
pip install sqlparse==0.4.3
pip install tzdata==2022.7
```
 
bunları indirdikten sonra komut satırına şunları yazın:
```
python manage.py makemigrations
python manage.py migrate
```
 
artık hazırsınız tek yapmanız gereken siteyi açmak!
```
python manage.py runserver
```
 
tebrikler!


site şuan demo sürümündedir geliştirilmeye devam ediliyor

<img width="959" alt="Ekran görüntüsü 2022-12-30 055604" src="https://user-images.githubusercontent.com/121471344/210030318-e4fab9d6-c665-47ef-b452-6f5cdbfc6ffc.png">


<img width="946" alt="Ekran görüntüsü 2022-12-30 055705" src="https://user-images.githubusercontent.com/121471344/210030286-b5caacda-547f-4ce7-8354-6660972c3a00.png">

<img width="960" alt="Ekran görüntüsü 2022-12-30 060052" src="https://user-images.githubusercontent.com/121471344/210030293-34391eb7-3ecc-46d8-b15a-d032ce12f1af.png">


<img width="960" alt="Ekran görüntüsü 2022-12-30 060004" src="https://user-images.githubusercontent.com/121471344/210030185-e0fcbe8a-3ba3-46c9-bc97-f64c3fe2025a.png">

<img width="960" alt="Ekran görüntüsü 2022-12-30 060032" src="https://user-images.githubusercontent.com/121471344/210030188-32eeee16-c0cd-4cc2-884f-54245509ba36.png">
<img width="960" alt="Ekran görüntüsü 2022-12-30 060104" src="https://user-images.githubusercontent.com/121471344/210030299-1e2f0749-27f6-4ba4-98f4-d1005ad3db08.png">



  
