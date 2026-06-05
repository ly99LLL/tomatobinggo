# 🍅 番茄钟桌面应用 — Tomatobinggo

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=white" alt="Platform: Windows">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status: Active">
  <img src="https://img.shields.io/badge/Dependencies-0-zero?logo=python&logoColor=white" alt="Zero Dependencies">
</p>

<p align="center">
  <strong>一个优雅、纯粹、零依赖的 Pomodoro 番茄钟桌面应用</strong><br>
  用 Python <code>tkinter</code> 手工打造，专为 Windows 深度专注场景而生
</p>

---

## 📑 目录

- [项目简介](#-项目简介)
- [创作缘由](#-创作缘由)
- [创作灵感](#-创作灵感)
- [核心特性](#-核心特性)
- [技术栈](#-技术栈)
- [项目成果](#-项目成果)
- [快速部署](#-快速部署)
- [项目意义](#-项目意义)
- [对我能力的提升](#-对我能力的提升)
- [使用说明](#-使用说明)
- [代码架构](#-代码架构)
- [自定义配置](#-自定义配置)
- [打包为可执行文件](#-打包为可执行文件)
- [路线图](#-路线图)
- [常见问题](#-常见问题)
- [贡献指南](#-贡献指南)
- [开源协议](#-开源协议)

---

## 🎯 项目简介

**Tomatobinggo** 是一款基于经典的 [番茄工作法（Pomodoro Technique）](https://francescocirillo.com/products/the-pomodoro-technique) 理念开发的 Windows 桌面计时应用。它使用 Python 标准库中的 `tkinter` 作为 GUI 框架，实现了一个完整的番茄钟计时器——从圆形进度条的 Canvas 手绘，到多线程安全的倒计时引擎，到自动化的"工作-休息"状态机流转，全部由纯 Python 代码驱动。

> **一句话概括**：用最少的依赖，做最趁手的番茄钟。

**核心数据：**

| 指标 | 数值 |
|------|------|
| 代码文件 | 1 个（`pomodoro.py`，257 行） |
| 第三方依赖 | **0** |
| 面向平台 | Windows |
| 专注时长 | 25 分钟（可配置） |
| 短休息 | 5 分钟 |
| 长休息 | 15 分钟（每 4 个番茄触发） |

---

## 💡 创作缘由

在日常的编程学习和项目开发中，我发现自己经常陷入两种极端状态：要么一口气编码数小时忘记休息，导致效率持续下降；要么频繁被手机通知、网页浏览打断，难以进入深度专注状态。

我尝试过手机上的番茄钟 App，也用过浏览器插件，但它们都有各自的问题：

- **手机 App**：手机本身就是最大的干扰源。打开手机设番茄钟 → 顺手刷短视频 → 番茄钟等于白设。
- **浏览器插件**：当我关闭浏览器、打开 IDE 写代码时，浏览器插件的提醒就与我无关了。
- **在线工具**：需要保持网页标签打开，网络不好时页面卡顿，而且广告和功能阉割令人烦躁。

于是我问自己：**"为什么不自己做一个？"**

一个运行在桌面上的、独立于浏览器和手机的、启动即用的番茄钟——这就是 **Tomatobinggo** 诞生的直接原因。更深层的动机是：**用自己写的工具来管理自己的时间**，这件事本身就充满了仪式感和掌控感。

---

## 🌟 创作灵感

本项目从以下多个维度汲取了灵感：

### 1. 番茄工作法的哲学

Francesco Cirillo 在 1980 年代创立的番茄工作法，核心理念极其简单却有效：

- **单线程工作**：一次只做一件事，拒绝多任务切换带来的认知损耗。
- **时间盒约束**：25 分钟的短周期让人更容易"开始"，降低了拖延的心理门槛。
- **强制休息**：休息不是偷懒，而是恢复注意力的必要投入。

这些理念深深影响了我对"专注工具"的设计——**工具本身也应该简单、不打扰、不造成额外的认知负担**。

### 2. Catppuccin 配色体系

应用的暗色主题配色方案来自 [Catppuccin Mocha](https://catppuccin.com/palette) 调色板，这是一个在开发者社区广受好评的开源配色方案。Catppuccin 的低对比度暖色调极暗背景，在长时间注视屏幕时能有效缓解眼部疲劳——对于一款面向"专注"场景的应用来说，视觉舒适度是核心体验的一环。

本应用使用的具体色值：

| 元素 | 色号 | 视觉效果 |
|------|------|---------|
| 背景 | `#1e1e2e` | 深邃暗紫基底，不刺眼 |
| 主文字 | `#cdd6f4` | 柔和浅白，高可读性 |
| 进度环（专注中） | `#cba6f7` | 淡紫，传递专注氛围 |
| 进度环（休息中） | `#89b4fa` | 淡蓝，暗示放松节奏 |
| 进度环（已完成） | `#a6e3a1` | 淡绿，完成的正向反馈 |
| 开始按钮 | `#a6e3a1` | 绿色，积极行动的视觉信号 |
| 暂停按钮 | `#f9e2af` | 黄色，温和的过渡状态 |
| 重置按钮 | `#f38ba8` | 粉色，谨慎操作的提示 |

### 3. "零依赖"的极简主义

Python 生态中有大量优秀的 GUI 框架——PyQt、wxPython、Kivy 等——但我刻意选择了标准库中的 `tkinter`。理由很简单：

- **任何安装了 Python 的 Windows 电脑，无需 `pip install`，直接运行。**
- 对于一款"番茄钟"来说，界面的复杂度不需要一个重量级框架来承载。
- 零依赖意味着零版本冲突、零安全审计负担、零"在我机器上跑不起来"的尴尬。

这种"用标准库解决问题"的思路，本身就是一种工程训练。

### 4. 桌面应用 ≠ 网页的延伸

在 Web 技术大行其道的今天，很多所谓"桌面应用"本质上是套了壳的网页（Electron）。我刻意选择了原生 GUI 方案，一方面是因为想要轻量和低内存占用（一个 Electron 空壳就要 100MB+ 内存），另一方面也是想深入理解"操作系统原生窗口系统"的工作方式——消息循环、事件驱动、线程模型——这些是 Web 开发者很难接触到的底层知识。

---

## ✨ 核心特性

| 特性 | 说明 | 实现方式 |
|------|------|---------|
| 🍅 **经典番茄工作法** | 25 分钟专注 + 5 分钟短休息 + 15 分钟长休息 | 状态机自动流转 |
| 🎨 **圆形进度条** | Canvas 手绘的弧形进度环，实时反映剩余时间 | `canvas.create_arc` 动态绘制 |
| 🔄 **智能休息** | 每完成 4 个番茄自动进入长休息，劳逸结合 | `SESSIONS_BEFORE_LONG` 常量控制 |
| 📌 **置顶窗口** | 可切换窗口置顶，随时查看剩余时间 | `root.attributes("-topmost")` |
| 🔊 **提示音** | 计时结束时自动蜂鸣提醒 | `winsound.Beep` 系统调用 |
| ⏯️ **暂停/继续** | 随时暂停计时，随时恢复 | 线程标志位控制 |
| 🔢 **完成计数** | 实时统计已完成番茄数 | `completed_sessions` 递增 |
| 🌙 **暗色主题** | Catppuccin Mocha 配色，长时间使用不伤眼 | 全局 `bg` / `fg` 配色 |
| 📦 **单文件** | 整个应用只有一个 `.py` 文件 | 类封装，无外部模块 |
| 🔒 **线程安全** | 后台计时与 UI 更新分离，无竞态 | `root.after(0, ...)` 调度 |
| 🪶 **极小资源占用** | 内存 ~15MB，CPU 空闲时近乎为零 | 纯 tkinter + `time.sleep` |
| 🆓 **零第三方依赖** | 仅使用 Python 标准库 | 无 `requirements.txt` 需要 |

---

## 🛠️ 技术栈

### 核心技术

| 技术 | 用途 | 所属 |
|------|------|------|
| **Python 3.8+** | 运行环境与编程语言 | 标准库 |
| **tkinter** | GUI 框架：窗口管理、控件布局、Canvas 绘图 | 标准库 |
| **threading** | 后台倒计时线程，不阻塞主 UI 线程 | 标准库 |
| **time** | `time.sleep` 实现每秒滴答 | 标准库 |
| **winsound** | 系统 Beep 提示音播放 | 标准库（Windows 专属） |
| **math** | 圆形进度条的弧度计算 | 标准库 |

### 架构设计决策

#### 1. 线程模型：UI 与计时的分离

```
┌──────────────────────┐         ┌──────────────────┐
│   Main Thread (UI)   │         │  Daemon Thread   │
│   ─────────────────  │         │  ──────────────  │
│   tkinter.mainloop() │◄────────│  _tick()         │
│   事件分发            │ after   │  time.sleep(1)   │
│   控件渲染            │  调度    │  倒计时逻辑       │
│   用户交互            │         │                  │
└──────────────────────┘         └──────────────────┘
```

- **后台守护线程 `_tick`**：负责 `time.sleep(1)` 的阻塞等待，每秒醒来更新倒计时。
- **UI 更新调度**：`_tick` 线程 **不直接操作** tkinter 控件，而是通过 `root.after(0, callback)` 将所有 UI 更新调度回主线程执行——这是 tkinter 线程安全的黄金法则。
- **暂停机制**：暂停时线程仍然运行，但跳过倒计时逻辑，以 0.2 秒间隔轮询检查是否恢复——兼顾响应速度与 CPU 效率。

#### 2. 状态机设计

```
                ┌──────┐
                │ 启动  │
                └──┬───┘
                   ▼
              ┌─────────┐
         ┌───►│  work   │───25 min───┐
         │    └─────────┘            │
         │                          ▼
         │                ┌──────────────────┐
         │   第1-3次      │  short_break     │
         │   完成后        │  5 min           │
         │                └────────┬─────────┘
         │                        │
         │    ┌───────────────────┘
         │    ▼
         │ ┌──────────────────┐
         │ │  long_break       │  ◄── 第4次完成后触发
         │ │  15 min           │
         │ └────────┬──────────┘
         │          │
         └──────────┘
```

状态切换由 `_session_end` 统一处理，逻辑清晰，易于扩展。

#### 3. 圆形进度条的绘制原理

```
        从 12 点钟方向 (90°)
        逆时针绘制弧形 extent = -(fraction × 360°)

           12点 (90°)
             ↑
            ╱ ╲
           ╱   ╲   ← 弧形从顶部开始逆时针递减
          ╱     ╲
         │       │
         │  MM:SS│   ← 中心显示剩余时间
         ╲       ╱
          ╲     ╱
           ╲   ╱
            ╲ ╱
              ↓
          弧形末端

        fraction = 1.0 → 完整圆环 (360°)
        fraction = 0.5 → 半圆环 (180°)
        fraction = 0.0 → 无弧线（仅灰色背景环）
```

使用 `canvas.create_arc` 的 `style="arc"` 模式绘制不填充的弧形，配合不同阶段的颜色，直观传递倒计时进度。

---

## 🏆 项目成果

### 功能成果

- ✅ 完整实现了番茄工作法的核心流程：专注 → 短休息 → 长休息 → 循环
- ✅ 圆形进度条实时反馈剩余时间，视觉直观
- ✅ 多线程架构保证 UI 始终流畅响应
- ✅ 置顶窗口功能，让番茄钟始终在视线范围内
- ✅ 零第三方依赖，代码干净纯粹
- ✅ 单个 `.py` 文件即可运行，分发成本为零
- ✅ 代码行数精简（257 行），注释清晰，适合作为 Python GUI 入门参考

### 项目管理成果

- ✅ Git 版本管理，提交历史清晰可追溯
- ✅ 撰写详尽的 README 文档与 CLAUDE.md 开发指南
- ✅ 项目开源在 GitHub，接受社区反馈

### 量化成果

| 指标 | 数据 |
|------|------|
| 代码行数 | 257 行（含注释和空行） |
| 核心类数 | 1 个（`PomodoroTimer`） |
| 方法数 | 15 个 |
| 支持的状态 | 3 种（work / short_break / long_break） |
| 第三方依赖 | 0 |
| 内存占用 | ~15 MB |
| IDE 运行时间 | 可无限循环 |

---

## 🚀 快速部署

### 环境要求

- **操作系统**：Windows 10/11
- **Python**：3.8 或更高版本
- **无需任何 pip 安装**

> 💡 tkinter 是 Python 标准库的一部分，随官方 Python 安装包自带。如果你在安装 Python 时勾选了 "tcl/tk and IDLE"，就无需额外操作。

验证 tkinter 可用：

```bash
python -c "import tkinter; print('tkinter OK')"
```

### 三步启动

```bash
# 1. 克隆仓库
git clone https://github.com/ly99LLL/tomatobinggo.git
cd tomatobinggo

# 2. 运行（带控制台窗口）
python pomodoro.py

# 3. 推荐方式：无控制台窗口启动
pythonw pomodoro.py
```

### 创建桌面快捷方式（Windows）

1. 右键桌面 → 新建 → 快捷方式
2. 位置填写：`pythonw.exe C:\path\to\tomatobinggo\pomodoro.py`
3. 名称填写：番茄钟
4. （可选）右键快捷方式 → 属性 → 更改图标

### 打包为独立 .exe

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name TomatoTimer pomodoro.py
# 输出：dist/TomatoTimer.exe
```

---

## 🌍 项目意义

### 对用户的实用价值

在一个注意力被算法和推送通知高度商品化的时代，**专注力是最稀缺的个人资源**。Tomatobinggo 不联网、不弹广告、不收集数据——它就是一个纯粹的计时器，帮助你在该专注的时候专注，在该休息的时候休息。它的存在本身就是一种态度：**把注意力还给自己**。

### 对 Python 社区的参考价值

本项目展示了如何用 Python 标准库**从零构建一个完整的桌面应用**，而不引入任何第三方框架。对于 Python 初学者来说，它是一个很好的参考项目：

- 理解 `tkinter` 的实际应用
- 理解多线程编程中 UI 线程安全的要点
- 理解状态机模式在真实项目中的运用
- 理解 Canvas 绑图与几何计算

### 对"工具哲学"的思考

> "我们不缺工具，缺的是趁手的工具。"

市面上的番茄钟 App 有几百款，但大多数要么功能臃肿（社区、积分、排行榜——到底是番茄钟还是社交软件？），要么广告满天飞，要么数据上传云端。Tomatobinggo 选择了另一条路：**做减法**。只保留最核心的功能，用最少的代码，跑在本地，不碰网络。这是一种对抗"软件膨胀"的姿态，也是对"工具应该服务于人而非绑架人"这一理念的实践。

---

## 📈 对我能力的提升

这个项目虽然代码量不大（257 行），但在构建过程中，我在多个维度获得了实实在在的成长：

### 1. GUI 编程能力

在此之前，我对桌面 GUI 编程的理解仅停留在理论层面。通过亲手构建 tkinter 应用的完整流程——窗口管理、控件布局、Canvas 绑图、事件绑定、样式配置——我切实掌握了 **原生桌面应用开发的完整链路**。

具体收获：
- 理解了 tkinter 的 `mainloop` 事件循环机制
- 掌握了 `pack` / `grid` 布局系统的实践技巧
- 学会了 Canvas 的底层绘制 API（`create_arc`、`create_oval`、`create_text`）
- 掌握了 `ttk.Style` 主题系统的使用

### 2. 多线程编程与线程安全

Python 的 GIL 让很多人以为"Python 不需要关心线程安全"。但 **GUI 编程是少数几个必须认真对待线程安全的场景之一**——tkinter **不是**线程安全的，从非主线程操作控件会导致未定义行为甚至崩溃。

本项目中的线程模型是我最得意的设计：
- 后台 `daemon` 线程负责阻塞式倒计时
- `root.after(0, callback)` 将所有 UI 更新调度回主线程
- 使用标志位而非锁来实现暂停/继续的状态同步

这套模式可以迁移到任何 tkinter / PyQt / 其他 GUI 框架的多线程场景中。

### 3. 状态机设计思维

在写 `_session_end` 方法时，我最初用了大量 `if-elif` 嵌套，代码很快变得难以维护。重构后采用了清晰的状态机设计——每个状态有明确的进入条件、退出动作和唯一的下一状态——这让代码逻辑变得一目了然，也为后续扩展（如添加自定义休息类型）留下了干净的接口。

### 4. 从零到一的完整项目交付

这不是一个课程作业或照着教程敲的 demo——这是我从**需求分析 → 技术选型 → 代码实现 → 测试调试 → Git 版本管理 → 开源发布**完整走完的真实项目。

关键成长：
- **技术选型能力**：在 tkinter / PyQt / Electron 之间做取舍，根据"最小可行"原则选择了零依赖方案
- **文档写作能力**：写了详尽的中文 README 和 CLAUDE.md ，学会了如何让一个陌生人快速理解和使用你的项目
- **Git 工作流**：init → add → commit → remote → push，完成了完整的版本管理流程
- **开源心态**：把代码放到 GitHub 上接受审视，本身就是一种成长

### 5. 对"专注"本身的反思

开发番茄钟的过程中，我实际上在反复思考一个问题：**"什么样的工具才能真正帮助我专注？"**

答案不是"功能越多越好"，而是"越少打扰越好"。这个洞察不仅影响了 Tomatobinggo 的设计理念，也反过来优化了我自己的工作习惯——少看手机、关掉不必要的通知、用自己写的番茄钟来管理节奏。**写工具的人，首先被工具改变。**

### 6. Canvas 绘图与图形学基础

圆形进度条看似简单，但实现涉及：
- 圆心坐标与半径的几何计算
- 弧度与角度的转换（`start` 和 `extent` 参数）
- 颜色随进度变化的视觉设计
- 重绘时 `delete("progress")` 的性能优化

这些经验为后续更复杂的 Canvas 绘图（图表、仪表盘、自定义控件）打下了基础。

---

## 📖 使用说明

1. 点击 **「开始」** 启动当前计时阶段（默认从 25 分钟专注开始）。
2. 计时过程中可随时点击 **「暂停」**，再次点击 **「继续」** 恢复。
3. 点击 **「重置」** 将恢复初始状态，清空已完成番茄计数。
4. 专注时间结束后自动进入休息阶段，同时播放蜂鸣提示音。
5. 使用 **「窗口置顶」** 复选框控制应用是否始终显示在最前端。
6. 每完成 4 个番茄，系统自动安排一次 15 分钟的长休息。

---

## 🏗️ 代码架构

### 类结构全景

```
PomodoroTimer
├── __init__()              # 初始化窗口属性、状态变量、调用 _setup_ui
├── run()                   # 启动 tkinter 主事件循环
│
├── UI 层
│   ├── _setup_ui()         # 构建全部控件（标签、Canvas、按钮、复选框）
│   ├── _draw_progress()    # Canvas 绘制圆形进度环
│   └── _update_display()   # 刷新倒计时文字与进度条
│
├── 逻辑层
│   ├── _tick()             # [后台线程] 每秒倒计时核心循环
│   ├── _session_end()      # 阶段结束处理：状态转换 + 提示音
│   ├── _set_session()      # 切换阶段并重置秒数
│   └── _total_seconds()    # 返回当前阶段总秒数
│
├── 用户操作
│   ├── start()             # 启动计时线程
│   ├── pause()             # 暂停 / 继续切换
│   ├── reset()             # 重置全部状态
│   └── _toggle_top()       # 窗口置顶开关
│
└── 系统回调
    └── _on_close()         # 窗口关闭时停止线程并销毁窗口
```

### 核心常量

```python
class PomodoroTimer:
    WORK_MIN = 25            # 专注时长（分钟）
    SHORT_BREAK_MIN = 5      # 短休息时长（分钟）
    LONG_BREAK_MIN = 15      # 长休息时长（分钟）
    SESSIONS_BEFORE_LONG = 4 # 每几个番茄后进入长休息
```

### 状态流转图

```
[启动]
   │
   ▼
┌─────────┐    25 分钟结束    ┌──────────────┐
│  work   │ ─────────────────► │ short_break  │ (第1-3次)
│  25 min │                    │  5 min       │
└─────────┘                    └──────┬───────┘
    ▲                                │ 5 分钟结束
    │                                │
    │      ┌──────────────┐          │
    │      │  long_break  │◄─────────┘ (第4次)
    │      │  15 min      │
    │      └──────┬───────┘
    │             │ 15 分钟结束
    └─────────────┘
```

---

## ⚙️ 自定义配置

### 调整时间参数

编辑 `pomodoro.py` 顶部的类常量：

```python
class PomodoroTimer:
    WORK_MIN = 30            # 改为 30 分钟专注
    SHORT_BREAK_MIN = 5      # 短休息保持 5 分钟
    LONG_BREAK_MIN = 20      # 长休息改为 20 分钟
    SESSIONS_BEFORE_LONG = 3 # 每 3 个番茄进入长休息
```

### 修改提示音

```python
# 当前：800Hz 持续 300ms
winsound.Beep(800, 300)

# 更高频率 + 更长 = 更"刺耳"的提醒
winsound.Beep(1000, 500)

# 双音符交替 = 更悦耳
winsound.Beep(800, 200)
winsound.Beep(1000, 200)
```

### 自定义配色

搜索 `#1e1e2e`（背景）、`#cdd6f4`（文字）等色值并替换为你喜欢的颜色。

---

## 📦 打包为可执行文件

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包（无控制台、单文件）
pyinstaller --onefile --noconsole --name TomatoTimer pomodoro.py

# 带自定义图标
pyinstaller --onefile --noconsole --icon=tomato.ico --name TomatoTimer pomodoro.py
```

---

## 📁 项目结构

```
tomatobinggo/
├── pomodoro.py          # 主程序 — 全部 UI 与业务逻辑（257 行）
├── README.md            # 项目文档（就是你正在看的这个）
├── CLAUDE.md            # Claude Code 开发指南
├── .gitignore           # Git 忽略规则
└── a.py                 # 空文件（预留）
```

---

## 🗺️ 路线图

- [ ] 可视化设置面板：在 GUI 中调整时间参数
- [ ] 跨平台音频：用 `pygame` 替代 `winsound`，支持 macOS / Linux
- [ ] 系统托盘最小化：关闭窗口时隐藏到托盘而非退出
- [ ] 番茄历史记录：本地 JSON 文件记录每日番茄数
- [ ] Windows Toast 通知：阶段切换时弹出系统通知
- [ ] 快捷键支持：空格暂停、Esc 重置
- [ ] 数据统计面板：周/月番茄趋势图
- [ ] 白噪音背景音效
- [ ] GitHub Actions 自动构建与发布

---

## ❓ 常见问题

<details>
<summary><strong>Q: 运行时提示 No module named 'tkinter'？</strong></summary>

重新安装 Python，在安装向导中勾选 **"tcl/tk and IDLE"** 选项。
</details>

<details>
<summary><strong>Q: macOS / Linux 可以用吗？</strong></summary>

当前版本使用 `winsound.Beep` 播放提示音，为 Windows 专属。如需跨平台，可将提示音逻辑替换为 `pygame.mixer` 或 `playsound`。
</details>

<details>
<summary><strong>Q: 倒计时线程会消耗很多 CPU 吗？</strong></summary>

不会。后台线程使用 `time.sleep(1)` 每秒唤醒一次（暂停时 0.2 秒轮询一次），绝大部分时间处于阻塞等待状态，CPU 占用近乎为零。
</details>

<details>
<summary><strong>Q: 为什么选择 tkinter 而不是 PyQt 或 Electron？</strong></summary>

零依赖 > 功能丰富。tkinter 随 Python 标准库分发，任何 Python 环境都能直接运行，无需安装数百 MB 的框架。对于番茄钟这类轻量级工具，够用就好。
</details>

<details>
<summary><strong>Q: 如何修改字体？</strong></summary>

在 `_setup_ui` 方法中修改 `font` 参数。Windows 推荐 `Microsoft YaHei`，macOS 推荐 `PingFang SC`。
</details>

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

```bash
# 1. Fork 本仓库
# 2. 创建功能分支
git checkout -b feature/your-feature

# 3. 提交更改（使用中文提交信息）
git commit -m 'feat: 添加系统托盘最小化'

# 4. 推送分支
git push origin feature/your-feature

# 5. 在 GitHub 创建 Pull Request
```

代码风格要求：中文注释、4 空格缩进、与现有代码风格保持一致。

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议——你可以自由使用、修改、分发，只需保留原始的版权声明。

---

<p align="center">
  <br>
  <strong>🍅 用自己写的番茄钟，管理自己的专注时间。</strong><br>
  <sub>Made with ❤️ and Python on Windows</sub>
</p>
