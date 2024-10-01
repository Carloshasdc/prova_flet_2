import flet as ft

cadastros = []

def main(page: ft.Page):
    nome_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="email", width=300)
    mensagen_input = ft.TextField(label="mensagen", width=300)

    def cadastrar(e):   
        cadastros.append({
            "nome": nome_input.value,
            "email": email_input.value,
            "mensagen": mensagen_input.value  })
        
        def segunda_pagina(page: ft.Page):
            page.title = "Dados Cadastrados"            
            tabela = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Nome")),
                    ft.DataColumn(ft.Text("email")),
                    ft.DataColumn(ft.Text("mensagen")),],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(cadastro["nome"])),
                            ft.DataCell(ft.Text(cadastro["email"])),
                            ft.DataCell(ft.Text(cadastro["mensagen"])),]) 
                    for cadastro in cadastros])
                        
            page.add(
                ft.Text("Dados Cadastrados", style="headlineMedium"),
                 tabela,
                ft.ElevatedButton(text="Voltar", on_click=lambda e: main(page)))

        page.clean()
        segunda_pagina(page)

    cadastrar_button = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar)   
    page.add(
        ft.Text("Cadastro de Pessoas", style="headlineMedium"),
        nome_input,
        email_input,
        mensagen_input,
        cadastrar_button)


ft.app(target=main)

print(cadastros)