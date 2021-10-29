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
    int(nilai)
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
    print()


def updateFile(namafile):
    f = open(namafile, "w")
    for i in range(len(nama_mhsw)):
        temp = nim_mhsw[i] + ";" + nama_mhsw[i] + ";" + username_mhsw[i] + ";" + password_mhsw[i] + ";\n"
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

openMatkul()
openNilai_Tugas()
openNilai_UTS()
openNilai_UAS()
x = int()
openMahasiswa()
def menu(x):
    root.destroy()
    root2 = tk.Tk()
    root2.title("Menu")
    root2.geometry("400x250")
    def inputnilai():
        def submitnilai():
            temp = nim_mhsw[x] + ";" + nama_mhsw[x] + ";" + str(matkul.get()) + ";" + str(nilai.get()) + ";\n"
            if jns_nilai.get() == "Nilai Tugas":
               n = 1
               input_nilai_eligibility = True
               for i in range(len(nama_mhsw_tgs)):
                   if nama_mhsw[x] == nama_mhsw_tgs[i]:
                       if matkul.get() == matkul_tgs[i]:
                           input_nilai_eligibility = False
               if input_nilai_eligibility:
                   inputNilai(n, temp)
                   nim_tgs.append(nim_mhsw[x])
                   nama_mhsw_tgs.append(nama_mhsw[x])
                   matkul_tgs.append(str(matkul.get()))
                   nilai_tgs.append(str(nilai.get()))
                   root3.destroy()
               else:
                   tk.Label(root3,text='Nilai sudah ada').pack()
            elif jns_nilai.get() == "Nilai UTS":
                n = 2
                input_nilai_eligibility = True
                for i in range(len(nama_mhsw_uts)):
                    if nama_mhsw[x] == nama_mhsw_uts[i]:
                        if matkul.get() == matkul_uts[i]:
                            input_nilai_eligibility = False
                if input_nilai_eligibility:
                    inputNilai(n,temp)
                    nim_uts.append(nim_mhsw[x])
                    nama_mhsw_uts.append(nama_mhsw[x])
                    matkul_uts.append(str(matkul.get()))
                    nilai_uts.append(str(nilai.get()))
                    root3.destroy()
                else:
                    tk.Label(root3, text='Nilai sudah ada').pack()
            elif jns_nilai.get() == "Nilai UAS":
                n = 3
                input_nilai_eligibility = True
                for i in range(len(nama_mhsw_uas)):
                    if nama_mhsw[x] == nama_mhsw_uas[i]:
                        if matkul.get() == matkul_uas[i]:
                            input_nilai_eligibility = False
                if input_nilai_eligibility:
                    inputNilai(n,temp)
                    nim_uas.append(nim_mhsw[x])
                    nama_mhsw_uas.append(nama_mhsw[x])
                    matkul_uas.append(str(matkul.get()))
                    nilai_uas.append(str(nilai.get()))
                    root3.destroy()
                else:
                    tk.Label(root3, text='Nilai sudah ada').pack()
        root3 = tk.Tk()
        matkul = tk.StringVar(root3)
        matkul.set(matkul_slrh[0])
        jns_nilai = tk.StringVar(root3)
        jns_nilai.set("Nilai Tugas")
        w = tk.OptionMenu(root3, matkul, matkul_slrh[0], matkul_slrh[1], matkul_slrh[2])
        y = tk.OptionMenu(root3, jns_nilai, "Nilai Tugas", "Nilai UTS", "Nilai UAS")
        w.pack()
        y.pack()
        nilai = tk.Entry(root3, bd=5)
        nilai.pack()
        tk.Button(root3, text="submit", command=submitnilai).pack()
        root3.mainloop()
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
                        zz=int(nilai_tgs[j])
                        nilai_seluruh.append([matkul_tgs[j], "Tugas", nilai_tgs[j],gradeHuruf(zz)])
            for k in range(len(nama_mhsw_uts)):
                if nama_mhsw_uts[k] == y:
                    if matkul_uts[k] == matkul_slrh[i]:
                        matkul_uts_user.append(matkul_uts[k])
                        nilai_uts_user.append(nilai_uts[k])
                        yy = int(nilai_uts[k])
                        nilai_seluruh.append([matkul_uts[k], "UTS", nilai_uts[k],gradeHuruf(yy)])
            for l in range(len(nama_mhsw_uas)):
                if nama_mhsw_uas[l] == y:
                    if matkul_uas[l] == matkul_slrh[i]:
                        matkul_uas_user.append(matkul_uas[l])
                        nilai_uas_user.append(nilai_uas[l])
                        xx = int(nilai_uas[l])
                        nilai_seluruh.append([matkul_uas[l], "UAS", nilai_uas[l],gradeHuruf(xx)])
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
            label = tk.Label(scores, text="Daftar Nilai", font=("Arial", 30)).grid(row=0, columnspan=3)
            cols = ('Mata Kuliah', 'Jenis Nilai', 'Nilai','Grade')
            listBox = ttk.Treeview(scores, columns=cols, show='headings')
            # set column headings
            for col in cols:
                listBox.heading(col, text=col, command= lambda c=col:treeview_sort_column(listBox,c,False))
            listBox.grid(row=1, column=0, columnspan=2)
            for i, (matkul, jenis_nilai, nilai,grade) in enumerate(nilai_seluruh, start=1):
                listBox.insert("", "end", values=(matkul, jenis_nilai, nilai,grade))
            scores.mainloop()
        else:
            tk.Label(root2,text="Anda belum memasukkan nilai.").pack()
    def lihatip():
        root4 = tk.Tk()
        root4.geometry("400x250")
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
            tk.Label(root4,text="Algorithm & Programming: 6 SKS").pack()
            tk.Label(root4, text="{0:.2f}".format(nilai_alpro)).pack()
            tk.Label(root4, text=gradeHuruf(nilai_alpro)).pack()
            tk.Label(root4, text="Program Design Methods: 4").pack()
            tk.Label(root4, text="{0:.2f}".format(nilai_pdm)).pack()
            tk.Label(root4, text=gradeHuruf(nilai_pdm)).pack()
            tk.Label(root4, text="Linear Algebra: 2 SKS").pack()
            tk.Label(root4, text="{0:.2f}".format(nilai_alin)).pack()
            tk.Label(root4, text=gradeHuruf(nilai_alin)).pack()
            tk.Label(root4,text="IP Anda: {0:.2f}".format(ip)).pack()
        else:
            tk.Label(root4,text="Nilai Anda belum lengkap. Silakan lengkapi nilai Anda.").pack()
        lihatnilai()
        root4.mainloop()
    def gantiusername():
        root3 = tk.Tk()
        root3.geometry("400x250")
        def ganti():
            pw_check = password.get()
            if pw_check == password_mhsw[x]:
                username_new = username.get()
                username_mhsw[x] = username_new
                updateFile("mahasiswa.txt")
                tk.Label(root3,text="Username berhasil diganti.").grid(row=4,column=1)
            else:
                tk.Label(root3,text="Password Salah.").grid(row=4,column=1)
        tk.Label(root3,text="Masukkan Password").grid(row=1,column=1)
        tk.Label(root3, text="Masukkan Username Baru").grid(row=2, column=1)
        password = tk.Entry(root3,show="*")
        password.grid(row=1,column=2)
        username = tk.Entry(root3)
        username.grid(row=2,column=2)
        tk.Button(root3,text="submit",command=ganti).grid(row=3,column=1)
        root3.mainloop()
        menu(x)
    def gantipassword():
        root3 = tk.Tk()
        root3.geometry("400x250")
        def ganti():
            pw_check = password.get()
            if pw_check == password_mhsw[x]:
                password_new = username.get()
                password_mhsw[x] = password_new
                updateFile("mahasiswa.txt")
                tk.Label(root3, text="Password berhasil diganti.").grid(row=4, column=1)
            else:
                tk.Label(root3, text="Password Salah.").grid(row=4, column=1)
        tk.Label(root3, text="Masukkan Password").grid(row=1, column=1)
        tk.Label(root3, text="Masukkan Password Baru").grid(row=2, column=1)
        password = tk.Entry(root3,show="*")
        password.grid(row=1, column=2)
        username = tk.Entry(root3)
        username.grid(row=2, column=2)
        tk.Button(root3, text="submit", command=ganti).grid(row=3, column=1)
        root3.mainloop()
        menu(x)
    tk.Button(root2, text="Input Nilai", command=inputnilai).pack()
    tk.Button(root2, text="Lihat Nilai", command=lihatnilai).pack()
    tk.Button(root2, text="Lihat IP", command=lihatip).pack()
    tk.Button(root2, text="Ganti Username",command=gantiusername).pack()
    tk.Button(root2, text= "Ganti Password",command=gantipassword).pack()
    tk.Button(root2, text="Keluar",command=exit).pack()
    root2.mainloop()
