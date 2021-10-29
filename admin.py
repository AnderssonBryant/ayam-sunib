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


def menuLihat():
    print("Bagaimana Anda ingin melihat data?")
    print("1. Urutkan berdasarkan NIM")
    print("2. Urutkan berdasarkan Nama")
    print("3. Urutkan berdasarkan Nilai")
    print()


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


def searchMahasiswa(index):
    print()
    print("Data Mahasiswa".center(30))
    print("NIM:", nim_mhsw[index])
    print("Nama:", nama_mhsw[index])
    print("Username:", username_mhsw[index])
    print()
    lanjut = True
    while lanjut:
        lanjut = isinyaMain(index)


def isinyaMain(x):
    print("Apa yang ingin Anda lakukan selanjutnya?")
    print("1. Lihat Nilai")
    print("2. Lihat IP")
    print("3. Ganti Username")
    print("4. Ganti Password")
    print("5. Ubah Nilai")
    print("0. Kembali")
    print()
    mainmenu = -1
    while mainmenu < 0 or mainmenu > 5:
        mainmenu = int(input("Masukkan pilihan: "))

    if mainmenu == 1:
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
            print("Belum ada nilai.")


    elif mainmenu == 2:
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

            ip = (bobot_alpro + bobot_pdm + bobot_alin) / 12
            print("IP : {0:.2f}".format(ip))
            print()
        else:
            print("Nilai belum lengkap.")
        print()

    elif mainmenu == 3:
        # ganti username
        print("Ganti Username".center(30))
        username_new = input("Mohon masukkan username baru: ")
        username_mhsw[x] = username_new
        updateFile("mahasiswa.txt")
        print("Username berhasil diganti.")
        print()

    elif mainmenu == 4:
        # ganti pw
        print("Ganti Password".center(30))
        password_new = input("Mohon masukkan password baru: ")
        while (len(password_new)) < 6:
            print("Password minimal terdiri dari 6 karakter!")
            password_new = input("Mohon masukkan password baru Anda: ")
        password_mhsw[x] = password_new
        updateFile("mahasiswa.txt")
        print("Password berhasil diganti.")
        print()

    elif mainmenu == 5:
        # ubah nilai
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
            jenis_nilai_pil = int(input("Jenis nilai yang akan diganti: "))

        input_nilai_eligibility = False
        if jenis_nilai_pil == 1:
            # tugas
            for i in range(len(nama_mhsw_tgs)):
                if nama_mhsw[x] == nama_mhsw_tgs[i]:
                    if matkul_slrh[matkul_pil - 1] == matkul_tgs[i]:
                        input_nilai_eligibility = True

        elif jenis_nilai_pil == 2:
            # uts
            for i in range(len(nama_mhsw_uts)):
                if nama_mhsw[x] == nama_mhsw_uts[i]:
                    if matkul_slrh[matkul_pil - 1] == matkul_uts[i]:
                        input_nilai_eligibility = True

        elif jenis_nilai_pil == 3:
            # uas
            for i in range(len(nama_mhsw_uas)):
                if nama_mhsw[x] == nama_mhsw_uas[i]:
                    if matkul_slrh[matkul_pil - 1] == matkul_uas[i]:
                        input_nilai_eligibility = True

        if input_nilai_eligibility:
            # input nilainya
            print("Rentang nilai adalah 0 sampai 100.")
            nilainya = -1
            while nilainya < 0 or nilainya > 100:
                nilainya = int(input("Nilai baru: "))
            nilainya = str(nilainya)
            if jenis_nilai_pil == 1:
                for n in range(len(matkul_tgs)):
                    if nama_mhsw[x] == nama_mhsw_tgs[n]:
                        if matkul_slrh[matkul_pil-1] == matkul_tgs[n]:
                            nilai_tgs[n] = nilainya
                            updateFile("nilaitgs.txt")
                            break

            elif jenis_nilai_pil == 2:
                for n in range(len(matkul_uts)):
                    if nama_mhsw[x] == nama_mhsw_uts[n]:
                        if matkul_slrh[matkul_pil-1] == matkul_uts[n]:
                            nilai_uts[n] = nilainya
                            updateFile("nilaiuts.txt")
                            break


            elif jenis_nilai_pil == 3:
                for n in range(len(matkul_uas)):
                    if nama_mhsw[x] == nama_mhsw_uas[n]:
                        if matkul_slrh[matkul_pil-1] == matkul_uas[n]:
                            nilai_uas[n] = nilainya
                            updateFile("nilaiuas.txt")
                            break
            print("Nilai berhasil diubah.")
        else:
            print("Mahasiswa tersebut belum memiliki nilai.")
            print()

    elif mainmenu == 0:
        return False
    return True


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

print("Binus Maybe")
login = False
while not login:
    verificator = input("Kata sandi admin: ")
    if verificator == "ayamsunib":
        login = True
print("Selamat datang, admin. <3")

