import os
import shutil
from pathlib import Path
from win32com.client import Dispatch

def create_shortcut(target_path, shortcut_path, working_directory):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = working_directory
    #shortcut.IconLocation = (icon_path, icon_index)
    shortcut.save()

#E:/Project/LANGUAGE/Memrapdesktopapp/reviseorlearn
#E:/Project/LANGUAGE/Memrapdesktopapp/main

if __name__ == "__main__":
    file1 = r"ROL.exe"
    file2 = r"Add.exe"
    shortcut_file1 = r"scROL.lnk"  # Đường dẫn đến nơi bạn muốn lưu tập tin shortcut
    shortcut_file2 = r"scAdd.lnk"
    working_dir = os.path.abspath(os.getcwd())
    working_dir = working_dir.replace("\\", "/")  # Thay thế tất cả "\" bằng "/"
    working_dir = r"{}/MEMRAP".format(working_dir)
    #icon_path = r"E:\Project\LANGUAGE\Memrapdesktopapp\revise.ico"  # Đường dẫn đến biểu tượng (nếu cần)
    #icon_index = 1  # Chỉ mục biểu tượng trong tệp .ico (nếu cần)
    startup_folder = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    desktop_folder = Path(os.path.expanduser("~/Desktop"))
    create_shortcut(file1, shortcut_file1, working_dir)
    create_shortcut(file2, shortcut_file2, working_dir)
    shortfile1 = Path("scROL.lnk")
    shortfile2 = Path("scAdd.lnk")
    #os.rename(old_file_path, new_file_name)
    try:
        # Di chuyển tệp shortcut đến thư mục Startup
        shutil.move(shortfile1, startup_folder / shortfile1.name)
        shutil.move(shortfile2, desktop_folder / shortfile2.name)
        print("Shortcut moved to Startup folder successfully!")
    except FileNotFoundError as e:
        print(f"Shortcut file not found: {e}")
    except shutil.Error as e:
        print(f"Error moving shortcut: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
