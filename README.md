# Port Tarama Aracı

Bu proje, Python ve tkinter kullanarak belirli bir IP adresi üzerindeki açık portları taramak ve bu portların ne işe yaradığını belirlemek için bir araç sunar. Ayrıca, kullanıcılara bu açık portların güvenliği hakkında bilgi verir.

## Kullanım

1. Proje dosyalarını bilgisayarınıza indirin veya bu repo'yu klonlayın.

2. Projeyi başlatmak için `port_tarama.py` dosyasını çalıştırın.

3. Açılan pencerede aşağıdaki bilgileri girin:
   - Hedef IP adresi
   - Başlangıç Port numarası
   - Bitiş Port numarası

4. "Tarama Başlat" düğmesine tıklayarak taramayı başlatın.

5. Tarama tamamlandığında, açık portlar ve bunların işlevleri hakkında bilgi içeren bir pencere görünecektir.

## Açık Portlar ve İşlevleri

Bu projede aşağıdaki portlar ve işlevleri tanımlanmıştır:

- **Port 21 (FTP - File Transfer Protocol):** Dosya transferi için kullanılır.
- **Port 22 (SSH - Remote Login Protocol):** Uzak sunucu bağlantı protokolüdür.
- **Port 23 (TELNET):** Uzak bilgisayarların haberleşmesini sağlar.
- **Port 25 (SMTP - Simple E-posta Transfer Protocol):** E-posta göndermek için kullanılır.
- **Port 53 (DNS - Domain Name Service):** Alan isimlendirme sistemi olarak kullanılır.
- **Port 80 (HTTP - Hyper Text Transfer Protocol):** Web sayfalarının görüntülenmesini sağlar.
- **Port 110 (POP3 - Post Office Protocol):** E-posta alımı için kullanılır.
- **Port 115 (SFTP - Secure File Transfer Protocol):** Güvenli dosya aktarım protokolüdür.
- **Port 139 (NetBIOS - Network Basic Input/Output System):** LAN üzerinde bilgisayarlar arasında veri paylaşımı için kullanılır.
- **Port 143 (IMAP - Internet Message Access Protocol):** Mailleri yerel email istemcilerine almak için kullanılır.
- **Port 161 (SNMP - Simple Network Management Protocol):** Basit ağ yönetim protokolüdür.
- **Port 443 (SSL - Secure Sockets Layer):** Güvenli bağlantı sağlar.
- **Port 445 (SMB - Server Message Blocked):** Server-client iletişimini sağlar.
- **Port 514 (SysLog):** Linux sistemlerde loglama yapısına verilen addır.
- **Port 3306 (MySQL):** Veritabanı yönetim sistemidir.
- **Port 3389 (RDP - Remote Desktop Connection):** Uzak Masaüstü Bağlantısıdır.

## Sonuç

Bu projeyi kullanarak hedef IP adresinizdeki açık portları taramak ve bu portların ne işe yaradığını öğrenmek için kullanışlı bir araç elde edersiniz. Ayrıca, güvenlik açıklarını kapatma ve gereksiz portları devre dışı bırakma konularında bilinçlenmiş olursunuz.

**Not:** Bu projeyi kullanırken, port taramanın yasal ve etik sınırlarını aşmadığınızdan emin olun ve sadece kendi ağlarınızda veya izin verilen sistemlerde kullanın.
