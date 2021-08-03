

import tkinter as tk

#Window
root = tk.Tk()
root.geometry("800x700")
root.title("SLID")

#Title_Frame
title_frame = tk.Frame(root, width=800, height=100, bg='#b1b7ba')
title_frame.pack(side='top')
title_label = tk.Label(title_frame, text="SLID", font='Courier 35 underline bold')
title_label.place(relx=0.40, rely=0.2)

#Account_Frame
account_frame = tk.Frame(root, width=800, height=700, bg='#9dd7f5')
account_frame.pack(side='right')

account = tk.Label(account_frame, text="Do you want to start the process?(y/n) If y, Then say something.....", font='Helvetica 15')
account.place(relx=0.01, rely=0.03)

add_account_button = tk.Button(account_frame, text="Yes", font='Courier 13')
add_account_button.place(relx=0.02, rely=0.125)

add_account_button = tk.Button(account_frame, text="No ", font='Courier 13')
add_account_button.place(relx=0.12, rely=0.125)

account = tk.Label(account_frame, text="Speaker's I/P:: tomar nam ki ", font='Helvetica 10')
account.place(relx=0.01, rely=0.225)

account = tk.Label(account_frame, text="Predicted O/P :: bangla ", font='Helvetica 10')
account.place(relx=0.01, rely=0.300)





account = tk.Label(account_frame, text="Do you want to start the process?(y/n) If y, Then say something.....", font='Helvetica 15')
account.place(relx=0.01, rely=0.400)

add_account_button = tk.Button(account_frame, text="Yes", font='Courier 13')
add_account_button.place(relx=0.02, rely=0.500)

add_account_button = tk.Button(account_frame, text="No ", font='Courier 13')
add_account_button.place(relx=0.12, rely=0.500)


account = tk.Label(account_frame, text="Speaker's I/P:: tuhara nam kiya hain ", font='Helvetica 10')
account.place(relx=0.01, rely=0.600)


account = tk.Label(account_frame, text="Predicted O/P :: hindi ", font='Helvetica 10')
account.place(relx=0.01, rely=0.700)




account = tk.Label(account_frame, text="Do you want to start the process?(y/n) If y, Then say something.....", font='Helvetica 15')
account.place(relx=0.01, rely=0.770)

add_account_button = tk.Button(account_frame, text="Yes", font='Courier 13')
add_account_button.place(relx=0.02, rely=0.850)

add_account_button = tk.Button(account_frame, text="No ", font='Courier 13')
add_account_button.place(relx=0.12, rely=0.850)


account = tk.Label(account_frame, text=" Thank you !.... :) ", font='Helvetica 10')
account.place(relx=0.01, rely=0.950)



root.mainloop()


