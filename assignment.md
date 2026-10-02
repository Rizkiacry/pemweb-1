LAPORAN 1 PEMROGRAMAN WEB
LAPORAN TEORI
Basic Difference: Jelaskan perbedaan mendasar antara HTML (HyperText Markup Language) dengan bahasa pemrograman logika (seperti Java atau C++) dari segi function dan code execution method-nya!
Semantic Tags: Jelaskan mengapa penggunaan semantic tags HTML5 (seperti header, nav, main, article, aside, dan footer) lebih recommended dibanding terus-menerus pakai tag div atau span tanpa henti! Give minimal 2 reasons (misalnya dari sisi SEO atau accessibility).
Image Alt Attribute: Mengapa saat embedding image (img) di dokumen HTML sangat disarankan untuk selalu memasukkan atribut alt? What happens kalau file gambarnya gagal load (broken image)?
Types of HTML Lists: Sebutkan 3 jenis list pada HTML (ol, ul, dl) beserta builder tags-nya, dan jelaskan dalam kondisi seperti apa masing-masing jenis list tersebut paling tepat digunakan!
Links and Attributes: Jelaskan perbedaan antara Internal Link dan External Link pada penggunaan tag a, serta jelaskan function dari atribut target="_blank"!
Multimedia Tags: Jelaskan fungsi dari atribut controls, autoplay, dan loop pada tag multimedia video dan audio! What is the purpose of the source element inside those media tags?
LAPORAN PRAKTIKUM
Kerjakan pembuatan sebuah simple website yang terdiri dari dua halaman (pages) sesuai ketentuan di bawah ini. All code harus diketik secara manual biar kalian bisa menentukan HTML element yang paling pas untuk setiap kebutuhan.
A. Folder Structure
Prepare a folder named NIM_NAMA_KELAS yang berisi 5 file berikut. Penulisan file name pada kode harus identical dengan nama file sebenarnya, baik case-sensitivity (huruf besar-kecil) maupun spacing-nya.
LAPRAK1_NIM/
index.html
pendaftaran.html
Logo multi.png
video.mp4
audio.mp3

B. Homepage (index.html)
Framework and Layout Structure: Build kerangka dokumen HTML versi terbaru yang mengatur bahasa Indonesia sebagai bahasa utamanya, dengan browser tab title: Laprak 1 Lab Multi - Beranda. Di bagian page body, susun area-area berikut dari atas ke bawah: header, navigation area, horizontal divider (hr), main content, sidebar, horizontal divider, dan footer. Use elements whose semantic meaning matches the function of each area.
Main Heading: Inside the header, tampilkan judul paling besar (heading level 1): Laporan Praktikum Laboratorium Multimedia.
Navigation Menu: Create 3 links yang dipisahkan oleh karakter garis tegak (|):
Beranda -> link ke index.html.
Pendaftaran -> link ke pendaftaran.html.
Web ITPLN -> link ke https://itpln.ac.id https://itpln.ac.id dan dibuka di new window/tab yang diberi nama ITPLN_WEB.
First Article: Pada main content, buat satu artikel yang diawali sub-heading level 2 Selamat Datang Di Laboratorium Multimedia. Lalu masukkan gambar logo lab yang sudah disediakan (alt text: Logo Lab, width: 120px). Setelah itu, buat 1 paragraf buatan sendiri yang memuat 4 frasa berikut dengan text styling masing-masing:
praktikum mahasiswa -> tampil bold dan bermakna sangat penting.
Harap menjaga kebersihan! -> tampil italic dan bermakna ditekankan.
Dilarang makan -> tampil strikethrough (dicoret) sebagai deleted text.
Dilarang membawa makanan dan minuman -> tampil underlined sebagai inserted text.
Second Article: Buat artikel lain dengan sub-heading level 2 Media Informasi yang berisi 2 bagian:
Sub-heading level 3 Video Profil, diikuti video player berukuran 320 x 240 piksel lengkap dengan tombol control, bersumber dari video.mp4 (type=video/mp4), dan fallback text: Browser Anda tidak mendukung tag video.
Note: Isi video adalah screen recording kalian saat menjelaskan code structure HTML pada laporan praktikum ini.