def signin():
    username = entry1.get()
    password = entry2.get()
    if username in username_mhsw:
        x = username_mhsw.index(username)
        if password == password_mhsw[x]:
            menu(x)
        else:
            tk.Label(root, text ="Login gagal. Mohon coba lagi.").grid(row=5,column=1)
    else:
        tk.Label(root, text ="Login gagal. Mohon coba lagi.").grid(row=5,column=1)
def register():
    root1 = tk.Tk()
    root1.title("Register")
    root1.geometry("400x250")
    def submit():
        nama_baru = entry2.get().lower()
        y = nama_baru.split(" ")
        nama_lengkap = ""
        for j in range(len(y)):
            nama_lengkap = nama_lengkap + y[j].capitalize()
            if j < (len(y)) - 1:
                nama_lengkap = nama_lengkap + " "

        nim_baru = entry1.get()
        while nim_baru in nim_mhsw:
            print("NIM sudah terdaftar!")
            nim_baru = input("NIM: ")
        while (len(nim_baru)) != 10:
            tk.Label(root1,text="NIM terdiri dari 10 angka").grid(row=6,column=1)
            nim_baru = entry1.get()

        username_baru = entry3.get()
        while username_baru in username_mhsw:
            tk.Label(root1,text="Username sudah digunakan!").grid(row=6,column=1)
            username_baru = entry3.get()

        password_baru = entry4.get()
        while (len(password_baru)) < 6:
            print("Password minimal terdiri dari 6 karakter!")
            password_baru = entry4.get()

        nama_mhsw.append(nama_lengkap)
        nim_mhsw.append(nim_baru)
        username_mhsw.append(username_baru)
        password_mhsw.append(password_baru)
        temp = nim_baru + ";" + nama_lengkap + ";" + username_baru + ";" + password_baru + ";\n"
        inputAkun(temp)
        root1.destroy()
    tk.Label(root1, text="NIM").grid(row=1, column=1)
    entry1 = tk.Entry(root1, bd=5)
    entry1.grid(row=1, column=2)
    tk.Label(root1, text="Nama").grid(row=2, column=1)
    entry2 = tk.Entry(root1, bd=5)
    entry2.grid(row=2, column=2)
    tk.Label(root1, text="Username").grid(row=3, column=1)
    entry3 = tk.Entry(root1, bd=5)
    entry3.grid(row=3, column=2)
    tk.Label(root1, text="Password").grid(row=4, column=1)
    entry4 = tk.Entry(root1, bd=5)
    entry4.grid(row=4, column=2)
    tk.Button(root1, text="Submit", command=submit).grid(row=5, column=1)
    root1.mainloop()
root = tk.Tk()
root.geometry("300x150")
tk.Button(root,text="Sign In",command=signin).grid(row=3,column=2)
tk.Button(root,text="Register",command=register).grid(row=4,column=2)
tk.Label(root, text = "Username").grid(row=1,column=1)
tk.Label(root, text = "Password").grid(row=2,column=1)
entry1 = tk.Entry(root,bd = 5)
entry1.grid(row=1,column=2)
entry2 = tk.Entry(root,bd = 5,show ="*")
entry2.grid(row=2,column=2)
root.mainloop()