import tkinter as tk
from tkinter import ttk
import threading
import time
import winsound
import math

class PomodoroTimer:
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 15
    SESSIONS_BEFORE_LONG = 4

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("番茄钟")
        self.root.geometry("340x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        # 托盘区域 / 顶部栏
        self.root.attributes("-topmost", True)

        self.running = False
        self.paused = False
        self.seconds_left = self.WORK_MIN * 60
        self.current_session = "work"  # work / short_break / long_break
        self.completed_sessions = 0

        self._setup_ui()
        self._update_display()

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _setup_ui(self):
        style = ttk.Style()
        style.theme_use("clam")

        # ---- 主容器 ----
        main = tk.Frame(self.root, bg="#1e1e2e")
        main.pack(expand=True, fill="both", padx=20, pady=20)

        # ---- 状态标签 ----
        self.status_label = tk.Label(
            main, text="🍅 专注时间",
            font=("Microsoft YaHei", 14, "bold"),
            fg="#cdd6f4", bg="#1e1e2e",
        )
        self.status_label.pack(pady=(0, 10))

        # ---- 圆形进度条 ----
        self.canvas_size = 240
        self.canvas = tk.Canvas(
            main,
            width=self.canvas_size,
            height=self.canvas_size,
            bg="#1e1e2e",
            highlightthickness=0,
        )
        self.canvas.pack(pady=10)

        # ---- 时间文字 ----
        self.timer_text = self.canvas.create_text(
            self.canvas_size // 2,
            self.canvas_size // 2,
            text="",
            font=("Consolas", 42, "bold"),
            fill="#cdd6f4",
        )

        # ---- 按钮区域 ----
        btn_frame = tk.Frame(main, bg="#1e1e2e")
        btn_frame.pack(pady=(15, 10))

        self.start_btn = tk.Button(
            btn_frame, text="开始", command=self.start,
            width=8, font=("Microsoft YaHei", 11),
            bg="#a6e3a1", fg="#1e1e2e", activebackground="#94d89f",
            relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
        )
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = tk.Button(
            btn_frame, text="暂停", command=self.pause,
            width=8, font=("Microsoft YaHei", 11),
            bg="#f9e2af", fg="#1e1e2e", activebackground="#f5d78a",
            relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
            state="disabled",
        )
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(
            btn_frame, text="重置", command=self.reset,
            width=8, font=("Microsoft YaHei", 11),
            bg="#f38ba8", fg="#1e1e2e", activebackground="#f06d8f",
            relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
        )
        self.reset_btn.grid(row=0, column=2, padx=5)

        # ---- 完成计数 ----
        self.count_label = tk.Label(
            main,
            text="已完成: 0 个番茄",
            font=("Microsoft YaHei", 10),
            fg="#a6adc8", bg="#1e1e2e",
        )
        self.count_label.pack(pady=(10, 0))

        # ---- 置顶复选框 ----
        self.top_var = tk.BooleanVar(value=True)
        self.top_cb = tk.Checkbutton(
            main, text="窗口置顶", variable=self.top_var,
            command=self._toggle_top,
            fg="#a6adc8", bg="#1e1e2e",
            selectcolor="#313244", activebackground="#1e1e2e",
            activeforeground="#cdd6f4",
            font=("Microsoft YaHei", 9),
        )
        self.top_cb.pack(pady=5)

    def _draw_progress(self, fraction: float):
        """绘制圆形进度条 (0..1)"""
        self.canvas.delete("progress")
        cx = cy = self.canvas_size // 2
        r = 90
        w = 10

        # 背景圆环
        self.canvas.create_oval(
            cx - r, cy - r, cx + r, cy + r,
            outline="#313244", width=w, tags="progress",
        )

        if fraction <= 0:
            return

        angle = fraction * 360.0
        # 从顶部 (90°) 逆时针绘制
        start_deg = 90
        extent = -angle  # tk 逆时针为负

        if fraction >= 1:
            color = "#a6e3a1"
        elif self.current_session == "work":
            color = "#cba6f7"
        else:
            color = "#89b4fa"

        self.canvas.create_arc(
            cx - r, cy - r, cx + r, cy + r,
            start=start_deg, extent=extent,
            outline=color, width=w, style="arc", tags="progress",
        )

    def _update_display(self):
        total = self._total_seconds()
        fraction = 1 - (self.seconds_left / total) if total > 0 else 0
        self._draw_progress(fraction)

        m = self.seconds_left // 60
        s = self.seconds_left % 60
        self.canvas.itemconfig(self.timer_text, text=f"{m:02d}:{s:02d}")

    def _total_seconds(self):
        if self.current_session == "work":
            return self.WORK_MIN * 60
        elif self.current_session == "short_break":
            return self.SHORT_BREAK_MIN * 60
        return self.LONG_BREAK_MIN * 60

    def _set_session(self, session: str):
        self.current_session = session
        self.seconds_left = self._total_seconds()

        if session == "work":
            self.status_label.config(text="🍅 专注时间")
        elif session == "short_break":
            self.status_label.config(text="☕ 短休息")
        else:
            self.status_label.config(text="🌴 长休息")

        self._update_display()

    def start(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.start_btn.config(state="disabled")
            self.pause_btn.config(state="normal")
            threading.Thread(target=self._tick, daemon=True).start()

    def pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_btn.config(text="继续")
        else:
            self.pause_btn.config(text="暂停")

    def reset(self):
        self.running = False
        self.paused = False
        self._set_session("work")
        self.completed_sessions = 0
        self.count_label.config(text="已完成: 0 个番茄")
        self.start_btn.config(state="normal")
        self.pause_btn.config(state="disabled", text="暂停")
        self._update_display()

    def _tick(self):
        while self.running:
            if not self.paused:
                time.sleep(1)
                self.seconds_left -= 1

                self.root.after(0, self._update_display)

                if self.seconds_left <= 0:
                    self.root.after(0, self._session_end)
                    return
            else:
                time.sleep(0.2)

    def _session_end(self):
        self.running = False
        self.paused = False
        self.start_btn.config(state="normal")
        self.pause_btn.config(state="disabled", text="暂停")

        # 播放提示音
        threading.Thread(target=lambda: winsound.Beep(800, 300), daemon=True).start()

        if self.current_session == "work":
            self.completed_sessions += 1
            suffix = "个番茄" if self.completed_sessions <= 1 else "个番茄"
            self.count_label.config(text=f"已完成: {self.completed_sessions} {suffix}")

            if self.completed_sessions % self.SESSIONS_BEFORE_LONG == 0:
                self._set_session("long_break")
            else:
                self._set_session("short_break")
        else:
            self._set_session("work")

    def _toggle_top(self):
        self.root.attributes("-topmost", self.top_var.get())

    def _on_close(self):
        self.running = False
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    PomodoroTimer().run()
