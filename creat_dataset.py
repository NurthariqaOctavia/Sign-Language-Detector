import cv2
import os

def create_dataset(output_path, label, num_samples):
    # Membuka kamera
    cap = cv2.VideoCapture(0)
    
    # Membuat folder jika belum ada
    output_folder = os.path.join(output_path, label)
    os.makedirs(output_folder, exist_ok=True)
    
    # Mengambil gambar dari webcam
    for i in range(num_samples):
        ret, frame = cap.read()
        cv2.imshow('Capturing Images (Press "q" to stop)', frame)
        
        # Simpan gambar
        image_path = os.path.join(output_folder, f"{label}_{i}.jpg")
        cv2.imwrite(image_path, frame)
        
        # Tunggu 100 milidetik (0.1 detik)
        cv2.waitKey(100)

    # Menutup kamera dan jendela
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Atur parameter sesuai kebutuhan Anda
    output_path = "C:/Users/TODAY/VSCode/Deteksi/dataset"  # Folder tempat dataset akan disimpan
    label = "A"        # Label untuk gambar yang diambil
    num_samples = 100        # Jumlah gambar yang akan diambil
    
    # Membuat dataset
    create_dataset(output_path, label, num_samples)
