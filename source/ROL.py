from gtts import gTTS
from tkinter import PhotoImage, messagebox
import datetime
import re
import threading
import random
import pygame
import pyttsx3
import tkinter as tk
from translate import Translator
from customtkinter import *
from tkinter import ttk
import numpy as np
import sys
set_appearance_mode("Dark")
set_default_color_theme("blue")

class Close:
    try:
        def __init__(self, root, mark, wrongs):
            self.root = root
            self.root.title("END GAME")
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.root.geometry("1000x700+300+50")
            self.score = mark
            self.wron = wrongs
            # print(self.score.txt)
            # print(wrongs)
            # self.root.attributes('-topmost', True)
            # self.root.config(bg="#B1DDC6")
            self.labels = CTkLabel(root, text="Kiểm Tra Đã Kết Thúc! Tạm Biệt !!!", text_color="#66B2FF",
                                   font=("Helvetica", 52))
            self.labels.pack(pady=20)
            self.labelss = CTkLabel(root, text="ヾ(＠⌒ー⌒＠)ノ             (●'◡'●)", text_color="#66B2FF",
                                    font=("Helvetica", 43))
            self.labelss.pack(pady=20)
            self.dater = CTkLabel(root, text=f"Ngày ôn tập tiếp theo:{self.getnextrevise()}", text_color="#66B2FF",
                                    font=("Helvetica", 52))
            self.dater.pack(pady=20)
            self.label = CTkLabel(root, text="", font=("Helvetica", 70))
            self.label.pack(pady=34)
            max_score = self.wron + self.score
            # if max_score == self.
            self.progress = ttk.Progressbar(root, orient="horizontal", length=700, mode="determinate")
            self.progress["maximum"] = max_score
            self.progress["value"] = mark
            self.progress.pack(pady=34)
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.update_label()
            self.ok_button = CTkButton(root, text="Tạm biệt", font=("Helvetica", 61), command=self.exit)
            self.ok_button.bind("<Return>", lambda event: self.exit)
            self.ok_button.pack(pady=52)
            for i in range(9):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(6):
                self.root.grid_columnconfigure(i, weight=1)
        def getnextrevise(self):
            with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                date = file.readlines()
            day = date[0].split()
            day = [int(x) for x in day]
            now = datetime.datetime.now()
            #current_day = now.day
            #current_month = now.month
            today = datetime.date.today()
            if int(datetime.datetime.now().weekday()) == day[0] or int(datetime.datetime.now().weekday()) == day[1] or int(datetime.datetime.now().weekday()) == day[2]:  # learn
                print("learn")
                if int(datetime.datetime.now().weekday()) == max(day[0:2]):
                    random_number = random.randint(0, max(day[0:2])-1)
                    days_until_desired_weekday = (random_number - today.weekday() + 7) % 7
                    next_date = today + datetime.timedelta(days=days_until_desired_weekday)
                    return f"{next_date.strftime('%d/%m/%Y')}"

                else:
                    closest_greater_number = min([number for number in day[0:2] if number > int(datetime.datetime.now().weekday())],
                                                 default=None)
                    days_until_desired_weekday = (closest_greater_number - today.weekday() + 7) % 7
                    next_date = today + datetime.timedelta(days=days_until_desired_weekday)
                    return f"{next_date.strftime('%d/%m/%Y')}"

            elif  int(datetime.datetime.now().weekday()) == day[3]:  # loadlist
                print("load list")
                if int(datetime.datetime.now().weekday()) == max(day[3:7]):
                    random_number = random.randint(0, max(day[3:7])-1)
                    days_until_desired_weekday = (random_number - today.weekday() + 7) % 7
                    next_date = today + datetime.timedelta(days=days_until_desired_weekday)
                    return f"{next_date.strftime('%d/%m/%Y')}"
                else:
                    closest_greater_number = min([number for number in day[3:7] if number > int(datetime.datetime.now().weekday())],
                                                 default=None)
                    days_until_desired_weekday = (closest_greater_number - today.weekday() + 7) % 7
                    next_date = today + datetime.timedelta(days=days_until_desired_weekday)
                    return f"{next_date.strftime('%d/%m/%Y')}"

            elif int(datetime.datetime.now().weekday()) == day[4] or int(datetime.datetime.now().weekday()) == day[5] or int(datetime.datetime.now().weekday()) == day[6]:  # reviselist
                print("revise list")
                if int(datetime.datetime.now().weekday()) == max(day[3:7]):
                    random_number = random.randint(0, max(day[3:7])-1)
                    days_until_desired_weekday = (random_number - today.weekday() + 7) % 7
                    next_date = today + datetime.timedelta(days=days_until_desired_weekday)
                    return f"{next_date.strftime('%d/%m/%Y')}"
                else:
                    closest_greater_number = min([number for number in day[3:7] if number > int(datetime.datetime.now().weekday())],
                                                 default=None)
                    days_until_desired_weekday = (closest_greater_number - today.weekday() + 7) % 7
                    next_date = today + datetime.timedelta(days=days_until_desired_weekday)
                    return f"{next_date.strftime('%d/%m/%Y')}"


        def on_closing(self):
            if messagebox.askokcancel("Lời Tạm Biệt", "Hôm nay, bạn làm tốt lắm! \n Cố gắng hơn nhá !"):
                with open("datastorage/score.txt", "a", encoding="utf-8") as file:
                    file.write(
                        f"{(self.score / self.progress['maximum']) * 10}\n")
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/delrevise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                    except FileNotFoundError:
                        messagebox.showerror("Lỗi", "Không tìm thấy file 'delrevise.txt'.")
                    if len(data) >= 1:
                        self.root.destroy()
                        root = CTk()
                        app = LearnApp(root)
                        root.mainloop()
                    elif len(data) <= 1:
                        try:
                            with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                                data = file.readlines()
                            with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                                nfile.writelines(data)
                        except Exception as e:
                            print(e)
                        sys.exit()
                else:
                    sys.exit()

        def exit(self):
            with open("datastorage/score.txt", "a", encoding="utf-8") as file:
                file.write(f"{(self.score / self.progress['maximum']) * 10}\n")
            with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                date = file.readlines()
            day = date[0].split()
            if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                    datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                # print("not learn")
                try:
                    with open("datastorage/delrevise.txt", "r", encoding="utf-8") as file:
                        data = file.readlines()
                except FileNotFoundError:
                    messagebox.showerror("Lỗi", "Không tìm thấy file 'delrevise.txt'.")
                if len(data) >= 1:
                    self.root.destroy()
                    root = CTk()
                    app = LearnApp(root)
                    root.mainloop()
                elif len(data) <= 1:
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    sys.exit()
            else:
                sys.exit()

        def update_label(self):
            self.label.configure(text=f"Kết Quả: {self.score}/{self.progress['maximum']} Câu")
    except Exception as e:
        print(e)

class Choose:
    try:
        def __init__(self, root, vocabulary, sc, wron):
            self.root = root
            self.root.title("Choose Right")
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.root.geometry("1000x700+300+50")
            self.vocabulary = vocabulary
            self.sc = sc
            self.wr = wron
            self.buttons = []
            self.check = []
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            pygame.init()
            self.create_buttons()
        def on_closing(self):
            if messagebox.askokcancel("Warning", "Bạn có chắc chắn không tiếp tục ôn tập không ?"):
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    self.root.destroy()
                else:
                    self.root.destroy()

        def create_buttons(self):
            self.labels = CTkLabel(self.root, text="Hãy Chọn 2 nút là TỪ và NGHĨA của nhau !", text_color="#66B2FF",
                                   font=("Helvetica", 43))
            self.labels.pack(padx=10, pady=10)
            random.shuffle(self.vocabulary)
            sides = ["left", "bottom", "right", "top"]

            for word, meaning in self.vocabulary:
                word_button = CTkButton(self.root, text=word, font=("Helvetica", 34),
                                        command=lambda w=word: self.display_word(w))
                word_button.pack(pady=10, padx=10, side=random.choice(sides))

                meaning_button = CTkButton(self.root, text=meaning, font=("Helvetica", 34),
                                           command=lambda m=meaning: self.display_word(m))
                meaning_button.pack(pady=10, padx=10, side=random.choice(sides))

                self.buttons.append((word_button, meaning_button))

        def display_word(self, word):
            # print(f"Word: {word}")
            if len(self.check) < 2:
                self.check.append(word)
                # print(self.vocabulary)
                if len(self.check) == 2:
                    if (self.check[0], self.check[1]) in self.vocabulary or (
                    self.check[1], self.check[0]) in self.vocabulary:
                        # print("1")
                        self.update_buttons()
                        pygame.mixer.init()
                        sound = pygame.mixer.Sound("song/right.mp3")
                        sound.play()
                    else:
                        pygame.mixer.init()
                        sound = pygame.mixer.Sound("song/wrong.mp3")
                        sound.play()
                        # print("1")
                    self.check = []
            # print(self.check)

        def update_buttons(self):
            if (self.check[0], self.check[1]) in self.vocabulary:
                self.vocabulary.remove((self.check[0], self.check[1]))
            elif (self.check[1], self.check[0]) in self.vocabulary:
                self.vocabulary.remove((self.check[1], self.check[0]))

            print(self.vocabulary)
            delb = []
            for word_button, meaning_button in self.buttons:
                if word_button.cget("text") in self.check:
                    word_button.destroy()
                    delb.append(word_button)
                if meaning_button.cget("text") in self.check:
                    meaning_button.destroy()
                    delb.append(meaning_button)

            if (delb[0], delb[1]) in self.buttons:
                self.buttons.remove((delb[0], delb[1]))
            elif (delb[1], delb[0]) in self.buttons:
                self.buttons.remove((delb[1], delb[0]))

            for word_button, meaning_button in self.buttons:
                word_button.destroy()
                meaning_button.destroy()
            self.labels.destroy()
            self.create_buttons()
            self.checkend()

        def checkend(self):
            if len(self.buttons) == 0 or len(self.vocabulary) == 0:
                self.root.destroy()
                r_root = CTk()
                reviseapp = Close(r_root, self.sc, self.wr)
                r_root.mainloop()
    except Exception as e:
        print(e)

