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
    for i in range(len(nama_mhsw)):
        temp = nim_mhsw[i] + ";" + nama_mhsw[i] + ";" + username_mhsw[i] + ";" + password_mhsw[i] + ";\n"
        f.write(temp)
    f.close()



nim_mhsw = list()
nama_mhsw = list()
username_mhsw = list()
password_mhsw = list()

openMahasiswa()


print(("*" * 30).center(30))
print("Aplikasi Akademik".center(30))
print(("*" * 30).center(30))

login = False
x = int()  # index mhsw
while not login:
    print("Menu Login".center(30))
    print("1. Login")
    print("2. Registrasi")
    print("0. Quit")
    print()
    menu = -1
    while menu < 0 or menu > 2:
        menu = int(input("Masukkan pilihan: "))

    if menu == 1:
        # login
        print("Halaman Login")
        while not login:
            username = input("Username: ")
            password = input("Password: ")
            if username in username_mhsw:
                x = username_mhsw.index(username)
                if password == password_mhsw[x]:
                    login = True
                else:
                    print("Login gagal. Mohon coba lagi.")
            else:
                print("Login gagal. Mohon coba lagi.")
    elif menu == 2:
        # regist
        print("Halaman Registrasi".center(30))
        nama_baru = input("Nama Lengkap: ").lower()
        y = nama_baru.split(" ")
        nama_lengkap = ""
        for j in range(len(y)):
            nama_lengkap = nama_lengkap + y[j].capitalize()
            if j < (len(y)) - 1:
                nama_lengkap = nama_lengkap + " "

        nim_baru = input("NIM: ")
        while nim_baru in nim_mhsw:
            print("NIM sudah terdaftar!")
            nim_baru = input("NIM: ")
        while (len(nim_baru)) != 10:
            print("NIM terdiri dari 10 angka")
            nim_baru = input("NIM: ")

        username_baru = input("Username: ")
        while username_baru in username_mhsw:
            print("Username sudah digunakan!")
            username_baru = input("Username: ")

        password_baru = input("Password: ")
        while (len(password_baru)) < 6:
            print("Password minimal terdiri dari 6 karakter!")
            password_baru = input("Password: ")

        nama_mhsw.append(nama_lengkap)
        nim_mhsw.append(nim_baru)
        username_mhsw.append(username_baru)
        password_mhsw.append(password_baru)
        temp = nim_baru + ";" + nama_lengkap + ";" + username_baru + ";" + password_baru + ";\n"
        inputAkun(temp)

    elif menu == 0:
        print("Terima kasih telah menggunakan aplikasi ini.")
        exit()

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

