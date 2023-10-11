from pathlib import Path
import os
import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":
    startup_folder = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

    lnk_file1 = "MEMRAP.lnk"

    lnk_path2 = startup_folder / lnk_file1
    #print(lnk_path1)
    #print(lnk_path2)

    if lnk_path2.exists():
        lnk_path2.unlink()
        print(f"{lnk_file1} đã bị xóa thành công!")
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("MEMRAP Thông báo ( ఠ ͟ʖ ఠ)", "✓ Đã Xóa Cài Đặt Thành Công! ✓\n MEMRAP Hẹn gặp lại bạn!")
        root.destroy()
    elif lnk_path1.exists() and not lnk_path2.exists():
        lnk_path1.unlink()
        print(f"{lnk_file1} đã bị xóa thành công!")
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("MEMRAP Thông báo ( ఠ ͟ʖ ఠ)", f"✓ {lnk_file1} đã bị xóa thành công! ✓")
        root.destroy()
    elif lnk_path2.exists() and not lnk_path1.exists():
        lnk_path2.unlink()
        print(f"{lnk_file2} đã bị xóa thành công!")
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("MEMRAP Thông báo ( ఠ ͟ʖ ఠ)", f"✓ {lnk_file2} đã bị xóa thành công! ✓")
        root.destroy()
    else:
        print("Không tìm thấy các tệp .lnk để xóa.")
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("MEMRAP Thông báo ( ఠ ͟ʖ ఠ)", "✓ Chưa thể xóa cài đặt! ✓")
        root.destroy()