class VocabularyQuizApp:
    try:
        def __init__(self, root, vocabulary, mark, w):
            self.root = root
            self.root.title("Game Đoán Từ")
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.khen = ['Exellent', 'Joy wha', 'Good job bro', 'Joy wha', 'Significant', 'Yes', 'Joy wha', 'Fantastic']
            self.che = ['No', 'Sorry']
            self.root.geometry("1000x700+300+50")
            # self.root.attributes('-topmost', True)
            self.sc = mark
            self.wr = w
            self.vocabulary = list(set(vocabulary))
            self.quiz_index = 0
            self.quiz_word = ""
            self.wrong = []
            self.off = False
            pygame.init()
            self.correct_sound = pygame.mixer.Sound("song/right.mp3")
            self.wrong_sound = pygame.mixer.Sound("song/wrong.mp3")
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.current_word = None
            self.chin = []
            self.vocabulary = self.check_and_remove_chinese_words(self.vocabulary)
            print(self.chin)
            self.create_ui()

        def check_and_remove_chinese_words(self, vocab):
            chinese_words = [(word, translation) for word, translation in vocab if re.search('[\u4e00-\u9fff]', word)]
            self.chin.extend(chinese_words)
            return [(word, translation) for word, translation in vocab if not re.search('[\u4e00-\u9fff]', word)]

        def on_closing(self):
            if messagebox.askokcancel("Warning", "Bạn có chắc chắn không tiếp tục ôn tập không ?"):
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    self.root.destroy()
                else:
                    self.root.destroy()

        def create_ui(self):
            # self.root.config(bg="#B1DDC6")
            self.word_label = CTkLabel(self.root, text="", font=("Arial", 70))
            self.word_label.pack(pady=20)

            self.okentry = CTkEntry(self.root, font=("Arial", 52), width=700)
            self.okentry.pack(pady=70)
            self.okentry.bind("<Return>", lambda event: self.check_answer())

            self.check_button = CTkButton(self.root, text="Kiểm Tra", font=("Arial", 52), command=self.check_answer)
            self.check_button.pack(pady=10)

            self.result_label = CTkLabel(self.root, text="", font=("Arial", 52))
            self.result_label.pack(pady=52)

            self.next_button = CTkButton(self.root, text="BỎ QUA", font=("Arial", 52), command=self.unknown)
            self.next_button.pack(pady=10)

            self.quiz_word = self.get_random_quiz_word()
            self.update_word_label()
            for i in range(9):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(6):
                self.root.grid_columnconfigure(i, weight=1)

        def get_random_quiz_word(self):
            # print(self.wrong)
            if self.quiz_index < len(self.vocabulary):
                self.current_word, meaning = self.vocabulary[self.quiz_index]
                self.current_word = self.process(self.current_word)
                self.quiz_index += 1
                return self.create_quiz_word(self.current_word)
            elif self.wrong != []:
                self.current_word = self.wrong[0]
                self.current_word = self.process(self.current_word)
                self.wrong.pop(0)
                return self.create_quiz_word(self.current_word)
            else:
                return None

        def unknown(self):
            if self.current_word not in self.wrong:
                self.wrong.append(self.current_word)
            self.quiz_word = self.get_random_quiz_word()
            self.update_word_label()
            self.result_label.configure(text="")
            self.okentry.delete(0, tk.END)

        def create_quiz_word(self, word):
            if len(word) <= 2:
                split = 2
            else:
                split = 3
            if '.' in word:
                so, word = word.split('.')
                word = word.strip()
            word_list = list(word)
            # random.shuffle(word_list)
            num_blanks = len(word) // split
            blanks_indices = random.sample(range(len(word)), num_blanks)
            for i in blanks_indices:
                word_list[i] = "_"
            return " ".join(word_list)

        def update_word_label(self):
            if self.quiz_word is not None:
                self.word_label.configure(text=self.quiz_word)
            else:
                if len(self.chin) > 0:
                    self.root.destroy()
                    r_root = CTk()
                    reviseapp = Choose(r_root, self.chin, self.sc, self.wr)
                    r_root.mainloop()
                else:
                    self.root.destroy()
                    r_root = CTk()
                    reviseapp = Close(r_root, self.sc, self.wr)
                    r_root.mainloop()

        def process(self, word):
            if '(' in word:
                word = re.sub(r'\(.*\)', '', word)
            if '.' in word:
                so, word = word.split('.')
                word = word.strip()
            return word

        def check_answer(self):
            if self.quiz_word is not None:
                user_answer = self.okentry.get().strip()
                original_word = self.current_word
                word = self.process(original_word)
                if user_answer.lower() == word.lower():
                    self.correct_sound.play()
                    self.result_label.configure(text="|✔| Correct! (≧▽≦)")
                    self.quiz_word = self.get_random_quiz_word()
                    self.okentry.delete(0, tk.END)
                    self.update_word_label()
                else:
                    self.wrong_sound.play()
                    self.result_label.configure(text="|✘| Incorrect! (┬┬﹏┬┬)")
                    self.okentry.delete(0, tk.END)
    except Exception as e:
        print(e)