print("Welcome,", nama_mhsw[x])
while True:
    print("Menu Utama".center(30))
    print("1. Memasukkan Nilai")
    print("2. Lihat Nilai")
    print("3. Lihat IP")
    print("4. Ganti Username")
    print("5. Ganti Password")
    print("0. Quit")
    print()
    mainmenu = -1
    while mainmenu < 0 or mainmenu > 5:
        mainmenu = int(input("Masukkan pilihan: "))

    if mainmenu == 1:
        # memasukkan nilai
        input_nilai = True
        while input_nilai:
            # pilih daftar matkul
            print("Daftar Mata Kuliah".center(30))
            for i in range(len(matkul_slrh)):
                print(("{}.".format(i + 1)).ljust(4), matkul_slrh[i])
            matkul_pil = -1
            while matkul_pil < 1 or matkul_pil > len(matkul_slrh):
                matkul_pil = int(input("Mata kuliah yang ingin dipilih: "))

            # pilih jenis nilai
            print("Jenis Nilai".center(30))
            print("1. Tugas")
            print("2. UTS")
            print("3. UAS")

            jenis_nilai_pil = -1
            while jenis_nilai_pil < 1 or jenis_nilai_pil > 3:
                jenis_nilai_pil = int(input("Jenis nilai yang akan dimasukkan: "))

            input_nilai_eligibility = True
            if jenis_nilai_pil == 1:
                # tugas
                for i in range(len(nama_mhsw_tgs)):
                    if nama_mhsw[x] == nama_mhsw_tgs[i]:
                        if matkul_slrh[matkul_pil-1] == matkul_tgs[i]:
                            input_nilai_eligibility = False

            elif jenis_nilai_pil == 2:
                # uts
                for i in range(len(nama_mhsw_uts)):
                    if nama_mhsw[x] == nama_mhsw_uts[i]:
                        if matkul_slrh[matkul_pil-1] == matkul_uts[i]:
                            input_nilai_eligibility = False

            elif jenis_nilai_pil == 3:
                # uas
                for i in range(len(nama_mhsw_uas)):
                    if nama_mhsw[x] == nama_mhsw_uas[i]:
                        if matkul_slrh[matkul_pil-1] == matkul_uas[i]:
                            input_nilai_eligibility = False

            if input_nilai_eligibility:
                # input nilainya
                print("Rentang nilai adalah 0 sampai 100.")
                print("Berapa nilai yang Anda peroleh?")
                nilainya = -1
                while nilainya < 0 or nilainya > 100:
                    nilainya = int(input("Nilai yang diperoleh: "))

                temp = nim_mhsw[x] + ";" + nama_mhsw[x] + ";" + matkul_slrh[matkul_pil - 1] + ";" + str(
                    nilainya) + ";\n"
                inputNilai(jenis_nilai_pil, temp)

                if jenis_nilai_pil == 1:
                    nim_tgs.append(nim_mhsw[x])
                    nama_mhsw_tgs.append(nama_mhsw[x])
                    matkul_tgs.append(matkul_slrh[matkul_pil-1])
                    nilai_tgs.append(str(nilainya))

                elif jenis_nilai_pil == 2:
                    nim_uts.append(nim_mhsw[x])
                    nama_mhsw_uts.append(nama_mhsw[x])
                    matkul_uts.append(matkul_slrh[matkul_pil - 1])
                    nilai_uts.append(str(nilainya))

                elif jenis_nilai_pil == 3:
                    nim_uas.append(nim_mhsw[x])
                    nama_mhsw_uas.append(nama_mhsw[x])
                    matkul_uas.append(matkul_slrh[matkul_pil - 1])
                    nilai_uas.append(str(nilainya))
            else:
                print("Anda sudah memiliki nilai.")

            print()
            print("Apakah Anda ingin memasukkan nilai lagi? (y/n)")
            lagi = input("Command: ").lower()
            if lagi == "n":
                input_nilai = False

    elif mainmenu == 2:
        # lihat nilai
        # print("Lihat Nilai".center(30))
        y = nama_mhsw[x]

        matkul_tgs_user = list()
        nilai_tgs_user = list()

        matkul_uts_user = list()
        nilai_uts_user = list()

        matkul_uas_user = list()
        nilai_uas_user = list()

        for i in range(3):
            for j in range(len(nama_mhsw_tgs)):
                if nama_mhsw_tgs[j] == y:
                    if matkul_tgs[j] == matkul_slrh[i]:
                        matkul_tgs_user.append(matkul_tgs[j])
                        nilai_tgs_user.append(nilai_tgs[j])
            for k in range(len(nama_mhsw_uts)):
                if nama_mhsw_uts[k] == y:
                    if matkul_uts[k] == matkul_slrh[i]:
                        matkul_uts_user.append(matkul_uts[k])
                        nilai_uts_user.append(nilai_uts[k])
            for l in range(len(nama_mhsw_uas)):
                if nama_mhsw_uas[l] == y:
                    if matkul_uas[l] == matkul_slrh[i]:
                        matkul_uas_user.append(matkul_uas[l])
                        nilai_uas_user.append(nilai_uas[l])

        adanilai = True
        if len(matkul_tgs_user) == 0 and len(matkul_uts_user) == 0 and len(matkul_uas_user) == 0:
            adanilai = False

        if adanilai:
            print("Daftar Nilai".center(30))
            print("Mata Kuliah".ljust(35), "Jenis Nilai".ljust(15), "Nilai".ljust(9), "Grade".ljust(5))
            for i in range(3):
                for n in range(len(matkul_tgs_user)):
                    if matkul_tgs_user[n] == matkul_slrh[i]:
                        huruf = gradeHuruf(int(nilai_tgs_user[n]))
                        print(matkul_tgs_user[n].ljust(35), "Tugas".ljust(15), nilai_tgs_user[n].ljust(9),
                              huruf.ljust(5))
                for n in range(len(matkul_uts_user)):
                    if matkul_uts_user[n] == matkul_slrh[i]:
                        huruf = gradeHuruf(int(nilai_uts_user[n]))
                        print(matkul_uts_user[n].ljust(35), "UTS".ljust(15), nilai_uts_user[n].ljust(9), huruf.ljust(5))
                for n in range(len(matkul_uas_user)):
                    if matkul_uas_user[n] == matkul_slrh[i]:
                        huruf = gradeHuruf(int(nilai_uas_user[n]))
                        print(matkul_uas_user[n].ljust(35), "UAS".ljust(15), nilai_uas_user[n].ljust(9), huruf.ljust(5))
        else:
            print("Anda belum memasukkan nilai.")


    elif mainmenu == 3:
        # lihat grade (ip)
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
                if i == 0:
                    print("Algorithm & Programming: 6 SKS")
                    print("Komponen".ljust(15), "Bobot".ljust(9), "Nilai".ljust(5))
                elif i == 1:
                    print("Program Design Methods: 4 SKS")
                    print("Komponen".ljust(15), "Bobot".ljust(9), "Nilai".ljust(5))
                elif i == 2:
                    print("Linear Algebra: 2 SKS")
                    print("Komponen".ljust(15), "Bobot".ljust(9), "Nilai".ljust(5))

                for n in range(len(nama_mhsw_tgs)):
                    if nama_mhsw[x] == nama_mhsw_tgs[n]:
                        if matkul_tgs[n] == matkul_slrh[i]:
                            if i == 0:
                                # alpro
                                print("Tugas".ljust(15), "25%".ljust(9), nilai_tgs[n].ljust(5))
                                nilaitemp = 0.25 * int(nilai_tgs[n])
                                nilai_alpro += nilaitemp
                            elif i == 1:
                                # pdm
                                print("Tugas".ljust(15), "20%".ljust(9), nilai_tgs[n].ljust(5))
                                nilaitemp = 0.2 * int(nilai_tgs[n])
                                nilai_pdm += nilaitemp
                            elif i == 2:
                                # alin
                                print("Tugas".ljust(15), "25%".ljust(9), nilai_tgs[n].ljust(5))
                                nilaitemp = 0.25 * int(nilai_tgs[n])
                                nilai_alin += nilaitemp

                for n in range(len(nama_mhsw_uts)):
                    if nama_mhsw[x] == nama_mhsw_uts[n]:
                        if matkul_uts[n] == matkul_slrh[i]:
                            if i == 0:
                                # alpro
                                print("UTS".ljust(15), "35%".ljust(9), nilai_uts[n].ljust(5))
                                nilaitemp = 0.35 * int(nilai_uts[n])
                                nilai_alpro += nilaitemp
                            elif i == 1:
                                # pdm
                                print("UTS".ljust(15), "30%".ljust(9), nilai_uts[n].ljust(5))
                                nilaitemp = 0.3 * int(nilai_uts[n])
                                nilai_pdm += nilaitemp
                            elif i == 2:
                                # alin
                                print("UTS".ljust(15), "35%".ljust(9), nilai_uts[n].ljust(5))
                                nilaitemp = 0.35 * int(nilai_uts[n])
                                nilai_alin += nilaitemp

                for n in range(len(nama_mhsw_uas)):
                    if nama_mhsw[x] == nama_mhsw_uas[n]:
                        if matkul_uas[n] == matkul_slrh[i]:
                            if i == 0:
                                # alpro
                                print("UAS".ljust(15), "40%".ljust(9), nilai_uas[n].ljust(5))
                                nilaitemp = 0.4 * int(nilai_uas[n])
                                nilai_alpro += nilaitemp

                            elif i == 1:
                                # pdm
                                print("UAS".ljust(15), "50%".ljust(9), nilai_uas[n].ljust(5))
                                nilaitemp = 0.5 * int(nilai_uas[n])
                                nilai_pdm += nilaitemp

                            elif i == 2:
                                # alin
                                print("UAS".ljust(15), "40%".ljust(9), nilai_uas[n].ljust(5))
                                nilaitemp = 0.4 * int(nilai_uas[n])
                                nilai_alin += nilaitemp

                if i == 0:
                    print("Nilai total:", nilai_alpro)
                    print("Grade:", gradeHuruf(nilai_alpro))
                    print()
                elif i == 1:
                    print("Nilai total:", nilai_pdm)
                    print("Grade:", gradeHuruf(nilai_pdm))
                    print()
                elif i == 2:
                    print("Nilai total:", nilai_alin)
                    print("Grade:", gradeHuruf(nilai_alin))
                    print()

            bobot_alpro = 6 * nilaiBobot(nilai_alpro)
            bobot_pdm = 4 * nilaiBobot(nilai_pdm)
            bobot_alin = 2 * nilaiBobot(nilai_alin)

            ip = (bobot_alpro + bobot_pdm + bobot_alin)/12
            print("IP Anda: {0:.2f}".format(ip))
            print()
        else:
            print("Nilai Anda belum lengkap. Silakan lengkapi nilai Anda.")
        print()

    elif mainmenu == 4:
        # ganti username
        print("Ganti Username".center(30))
        pw_check = input("Mohon masukkan password Anda: ")
        if pw_check == password_mhsw[x]:
            username_new = input("Mohon masukkan username baru Anda: ")
            username_mhsw[x] = username_new
            updateFile("mahasiswa.txt")
            print("Username berhasil diganti.")
        else:
            print("Password salah!")
        print()
    elif mainmenu == 5:
        # ganti pw
        print("Ganti Password".center(30))
        pw_check = input("Mohon masukkan password Anda: ")
        if pw_check == password_mhsw[x]:
            password_new = input("Mohon masukkan password baru Anda: ")
            password_mhsw[x] = password_new
            updateFile("mahasiswa.txt")
            print("Password berhasil diganti.")
        else:
            print("Password salah!")
        print()
    elif mainmenu == 0:
        print("Terima kasih telah menggunakan aplikasi ini.")
        exit()
