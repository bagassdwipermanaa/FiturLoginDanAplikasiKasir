import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. CONFIG USERNAME & PASSWORD
# ==========================================
USERNAME_BENAR = "admin"  
PASSWORD_BENAR = "123"    

# ==========================================
# 2. FUNGSI-FUNGSI
# ==========================================
def login():
    # Ambil data dari inputan
    user = entry_username.get()
    pwd = entry_password.get()
    
    # Cek apakah username & password benar
    if user == USERNAME_BENAR and pwd == PASSWORD_BENAR:
        messagebox.showinfo("Sukses", "Login Berhasil!")
        root.withdraw() # Tutup jendela login
        buka_kasir()    # Buka jendela kasir
    else:
        messagebox.showerror("Gagal", "Username atau Password Salah!")

def buka_kasir():
    # Buat jendela baru untuk Kasir
    kasir_window = tk.Toplevel()
    kasir_window.title("tk") 
    kasir_window.geometry("300x500")
    
    # --- UI KASIR ---
    tk.Label(kasir_window, text="Nama Pembeli").pack(pady=(10,0))
    entry_nama = tk.Entry(kasir_window)
    entry_nama.pack()

    tk.Label(kasir_window, text="Nama Barang:").pack(pady=(5,0))
    entry_barang = tk.Entry(kasir_window)
    entry_barang.pack()

    tk.Label(kasir_window, text="Jumlah Produk: (Angka)").pack(pady=(5,0))
    entry_jumlah = tk.Entry(kasir_window)
    entry_jumlah.pack()

    tk.Label(kasir_window, text="Harga Produk: (Angka)").pack(pady=(5,0))
    entry_harga = tk.Entry(kasir_window)
    entry_harga.pack()

    tk.Label(kasir_window, text="Uang Pembeli: (Angka)").pack(pady=(5,0))
    entry_bayar = tk.Entry(kasir_window)
    entry_bayar.pack()

    # Fungsi Hitung dan Cetak Invoice
    def cetak_invoice():
        try:
            # Validasi input harus angka
            if not entry_jumlah.get().isdigit() or not entry_harga.get().isdigit() or not entry_bayar.get().isdigit():
                messagebox.showerror("Error", "Jumlah, Harga, dan Uang harus berupa Angka!")
                return

            # Ambil data
            nama_pembeli = entry_nama.get()
            nama_barang = entry_barang.get()
            jumlah = int(entry_jumlah.get()) 
            harga = int(entry_harga.get())   
            bayar = int(entry_bayar.get())   
            
            # Hitung
            total_belanja = jumlah * harga
            kembali = bayar - total_belanja
            
            # Cek uang cukup atau tidak
            if bayar < total_belanja:
                messagebox.showwarning("Warning", "Uang pembeli kurang!")
                return

            # Format Text Invoice (Sesuai Screenshot)
            invoice_text = f"""
Nama Pembeli = {nama_pembeli}
===================================
Nama Barang = {nama_barang}
Jumlah Barang = {jumlah}
Harga Rp. {harga}
===================================
Total = Rp. {total_belanja}
Tunai = Rp. {bayar}
-----------------------------------
Kembali = Rp. {kembali}

Terima Kasih Telah Berbelanja!!
            """
            
            # Tampilkan Invoice
            messagebox.showinfo("Invoice", invoice_text)
            
        except Exception:
            messagebox.showerror("Error", "Terjadi kesalahan input data.")

    # Tombol Total
    tk.Button(kasir_window, text="Total", command=cetak_invoice, width=10).pack(pady=20)

# ==========================================
# 3. MAIN PROGRAM (JENDELA UTAMA LOGIN)
# ==========================================
root = tk.Tk()
root.title("tk") 
root.geometry("300x250")

tk.Label(root, text="Username").pack(pady=(20,0))
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack(pady=(10,0))
entry_password = tk.Entry(root, show="*") 
entry_password.pack()

tk.Button(root, text="Login", command=login, width=10).pack(pady=20)

root.mainloop()