class Listen:
    try:
        def __init__(self, root, vocabulary, mark, w):
            self.root = root
            self.root.title("Nghe")
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.root.geometry("1000x700+300+50")
            self.cscore = mark
            self.w = w
            # self.root.attributes('-topmost', True)
            self.vocabulary = list(set(vocabulary))
            self.items = list(set(vocabulary))
            random.shuffle(self.items)
            # print(self.items[0][1])
            self.current_word = None
            self.current_meaning = None
            self.curpos = 0
            self.pos = 0
            pygame.init()
            self.off = False
            # self.correct_sound = pygame.mixer.Sound("song/right.mp3")
            # self.wrong_sound = pygame.mixer.Sound("song/wrong.mp3")
            self.wrong = []
            self.correct_answers = 0
            self.total_questions = 0
            self.create_ui()
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            # self.update_sscore_label()
            self.next_question()

        def on_closing(self):
            if messagebox.askokcancel("Warning", "Bạn có chắc chắn không tiếp tục ôn tập không ?"):
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    self.root.destroy()
                else:
                    self.root.destroy()

        def create_ui(self):
            # self.root.config(bg="#B1DDC6")
            self.question_label = CTkLabel(self.root, text="Hãy Nhấn vào nút start để bắt đầu", font=("Helvetica", 61))
            self.question_label.pack(pady=20)
            self.read_button = CTkButton(self.root, text="Speak Again", font=("Helvetica", 34),
                                         command=lambda: self.read_word(self.current_word))
            self.read_button.pack(pady=20)
            self.start_button = CTkButton(self.root, text="Start", font=("Haelvetica", 34),
                                          command=self.start_reading_vocabulary)
            self.start_button.pack()
            self.nlabel = CTkLabel(self.root, text="Hãy nhấn vào nút START để bắt đầu nghe !!!", font=("Helvetica", 43))
            self.nlabel.pack(pady=20)

            entry_font = ("Helvetica", 43)
            self.answer = CTkEntry(self.root, font=entry_font, width=700, state=tk.DISABLED)
            self.answer.pack(pady=30)
            self.score_label = CTkLabel(self.root, text=f"Điểm số: 0/{len(self.items)}", font=("Helvetica", 52))
            self.score_label.pack(pady=10, side=BOTTOM)
            self.ok = CTkButton(self.root, text="OK", font=("Helvetica", 52), command=self.check_answer)
            self.ok.pack(pady=10)
            self.answer.bind("<Return>", lambda event: self.check_answer())

            self.label = CTkLabel(self.root, text="", font=("Helvetica", 43))
            self.label.pack(pady=20)
            for i in range(9):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(6):
                self.root.grid_columnconfigure(i, weight=1)

        def start_reading_vocabulary(self):
            self.start_button.destroy()
            self.answer.configure(state=tk.NORMAL)
            self.nlabel.configure(text='Nhập đáp án dưới đây:')
            self.read_word(self.current_word)

        def next_question(self):
            # self.root.after(1000)
            self.answer.delete(0, tk.END)
            # print(type(self.items))
            if self.curpos < len(self.items):
                self.current_word, self.current_meaning = self.items[self.curpos]
                self.current_word = self.current_word.lstrip('- ')
                if re.search('[\u4e00-\u9fff]', self.current_word):
                    self.question_label.configure(text=f"Listen And Write The MEANING!")
                else:
                    self.question_label.configure(text=f"Listen And Write The WORD!")
                if self.curpos > 0:
                    self.root.after(2500, self.read_word, self.current_word)
                self.curpos += 1
            elif self.pos < len(self.wrong):
                # self.items = self.wrong.copy()
                # self.wrong = []
                self.current_word, self.current_meaning = self.wrong[self.pos]
                self.current_word = self.current_word.lstrip('- ')
                if re.search('[\u4e00-\u9fff]', self.current_word):
                    self.question_label.configure(text=f"Listen And Write The MEANING!")
                else:
                    self.question_label.configure(text=f"Listen And Write The WORD!")
                self.root.after(2500, self.read_word, self.current_word)
                self.pos += 1
            else:
                self.off = False
                vocabs = self.check_and_remove_chinese_words(self.vocabulary)
                if len(vocabs) > 0:
                    self.root.destroy()
                    rd_root = CTk()
                    # print("-----------------------------")
                    # print(self.cscore+self.correct_answers)
                    # print(self.total_questions-self.cscore+self.w)
                    flard_app = VocabularyQuizApp(rd_root, self.vocabulary, (self.cscore + self.correct_answers),
                                                  (self.total_questions - self.correct_answers + self.w))
                    rd_root.mainloop()
                else:
                    self.root.destroy()
                    rd_root = CTk()
                    # print("-----------------------------")
                    # print(self.cscore+self.correct_answers)
                    # print(self.total_questions-self.cscore+self.w)
                    flard_app = Choose(rd_root, self.vocabulary, (self.cscore + self.correct_answers),
                                       (self.total_questions - self.correct_answers + self.w))
                    rd_root.mainloop()
            # self.read_word(self.current_word)

        def check_and_remove_chinese_words(self, vocab):
            return [(word, translation) for word, translation in vocab if not re.search('[\u4e00-\u9fff]', word)]

        def read_enword_thread(self, word):
            try:
                self.label.configure(text="")
                self.label.configure(text_color="white")
                engine = pyttsx3.init()
                engine.setProperty('rate', 106)
                engine.setProperty('volume', 2)
                engine.say(word)
                engine.runAndWait()
                return
            except Exception as e:
                print(e)

        def read_cnword_thread(self, word):
            try:
                self.label.configure(text="")
                self.label.configure(text_color="white")
                tts = gTTS(word, lang='zh-cn')
                temp_file = "temp.mp3"
                tts.save(temp_file)
                pygame.mixer.init()
                pygame.mixer.music.load(temp_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.quit()
                os.remove(temp_file)
            except Exception as e:
                print(e)

        def read_word(self, word):
            try:
                if re.search('[\u4e00-\u9fff]', self.current_word):
                    thread = threading.Thread(target=self.read_cnword_thread, args=(word,))
                    thread.start()
                else:
                    thread = threading.Thread(target=self.read_enword_thread, args=(word,))
                    thread.start()
            except Exception as e:
                print(e)

        def check_answer(self):
            selected_ans = self.answer.get().lower().strip()
            if selected_ans == "" or selected_ans == " " or selected_ans == "  " or selected_ans == "   ":
                return
            if re.search('[\u4e00-\u9fff]', self.current_word):
                rightword = self.current_meaning.lower()
                # word = self.current_meaning
            else:
                rightword = self.current_word.lower()
                # word = self.current_word
            # if '(' in word:
            #    word = re.sub(r'\(.*\)', '', word)
            if '(' in rightword:
                rightword = re.sub(r'\(.*\)', '', rightword)
            if selected_ans in rightword:
                self.label.configure(text=f"|✔| Correct! (≧▽≦)\nKết quả=> |{rightword}|")
                self.label.configure(text_color="green")
                self.correct_answers += 1
                pygame.mixer.init()
                sound = pygame.mixer.Sound("song/right.mp3")
                sound.play()
            else:
                self.label.configure(text=f"|✘| Incorrect! (┬┬﹏┬┬)\nĐáp án=> |{rightword}|")
                self.label.configure(text_color="red")
                self.wrong.append((self.current_word, self.current_meaning))
                # messagebox.showinfo("Kết quả", f"Sai! Đáp án đúng là '{rightword}'")
                pygame.mixer.init()
                sound = pygame.mixer.Sound("song/wrong.mp3")
                sound.play()

            self.total_questions += 1
            self.update_score_label()
            self.next_question()

        def update_score_label(self):
            score_text = f"Điểm: {self.correct_answers}/{self.total_questions}"
            self.score_label.configure(text=score_text)
    except Exception as e:
        print(e)

class TL:
    try:
        def __init__(self, root, vocabulary, mark, w):
            self.root = root
            self.root.title("Tự luận")
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.root.geometry("1000x700+300+50")
            self.cscore = mark
            self.w = w
            self.khen = ['Good', 'Triple kill', 'Exellent', 'Mega kill', 'Ace', 'Fantastic']
            self.che = ['No', 'Sorry']
            # self.root.attributes('-topmost', True)
            self.vocab = list(set(vocabulary))
            self.items = list(set(vocabulary))
            random.shuffle(self.items)
            # print(self.items[0][1])
            self.current_word = None
            self.current_meaning = None
            self.curpos = 0
            self.wrong = []
            self.correct_answers = 0
            self.total_questions = 0
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.off = False
            pygame.init()
            self.correct_sound = pygame.mixer.Sound("song/right.mp3")
            self.create_ui()
            self.update_score_label()
            self.next_question()

        def on_closing(self):
            if messagebox.askokcancel("Warning", "Bạn có chắc chắn không tiếp tục ôn tập không ?"):
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    self.root.destroy()
                else:
                    self.root.destroy()

        def create_ui(self):
            # self.root.config(bg="#B1DDC6")
            self.question_label = CTkLabel(self.root, text="", font=("Helvetica", 52))
            self.question_label.pack(pady=20)
            # self.nlabel = CTkLabel(self.root, text="Nhập đáp án dưới đây:", font=("Helvetica", 43))
            # self.nlabel.pack(pady=30)
            entry_font = ("Helvetica", 52)
            self.answer = CTkEntry(self.root, font=entry_font, width=700, placeholder_text="Nhập đáp án ở đây ...")
            self.answer.pack(pady=70)

            self.ok = CTkButton(self.root, text="OK", font=("Helvetica", 43), command=self.check_answer)
            self.ok.pack(pady=10)
            self.answer.bind("<Return>", lambda event: self.check_answer())

            self.label = CTkLabel(self.root, text="", font=("Helvetica", 43))
            self.label.pack(pady=20)

            self.score_label = CTkLabel(self.root, text="", font=("Helvetica", 52))
            self.score_label.pack(pady=10, side=BOTTOM)
            for i in range(9):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(6):
                self.root.grid_columnconfigure(i, weight=1)

        def next_question(self):
            # print(type(self.items))
            if self.curpos < len(self.items):
                self.current_word, self.current_meaning = self.items[self.curpos]
                self.current_word = self.current_word.lstrip('- ')
                if re.search('[\u4e00-\u9fff]', self.current_word):
                    self.question_label.configure(text=f"What is the meaning of '{self.current_word}'?")
                else:
                    self.question_label.configure(text=f"What is the meaning of '{self.current_meaning}'?")
                self.curpos += 1
            elif self.wrong:
                self.items = self.wrong.copy()
                self.wrong = []
                self.curpos = 0
            else:
                self.off = True
                self.root.destroy()
                l_root = CTk()
                # print("------------------")
                # print(self.cscore+self.correct_answers)
                # print(self.total_questions-self.cscore+self.w)
                l = Listen(l_root, self.vocab, (self.cscore + self.correct_answers),
                           (self.total_questions - self.correct_answers + self.w))
                l_root.mainloop()

        def hide_label(self):
            self.label.configure(text="")
            self.label.configure(text_color="white")

        def check_answer(self):
            selected_ans = self.answer.get().lower().strip()
            # print(len(selected_ans))
            # print(len(self.current_meaning)/2)
            if selected_ans == "" or selected_ans == " " or selected_ans == "  " or selected_ans == "   ":
                return
            if re.search('[\u4e00-\u9fff]', self.current_word):
                rightword = self.current_meaning.lower()
                # word = self.current_meaning
            else:
                rightword = self.current_word.lower()
                # word = self.current_word
            if '(' in rightword:
                rightword = re.sub(r'\(.*\)', '', rightword)
            if selected_ans in rightword:
                # self.read_word()
                pygame.mixer.init()
                sound = pygame.mixer.Sound("song/right.mp3")
                sound.play()
                self.read_word(f"{self.current_word}")
                self.label.configure(text=f"|✔| Correct! (≧▽≦) \nKết quả => |{rightword}| ")
                self.label.configure(text_color="green")
                self.correct_answers += 1

                self.answer.delete(0, tk.END)
            else:
                # self.read_word(random.choice(self.che))
                pygame.mixer.init()
                sound = pygame.mixer.Sound("song/wrong.mp3")
                sound.play()
                # self.read_word(f"{word}")
                self.label.configure(text=f"|✘| Incorrect! (┬┬﹏┬┬) \nĐáp án => |{rightword}| ")
                # messagebox.showinfo("Kết quả", f"Sai!(┬┬﹏┬┬) \n Đáp án đúng là '{self.current_word}'")
                self.label.configure(text_color="red")
                self.wrong.append((self.current_word, self.current_meaning))
                # self.root.after(2500, self.hide_label)
                self.answer.delete(0, tk.END)
            self.root.after(2500, self.hide_label)
            self.total_questions += 1
            self.update_score_label()

            self.next_question()

        def update_score_label(self):
            score_text = f"Điểm: {self.correct_answers}/{self.total_questions}"
            self.score_label.configure(text=score_text)

        def read_enword_thread(self, word):
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 124)
                engine.setProperty('volume', 2)
                engine.say(word)
                engine.runAndWait()

                return
            except Exception as e:
                print(e)

        def read_cnword_thread(self, word):
            try:
                self.label.configure(text="")
                self.label.configure(text_color="white")
                tts = gTTS(word, lang='zh-cn')
                temp_file = "temp.mp3"
                tts.save(temp_file)
                pygame.mixer.init()
                pygame.mixer.music.load(temp_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.quit()
                os.remove(temp_file)
            except Exception as e:
                print(e)

        def read_word(self, word):
            try:
                if re.search('[\u4e00-\u9fff]', word):
                    thread = threading.Thread(target=self.read_cnword_thread, args=(word,))
                    thread.start()
                else:
                    thread = threading.Thread(target=self.read_enword_thread, args=(word,))
                    thread.start()
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

class Multichoice:
    try:
        def __init__(self, root, vocabulary):
            vocabulary = list(set(vocabulary))
            self.root = root
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.root.title("Multiple Choice Quiz")
            self.root.geometry("1000x700+300+50")
            self.root.attributes('-topmost', True)
            # self.vocabulary = vocabulary
            self.items = list(set(vocabulary))
            random.shuffle(self.items)
            self.items = list(set(self.items))
            self.current_word = None
            self.current_meaning = None
            self.options = []
            self.curpos = 0
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.khen = ['Exellent', 'Joy wha', 'Good job bro', 'Joy wha', 'Significant', 'Yes', 'Joy wha',
                         'Fantastic']
            # self.khen = ['Good','Yes','Wow','Join Wa', 'Triple kill', 'Exellent', 'Mega kill', 'Ace', 'Fantastic']
            self.che = ['No', 'Sorry']
            self.wrong = []
            # pygame.init()
            # self.correct_sound = pygame.mixer.Sound("song/right.mp3")
            # self.wrong_sound = pygame.mixer.Sound("song/wrong.mp3")
            self.score = 0
            self.total_questions = 0
            self.create_ui()
            self.off = False
            self.next_question()

        def on_closing(self):
            if messagebox.askokcancel("Warning", "Bạn có chắc chắn không tiếp tục ôn tập không ?"):
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    self.root.destroy()
                else:
                    self.root.destroy()

        def create_ui(self):
            self.question_label = CTkLabel(self.root, text="", font=("Helvetica", 52))
            self.question_label.pack(pady=20)
            # self.root.config(bg="#B1DDC6")
            self.option_buttons = []
            for i in range(4):
                button = CTkButton(self.root, text="", font=("Helvetica", 52),
                                   command=lambda i=i: self.check_answer(i))
                button.pack(pady=16)
                self.option_buttons.append(button)
            self.label = CTkLabel(self.root, text="", font=("Helvetica", 43))
            self.label.pack(pady=20)
            self.score_label = CTkLabel(self.root, text=f"Điểm số: 0/{len(self.items)}", font=("Helvetica", 52))
            self.score_label.pack(pady=16, side=BOTTOM)
            for i in range(9):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(6):
                self.root.grid_columnconfigure(i, weight=1)

        def next_question(self):
            if self.curpos < len(self.items):
                self.current_word, self.current_meaning = self.items[self.curpos]
                self.curpos += 1
                self.question_label.configure(text=f"What is the meaning of '{self.current_word}'?")
                self.options = [self.current_meaning]
                while len(self.options) < 4:
                    option = random.choice([pair[1] for pair in self.items])
                    if option not in self.options:
                        self.options.append(option)
                random.shuffle(self.options)
                for i, option in enumerate(self.options):
                    self.option_buttons[i].configure(text=option)
            elif self.wrong:
                self.current_word, self.current_meaning = self.wrong.pop(0)
                self.question_label.configure(text=f"What is the meaning of '{self.current_word.lstrip('- ')}'?")
                self.options = [self.current_meaning]
                while len(self.options) < 4:
                    option = random.choice([pair[1] for pair in self.items])
                    if option not in self.options:
                        self.options.append(option)
                random.shuffle(self.options)
                for i, option in enumerate(self.options):
                    self.option_buttons[i].configure(text=option)
            else:
                self.off = True
                self.root.destroy()
                Tl_root = CTk()
                # print(self.score.txt)
                # print(self.total_questions-self.score.txt)
                Tl = TL(Tl_root, self.items, self.score, (self.total_questions - self.score))
                Tl_root.mainloop()

        def read_word_thread(self, word):
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 124)
                engine.setProperty('volume', 2)
                engine.say(word)
                engine.runAndWait()
                return
            except Exception as e:
                print(e)

        def read_word(self, word):
            try:
                thread = threading.Thread(target=self.read_word_thread, args=(word,))
                thread.start()
            except Exception as e:
                print(e)

        def check_answer(self, selected_option):
            selected_meaning = self.options[selected_option]
            if selected_meaning == self.current_meaning:
                pygame.mixer.init()
                sound = pygame.mixer.Sound("song/right.mp3")
                sound.play()
                # self.read_word(f"{random.choice(self.khen)}")
                self.label.configure(text="|✔| Correct! (≧▽≦)")
                self.label.configure(text_color="green")
                # messagebox.showinfo("Kết quả", f"Đúng! Là {self.current_word}")
                self.score += 1  # Tăng điểm số nếu đúng
                self.total_questions += 1
                # self.root.after(1501, self.hide_label)
            else:
                # self.read_word(random.choice(self.che))
                pygame.mixer.init()
                sound = pygame.mixer.Sound("song/wrong.mp3")
                sound.play()
                self.label.configure(text="|✘| Incorrect! (┬┬﹏┬┬)")
                self.label.configure(text_color="red")
                self.wrong.append((self.current_word, self.current_meaning))
                # messagebox.showinfo("Kết quả", f"Sai! Đáp án đúng là '{self.current_meaning}'")
                self.total_questions += 1
            self.root.after(2500, self.hide_label)
            self.update_score_label()
            self.next_question()

        def hide_label(self):
            self.label.configure(text="")
            self.label.configure(text_color="white")

        def update_score_label(self):
            score_text = f"Điểm số: {self.score} / {self.total_questions}"
            self.score_label.configure(text=score_text)
    except Exception as e:
        print(e)
