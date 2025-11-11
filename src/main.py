import customtkinter 


class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Init root window -------------------------------------------
        self.title("PY-808")
        self.geometry("1220x650")

        


def main():
    root = Root()
    root.mainloop()

main()
