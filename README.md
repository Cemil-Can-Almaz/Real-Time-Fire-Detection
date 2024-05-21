# Yangın Tespit Sistemi
Bu proje, YOLOv8 nesne algılama algoritması kullanılarak yangın tespiti yapmak için eğitilmiş bir model içerir.

## Kurulum
#### Projenin çalıştırılması için Python ve diğer gerekli kütüphanelerin yüklenmesi gerekmektedir. Aşağıdaki komutlarla gerekli bağımlılıkların yüklenmesi sağlanabilir:

``` pip install -r requirements.txt```

 ### Ayrıca, projeye bir arayüz eklendi. Arayüz, kullanıcıların kolayca yangın tespiti yapmasını sağlar.
 
 ![image](https://github.com/cemilcan99/Real-Time-Fire-Detection/assets/65957701/9ad49428-6d5e-48e8-aee5-2cc7431a6db4)


 ## Arayüz Kurulumu

Arayüz, Tkinter kütüphanesi kullanılarak yapılmıştır. Eğer bilgisayarınızda Tkinter yüklü değilse, aşağıdaki komutları kullanarak yükleyebilirsiniz:


```pip install tk```

## Arayüz Kullanımı

Yangın tespit sistemi arayüzünü kullanmak için aşağıdaki adımları izleyin:

1. Proje dosyalarını bilgisayarınıza indirin.
2. Ana dizinde bulunan "Fire.py" dosyasını çalıştırın.
3. Video ile tespit için arayüz penceresi açıldığında, "Select Video" düğmesine tıklayarak istediğiniz video dosyasını seçin.
4. Gerçek zamanlı tespit için arayüz penceresi açıldığında "Live Detection" düğmesine tıklayarak tespiti başlatabilirsiniz.
5. Video otomatik olarak oynatılacak ve yangın tespiti işlemi başlayacaktır.
6. İşlem tamamlandığında, videoyu kapatmak için klavyeden "1" tuşuna basın ve arayüzü kapatmak için "Quit" düğmesine tıklayın.