class Transl:
    try:
        def __init__(self, troot):
            self.troot = troot
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.troot.winfo_id())
                self.troot.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.translated_text = ""
            troot.title("TRANSLATOR")
            self.troot.configure(bg="black")
            # self.troot.geometry("300x400")
            self.troot.attributes('-topmost', True)
            self.language_frame = tk.Frame(troot, bg="black")
            self.language_frame.pack(pady=5, padx=10, side=tk.TOP)
            self.from_lang_var = tk.StringVar()
            self.to_lang_var = tk.StringVar()
            self.from_lang_var.set("vi")
            self.to_lang_var.set("en")
            self.from_lang_menu = tk.OptionMenu(self.language_frame, self.from_lang_var, "vi", "en")
            self.from_lang_menu.pack(padx=5, side=tk.LEFT)
            self.to_lang_menu = tk.OptionMenu(self.language_frame, self.to_lang_var, "vi", "en")
            self.to_lang_menu.pack(padx=5, side=tk.RIGHT)
            self.input_text_widget = tk.Text(troot, height=10, width=30)
            self.input_text_widget.pack(pady=5, padx=10, side=tk.LEFT)
            self.translate_button = tk.Button(troot, text="Translate ➠", command=self.translate_text, bg="green",
                                              fg="white", font=("Arial", 16))
            self.translate_button.pack(side=tk.LEFT)
            self.read_en_button = tk.Button(troot, text="Đọc", command=self.read_word, bg="red",
                                            fg="white", font=("Arial", 16))
            self.read_en_button.pack(side=tk.LEFT)
            # self.slabel = tk.Label(text='➠', bg="black", fg="white", font=("Arial", 25))
            # self.slabel.pack(side=tk.LEFT)
            self.output_text_widget = tk.Text(troot, height=10, width=30)
            self.output_text_widget.pack(pady=5, padx=10, side=tk.LEFT)

        def read_word(self):
            engine = pyttsx3.init()
            engine.setProperty('rate', 106)
            engine.setProperty('volume', 2)
            engine.say(self.translated_text)
            engine.runAndWait()

        def translate_text(self):
            input_text = self.input_text_widget.get("1.0", "end-1c")
            from_lang = self.from_lang_var.get()
            to_lang = self.to_lang_var.get()
            if from_lang != to_lang:
                translator = Translator(to_lang=to_lang, from_lang=from_lang)
                self.translated_text = translator.translate(input_text)
                self.output_text_widget.delete("1.0", "end")
                self.output_text_widget.insert("1.0", self.translated_text)
            else:
                self.output_text_widget.delete("1.0", "end")
                self.output_text_widget.insert("1.0", f"{input_text}\n Hãy chọn ngôn ngữ khác.")
    except Exception as e:
        print(e)
