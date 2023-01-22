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

    view = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(
                        value="FORM MAHASISWA",
                        style=ft.TextThemeStyle.HEADLINE_SMALL,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                height=50
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            kolomNama, kolomNIM, kolomJurusan,
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton(
                        "Simpan", on_click=simpanData),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    tempatPesan
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Text(value="Nama Yang Terakhir Di Entry Adalah " +
                    page.client_storage.get("nama"))
        ]
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(target=main)
