import tkinter as tk

def tahtayı_yazdır(tahta):
    for row in tahta:
        print(" ".join(map(str, row)))

def hamle_gecerli_mi(tahta, satir, sutun, num):
    n = len(tahta)
    # Satır ve sütun kontrolü
    for i in range(n):
        if tahta[satir][i] == num or tahta[i][sutun] == num:
            return False

    # Küçük ızgara kontrolü
    bas_satir, bas_sutun = 3 * (satir // 3), 3 * (sutun // 3)
    for i in range(3):
        for j in range(3):
            if tahta[bas_satir + i][bas_sutun + j] == num:
                return False

    return True

def bos_hucre_bul(tahta):
    n = len(tahta)
    for i in range(n):
        for j in range(n):
            if tahta[i][j] == 0:
                return i, j
    return None

def sudoku_coz(tahta):
    bos_hucre = bos_hucre_bul(tahta)
    if not bos_hucre:
        return True

    satir, sutun = bos_hucre
    for num in range(1, 10):
        if hamle_gecerli_mi(tahta, satir, sutun, num):
            tahta[satir][sutun] = num

            if sudoku_coz(tahta):
                return True

            tahta[satir][sutun] = 0

    return False

def tahtayı_guncelle():
    for i in range(board_size):
        for j in range(board_size):
            cell_value = cells[i][j].get()
            tahta[i][j] = int(cell_value) if cell_value else 0

def solve_sudoku():
    tahtayı_guncelle()
    if sudoku_coz(tahta):
        for i in range(board_size):
            for j in range(board_size):
                cells[i][j].delete(0, tk.END)
                cells[i][j].insert(0, str(tahta[i][j]))
    else:
        print("Sudoku çözülemedi.")

def on_board_size_change(event):
    global board_size, cells, tahta
    board_size = int(board_size_var.get())

    for row in cells:
        for cell in row:
            cell.grid_forget()

    tahta = [[0 for _ in range(board_size)] for _ in range(board_size)]
    cells = [[None for _ in range(board_size)] for _ in range(board_size)]

    for i in range(board_size):
        for j in range(board_size):
            cell = tk.Entry(root, width=5, font=("Arial", 20), justify='center')
            cell.grid(row=i+2, column=j)
            cells[i][j] = cell

    solve_button.grid(row=board_size+2, columnspan=board_size)

root = tk.Tk()
root.title("Sudoku Çözücü")

board_size_var = tk.StringVar()
board_size_var.set("9")

board_size_menu = tk.OptionMenu(root, board_size_var, "4", "9", "16", command=on_board_size_change)
board_size_menu.grid(row=0, columnspan=9)

board_size = int(board_size_var.get())
tahta = [[0 for _ in range(board_size)] for _ in range(board_size)]
cells = [[None for _ in range(board_size)] for _ in range(board_size)]

for i in range(board_size):
    for j in range(board_size):
        cell = tk.Entry(root, width=5, font=("Arial", 20), justify='center')
        cell.grid(row=i+2, column=j)
        cells[i][j] = cell

solve_button = tk.Button(root, text="Çöz", command=solve_sudoku)
solve_button.grid(row=board_size+2, columnspan=board_size)

root.mainloop()
