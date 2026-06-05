# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A single-file Pomodoro timer desktop application written in Python using `tkinter`. It runs on Windows only because it uses `winsound.Beep` for session-end alerts.

## Running the app

```bash
python pomodoro.py
```

On Windows, use `pythonw` to launch without a console window:

```bash
pythonw pomodoro.py
```

## Architecture

- **Single file**: all logic lives in `pomodoro.py` inside the `PomodoroTimer` class.
- **UI framework**: `tkinter` with a custom circular progress bar drawn on a `Canvas`.
- **Threading model**: a daemon `threading.Thread` (`_tick`) handles the countdown sleep loop. UI updates are marshalled back to the main thread via `root.after(0, ...)` to keep tkinter single-thread safe.
- **Session state machine**: `work` → `short_break` (or `long_break` every 4 sessions) → `work`. State transitions happen in `_session_end`.
- **Windows-specific**: imports `winsound` and calls `winsound.Beep(800, 300)` on session end.

## Key constants

- `WORK_MIN = 25`
- `SHORT_BREAK_MIN = 5`
- `LONG_BREAK_MIN = 15`
- `SESSIONS_BEFORE_LONG = 4`

## Notes

- There are currently no tests, lint rules, or package management files (e.g., `requirements.txt`, `pyproject.toml`).
- `a.py` is empty and unused.
