import tkinter as tk
from tkinter import ttk

def openMahasiswa():
    f = open("mahasiswa.txt", "r")
    for line in f:
        field = line.split(";")
        nim_mhsw.append(field[0])
        nama_mhsw.append(field[1])
        username_mhsw.append(field[2])
        password_mhsw.append(field[3])
    f.close()


def openMatkul():
    f = open("matkul.txt", "r")
    for line in f:
        field = line.split("\n")
        matkul_slrh.append(field[0])
    f.close()


def openNilai_Tugas():
    f = open("nilaitgs.txt", "r")
    for line in f:
        field = line.split(";")
        nim_tgs.append(field[0])
        nama_mhsw_tgs.append(field[1])
        matkul_tgs.append(field[2])
        nilai_tgs.append(field[3])
    f.close()


def openNilai_UTS():
    f = open("nilaiuts.txt", "r")
    for line in f:
        field = line.split(";")
        nim_uts.append(field[0])
        nama_mhsw_uts.append(field[1])
        matkul_uts.append(field[2])
        nilai_uts.append(field[3])
    f.close()


def openNilai_UAS():
    f = open("nilaiuas.txt", "r")
    for line in f:
        field = line.split(";")
        nim_uas.append(field[0])
        nama_mhsw_uas.append(field[1])
        matkul_uas.append(field[2])
        nilai_uas.append(field[3])
    f.close()

