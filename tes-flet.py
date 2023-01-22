import flet as ft


def main(page):
    page.title = "Nyan Ban Hai"

    def tampilPesan(pesan):
        tempatPesan.controls.append(ft.Text(value=pesan))

    def simpanData(e):
        if (kolomNama.value == ''):
            tampilPesan("Nama tidak boleh kosong!")
            page.update()
        elif (kolomNIM.value == ''):
            tampilPesan("NIM tidak boleh kosong!")
            page.update()
        elif (kolomJurusan.value == ''):
            tampilPesan("Jurusan tidak boleh kosong!")
            page.update()
        else:
            page.client_storage.set("nama", kolomNama.value)
            tampilPesan("Berhasil simpan data!")
            value = page.client_storage.get("nama")
            print(str(value))
            page.update()

    tempatPesan = ft.Column()
    kolomNama = ft.TextField(label="Nama", width=300)
    kolomNIM = ft.TextField(label="NIM", width=300)
    kolomJurusan = ft.TextField(label="Jurusan", width=300)

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Row([
                            ft.Text(
                                value="FORM MAHASISWA",
                                style=ft.TextThemeStyle.HEADLINE_SMALL,
                            ),
                        ], height=50),
                        ft.Column(
                            [
                                kolomNama, kolomNIM, kolomJurusan,
                                ft.ElevatedButton(
                                    "Simpan", on_click=simpanData),
                                tempatPesan
                            ],
                        ),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Text(value="Nama Yang Terakhir Di Entry Adalah " +
                page.client_storage.get("nama"))
    )


ft.app(target=main)