class LinearRegression:
    try:
        def __init__(self):
            self.A = np.array(
                [[2.3, 4.1, 6.0, 3.4, 8.2, 5.5, 7.7, 9.0, 1.8, 0.9, 3.1, 7.0, 5.3, 2.7, 4.6, 8.7, 6.9, 1.5, 0.3, 2.0,
                  3.8,
                  4.8, 5.9, 9.5, 7.2, 6.4, 8.0, 1.2, 0.5, 2.5, 4.4, 3.0, 6.8, 5.2, 9.8, 7.9, 5.7, 8.5, 7.4, 2.2, 3.6,
                  1.0,
                  4.9, 6.6, 8.9, 9.3, 8.5, 7.2, 9.1, 7.8, 8.0, 7.3, 9.5, 8.9, 8.2, 7.7, 7.1, 9.3, 8.4, 7.9, 8.6, 9.0,
                  7.5,
                  8.8, 8.3, 7.6, 9.2, 7.4, 8.7, 8.1, 7.0, 9.4, 8.2, 7.8, 8.9, 7.3, 9.1, 8.5, 7.2, 9.0, 8.6, 7.5, 8.7,
                  8.1,
                  7.6, 9.2, 8.4, 7.9, 9.3, 8.3, 7.1, 9.5, 8.8, 8.0, 7.5, 8.2, 7.9, 10.0, 9.1, 11.5, 9.8, 8.7, 8.0, 10.4,
                  9.3, 8.6, 7.2, 11.2, 7.8, 9.7, 10.8, 7.4, 10.6, 11.0, 8.5, 10.3, 7.1, 9.0, 8.9, 11.4, 10.7, 9.6, 11.1,
                  8.8, 8.4, 10.5, 9.4, 9.5, 11.3, 7.3, 7.7, 8.1, 10.2, 7.6, 7.0, 10.9, 9.2, 8.3, 10.1, 7.5, 9.9, 7.9,
                  10.0, 7.3, 8.1, 6.7, 9.2, 7.8, 8.5, 9.8, 6.2, 8.9, 7.0, 7.5, 8.2, 7.1, 9.4, 6.9, 8.7, 6.5, 9.1, 7.2,
                  8.4, 7.7, 8.0, 9.5, 6.6, 8.3, 7.4, 8.6, 6.3, 9.3, 6.8, 9.7, 8.8, 7.9, 9.0, 6.4, 8.5, 7.6, 8.1, 6.7,
                  9.2, 7.8, 9.6, 6.1, 8.0, 7.3, 9.5, 0.5, 1.2, 2.0, 3.3, 4.1, 5.7, 6.2, 7.8, 8.0, 3.9, 4.5, 9.2, 7.0,
                  1.8, 0.9, 2.5, 6.6, 5.0, 3.7, 9.8, 1.0, 4.9, 7.5, 6.7, 5.2, 2.8, 0.2, 1.5, 8.5, 3.0, 4.8, 9.5, 8.7,
                  7.2, 2.3, 5.9, 1.7, 0.7, 6.9, 9.0, 8.2, 3.5, 0.1, 4.0, 2.2, 5.4, 7.7, 8.9, 1.3, 6.0, 7.5, 8.2, 6.8,
                  9.4, 7.1, 8.7, 6.5, 9.0, 7.9, 8.1, 6.2, 8.5, 7.3, 9.2, 7.7, 6.4, 8.9, 7.0, 8.6, 6.1, 9.1, 7.6, 8.8,
                  6.7, 9.3, 7.8, 8.3, 6.6, 8.4, 7.2, 9.5, 6.9, 8.0, 7.4, 9.6, 6.3, 8.7, 7.5, 9.4, 7.1, 8.2, 6.8, 9.0,
                  7.9, 8.1, 6.2, 8.5, 7.3, 9.2, 7.7, 7.5, 8.2, 6.8, 9.3, 7.1, 8.5, 7.7, 8.0, 7.9, 8.8, 7.3, 9.0, 8.4,
                  7.2, 9.6, 7.4, 8.1, 7.0, 8.6, 8.7, 6.5, 9.2, 7.8, 8.3, 6.9, 9.1, 8.9, 7.6, 9.4, 7.5, 8.2, 6.8, 9.3,
                  7.1, 8.5, 7.7, 8.0, 7.9, 8.8, 7.3, 9.0, 8.4, 7.2, 9.6, 7.4, 8.1, 7.0, 8.6]]).T
            self.b = np.array(
                [[11, 13, 14, 12, 18, 15, 17, 20, 10, 10, 11, 16, 15, 12, 13, 19, 16, 10, 10, 11, 12, 14, 15, 20,
                  17, 16, 18,
                  10, 10, 11, 13, 12, 16, 14, 20, 18, 15, 19, 17, 11, 12, 10, 14, 16, 20, 20, 12, 10, 14, 11, 13,
                  9, 16, 15,
                  12, 10, 8, 17, 13, 11, 14, 15, 10, 16, 12, 9, 15, 11, 14, 13, 8, 17, 12, 11, 15, 9, 14, 12, 10,
                  15, 14, 10,
                  14, 13, 9, 15, 13, 11, 17, 12, 8, 16, 16, 13, 8, 10, 9, 14, 11, 15, 12, 11, 10, 14, 12, 11, 8,
                  15, 9, 12, 14, 8, 14, 15, 11, 14, 8, 11, 11, 15, 14, 12, 15, 11, 11, 14, 12, 12, 15, 8, 9, 10,
                  14, 9, 8, 14, 12, 11, 14, 8, 12, 9, 14, 13, 11, 14, 15, 12, 18, 20, 10, 16, 13, 15, 17, 12, 19, 11,
                  18, 10, 16, 13, 17, 15, 14, 19, 10, 17, 14, 18, 11, 20, 12, 19, 19, 16, 17, 11, 18, 14, 17, 13, 20,
                  15, 20, 10, 16, 13, 19, 10, 12, 13, 15, 14, 16, 17, 18, 15, 12, 14, 17, 16, 11, 10, 13, 17, 15, 13,
                  18, 11, 15, 17, 16, 14, 12, 10, 12, 18, 13, 15, 18, 18, 16, 11, 16, 11, 11, 17, 18, 18, 14, 10, 14,
                  12, 15, 17, 18, 11, 16, 10, 11, 10, 12, 11, 13, 10, 12, 11, 13, 10, 12, 11, 14, 13, 10, 12, 11, 14,
                  10, 13, 11, 14, 10, 13, 11, 15, 10, 14, 11, 15, 10, 14, 11, 15, 10, 14, 11, 16, 12, 15, 11, 16, 12,
                  15, 11, 16, 12, 15, 16, 11, 12, 10, 14, 11, 13, 12, 11, 12, 14, 11, 15, 13, 11, 16, 11, 12, 11, 14,
                  14, 10, 14, 12, 13, 10, 15, 15, 11, 15, 12, 13, 10, 15, 11, 13, 12, 12, 12, 14, 11, 15, 13, 11, 16,
                  11, 12, 11, 14]]).T
            self.ones = np.ones((self.A.shape[0], 1), dtype=np.int8)
            self.A = np.concatenate((self.A, self.ones), axis=1)
            self.x_init = np.array([[1], [2]])
            self.iteration = 90
            self.learning_rate = 0.0001
            self.coefficients = self.gradient_descent(self.x_init, self.learning_rate, self.iteration)

        def cost(self, x):
            m = self.A.shape[0]
            return 0.5 / m * np.linalg.norm(self.A.dot(x) - self.b, 2) ** 2

        def grad(self, x):
            m = self.A.shape[0]
            return 1 / m * self.A.T.dot(self.A.dot(x) - self.b)

        def check_grad(self, x):
            eps = 1e-4
            g = np.zeros_like(x)
            for i in range(len(x)):
                x1 = x.copy()
                x2 = x.copy()
                x1[i] += eps
                x2[i] -= eps
                g[i] = (self.cost(x1) - self.cost(x2)) / (2 * eps)

            g_grad = self.grad(x)
            if np.linalg.norm(g - g_grad) > 1e-5:
                print("WARNING: CHECK GRADIENT FUNC!")

        def gradient_descent(self, x_init, learning_rate, iteration):
            x_list = [x_init]
            m = self.A.shape[0]

            for i in range(iteration):
                x_new = x_list[-1] - learning_rate * self.grad(x_list[-1])
                if np.linalg.norm(self.grad(x_new)) / m < 0.5:  # stop GD
                    break
                x_list.append(x_new)

            return x_list

        def get_num_vocab(self, score):
            num_vocab = score * self.coefficients[-1][1] + self.coefficients[-1][0]
            return int(num_vocab)
            # predictor = VocabularyPredictor()
            # x_test = 9
            # predicted_vocab = predictor.get_num_vocab(x_test)
            # print(f"Predicted Vocabulary: {predicted_vocab}")
    except Exception as e:
        print(e)
