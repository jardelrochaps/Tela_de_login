import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("400x300")

def clique():
    print("Login efetuado com sucesso!")

texto = customtkinter.CTkLabel(janela, text="FAZER LOGIN", font=("Century Gothic", 17))
email = customtkinter.CTkEntry(janela, placeholder_text="E-mail")
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
botao = customtkinter.CTkButton(janela, text="Login", command=clique)
caixa = customtkinter.CTkCheckBox(janela, text="Lembrar-me")

texto.pack(padx=10, pady=20)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)
caixa.pack(padx=10, pady=10)

janela.mainloop()