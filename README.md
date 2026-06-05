# 🍅 番茄钟桌面应用

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=white" alt="Platform: Windows">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
</p>

<p align="center">
  一个简洁、美观、单文件可运行的 Pomodoro 番茄钟桌面应用，<br>
  基于 Python <code>tkinter</code> 开发，帮助你高效管理专注时间与休息节奏。
</p>

---

## 📑 目录

- [功能特性](#-功能特性)
- [界面预览](#-界面预览)
- [技术栈与架构](#-技术栈与架构)
- [环境要求](#-环境要求)
- [快速开始](#-快速开始)
- [使用说明](#-使用说明)
- [代码架构详解](#-代码架构详解)
- [自定义配置](#-自定义配置)
- [打包为可执行文件](#-打包为可执行文件)
- [项目结构](#-项目结构)
- [常见问题](#-常见问题)
- [路线图](#-路线图)
- [贡献指南](#-贡献指南)
- [开源协议](#-开源协议)

---

## ✨ 功能特性

| 特性 | 说明 |
|------|------|
| 🍅 **经典番茄工作法** | 默认 25 分钟专注 + 5 分钟短休息 + 15 分钟长休息 |
| 📊 **可视化进度条** | 圆形进度环实时显示剩余时间，直观清晰 |
| 🔄 **自动循环提醒** | 每完成 4 个番茄后自动进入长休息，劳逸结合 |
| 📌 **置顶窗口** | 支持窗口始终置顶，方便随时查看剩余时间 |
| 🔊 **系统提示音** | 计时结束时播放蜂鸣提示音（Windows） |
| 🎨 **精致暗色主题** | 采用 Catppuccin Mocha 配色，护眼舒适 |
| 📦 **单文件运行** | 整个应用仅一个 `pomodoro.py`，无需安装依赖 |
| 🧵 **线程安全** | 后台计时与 UI 更新分离，运行流畅不卡顿 |

---

## 🖼️ 界面预览

应用主界面采用居中布局，暗色背景搭配柔和配色：

- **顶部状态标签**：动态显示当前阶段（🍅 专注时间 / ☕ 短休息 / 🌴 长休息）
- **中央圆形进度条**：240×240 画布绘制的圆环进度，随时间递减
- **大字体倒计时**：中央显示 `MM:SS` 格式剩余时间
- **操作按钮区**：开始 / 暂停 / 重置，扁平化设计
- **底部信息栏**：已完成番茄计数 + 窗口置顶开关

---

## 🛠️ 技术栈与架构

### 核心技术

| 技术 | 用途 | 版本要求 |
|------|------|---------|
| Python 3 | 核心运行环境 | ≥ 3.8 |
| tkinter | GUI 界面框架 | 标准库内置 |
| threading | 后台倒计时线程 | 标准库 |
| winsound | Windows 系统蜂鸣提示 | 标准库（仅 Windows） |
| math | 圆形进度条几何计算 | 标准库 |

### 设计决策

- **单文件架构**：所有逻辑封装在 `PomodoroTimer` 类中，便于分发和维护
- **线程安全模型**：
  - 后台 `daemon` 线程（`_tick`）负责 `time.sleep` 倒计时
  - UI 更新通过 `root.after(0, ...)` 调度回主线程，避免 tkinter 多线程崩溃
- **状态机驱动**：`work` → `short_break` / `long_break` → `work` 自动循环
- **零依赖**：除 Python 标准库外无需安装任何第三方包

---

## 🖥️ 环境要求

- **操作系统**：Windows（因使用 `winsound.Beep`）
- **Python 版本**：3.8 或更高
- **tkinter**：通常随 Python 官方安装包自带

检查 tkinter 是否可用：

```bash
python -c "import tkinter; print(tkinter.Tcl().eval('info patchlevel'))"
```

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/ly99LLL/tomatobinggo.git
cd tomatobinggo
```

### 2. 运行应用

常规方式（会显示控制台窗口）：

```bash
python pomodoro.py
```

**推荐方式**（Windows 无控制台启动）：

```bash
pythonw pomodoro.py
```

> 💡 提示：可将 `pythonw pomodoro.py` 创建为桌面快捷方式，方便一键启动。

---

## 📖 使用说明

1. 点击 **「开始」** 启动当前计时阶段（默认从专注时间开始）。
2. 计时过程中可随时点击 **「暂停」**，再次点击 **「继续」** 恢复。
3. 点击 **「重置」** 将恢复初始状态，清空已完成计数。
4. 专注时间结束后自动进入休息阶段，并播放提示音。
5. 使用 **「窗口置顶」** 复选框控制应用是否始终显示在最前端。
6. 完成 4 个番茄后，系统将自动安排一次 15 分钟的长休息。

---

## 🏗️ 代码架构详解

### 类结构

```
PomodoroTimer
├── __init__()           # 初始化窗口、状态变量、UI 组件
├── _setup_ui()          # 构建所有 tkinter 控件
├── _draw_progress()     # Canvas 绘制圆形进度环
├── _update_display()    # 更新倒计时文字与进度条
├── _total_seconds()     # 返回当前阶段总秒数
├── _set_session()       # 切换工作/休息阶段
├── start()              # 启动后台计时线程
├── pause()              # 暂停/继续切换
├── reset()              # 重置全部状态
├── _tick()              # 后台线程：每秒倒计时
├── _session_end()       # 阶段结束处理与状态转换
├── _toggle_top()        # 窗口置顶切换
└── _on_close()          # 关闭窗口清理
```

### 核心常量

```python
WORK_MIN = 25            # 专注时长（分钟）
SHORT_BREAK_MIN = 5      # 短休息时长（分钟）
LONG_BREAK_MIN = 15      # 长休息时长（分钟）
SESSIONS_BEFORE_LONG = 4 # 长休息间隔（个番茄）
```

### 状态流转

```
[启动] → work ──25min──► short_break ──5min──► work ──25min──► ...
                                     （每 4 个番茄后）
                                          ▼
                                    long_break ──15min──► work
```

### 颜色配置

| 元素 | 色值 | 说明 |
|------|------|------|
| 背景色 | `#1e1e2e` | Catppuccin Mocha 基底 |
| 文字色 | `#cdd6f4` | 主文字 |
| 进度条-专注 | `#cba6f7` | 紫色 |
| 进度条-休息 | `#89b4fa` | 蓝色 |
| 进度条-完成 | `#a6e3a1` | 绿色 |
| 按钮-开始 | `#a6e3a1` | 绿色 |
| 按钮-暂停 | `#f9e2af` | 黄色 |
| 按钮-重置 | `#f38ba8` | 粉色 |

---

## ⚙️ 自定义配置

### 调整时间参数

编辑 `pomodoro.py` 中的类常量：

```python
class PomodoroTimer:
    WORK_MIN = 25          # 专注时长（分钟）
    SHORT_BREAK_MIN = 5    # 短休息时长（分钟）
    LONG_BREAK_MIN = 15    # 长休息时长（分钟）
    SESSIONS_BEFORE_LONG = 4  # 几个番茄后进入长休息
```

### 调整提示音

修改 `_session_end` 方法中的 `winsound.Beep` 参数：

```python
winsound.Beep(800, 300)  # 频率(Hz), 持续时间(ms)
```

### 调整窗口大小

修改 `__init__` 中的几何参数：

```python
self.root.geometry("340x420")  # 宽度 x 高度
```

---

## 📦 打包为可执行文件

使用 [PyInstaller](https://pyinstaller.org/) 打包为独立的 `.exe` 文件：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包（无控制台窗口，单文件）
pyinstaller --onefile --noconsole --name TomatoTimer pomodoro.py

# 输出目录：dist/TomatoTimer.exe
```

可选：添加图标

```bash
pyinstaller --onefile --noconsole --icon=tomato.ico --name TomatoTimer pomodoro.py
```

---

## 📁 项目结构

```
tomatobinggo/
├── pomodoro.py          # 主程序入口（全部 UI 与业务逻辑）
├── README.md            # 项目说明文档
├── CLAUDE.md            # Claude Code 开发指南
├── .gitignore           # Git 忽略规则
└── a.py                 # 预留空文件（暂未使用）
```

> 本项目遵循极简哲学，核心功能全部集中在单个文件中，降低维护复杂度。

---

## ❓ 常见问题

**Q: 运行时提示 `No module named 'tkinter'`？**
> A: 请重新安装 Python，并在安装向导中勾选 **"tcl/tk and IDLE"** 选项。

**Q: macOS/Linux 可以运行吗？**
> A: 当前版本使用 `winsound` 播放提示音，为 Windows 专属。如需跨平台支持，可将 `winsound.Beep` 替换为 `pygame` 或 `playsound` 库。

**Q: 倒计时线程会占用很多 CPU 吗？**
> A: 不会。后台线程使用 `time.sleep(1)` 每秒唤醒一次，暂停时使用 `time.sleep(0.2)`，CPU 占用极低。

**Q: 如何修改字体？**
> A: 在 `_setup_ui` 中修改 `font=("字体名", 大小, "粗细")` 参数。推荐 Windows 使用 `"Microsoft YaHei"`，macOS 使用 `"PingFang SC"`。

---

## 🗺️ 路线图

- [ ] GUI 设置面板：可视化调整时间参数
- [ ] 跨平台音频支持（替换 `winsound`）
- [ ] 最小化到系统托盘
- [ ] 任务标签与番茄历史统计
- [ ] 数据持久化（本地 JSON/ SQLite）
- [ ] 番茄完成时的桌面通知（Windows Toast）
- [ ] 快捷键支持（空格暂停、ESC 重置）
- [ ] 白噪音背景音选项
- [ ] 自动打包脚本与 GitHub Actions 发布

---

## 🤝 贡献指南

欢迎提交 Issue 或 Pull Request！

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/xxx`
3. 提交更改：`git commit -m 'feat: add some feature'`
4. 推送分支：`git push origin feature/xxx`
5. 创建 Pull Request

请确保代码风格与现有文件保持一致（中文注释、4 空格缩进）。

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

<p align="center">
  Made with 🍅 and Python
</p>