while True:
    print()
    print("Menu Utama".center(30))
    print("1. Lihat Data")
    print("2. Cari Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("0. Exit")
    menu = -1
    while menu < 0 or menu > 3: # pastiin lg
        menu = int(input("Masukkan pilihan: "))
    if menu == 1:
        # lihat data
        print()
        print("Daftar Mata Kuliah")
        for n in range(len(matkul_slrh)):
            print(("{}.".format(n + 1)).ljust(4), matkul_slrh[n])
        matkul_lih = int(input("Mata kuliah yang ingin dilihat: "))
        while matkul_lih < 1 or matkul_lih > len(matkul_slrh):
            print("Masukkan angka yang tertera pada daftar mata kuliah!")
            print()
            print("Daftar Mata Kuliah")
            for n in range(len(matkul_slrh)):
                print(("{}.".format(n + 1)).ljust(4), matkul_slrh[n])
            matkul_lih = int(input("Mata kuliah yang ingin dilihat: "))

        print()
        print("Jenis Nilai".center(30))
        print("1. Tugas")
        print("2. UTS")
        print("3. UAS")

        jenis_nilai_lih = -1
        while jenis_nilai_lih < 1 or jenis_nilai_lih > 3:
            jenis_nilai_lih = int(input("Jenis nilai yang akan dimasukkan: "))

        y = matkul_slrh[matkul_lih - 1]

        if jenis_nilai_lih == 1:
            menuLihat()
            sortmenu = -1
            while sortmenu < 1 or sortmenu > 3:
                sortmenu = int(input("Masukkan pilihan: "))
                if sortmenu == 2:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_tgs)):
                        if matkul_tgs[j] == y:
                            a = list()
                            a.append(nama_mhsw_tgs[j])
                            a.append(nim_tgs[j])
                            a.append(nilai_tgs[j])
                            b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    print(y)
                    print("Jenis nilai: Tugas")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), b_sorted[k][1].ljust(15), b_sorted[k][0].ljust(35),
                              str(b_sorted[k][2]).ljust(10))

                elif sortmenu == 1:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_tgs)):
                        if matkul_tgs[j] == y:
                            a = list()
                            a.append(int(nim_tgs[j]))
                            a.append(nilai_tgs[j])
                            a.append(nama_mhsw_tgs[j])
                            b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    print(y)
                    print("Jenis nilai: Tugas")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), str(b_sorted[k][0]).ljust(15), b_sorted[k][2].ljust(35),
                              str(b_sorted[k][1]).ljust(10))

                elif sortmenu == 3:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_tgs)):
                        if matkul_tgs[j] == y:
                            a = list()
                            a.append(int(nilai_tgs[j]))
                            a.append(nim_tgs[j])
                            a.append(nama_mhsw_tgs[j])
                            b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    b_sorted = b_sorted[::-1]
                    print(y)
                    print("Jenis nilai: Tugas")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), b_sorted[k][1].ljust(15), b_sorted[k][2].ljust(35),
                              str(b_sorted[k][0]).ljust(10))

        elif jenis_nilai_lih == 2:
            menuLihat()
            sortmenu = -1
            while sortmenu < 1 or sortmenu > 3:
                sortmenu = int(input("Masukkan pilihan: "))
                if sortmenu == 2:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_uts)):
                        if matkul_uts[j] == y:
                            a = list()
                            a.append(nama_mhsw_uts[j])
                            a.append(nim_uts[j])
                            a.append(nilai_uts[j])
                            b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    print(y)
                    print("Jenis nilai: UTS")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), b_sorted[k][1].ljust(15), b_sorted[k][0].ljust(35),
                              str(b_sorted[k][2]).ljust(10))

                elif sortmenu == 1:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_uts)):
                        b = list()
                        for j in range(len(matkul_uts)):
                            if matkul_uts[j] == y:
                                a = list()
                                a.append(int(nim_uts[j]))
                                a.append(nilai_uts[j])
                                a.append(nama_mhsw_uts[j])
                                b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    print(y)
                    print("Jenis nilai: UTS")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), str(b_sorted[k][0]).ljust(15), b_sorted[k][2].ljust(35),
                              str(b_sorted[k][1]).ljust(10))

                elif sortmenu == 3:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_uts)):
                        if matkul_uts[j] == y:
                            a = list()
                            a.append(int(nilai_uts[j]))
                            a.append(nim_uts[j])
                            a.append(nama_mhsw_uts[j])
                            b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    b_sorted = b_sorted[::-1]
                    print(y)
                    print("Jenis nilai: UTS")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), b_sorted[k][1].ljust(15), b_sorted[k][2].ljust(35),
                              str(b_sorted[k][0]).ljust(10))

        elif jenis_nilai_lih == 3:
            menuLihat()
            sortmenu = -1
            while sortmenu < 1 or sortmenu > 3:
                sortmenu = int(input("Masukkan pilihan: "))
                if sortmenu == 2:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_uas)):
                        if matkul_uas[j] == y:
                            a = list()
                            a.append(nama_mhsw_uas[j])
                            a.append(nim_uas[j])
                            a.append(nilai_uas[j])
                            b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    print(y)
                    print("Jenis nilai: UAS")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), b_sorted[k][1].ljust(15), b_sorted[k][0].ljust(35),
                              str(b_sorted[k][2]).ljust(10))

                elif sortmenu == 1:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_uas)):
                        b = list()
                        for j in range(len(matkul_uas)):
                            if matkul_uas[j] == y:
                                a = list()
                                a.append(int(nim_uas[j]))
                                a.append(nilai_uas[j])
                                a.append(nama_mhsw_uas[j])
                                b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    print(y)
                    print("Jenis nilai: UAS")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), str(b_sorted[k][0]).ljust(15), b_sorted[k][2].ljust(35),
                              str(b_sorted[k][1]).ljust(10))

                elif sortmenu == 3:
                    b = list()
                    b_sorted = list()
                    for j in range(len(matkul_uas)):
                        if matkul_uas[j] == y:
                            a = list()
                            a.append(int(nilai_uas[j]))
                            a.append(nim_uas[j])
                            a.append(nama_mhsw_uas[j])
                            b.append(a)

                    for ele in sorted(b):
                        b_sorted.append(ele)
                    b_sorted = b_sorted[::-1]
                    print(y)
                    print("Jenis nilai: UAS")
                    print("No".ljust(3), "NIM".ljust(15), "Nama Mahasiswa".ljust(35), "Nilai".ljust(10))
                    for k in range(len(b_sorted)):
                        print(("{}.".format(k + 1)).ljust(3), b_sorted[k][1].ljust(15), b_sorted[k][2].ljust(35),
                              str(b_sorted[k][0]).ljust(10))
    elif menu == 2:
        # cari mahasiswa
        print()
        print("Bagaimana Anda ingin mencari mahasiswa?")
        print("1. Cari berdasarkan NIM")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Username")

        searchmenu = -1
        while searchmenu < 1 or searchmenu > 3:
            searchmenu = int(input("Masukkan pilihan: "))

        if searchmenu == 1:
            # nim
            search_nim = input("Masukkan NIM yang ingin dicari: ")
            if search_nim in nim_mhsw:
                z = nim_mhsw.index(search_nim)
                searchMahasiswa(z)
            else:
                print("NIM tidak ditemukan!")
            print()
        elif searchmenu == 2:
            # nama
            search_nama = input("Masukkan nama yang ingin dicari: ")
            if search_nama in nama_mhsw:
                z = nama_mhsw.index(search_nama)
                searchMahasiswa(z)
            else:
                print("Nama tidak ditemukan!")
            print()
        elif searchmenu == 3:
            # username
            search_user = input("Masukkan username yang ingin dicari: ")
            if search_user in username_mhsw:
                z = username_mhsw.index(search_user)
                searchMahasiswa(z)
            else:
                print("Username tidak ditemukan!")
            print()
        print()
    elif menu == 3:
        # hapus
        nim_hapus = input("Masukkan NIM dari data yang ingin dihapus: ")
        if nim_hapus in nim_mhsw:
            z = nim_mhsw.index(nim_hapus)
            counter = 0
            for n in range(len(nim_mhsw)):
                i = n - counter
                if nim_hapus == nim_mhsw[i]:
                    nim_mhsw.pop(i)
                    nama_mhsw.pop(i)
                    username_mhsw.pop(i)
                    password_mhsw.pop(i)
                    counter += 1
            counter = 0
            for n in range(len(nim_tgs)):
                i = n - counter
                if nim_hapus == nim_tgs[i]:
                    nim_tgs.pop(i)
                    nama_mhsw_tgs.pop(i)
                    matkul_tgs.pop(i)
                    nilai_tgs.pop(i)
                    counter += 1
            counter = 0
            for n in range(len(nim_uts)):
                i = n - counter
                if nim_hapus == nim_uts[i]:
                    nim_uts.pop(i)
                    nama_mhsw_uts.pop(i)
                    matkul_uts.pop(i)
                    nilai_uts.pop(i)
                    counter += 1
            counter = 0
            for n in range(len(nim_uas)):
                i = n - counter
                if nim_hapus == nim_uas[i]:
                    nim_uas.pop(i)
                    nama_mhsw_uas.pop(i)
                    matkul_uas.pop(i)
                    nilai_uas.pop(i)
                    counter += 1
            updateFile("mahasiswa.txt")
            updateFile("nilaitgs.txt")
            updateFile("nilaiuts.txt")
            updateFile("nilaiuas.txt")
        else:
            print("NIM tidak ditemukan.")
        print("Data mahasiswa telah dihapus.")
        print()
    elif menu == 0:
        print("Sampai jumpa, admin.")
        exit()
