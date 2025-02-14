import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment

def convert_ogg_to_mp3():
    # Kullanıcının dosya seçmesini sağla
    file_paths = filedialog.askopenfilenames(filetypes=[("OGG Files", "*.ogg")])

    if not file_paths:
        messagebox.showwarning("Uyarı", "Hiçbir dosya seçilmedi!")
        return

    success_count = 0

    for file_path in file_paths:
        try:
            # Dosyanın dizinini ve adını al
            dir_name = os.path.dirname(file_path)
            file_name = os.path.splitext(os.path.basename(file_path))[0]

            # Çıktı dosya yolu (Aynı dizinde, sadece uzantısı .mp3 olacak)
            output_path = os.path.join(dir_name, f"{file_name}.mp3")

            # OGG dosyasını MP3'e dönüştür
            audio = AudioSegment.from_ogg(file_path)
            audio.export(output_path, format="mp3", bitrate="192k")

            success_count += 1
        except Exception as e:
            messagebox.showerror("Hata", f"{file_name}.ogg dönüştürülürken hata oluştu:\n{e}")

    messagebox.showinfo("İşlem Tamamlandı", f"{success_count} dosya başarıyla dönüştürüldü!")

# Tkinter Arayüzü
root = tk.Tk()
root.title("OGG to MP3 Dönüştürücü")
root.geometry("400x200")

label = tk.Label(root, text="OGG dosyalarını MP3'e dönüştür", font=("Arial", 12))
label.pack(pady=20)

convert_button = tk.Button(root, text="Dosya Seç ve Dönüştür", command=convert_ogg_to_mp3, font=("Arial", 10), padx=10, pady=5)
convert_button.pack()

root.mainloop()
