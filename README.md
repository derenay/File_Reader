# Directory Watcher - C++ ile Dosya İzleme ve Güncelleme Aracı

Bu proje, belirli bir dizindeki dosyaları periyodik olarak tarayan ve dizindeki değişiklikleri algılayarak `config.txt` dosyasını otomatik olarak güncelleyen çok iş parçacıklı (multi-threaded) bir C++ uygulamasıdır.

## 🧠 Özellikler

- Belirtilen dizindeki tüm dosyaların yolunu okur (`recursive_directory_iterator` ile).
- `config.txt` dosyasını izleyerek içerik değişimlerini algılar.
- Dosya listesindeki herhangi bir değişiklikte `config.txt`'yi günceller.
- `mutex` ile thread-safe okuma/yazma.
- Gerçek zamanlı değişiklik takibi (`std::thread` ve `std::chrono` kullanılarak).


## 🛠️ Gereksinimler

- C++17 veya üzeri
- Derleyici: GCC / Clang / MSVC
- `std::filesystem` desteği (C++17 ile gelmiştir)

## 🚀 Derleme ve Çalıştırma

### 1. Derleme

```bash
g++ -std=c++17 -pthread -o directory_watcher main.cpp


📌 Nasıl Çalışır?
Uygulama, gelen_fotograflar/ dizinindeki dosya yollarını alır.

Bu yolları config.txt dosyasındaki mevcut liste ile karşılaştırır.

Eğer fark varsa, config.txt dosyasını yeni içerikle günceller.

Arka planda sürekli olarak config.txt okunarak değişiklikler izlenir (başka bir uygulama bu dosyayı değiştirirse, algılanır).

📷 Kullanım Senaryosu
Bu uygulama aşağıdaki gibi senaryolarda kullanılabilir:

Gerçek zamanlı olarak yeni fotoğrafların sisteme gelip gelmediğini izlemek.

Bir başka yazılımın config.txt üzerinden gelen verilerle çalışmasını sağlamak.

Dosya değişikliklerini loglamak veya tetikleyici olarak kullanmak.

🛡️ Güvenlik ve Performans
Çok iş parçacıklı yapısı sayesinde izleme ve güncelleme işlemleri aynı anda çalışır.

mutex kullanımı ile veri tutarlılığı sağlanır.

2 saniyelik izleme döngüsü ile sistem performansına zarar vermez.

📄 Lisans
Bu proje MIT lisansı ile lisanslanmıştır.

👤 Geliştirici
İsim: Erenay ARSAL

GitHub: [github.com/derenay
