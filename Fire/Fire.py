import tkinter as tk
from tkinter import filedialog
import cv2
import math
from PIL import Image, ImageTk
from ultralytics import YOLO

# Videoyu yüklemek için fonksiyon
def choose_video():
    file_path = filedialog.askopenfilename(title="Select a video file",
                                           filetypes=[("Video files", "*.mp4")])
    if file_path:
        print("Seçilen video dosyası:", file_path)
    return file_path

# Videoyu oynatmak için fonksiyon
def play_video(video_source=None):
    if video_source is not None:
        cap = cv2.VideoCapture(video_source)

        # Video dosyasının genişlik ve yüksekliğini al
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Video dosyasını oluştur ve ayarlarını belirle
        out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

        model = YOLO("best.pt")  # Kendi verisetiyle eğittiğim YOLO modelini yükleme
        classNames = ["Fire"]  # Sınıf ismini belirleme

        while cap.isOpened():
            ret, img = cap.read()  # Kameradan bir kare okuma

            if ret:
                # YOLOv8 kullanarak kareleri tespit etme
                # stream = True, daha verimli bir şekilde çalışmasını sağlar
                # conf=0.6, modelin tahmini gerçek bir tahmin olarak kabul edeceği minimum puandır ve
                # 0.6 değeri yüzde 60'ın üstündeki emin olunan tahminleri gösterir
                results = model(img, stream=True, conf=0.60)

                # Tespit sonuçlarını kontrol etme
                for r in results:
                    # Her bir tespit sonucunda sınırlayıcı kutuları alırız"
                    boxes = r.boxes
                    # Her bir sınırlayıcı kutu için işlemleri yapma
                    for box in boxes:
                        # tespit etiketinin koordinatlarını alıp dikdörtgen çizme
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        print(x1, y1, x2, y2)
                        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                        # Güven değerini alıp yazdırma
                        conf = math.ceil((box.conf[0]*100))/100
                        cls = int(box.cls[0])
                        class_name = classNames[cls]
                        label = f'{class_name}{conf}'
                        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2)[0]

                        # Etiketin boyutunu hesaplayıp arkaplanı çizme
                        c2 = x1 + t_size[0], y1 - t_size[1]-3
                        cv2.rectangle(img, (x1, y1), c2, [255, 0, 255],-1, cv2.LINE_AA)

                        # Etiketi yazma
                        cv2.putText(img, label, (x1, y1), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

                # Görüntüyü video dosyasına yazma
                cv2.imshow("Image", img)
                out.write(img)

                # '1' tuşuna basıldığında döngüyü sonlandırma hangi tuş isterseniz yazabilirsiniz ---> ord('1')
                if cv2.waitKey(1) & 0xFF == ord('1'):
                    break

        # Video yazma nesnesini serbest bırakma


        out.release()
        # Video oynatıcısını ve tüm pencereleri kapatma
        cap.release()
        cv2.destroyAllWindows()

# Arayüzü oluştur

root = tk.Tk()
root.title("Yangın Tespit Sistemi")
root.geometry("800x600")
root.iconbitmap("Fire-icon_30333.ico")

# Arka plana foto eklemek için Canvas oluştur
background_image = Image.open("pexels-pixabay-70573.jpg")
background_image = background_image.resize((800, 600), Image.BICUBIC)  # Arka plan resmini boyutlandır
background_image = ImageTk.PhotoImage(background_image)

# Arka plan resmini canvas'a ekle
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)


# Başlık metni
title_label = tk.Label(root, text="Fire Detection", font=("Helvetica", 30))
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

created_by_text = "created by Cemil Can"
created_by_label = tk.Label(root, text=created_by_text, font=("Helvetica", 10, "italic"))
created_by_label.place(relx=0.99, rely=0.99, anchor=tk.SE)

# Videoyu seçme butonu
select_button = tk.Button(root, text="\U0001F4C1 Select Video", font=("Helvetica", 14), command=lambda: play_video(choose_video()))
select_button.place(relx=0.62, rely=0.5, anchor=tk.CENTER)
# Gerçek zamanlı tespit butonu
live_button = tk.Button(root,  text="\U0001F4F9 Live Detection", font=("Helvetica", 14), command=lambda: play_video(0),  borderwidth=2)
live_button.place(relx=0.3, rely=0.5, anchor=tk.W)
# Çıkış butonu
quit_button = tk.Button(root, text="\u2716 Quit", font=("Helvetica", 14), command=root.destroy)
quit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Arayüzü çalıştır
root.mainloop()