from __future__ import annotations

from tkinter import messagebox, PhotoImage
import tkinter as tk
import os

from system import ServerConfiguration, request_server

def _request_update_server() -> None:
    server_information = request_server()
    if server_information:
        label_name_value.config(text=server_information["name"])
        label_map_value.config(text=server_information["map"])
        label_game.config(text=server_information["game"])
        label_vac.config(text="Присутствует" if server_information["vac"] == 1 else "Отсутствует")
        label_version.config(text=server_information["version"])
        label_players_value.config(text=server_information["players"])
        player_listbox.delete(0, tk.END)
        for player in server_information["players_list"]:
            player_listbox.insert(tk.END, player)
    else:
        messagebox.showerror("Ошибка", "Не удалось подключиться к серверу")

from dataclasses import dataclass

@dataclass
class WindowConfiguration:
    window_title: str = "EtoМажор :\ Турниры КС:С"
    window_sizes: str = "590x300"; window_resize: bool = False

window: tk.Tk = tk.Tk()
window.title(WindowConfiguration.window_title)
window.geometry(WindowConfiguration.window_sizes)
window.resizable(width=WindowConfiguration.window_resize, height=WindowConfiguration.window_resize)

icon = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'resources', 'favicon.png')); window.iconphoto(True, icon)

def _connect_server_to() -> None:
    window.clipboard_clear()
    window.clipboard_append(f"connect {ServerConfiguration.mazhor_css_ip}; password {ServerConfiguration.mazhor_css_password}")
    messagebox.showinfo("Команда для подключения скопирована", "Команда для присоединения к серверу скопирована в буфер обмена. Зайдите в игру и через консоль (~) подключитесь к серверу, просто вставив данную команду")

left_frame = tk.Frame(window)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

label_name = tk.Label(left_frame, text="Название сервера:")
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)
label_name_value = tk.Label(left_frame, text="...")
label_name_value.grid(row=0, column=1, sticky="w", padx=10, pady=5)

label_map = tk.Label(left_frame, text="Карта:")
label_map.grid(row=1, column=0, sticky="w", padx=10, pady=5)
label_map_value = tk.Label(left_frame, text="...")
label_map_value.grid(row=1, column=1, sticky="w", padx=10, pady=5)

label_game = tk.Label(left_frame, text="Сервер подключения:")
label_game.grid(row=2, column=0, sticky="w", padx=10, pady=5)
label_game = tk.Label(left_frame, text="...")
label_game.grid(row=2, column=1, sticky="w", padx=10, pady=5)

label_vac = tk.Label(left_frame, text="Античит VAC:")
label_vac.grid(row=3, column=0, sticky="w", padx=10, pady=5)
label_vac = tk.Label(left_frame, text="...")
label_vac.grid(row=3, column=1, sticky="w", padx=10, pady=5)

label_version = tk.Label(left_frame, text="Версия клиента-сервера:")
label_version.grid(row=4, column=0, sticky="w", padx=10, pady=5)
label_version = tk.Label(left_frame, text="...")
label_version.grid(row=4, column=1, sticky="w", padx=10, pady=5)

label_players = tk.Label(left_frame, text="Игроки:")
label_players.grid(row=5, column=0, sticky="w", padx=10, pady=5)
label_players_value = tk.Label(left_frame, text="...")
label_players_value.grid(row=5, column=1, sticky="w", padx=10, pady=5)

label_copyright = tk.Label(left_frame, text="Copyright (c) 2024 EtoMazhorInc")
label_copyright.grid(row=6, column=0, sticky="w", padx=10, pady=5)


right_frame = tk.Frame(window)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

label_players_list = tk.Label(right_frame, text="Список игроков:")
label_players_list.grid(row=0, column=0, sticky="w", padx=10, pady=5)
player_listbox = tk.Listbox(right_frame, height=10, width=30, relief="solid", border=0)
player_listbox.grid(row=1, column=0, padx=10, pady=5)

btn_update = tk.Button(right_frame, text="Обновить", command=_request_update_server, width=25, relief="solid", border=0)
btn_update.grid(row=2, column=0, padx=10, pady=5)

btn_connect = tk.Button(right_frame, text="Подключиться", command=_connect_server_to, width=25, relief="solid", border=0)
btn_connect.grid(row=3, column=0, padx=10, pady=5)

if __name__ == "__main__":
    _request_update_server(); window.mainloop()