Sub-heading level 3 Audio, diikuti audio player dengan tombol control, bersumber dari audio.mp3 (type=audio/mpeg), dan fallback text: Browser Anda tidak mendukung tag audio.. Untuk jenis/bentuk audionya bebas (internal/external), tapi audio track-nya gunakan lagu Sunroof - Nicky Youre, dazy.
Sidebar: Outside the main content, sediakan panel samping (sidebar) berisi sub-heading level 3 Pengumuman dan paragraf: Praktikan wajib menggunakan Almamater saat praktikum berlangsung, dan menaati seluruh peraturan Laboratorium.
Footer: Tuliskan copyright notice menggunakan simbol © (pakai HTML entity-nya), tahun 2026, lalu diikuti Nama_NIM Kalian.
C. Registration Page (pendaftaran.html)
Framework and Navigation: Buat kerangka dokumen dengan browser tab title: Laporan Praktikum - Pendaftaran. At the very top, letakkan navigation menu berisi Beranda (index.html) dan Pendaftaran (pendaftaran.html), diikuti horizontal divider (hr).
Heading: Buat sub-heading level 2: Form Pendaftaran Praktikan.
Form Setup: Buat form dengan method post dan action URL dikosongkan (action=). Layout isian harus menggunakan tabel 2 kolom: label di kolom kiri, sedangkan kolom kanan diawali tanda titik dua (:) baru input field-nya.
Form Field Details:
No 1 Label Nama Lengkap Input Type / Field Description Single-line text input biasa name Attribute Value nama
No 2 Label Password Input Type / Field Description Password input (karakter disamarkan) name Attribute Value pass
No 3 Label NIM Input Type / Field Description Number input (hanya terima angka) name Attribute Value nim
No 4 Label Tanggal Lahir Input Type / Field Description Date picker (menampilkan pop-up kalender) name Attribute Value tgl
No 5 Label Jenis Kelamin Input Type / Field Description Radio button (2 pilihan: Laki-Laki dengan value=L, Perempuan dengan value=P) name Attribute Value jk
No 6 Label Minat bidang Input Type / Field Description Checkbox (3 pilihan: Web dengan value=web, Jaringan dengan value=network, Design/Modeling) name Attribute Value minat
No 7 Label Program Studi Input Type / Field Description Dropdown select menu: S1 Teknik Informatika (value=IF) dan S1 Sistem Informasi (value=SI) name Attribute Value prodi
No 8 Label Alasan Mendaftar Input Type / Field Description Textarea (3 rows dan 20 cols) name Attribute Value alasan
No 9 Label (dikosongkan) Input Type / Field Description Submit button berlabel Kirim dan Reset button berlabel Reset name Attribute Value -
Important Note: Pada baris nomor 5 (Jenis Kelamin), kedua pilihan radio button wajib menggunakan nilai atribut name yang sama supaya bersifat single-choice (hanya 1 yang bisa dipilih).

D. Expected Results (Hasil yang Diharapkan)
Homepage (index.html)
Top area menampilkan main title, menu Beranda | Pendaftaran | Web ITPLN, dan divider line.
First article menampilkan sapaan, logo, dan paragraf dengan 4 jenis text styling (bold, italic, strikethrough, underline).
Video player dan audio player tampil dengan baik dan playable.
Section Pengumuman muncul di bawah main content, lalu diakhiri divider line dan footer.
Link Web ITPLN membuka website ITPLN pada tab/window terpisah.
Registration Page (pendaftaran.html)
Form layout tersusun rapi dalam 2 kolom.
Field password menyamarkan masukan, field NIM number-only, dan field tanggal lahir memunculkan calendar pop-up.
Radio button jenis kelamin hanya bisa dipilih salah satu, sedangkan checkbox minat bidang bisa dicentang multiple items sekaligus.
Reset button berfungsi mengosongkan seluruh isi form. Submit button hanya akan refresh/reload halaman karena belum terhubung ke backend processing/server-side.