def gradeHuruf(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 85:
        return "A-"
    elif nilai >= 80:
        return "B+"
    elif nilai >= 75:
        return "B"
    elif nilai >= 70:
        return "B-"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    elif nilai > 0:
        return "E"
    else:
        return "F"


def nilaiBobot(nilai):
    if nilai >= 90:
        return 4.00
    elif nilai >= 85:
        return 3.67
    elif nilai >= 80:
        return 3.33
    elif nilai >= 75:
        return 3.00
    elif nilai >= 70:
        return 2.5
    elif nilai >= 65:
        return 2
    elif nilai >= 50:
        return 1
    elif nilai > 0:
        return 0
    else:
        return 0


def inputAkun(str):
    f = open("mahasiswa.txt", "a")
    f.write(str)
    f.close()
    print()


def inputNilai(n, str):
    namafile = "nilai"
    if n == 1:
        namafile += "tgs.txt"
    elif n == 2:
        namafile += "uts.txt"
    elif n == 3:
        namafile += "uas.txt"
    f = open(namafile, "a")
    f.write(str)
    f.close()
    print("Nilai berhasil ditambahkan.")
    print()


def updateFile(namafile):
    f = open(namafile, "w")
    if namafile == "mahasiswa.txt":
        for i in range(len(nama_mhsw)):
            temp = nim_mhsw[i] + ";" + nama_mhsw[i] + ";" + username_mhsw[i] + ";" + password_mhsw[i] + ";\n"
            f.write(temp)
    elif namafile == "nilaitgs.txt":
        for i in range(len(matkul_tgs)):
            temp = nim_tgs[i] + ";" + nama_mhsw_tgs[i] + ";" + matkul_tgs[i] + ";" + nilai_tgs[i] + ";\n"
            f.write(temp)
    elif namafile == "nilaiuts.txt":
        for i in range(len(matkul_uts)):
            temp = nim_uts[i] + ";" + nama_mhsw_uts[i] + ";" + matkul_uts[i] + ";" + nilai_uts[i] + ";\n"
            f.write(temp)
    elif namafile == "nilaiuas.txt":
        for i in range(len(matkul_uas)):
            temp = nim_uas[i] + ";" + nama_mhsw_uas[i] + ";" + matkul_uas[i] + ";" + nilai_uas[i] + ";\n"
            f.write(temp)
    f.close()

nim_mhsw = list()
nama_mhsw = list()
username_mhsw = list()
password_mhsw = list()

matkul_slrh = list()

nim_tgs = list()
nama_mhsw_tgs = list()
matkul_tgs = list()
nilai_tgs = list()

nim_uts = list()
nama_mhsw_uts = list()
matkul_uts = list()
nilai_uts = list()

nim_uas = list()
nama_mhsw_uas = list()
matkul_uas = list()
nilai_uas = list()

openMahasiswa()
openMatkul()
openNilai_Tugas()
openNilai_UTS()
openNilai_UAS()

def mainmenu():
    root1 = tk.Tk()
    root1.geometry("400x250")
    def liatdata():
        root1.destroy()
        root2 = tk.Tk()
        root2.geometry("400x250")
        def lihdata():
            nilai_seluruh = list()
            if jns_nilai.get() == "Nilai Tugas":
                for j in range(len(matkul_tgs)):
                    if matkul_tgs[j] == matkul.get():
                        xx = int(nilai_tgs[j])
                        nilai_seluruh.append([nim_tgs[j], nama_mhsw_tgs[j], nilai_tgs[j], gradeHuruf(xx)])
            elif jns_nilai.get() == "Nilai UTS":
                for j in range(len(matkul_uts)):
                    if matkul_uts[j] == matkul.get():
                        xx = int(nilai_uts[j])
                        nilai_seluruh.append([nim_uts[j], nama_mhsw_uts[j], nilai_uts[j], gradeHuruf(xx)])
            elif jns_nilai.get() == "Nilai UAS":
                for j in range(len(matkul_uas)):
                    if matkul_uas[j] == matkul.get():
                        xx = int(nilai_uas[j])
                        nilai_seluruh.append([nim_uas[j], nama_mhsw_uas[j], nilai_uas[j], gradeHuruf(xx)])
            def treeview_sort_column(tv, col, reverse):
                l = [(tv.set(k, col), k) for k in tv.get_children('')]
                try:
                    l.sort(key=lambda t: int(t[0]), reverse=reverse)
                except ValueError:
                    l.sort(key=lambda t: t[0], reverse=reverse)
                #      ^^^^^^^^^^^^^^^^^^^^^^^
                for index, (val, k) in enumerate(l):
                    tv.move(k, '', index)
                tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))
            scores = tk.Tk()
            tk.Label(scores, text="Daftar Nilai", font=("Arial", 30)).grid(row=0, columnspan=3)
            cols = ('NIM', 'Nama Mahasiswa', 'Nilai', 'Grade')
            listBox = ttk.Treeview(scores, columns=cols, show='headings')
            # set column headings
            for col in cols:
                listBox.heading(col, text=col,
                                command=lambda c=col: treeview_sort_column(listBox, c, False))
            listBox.grid(row=1, column=0, columnspan=2)
            for i, (NIM, nama, nilai, grade) in enumerate(nilai_seluruh, start=1):
                listBox.insert("", "end", values=(NIM, nama, nilai, grade))
            scores.mainloop()
        matkul = tk.StringVar(root2)
        matkul.set(matkul_slrh[0])
        jns_nilai = tk.StringVar(root2)
        jns_nilai.set("Nilai Tugas")
        m = tk.OptionMenu(root2, matkul, matkul_slrh[0], matkul_slrh[1], matkul_slrh[2]).pack()
        n = tk.OptionMenu(root2, jns_nilai, "Nilai Tugas", "Nilai UTS", "Nilai UAS").pack()
        tk.Button(root2, text="Lihat", command=lihdata).pack()
        tk.Button(root2, text="Back", command=mainmenu).pack()
        root2.mainloop()
    def carimahasiswa():
        root1.destroy()
        root2 = tk.Tk()
        root2.geometry("400x250")
        def menu(x):
            root2.destroy()
            root3 = tk.Tk()
            root3.title("Menu")
            root3.geometry("400x250")
            def lihatnilai():
                y = nama_mhsw[x]
                matkul_tgs_user = list()
                nilai_tgs_user = list()
                matkul_uts_user = list()
                nilai_uts_user = list()
                matkul_uas_user = list()
                nilai_uas_user = list()
                nilai_seluruh = list()
                for i in range(3):
                    for j in range(len(nama_mhsw_tgs)):
                        if nama_mhsw_tgs[j] == y:
                            if matkul_tgs[j] == matkul_slrh[i]:
                                matkul_tgs_user.append(matkul_tgs[j])
                                nilai_tgs_user.append(nilai_tgs[j])
                                zz = int(nilai_tgs[j])
                                nilai_seluruh.append([matkul_tgs[j], "Tugas", nilai_tgs[j], gradeHuruf(zz)])
                    for k in range(len(nama_mhsw_uts)):
                        if nama_mhsw_uts[k] == y:
                            if matkul_uts[k] == matkul_slrh[i]:
                                matkul_uts_user.append(matkul_uts[k])
                                nilai_uts_user.append(nilai_uts[k])
                                yy = int(nilai_uts[k])
                                nilai_seluruh.append([matkul_uts[k], "UTS", nilai_uts[k], gradeHuruf(yy)])
                    for l in range(len(nama_mhsw_uas)):
                        if nama_mhsw_uas[l] == y:
                            if matkul_uas[l] == matkul_slrh[i]:
                                matkul_uas_user.append(matkul_uas[l])
                                nilai_uas_user.append(nilai_uas[l])
                                xx = int(nilai_uas[l])
                                nilai_seluruh.append([matkul_uas[l], "UAS", nilai_uas[l], gradeHuruf(xx)])
                adanilai = True
                if len(matkul_tgs_user) == 0 and len(matkul_uts_user) == 0 and len(matkul_uas_user) == 0:
                    adanilai = False
                if adanilai:
                    def treeview_sort_column(tv, col, reverse):
                        l = [(tv.set(k, col), k) for k in tv.get_children('')]
                        try:
                            l.sort(key=lambda t: int(t[0]), reverse=reverse)
                        except ValueError:
                            l.sort(key=lambda t: t[0], reverse=reverse)
                        #      ^^^^^^^^^^^^^^^^^^^^^^^
                        for index, (val, k) in enumerate(l):
                            tv.move(k, '', index)
                        tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

                    scores = tk.Tk()
                    tk.Label(scores, text="Daftar Nilai", font=("Arial", 30)).grid(row=0, columnspan=3)
                    cols = ('Mata Kuliah', 'Jenis Nilai', 'Nilai', 'Grade')
                    listBox = ttk.Treeview(scores, columns=cols, show='headings')
                    # set column headings
                    for col in cols:
                        listBox.heading(col, text=col,
                                        command=lambda c=col: treeview_sort_column(listBox, c, False))
                    listBox.grid(row=1, column=0, columnspan=2)
                    for i, (matkul, jenis_nilai, nilai, grade) in enumerate(nilai_seluruh, start=1):
                        listBox.insert("", "end", values=(matkul, jenis_nilai, nilai, grade))
                    scores.mainloop()
                    menu(x)
                else:
                    tk.Label(root3, text="Anda belum memasukkan nilai.").pack()
            def lihatip():
                root5 = tk.Tk()
                root5.geometry("400x250")
                alpro_valid = False
                pdm_valid = False
                alin_valid = False
                for i in range(3):
                    ada_tugas = False
                    ada_uts = False
                    ada_uas = False
                    for n in range(len(nama_mhsw_tgs)):
                        if nama_mhsw[x] == nama_mhsw_tgs[n]:
                            if matkul_tgs[n] == matkul_slrh[i]:
                                ada_tugas = True
                    for n in range(len(nama_mhsw_uts)):
                        if nama_mhsw[x] == nama_mhsw_uts[n]:
                            if matkul_uts[n] == matkul_slrh[i]:
                                ada_uts = True
                    for n in range(len(nama_mhsw_uas)):
                        if nama_mhsw[x] == nama_mhsw_uas[n]:
                            if matkul_uas[n] == matkul_slrh[i]:
                                ada_uas = True
                    if ada_tugas and ada_uts and ada_uas:
                        if i == 0:
                            alpro_valid = True
                        elif i == 1:
                            pdm_valid = True
                        elif i == 2:
                            alin_valid = True
                if alpro_valid and pdm_valid and alin_valid:
                    # hitung ipk
                    nilai_alpro = 0
                    nilai_pdm = 0
                    nilai_alin = 0
                    for i in range(3):
                        for n in range(len(nama_mhsw_tgs)):
                            if nama_mhsw[x] == nama_mhsw_tgs[n]:
                                if matkul_tgs[n] == matkul_slrh[i]:
                                    if i == 0:
                                        # alpro
                                        nilaitemp = 0.25 * int(nilai_tgs[n])
                                        nilai_alpro += nilaitemp
                                    elif i == 1:
                                        # pdm
                                        nilaitemp = 0.2 * int(nilai_tgs[n])
                                        nilai_pdm += nilaitemp
                                    elif i == 2:
                                        # alin
                                        nilaitemp = 0.25 * int(nilai_tgs[n])
                                        nilai_alin += nilaitemp
                        for n in range(len(nama_mhsw_uts)):
                            if nama_mhsw[x] == nama_mhsw_uts[n]:
                                if matkul_uts[n] == matkul_slrh[i]:
                                    if i == 0:
                                        # alpro
                                        nilaitemp = 0.35 * int(nilai_uts[n])
                                        nilai_alpro += nilaitemp
                                    elif i == 1:
                                        # pdm
                                        nilaitemp = 0.3 * int(nilai_uts[n])
                                        nilai_pdm += nilaitemp
                                    elif i == 2:
                                        # alin
                                        nilaitemp = 0.35 * int(nilai_uts[n])
                                        nilai_alin += nilaitemp
                        for n in range(len(nama_mhsw_uas)):
                            if nama_mhsw[x] == nama_mhsw_uas[n]:
                                if matkul_uas[n] == matkul_slrh[i]:
                                    if i == 0:
                                        # alpro
                                        nilaitemp = 0.4 * int(nilai_uas[n])
                                        nilai_alpro += nilaitemp
                                    elif i == 1:
                                        # pdm
                                        nilaitemp = 0.5 * int(nilai_uas[n])
                                        nilai_pdm += nilaitemp
                                    elif i == 2:
                                        # alin
                                        nilaitemp = 0.4 * int(nilai_uas[n])
                                        nilai_alin += nilaitemp
                    bobot_alpro = 6 * nilaiBobot(nilai_alpro)
                    bobot_pdm = 4 * nilaiBobot(nilai_pdm)
                    bobot_alin = 2 * nilaiBobot(nilai_alin)
                    ip = (bobot_alpro + bobot_pdm + bobot_alin) / 12
                    tk.Label(root5, text="Algorithm & Programming: 6 SKS").pack()
                    tk.Label(root5, text="{0:.2f}".format(nilai_alpro)).pack()
                    tk.Label(root5, text=gradeHuruf(nilai_alpro)).pack()
                    tk.Label(root5, text="Program Design Methods: 4").pack()
                    tk.Label(root5, text="{0:.2f}".format(nilai_pdm)).pack()
                    tk.Label(root5, text=gradeHuruf(nilai_pdm)).pack()
                    tk.Label(root5, text="Linear Algebra: 2 SKS").pack()
                    tk.Label(root5, text="{0:.2f}".format(nilai_alin)).pack()
                    tk.Label(root5, text=gradeHuruf(nilai_alin)).pack()
                    tk.Label(root5, text="IP Anda: {0:.2f}".format(ip)).pack()
                else:
                    tk.Label(root5, text="Nilai Anda belum lengkap. Silakan lengkapi nilai Anda.").pack()
                lihatnilai()
                root5.mainloop()
                menu(x)
            def gantiusername():
                root4 = tk.Tk()
                root4.geometry("400x250")
                def ganti():
                    username_new = username.get()
                    username_mhsw[x] = username_new
                    updateFile("mahasiswa.txt")
                    root4.destroy()
                tk.Label(root4, text="Masukkan Username Baru").grid(row=1, column=1)
                username = tk.Entry(root4)
                username.grid(row=1, column=2)
                tk.Button(root4, text="submit", command=ganti).grid(row=2, column=1)
                root4.mainloop()
            def gantipassword():
                root4 = tk.Tk()
                root4.geometry("400x250")
                def ganti():
                    if (len(password1.get())) < 6:
                        tk.Label(root4, text="Password minimal terdiri dari 6 karakter!").grid(row=4, column=1)
                    password_mhsw[x] = password1.get()
                    updateFile("mahasiswa.txt")
                    root4.destroy()
                tk.Label(root4, text="Masukkan Password Baru").grid(row=1, column=1)
                password1 = tk.Entry(root4, show="*")
                password1.grid(row=1, column=2)
                tk.Button(root4, text="submit", command=ganti).grid(row=3, column=1)
                root4.mainloop()
            def ubahnilai():
                def submitnilai():
                    if jns_nilai.get() == "Nilai Tugas":
                        input_nilai_eligibility = False
                        for i in range(len(nama_mhsw_tgs)):
                            if nama_mhsw[x] == nama_mhsw_tgs[i]:
                                if matkul.get() == matkul_tgs[i]:
                                    input_nilai_eligibility = True
                        if input_nilai_eligibility:
                            for n in range(len(matkul_tgs)):
                                if nama_mhsw[x] == nama_mhsw_tgs[n]:
                                    if matkul.get() == matkul_tgs[n]:
                                        nilai_tgs[n] = nilai.get()
                                        updateFile("nilaitgs.txt")
                            root4.destroy()
                        else:
                            tk.Label(root4, text='Nilai belum ada').pack()
                    elif jns_nilai.get() == "Nilai UTS":
                        input_nilai_eligibility = False
                        for i in range(len(nama_mhsw_uts)):
                            if nama_mhsw[x] == nama_mhsw_uts[i]:
                                if matkul.get() == matkul_uts[i]:
                                    input_nilai_eligibility = True
                        if input_nilai_eligibility:
                            for n in range(len(matkul_uts)):
                                if nama_mhsw[x] == nama_mhsw_uts[n]:
                                    if matkul.get() == matkul_uts[n]:
                                        nilai_uts[n] = nilai.get()
                                        updateFile("nilaiuts.txt")
                            root4.destroy()
                        else:
                            tk.Label(root4, text='Nilai belum ada').pack()
                    elif jns_nilai.get() == "Nilai UAS":
                        input_nilai_eligibility = False
                        for i in range(len(nama_mhsw_uas)):
                            if nama_mhsw[x] == nama_mhsw_uas[i]:
                                if matkul.get() == matkul_uas[i]:
                                    input_nilai_eligibility = True
                        if input_nilai_eligibility:
                            for n in range(len(matkul_uas)):
                                if nama_mhsw[x] == nama_mhsw_uas[n]:
                                    if matkul.get() == matkul_uas[n]:
                                        nilai_uas[n] = nilai.get()
                                        updateFile("nilaiuas.txt")
                            root4.destroy()
                        else:
                            tk.Label(root4, text='Nilai belum ada').pack()
                root4 = tk.Tk()
                matkul = tk.StringVar(root4)
                matkul.set(matkul_slrh[0])
                jns_nilai = tk.StringVar(root4)
                jns_nilai.set("Nilai Tugas")
                w = tk.OptionMenu(root4, matkul, matkul_slrh[0], matkul_slrh[1], matkul_slrh[2])
                y = tk.OptionMenu(root4, jns_nilai, "Nilai Tugas", "Nilai UTS", "Nilai UAS")
                w.pack()
                y.pack()
                nilai = tk.Entry(root4, bd=5)
                nilai.pack()
                tk.Button(root4, text="submit", command=submitnilai).pack()
                root4.mainloop()
            tk.Label(root3, text=nim_mhsw[x]).pack()
            tk.Label(root3, text=nama_mhsw[x]).pack()
            tk.Label(root3, text=username_mhsw[x]).pack()
            tk.Button(root3, text="Lihat Nilai", command=lihatnilai).pack()
            tk.Button(root3, text="Lihat IP", command=lihatip).pack()
            tk.Button(root3, text="Ganti Username", command=gantiusername).pack()
            tk.Button(root3, text="Ganti Password", command=gantipassword).pack()
            tk.Button(root3, text="Ubah Nilai", command=ubahnilai).pack()
            tk.Button(root3, text="Mainmenu", command=mainmenu).pack()
            root3.mainloop()
        def cari():
            if searchmenu.get() == "NIM":
                search_nim = var1.get()
                if search_nim in nim_mhsw:
                    z = nim_mhsw.index(search_nim)
                    menu(z)
                else:
                    tk.Label(root2, text="NIM tidak ditemukan!").pack()
            elif searchmenu.get() == "Nama":
                search_nama = var1.get()
                if search_nama in nama_mhsw:
                    z = nama_mhsw.index(search_nama)
                    menu(z)
                else:
                    tk.Label(root2, text="Nama tidak ditemukan!").pack()
            elif searchmenu.get() == "Username":
                search_user = var1.get()
                if search_user in username_mhsw:
                    z = username_mhsw.index(search_user)
                    menu(z)
                else:
                    tk.Label(root2, text="Username tidak ditemukan!").pack()
        tk.Label(root2, text="Cari Mahasiswa").pack()
        tk.Label(root2, text="Berdasarkan").pack()
        searchmenu = tk.StringVar(root2)
        searchmenu.set("NIM")
        w = tk.OptionMenu(root2, searchmenu, "NIM", "Nama", "Username")
        w.pack()
        var1 = tk.Entry(root2, bd=5)
        var1.pack()
        tk.Button(root2, text="cari", command=cari).pack()
        tk.Button(root2, text="Back", command=mainmenu).pack()
        root2.mainloop()
    def hapus():
        root1.destroy()
        root2 = tk.Tk()
        root2.geometry("400x250")
        def confirm():
            if nim_hapus.get() in nim_mhsw:
                z = nim_mhsw.index(nim_hapus.get())
                counter = 0
                for n in range(len(nim_mhsw)):
                    i = n - counter
                    if nim_hapus.get() == nim_mhsw[i]:
                        nim_mhsw.pop(i)
                        nama_mhsw.pop(i)
                        username_mhsw.pop(i)
                        password_mhsw.pop(i)
                        counter += 1
                counter = 0
                for n in range(len(nim_tgs)):
                    i = n - counter
                    if nim_hapus.get() == nim_tgs[i]:
                        nim_tgs.pop(i)
                        nama_mhsw_tgs.pop(i)
                        matkul_tgs.pop(i)
                        nilai_tgs.pop(i)
                        counter += 1
                counter = 0
                for n in range(len(nim_uts)):
                    i = n - counter
                    if nim_hapus.get() == nim_uts[i]:
                        nim_uts.pop(i)
                        nama_mhsw_uts.pop(i)
                        matkul_uts.pop(i)
                        nilai_uts.pop(i)
                        counter += 1
                counter = 0
                for n in range(len(nim_uas)):
                    i = n - counter
                    if nim_hapus.get() == nim_uas[i]:
                        nim_uas.pop(i)
                        nama_mhsw_uas.pop(i)
                        matkul_uas.pop(i)
                        nilai_uas.pop(i)
                        counter += 1
                updateFile("mahasiswa.txt")
                updateFile("nilaitgs.txt")
                updateFile("nilaiuts.txt")
                updateFile("nilaiuas.txt")
                root2.destroy()
            else:
                tk.Label(root2, text="NIM tidak ditemukan.").grid(row=4, column=2)
        tk.Label(root2, text="Hapus data Mahasiswa").grid(row=1, column=1, columnspan=2)
        tk.Label(root2, text="NIM").grid(row=2, column=1)
        nim_hapus = tk.Entry(root2, bd=5)
        nim_hapus.grid(row=2, column=2)
        tk.Button(root2, text="Confirm", command=confirm).grid(row=3, column=2)
        tk.Button(root2, text= "Back",command= mainmenu).grid(row = 3, column =1)
        root2.mainloop()
    tk.Label(root1, text="Selamat datang, admin").pack()
    tk.Label(root1, text="Menu").pack()
    tk.Button(root1, text="Lihat Data", command=liatdata).pack()
    tk.Button(root1, text="Cari Mahasiswa", command=carimahasiswa).pack()
    tk.Button(root1, text="Hapus data mahasiswa", command=hapus).pack()
    tk.Button(root1, text="Exit", command=exit).pack()
    root1.mainloop()
root = tk.Tk()
def signin():
    if str(password.get()) == "ayamsunib":
        root.destroy()
        mainmenu()
    else:
        tk.Label(root,text="Password salah").grid(row=4,column=2)
tk.Label(root,text="Binus Maybe").grid(row=1,column=1,columnspan=2)
tk.Label(root,text="Kata sandi admin").grid(row=2,column=1)
password=tk.Entry(root,show="*",bd=5)
password.grid(row=2,column=2)
tk.Button(root,text="submit",command=signin).grid(row=3,column=2)
root.mainloop()