class SpacedRepetitionScheduler:
    try:
        def __init__(self):
            self.items = []

        def next_review_time(self, last_review_time, difficulty):
            initial_interval = datetime.timedelta(days=1)
            increase_factor = 2.5
            interval = initial_interval * (2 ** (difficulty - 1) * increase_factor)
            next_time = last_review_time + interval
            return next_time

        def schedule_next_reviews(self):
            current_time = datetime.datetime.now()
            for item in self.items:
                last_review_time = current_time
                next_time = self.next_review_time(last_review_time, item["difficulty"])
                print(f"{item['name']}: {next_time}")
    except Exception as e:
        print(e)
class FlashcardApp:
    try:
        def __init__(self, root, vocab):
            self.root = root
            self.root.title("Ôn Tập FlashCard")
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            self.root.config(padx=50, pady=50)
            self.root.geometry("1000x700+300+50")
            # self.root.attributes('-topmost', True)
            self.unknown_words = []
            self.items = vocab
            # random.shuffle(self.items)
            # print(vocabulary)
            self.current_pos = 0
            self.off = False
            self.current_word = self.items[0][0].lstrip('- ')
            self.current_meaning = self.items[0][1]
            self.show_mean = False
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.vocabu = []
            # print(self.fisrtvocab)
            self.create_ui()

        def on_closing(self):
            if messagebox.askokcancel("Warning", "Bạn có chắc chắn không tiếp tục ôn tập không ?"):
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    self.root.destroy()
                else:
                    self.root.destroy()


        def tranlate(self):
            self.transl_window = tk.Toplevel(self.root)
            trans = Transl(self.transl_window)

        def create_ui(self):
            self.trans_button = CTkButton(self.root, text="Dịch", font=("Ariel", 34, "italic"), command=self.tranlate)
            self.trans_button.grid(row=0, column=0, padx=70)

            self.show_button = CTkButton(self.root, text="Show", font=("Ariel", 34, "italic"),
                                         command=self.show_meaning)
            self.show_button.grid(row=0, column=3, padx=50)

            self.read_button = CTkButton(self.root, text="Read", font=("Ariel", 34, "italic"), command=self.read_word)
            self.read_button.grid(row=0, column=5, padx=50)

            self.card_title = CTkLabel(self.root, text="Tiếng Anh", font=("Ariel", 34, "italic"))
            self.card_title.grid(row=1, column=3, pady=25)
            if self.items[0][0].lstrip('- ').count(".") == 1:
                self.items[0][0] = self.items[0][0].lstrip('- ').split(".")[1]
            self.card_word = CTkLabel(self.root, text=self.items[0][0], font=("Ariel", 52, "bold"))
            self.card_word.grid(row=5, column=3, columnspan=2, padx=20, pady=20, sticky="nsew")

            self.wrong_img = PhotoImage(file="images/wrong.png")
            self.unknown_button = tk.Button(self.root, image=self.wrong_img, highlightthickness=0,
                                            command=self.unknown_word)
            self.unknown_button.grid(row=7, column=0)

            self.check_image = PhotoImage(file="images/right.png")
            self.known_button = tk.Button(self.root, image=self.check_image, highlightthickness=0,
                                          command=self.next_card)
            self.known_button.grid(row=7, column=5)

            self.previous_button = CTkButton(self.root, text="Quay lại", font=("Ariel", 34, "italic"),
                                             command=self.show_previous_card)
            self.previous_button.grid(row=8, column=2, columnspan=2)
            for i in range(9):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(6):
                self.root.grid_columnconfigure(i, weight=1)

        def savefile(self):
            print("!")
            with open("afterevise.txt", "r", encoding="utf-8") as revise_file:
                lines = revise_file.readlines()
            for line in lines:
                linee = line.split(':')
                self.vocabu.append(linee)

        def read_enword_thread(self, word):
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 106)  # Tốc độ nói (từ 50 đến 300)
                engine.setProperty('volume', 2)
                engine.say(word)
                engine.runAndWait()
                return
            except Exception as e:
                print(e)

        def read_cnword_thread(self, word):
            try:
                tts = gTTS(word, lang='zh-cn')
                temp_file = "temp.mp3"
                tts.save(temp_file)
                pygame.mixer.init()
                pygame.mixer.music.load(temp_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.quit()
                os.remove(temp_file)
            except Exception as e:
                print(e)

        def read_word(self):
            try:
                if re.search('[\u4e00-\u9fff]', self.current_word):
                    thread = threading.Thread(target=self.read_cnword_thread, args=(self.current_word,))
                    thread.start()
                else:
                    thread = threading.Thread(target=self.read_enword_thread, args=(self.current_word,))
                    thread.start()
            except Exception as e:
                print(e)

        def show_previous_card(self):
            if self.current_pos > 0:
                self.current_pos -= 1
                self.current_word, self.current_meaning = self.items[self.current_pos]
                if self.current_word.count(".") == 1:
                    self.current_word = self.current_word.split(".")[1]
                # self.vd.config(text=f"Vd:{self.get_sentence_with_word(self.current_word)}")
                # print(self.vocabulary_annotations[self.current_pos])
                self.card_word.configure(text=self.current_word.lstrip('- '))
                self.card_title.configure(text="Tiếng Anh")
                self.show_mean = False

        def show_meaning(self):
            self.show_mean = not (self.show_mean)
            # print(self.show_mean)
            if self.show_mean:
                self.card_word.configure(text=self.current_meaning)
                self.card_title.configure(text="Tiếng Việt")
            else:
                self.card_word.configure(text=self.current_word)
                self.card_title.configure(text="Tiếng Anh")

        def next_card(self):
            if self.current_pos + 1 < len(self.items):
                self.current_pos += 1
                key, value = self.items[self.current_pos]
                self.current_word = key.lstrip('- ')
                if self.current_word.count(".") == 1:
                    self.current_word = self.current_word.split(".")[1]
                self.current_meaning = value
                self.card_word.configure(text=self.current_word)
                # self.vd.config(text=f"Vd:{self.get_sentence_with_word(self.current_word)}")
            else:
                if len(self.unknown_words):
                    self.current_word = self.unknown_words[0][0].lstrip('- ')
                    if self.current_word.count(".") == 1:
                        self.current_word = self.current_word.split(".")[1]
                    self.current_meaning = self.unknown_words[0][1]
                    # self.vd.config(text=f"Vd:{self.get_sentence_with_word(self.current_word)}")
                    self.card_word.configure(text=self.current_word)
                    self.unknown_words = list(self.unknown_words)
                    self.unknown_words.pop(0)
                    self.unknown_words = tuple(self.unknown_words)
                else:
                    # time.sleep(0.7)
                    self.root.destroy()
                    try:
                        print(self.items)
                        print("2")
                        M_root = CTk()
                        Mul = Multichoice(M_root, self.items)
                        M_root.mainloop()
                    except Exception as e:
                        print(e)


        def unknown_word(self):
            self.unknown_words = list(self.unknown_words)  # Chuyển từ tuple sang list
            self.unknown_words.append((self.current_word, self.current_meaning))
            self.unknown_words = tuple(self.unknown_words)
            self.next_card()

        '''
        def loadvocab(self):
            vocab  = []
            with open("delrevise.txt","r",encoding="utf-8") as file:
                data = file.readlines()
            for idx,line in enumerate(data,start=0):
                if line.strip() and line.count(":") == 1:
                    word, mean = line.split(":")
                    # if '(' in word:
                    #    word = re.sub(r'\(.*\)', '', word)
                    vocab.append((word.strip(), mean.strip()))
                elif "---------------" in line:
                    end = idx
                    break
            with open("delrevise.txt","w",encoding="utf-8") as file:
                file.writelines(data[end+1:])
            return vocab
        '''
    except Exception as e:
        print(e)
class LearnApp:
    try:
        def __init__(self, root):
            self.root = root
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = windll.user32.GetParent(self.root.winfo_id())
                self.root.iconbitmap("images/revise.ico")
                title_bar_color = 0x00242424
                title_text_color = 0x00FFFFFF
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    35,
                    byref(c_int(title_bar_color)),
                    sizeof(c_int))
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    36,
                    byref(c_int(title_text_color)),
                    sizeof(c_int))
            except:
                pass
            with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                date = file.readlines()
            day = date[0].split()
            # print(day)
            self.title = ""
            if int(datetime.datetime.now().weekday()) == int(day[0]) or int(datetime.datetime.now().weekday()) == int(
                    day[1]) or int(datetime.datetime.now().weekday()) == int(day[2]):  # learn
                print("learn")
                self.vocabulary = list(set(self.load_learn()))
                self.title = "Ôn tập đã thêm gần đây"

            elif int(datetime.datetime.now().weekday()) == int(day[3]):  # loadlist

                if self.check_log(datetime.datetime.now().strftime("%Y-%m-%d")):
                    print("load list")
                    self.vocabulary = list(set(self.reviseload()))
                else:
                    print("load list rồi")
                    self.load_list()
                    self.checkok()
                    self.vocabulary = list(set(self.reviseload()))
                self.title = "Học từ vựng mới"

            else:  # reviselist
                print("revise list")
                self.clearcheck()
                self.vocabulary = list(set(self.reviseload()))
                self.title = "Ôn tập các từ vựng đã học"

            if int(datetime.datetime.now().weekday()) == 0 and not self.checkran(
                    datetime.datetime.now().strftime("%Y-%m-%d")):
                day = self.changedate(date)
                self.tick()
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.title(f"{self.title}")
            self.root.geometry("1000x700+300+50")
            # current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.root.attributes('-topmost', True)
            # self.load_list()
            # self.vocabulary = self.reviseload()
            # print(self.vocabulary)
            # self.root.config(bg="red")
            self.label = CTkLabel(root,
                                  text=f"Hôm Nay Chúng Ta Sẽ Dành ra ít PHÚT để {self.title} nhé:\n(●ˇ∀ˇ●)                         (●'◡'●)",
                                  font=("Helvetica", 25, "bold"))
            self.label.pack(pady=10)

            self.textbox = CTkTextbox(root, width=900, height=500, scrollbar_button_color="#FFCC70", corner_radius=16,
                                      border_color="#FFCC70", border_width=2, wrap=tk.WORD, font=("Helvetica", 34))
            self.textbox.pack(padx=20, pady=10)

            self.ok_button = CTkButton(root, text="Học Thôi", font=("Helvetica", 34), command=self.confirm_learning)
            self.ok_button.pack(pady=10)
            self.pass_button = CTkButton(root, text="Bỏ Qua", font=("Helvetica", 34), command=self.changelist)
            self.pass_button.pack(side=RIGHT)
            self.loadtext()

            # self.root.destroy()
        def changelist(self):
            with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                date = file.readlines()
            day = date[0].split()
            if int(datetime.datetime.now().weekday()) == int(day[0]) or int(datetime.datetime.now().weekday()) == int(day[1]) or int(datetime.datetime.now().weekday()) == int(day[2]):  # learn
                sys.exit()
                return
            else:  #  reviselist
                vocab = []
                try:
                    with open("datastorage/delrevise.txt", "r", encoding="utf-8") as file:
                        data = file.readlines()
                except FileNotFoundError:
                    messagebox.showerror("Lỗi", "Không tìm thấy file 'learn.txt'.")
                    return

                if self.precheck(data) < 4:
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    sys.exit()
                for idx, line in enumerate(data, start=0):
                    if line.strip() and line.count(":") == 1:
                        word, mean = line.split(":")
                        # if '(' in word:
                        #    word = re.sub(r'\(.*\)', '', word)
                        vocab.append((word.strip(), mean.strip()))
                    elif "---------------" in line:
                        end = idx
                        break
                with open("datastorage/delrevise.txt", "w", encoding="utf-8") as file:
                    file.writelines(data[end + 1:])
                # print(selected_vocabulary)
                self.vocabulary = list(set(vocab))
                self.loadtext()

        def checkran(self, date):
            if os.path.exists('datastorage/loadsche.txt'):
                with open('datastorage/loadsche.txt', "r") as log_file:
                    logged_dates = log_file.read().splitlines()
                if date in logged_dates:
                    return True
                else:
                    return False

        def tick(self):
            with open("datastorage/loadsche.txt", "w", encoding="utf-8") as file:
                file.write(datetime.datetime.now().strftime("%Y-%m-%d"))

        def changedate(self, date):
            random.shuffle(date)
            with open("datastorage/env.txt", "w", encoding="utf-8") as file:
                file.writelines(date)
            return date[0]

        def clearcheck(self):
            with open("datastorage/checklearn.txt", "w", encoding="utf-8") as file:
                pass

        def loadtext(self):
            self.textbox.configure(state=tk.NORMAL)
            self.textbox.delete(1.0, "end")
            vocab_list = "\n".join([f"{word}: {meaning}" for word, meaning in self.vocabulary])
            self.textbox.insert("0.0", vocab_list)
            self.textbox.configure(state=tk.DISABLED)

        def check_log(self, date):
            if os.path.exists('datastorage/checklearn.txt'):
                with open('datastorage/checklearn.txt', "r") as log_file:
                    logged_dates = log_file.read().splitlines()
                if date in logged_dates:
                    return True
                else:
                    return False

        def checkok(self):
            with open("datastorage/checklearn.txt", "w", encoding="utf-8") as file:
                file.write(datetime.datetime.now().strftime("%Y-%m-%d"))

        def on_closing(self):
            if messagebox.askokcancel("Cảnh Báo",
                                      "Bạn có chắc chắn không tiếp tục ôn tập không ?"):
                with open("datastorage/env.txt", "r", encoding="utf-8") as file:
                    date = file.readlines()
                day = date[0].split()
                if (int(datetime.datetime.now().weekday()) != int(day[1].strip()) and int(
                        datetime.datetime.now().weekday()) != int(day[0].strip())):  # not learn
                    # print("not learn")
                    try:
                        with open("datastorage/revise.txt", "r", encoding="utf-8") as file:
                            data = file.readlines()
                        with open("datastorage/delrevise.txt", "w", encoding="utf-8") as nfile:
                            nfile.writelines(data)
                    except Exception as e:
                        print(e)
                    self.root.destroy()
                else:
                    self.root.destroy()

        def confirm_learning(self):
            print(self.vocabulary)
            self.root.destroy()
            M_root = CTk()
            Mul = FlashcardApp(M_root, self.vocabulary)
            #close = Close(M_root, 10, 0)
            M_root.mainloop()

        def precheck(self, lines):
            vocabulary = []
            # TOPIC
            # pos.txt = min(pos.txt, len(lines) - step - 1)
            for line in lines:
                if line and line.count(":") == 1:
                    word, meaning = line.split(":")
                    vocabulary.append((word.strip(), meaning.strip()))
                else:
                    pass
            vocab = list(set(vocabulary))
            return len(vocab)

        def load_learn(self):
            with open("datastorage/tempv.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            # print(lines)

            if len(lines) == 0:
                with open("datastorage/learn.txt", "r", encoding="utf-8") as file:
                    li = file.readlines()
                # print(li)
                # num_lines_to_extract = int(len(li) * 0.2)
                lines = li[-4:]
                # print(lines)
            if self.precheck(lines) < 4:
                sys.exit()

            lines = [line for line in lines if line.strip()]
            # pos.txt, vocab = lines[0].split("#")
            # num_curtopic = int(num_curtopic)
            # pos.txt = int(pos.txt)
            # step = int(vocab)
            # print(num_curtopic)
            # print(vocab)
            vocabulary = []
            # TOPIC
            # pos.txt = min(pos.txt, len(lines) - step - 1)
            for line in lines:
                if line and line.count(":") == 1:
                    word, meaning = line.split(":")
                    vocabulary.append((word.strip(), meaning.strip()))
                else:
                    pass
            # pos.txt = pos.txt + step
            # print(vocabulary)
            return vocabulary

        def reviseload(self):
            vocab = []
            try:
                with open("datastorage/delrevise.txt", "r", encoding="utf-8") as file:
                    data = file.readlines()
            except FileNotFoundError:
                messagebox.showerror("Lỗi", "Không tìm thấy file 'learn.txt'.")
                return

            if self.precheck(data) < 4:
                sys.exit()
                return
            for idx, line in enumerate(data, start=0):
                if line.strip() and line.count(":") == 1:
                    word, mean = line.split(":")
                    # if '(' in word:
                    #    word = re.sub(r'\(.*\)', '', word)
                    vocab.append((word.strip(), mean.strip()))
                elif "---------------" in line:
                    end = idx
                    break
            with open("datastorage/delrevise.txt", "w", encoding="utf-8") as file:
                file.writelines(data[end + 1:])
            return vocab
            # print(selected_vocabulary)

        def load_list(self):
            listname = []
            pos = []
            with open("datastorage/revise.txt", "w", encoding="utf-8"):
                pass
            with open("datastorage/delrevise.txt", "w", encoding="utf-8"):
                pass
            with open("datastorage/nlist.txt", "r", encoding="utf-8") as file:
                line = file.readlines()
                for l in line:
                    if l.strip():
                        listname.append(l)
            if len(listname) == 0:
                sys.exit()
            with open("datastorage/pos.txt", "r", encoding="utf-8") as fpos:
                lin = fpos.readlines()
                for line in lin:
                    if line.strip():
                        pos.append(line)
            with open("datastorage/vlist.txt", "r", encoding="utf-8") as data:
                lines = data.readlines()

            # print(pos)

            for idx in range(len(listname)):
                st, en = self.findse(lines, listname[idx])
                learnline = lines[st:en + 1]
                if len(learnline) <= 4:
                    # print("pass")
                    continue
                # print(learnline)
                # print("-------------")
                if self.checktype(learnline):
                    # print("topic")
                    vocablist = []
                    # print(listname[idx])
                    # print(learnline)
                    # print(idx)
                    num_curtopic = int(pos[idx])
                    # print(pos[idx])
                    # print(type(num_curtopic))
                    # print(num_curtopic)
                    st = False
                    # plused = False
                    while not st:
                        for i, line in enumerate(learnline[1:], start=1):
                            if "." in line:
                                if line.strip() and num_curtopic == int(line.split(".")[0]) and ':' not in line:
                                    start = i
                                    st = True
                                    break
                        if st == False:
                            # plused = True
                            num_curtopic += 1
                    for line in learnline[start + 1:]:
                        if line.strip() and line.count(":") == 1:
                            word, meaning = line.split(":")
                            vocablist.append((word.strip(), meaning.strip()))
                        elif ":" not in line and "." in line:
                            break
                        else:
                            pass
                    # print(pos)
                    num_curtopic += 1

                    # print(pos)
                    pos[idx] = str(num_curtopic) + '\n'
                    with open("datastorage/pos.txt", "w", encoding="utf-8") as fpos:
                        fpos.writelines(pos)
                    with open("datastorage/revise.txt", "a", encoding="utf-8") as file:
                        for word, meaning in vocablist:
                            file.write(f"{word}:{meaning}\n")
                        file.write("----------------\n")
                    with open("datastorage/delrevise.txt", "a", encoding="utf-8") as file:
                        for word, meaning in vocablist:
                            file.write(f"{word}:{meaning}\n")
                        file.write("----------------\n")
                    print("Đây là topiclist:")
                    print(vocablist)
                    print("----------------------------------------------------------------------------------")

                else:
                    # print("list")
                    vocablist = []
                    # print(learnline)
                    poss = int(pos[idx])
                    # print(f"{fr}")
                    if len(learnline) == 5:
                        selected_count = 4
                    elif len(learnline) >= 5 and len(learnline) <= 15:
                        selected_count = int(0.7 * len(learnline))
                    elif len(learnline) <= 30:
                        selected_count = int(0.4 * len(learnline))
                    else:
                        selected_count = random.randint(10, 16)
                    newpos = poss + selected_count
                    if newpos >= len(learnline) - 1:
                        newpos = len(learnline) - 1
                    # print(poss)
                    # print(newpos)
                    vocabline = learnline[poss:newpos + 1]
                    # print(vocabline)
                    for line in vocabline:
                        if line.strip() and line.count(":") == 1:
                            word, mean = line.split(":")
                            if "." in word:
                                word = word.split(".")[1]
                            # if '(' in word:
                            #    word = re.sub(r'\(.*\)', '', word)
                            vocablist.append((word.strip(), mean.strip()))
                    # print(pos)
                    # print("Đây là vocablist:")
                    # print(vocablist)
                    # print(len(vocablist))
                    # print("----------------------------------------------------------------------------------")
                    # print(type(pos[idx]))
                    # print(type(newpos))
                    if len(vocablist) < 4:
                        continue
                    pos[idx] = str(newpos) + "\n"
                    # print(pos)
                    with open("datastorage/pos.txt", "w", encoding="utf-8") as fpos:
                        fpos.writelines(pos)
                    # print(vocablist)
                    with open("datastorage/revise.txt", "a", encoding="utf-8") as file:
                        for word, meaning in vocablist:
                            file.write(f"{word}:{meaning}\n")
                        file.write("----------------\n")
                    with open("datastorage/delrevise.txt", "a", encoding="utf-8") as file:
                        for word, meaning in vocablist:
                            file.write(f"{word}:{meaning}\n")
                        file.write("----------------\n")

                # print(vocablist)
                # print(learnline)
                # print(vocabline)
            # print(listname)
            # print(pos)

        def checktype(self, lines):
            s = 0
            for line in lines:
                if ':' not in line and line.strip() and "." in line:
                    s += 1
            return s > 7

        def findse(self, lines, word):
            en = len(lines)
            for idx, line in enumerate(lines):
                if word.strip() in line.strip() and "##*###**" in line.strip():
                    st = idx
                    break
            for idx, line in enumerate(lines[st + 1:]):
                if "##*###**" in line.strip():
                    en = idx
                    break
            # print(f"{st}")
            # print(f"{en}")
            en = en + st
            # print(f"//{en}")
            return st, en
    except Exception as e:
        print(e)
if __name__ == "__main__":
    #vocabulary = [('tasty', 'ngon'), ('爸爸', 'father (bàba)'), ('北京', 'Beijing (běijīng)'), ('上', 'upper, up side (shàng)'), ('fizzy', 'có ga')]
    #vocab = [('4', '4'), ('5', '5'), ('6', '6'), ('a', 'a'), ('b', 'b')]
    root = CTk()
    #app = Multichoice(root, vocab)
    #root = CTk()
    app = LearnApp(root)
    root.mainloop()
    #nroot = CTk()
    #napp = Close(root,10,1)
    #root.mainloop()

