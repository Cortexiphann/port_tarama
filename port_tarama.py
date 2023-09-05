#FurkanFililkci
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import socket
import threading

def port_tarama():
    hedef_ip = entry_ip.get()
    baslangic_port = int(entry_baslangic_port.get())
    bitis_port = int(entry_bitis_port.get())

    progress_bar["maximum"] = bitis_port - baslangic_port + 1

    def tarama():
        acik_portlar = []

        for port in range(baslangic_port, bitis_port + 1):
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soket.settimeout(1)
            sonuc = soket.connect_ex((hedef_ip, port))
            if sonuc == 0:
                acik_portlar.append(port)
            soket.close()
            progress_bar["value"] = port - baslangic_port + 1
            root.update_idletasks()

        # Açık portlar ve işlevleri
        port_aciklama = {
            21: "FTP (File Transfer Protocol): İstemcinin bilgisayarı ile bir bilgisayar ağındaki sunucuya dosya göndermeyi sağlayan ağ protokolüdür.",
            22: "SSH (Remote Login Protocol): Uzak sunucu bağlantı protokolüdür. Güvenli iletişim kanalları gerektiren durumların tamamında kullanılabilmektedir.",
            23: "TELNET: Uzak bilgisayarların birbirleriyle haberleşmeleri, erişim ve komut verebilmeleri için telnet üzerinden haberleşme sağlanır. Dikkat edilmesi gerekir.",
            25: "SMTP (Simple E-posta Transfer Protocol): Bir e-posta göndermek için sunucu ile istemci arasındaki iletişimi sağlayan protokoldür.",
            53: "DNS (Domain Name Service): Alan isimlendirme sistemi olarak adlandırılır. İsimlerin IP’ye dönüştürülmesi maksadıyla kullanılır.",
            80: "HTTP (Hyper Text Transfer Protocol): Bilginin sunucudan kullanıcıya nasıl ve ne şekilde aktarılacağını gösteren protokoldür.",
            110: "POP3 (Post Office Protocol): Emailleri serverdan çekip lokalde saklamamıza imkân veren email protokolüdür.",
            115: "SFTP (Secure File Transfer Protocol): Güvenli dosya aktarım protokolüdür. SFTP bir SSH bağlantısından yararlanır.",
            139: "NetBIOS (Network Basic Input/Output System): LAN üzerinde farklı bilgisayarların birbiri ile iletişim kurmasını sağlayan bir protokoldür.",
            143: "IMAP (Internet Message Access Protocol): POP3 gibi mailleri yerel email istemcilerine almak için kullanılır.",
            161: "SNMP (Simple Network Management Protocol): Basit ağ yönetim protokolüdür.",
            443: "SSL (Secure Sockets Layer): Güvenli Soket Katmanı olarak da bilinir. Web sitelerine güvenli bağlantıyı sağlayan sertifikalardır.",
            445: "SMB (Server Message Blocked): Server-client arasındaki iletişimi sağlayan bir protokol. Paylaşılan dosyalara erişimi, ağlar, yazıcılar ve çeşitli bağlantıları sağlar.",
            514: "SysLog: Linux sistemlerdeki loglama yapısına verilen addır. Syslog, Linux sistemlerde yapılan her işlemin kaydının tutulduğu sistemlerdir.",
            3306: "MySQL: Uzay bilgisayarda MySQL erişim sağlayabilmek için kullanılan port numarası 3306’dır.",
            3389: "RDP (Remote Desktop Connection): Uzak Masaüstü Bağlantısıdır. Windows bulunan aynı ağdaki herhangi bir makinaya bağlanmaya yarar."
        }

        acik_port_bilgisi = [f"Port {port}: {port_aciklama.get(port, 'Bilinmeyen ama açık')}" for port in acik_portlar]

        # Tarama tamamlandığında açık portları göster ve güvenlik uyarısı ver
        sonuc_mesaji = f"{hedef_ip} üzerinde açık portlar ve işlevleri:\n\n"
        sonuc_mesaji += "\n".join(acik_port_bilgisi)
        sonuc_mesaji += "\n\nBu açık portları dikkatlice kontrol edin ve gereksiz olanları kapatın. Güvenlik önlemleri almayı unutmayın."

        messagebox.showinfo("Sonuç", sonuc_mesaji)
        progress_bar["value"] = 0

    threading.Thread(target=tarama).start()

# Ana pencere
root = tk.Tk()
root.title("Port Tarama Aracı")

# Pencere boyutu
root.geometry("400x400")  # Genişlik x Yükseklik

# IP Giriş Etiketi ve Giriş Kutusu
label_ip = tk.Label(root, text="Hedef IP:")
label_ip.pack()
entry_ip = tk.Entry(root)
entry_ip.pack()

# Başlangıç Port Etiketi ve Giriş Kutusu
label_baslangic_port = tk.Label(root, text="Başlangıç Portu:")
label_baslangic_port.pack()
entry_baslangic_port = tk.Entry(root)
entry_baslangic_port.pack()

# Bitiş Port Etiketi ve Giriş Kutusu
label_bitis_port = tk.Label(root, text="Bitiş Portu:")
label_bitis_port.pack()
entry_bitis_port = tk.Entry(root)
entry_bitis_port.pack()

# Tarama Butonu
tarama_buton = tk.Button(root, text="Tarama Başlat", command=port_tarama)
tarama_buton.pack()

# İlerleme Çubuğu
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack()

# Ana döngüyü başlat
root.mainloop()
