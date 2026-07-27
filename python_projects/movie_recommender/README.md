<div align="center">

# 🎬 KRYOS Movie Recommender

### A layered, object-oriented console application for discovering, managing, and organizing your movie collection.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()
[![Architecture](https://img.shields.io/badge/Architecture-Layered%20%2F%20OOP-orange?style=for-the-badge)]()

*Part of the [`python-learning-journey`](../../) repository — `python_project/movie_recommender`*

[Overview](#-overview) • [Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure) • [Design Highlights](#-design--engineering-highlights) • [Roadmap](#-roadmap)

</div>

---

## 📖 Overview

**KRYOS Movie Recommender** is a fully interactive, terminal-based application that lets users **recommend**, **add**, **search**, **delete**, and **browse** movies organized by genre. While the feature set is intentionally simple, the *engineering* behind it is not — this project is built as a demonstration of clean, layered software architecture applied to a small, real-world problem.

Rather than a single monolithic script, the application is decomposed into distinct responsibility layers — **presentation**, **business logic**, **validation**, **persistence**, and **cross-cutting concerns** (logging & configuration) — each isolated in its own module. This mirrors the architectural patterns used in production-grade software, scaled down to a learning-friendly size.

> 💡 **Why this project matters:** It's not "just a movie picker." It's a case study in separation of concerns, dependency injection, consistent error handling via status codes, and defensive, fail-safe I/O — all written in plain, dependency-free Python.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Recommend** | Instantly get a random movie suggestion from any genre in your library |
| ➕ **Add** | Add new movies to existing genres, or create brand-new genres on the fly |
| 🔍 **Search** | Case-insensitive, partial-match search across the entire movie library |
| 🗑️ **Delete** | Find and remove movies with confirmation prompts to prevent accidental data loss |
| 🍿 **Show Library** | Browse the full collection, neatly grouped and numbered by genre |
| 🧠 **Smart Duplicate Detection** | Prevents the same movie from being added twice, across *any* genre |
| 💾 **Persistent Storage** | All data is saved to a human-readable JSON file — no database setup required |
| 📋 **Structured Logging** | Every operation is logged with full context (file, line, timestamp) for diagnostics |
| 🛡️ **Graceful Failure Handling** | Corrupted files, missing files, and I/O errors are handled without crashing |
| ⌨️ **Consistent Navigation** | Every menu supports `0` / `stop` to safely return to the main menu at any point |

---

## 🏗 Architecture

The application follows a **layered architecture**, where each layer has a single, well-defined responsibility and communicates with adjacent layers through simple, predictable contracts (primarily `(bool, result)` and `MovieStatus` return values — never raw exceptions leaking across layers).

```
┌─────────────────────────────────────────────────────────────────┐
│                         main.py  (UI Layer)                     │
│   Menus · Input collection · Output formatting · Program flow   │
└───────────────────────────────┬─────────────────────────────────┘
                                 │  calls
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                  movie_service.py  (Service Layer)               │
│     Business logic · Orchestration · Status resolution           │
└──────────────┬──────────────────────────────────┬───────────────┘
               │  validates via                   │  persists via
               ▼                                  ▼
┌─────────────────────────────┐      ┌─────────────────────────────┐
│   validators.py             │      │   storage.py                │
│   Input validation & rules  │      │   JSON read/write, defaults │
└─────────────────────────────┘      └─────────────────────────────┘
               │                                  │
               └───────────────┬──────────────────┘
                                ▼
                 ┌──────────────────────────────┐
                 │   status.py  /  config.py     │
                 │   Shared status codes &        │
                 │   application-wide constants   │
                 └──────────────────────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │   logger_config.py             │
                 │   Centralized dual-handler      │
                 │   logging (console + file)      │
                 └──────────────────────────────┘
```

**Key architectural principles applied:**

- **Separation of Concerns** — the UI never touches storage directly, and the service layer never calls `print()` or `input()`.
- **Dependency Injection** — `MovieService` receives a `MovieStorage` instance through its constructor rather than instantiating one itself, making the service trivially testable with mock storage.
- **Single Source of Truth for Outcomes** — every operation across the app returns a `MovieStatus` code, which the UI layer alone is responsible for translating into user-facing text. Business logic never contains display strings.
- **Fail-Safe I/O** — storage operations catch and log every failure mode (missing file, corrupted JSON, disk errors) and always return a predictable, well-typed result instead of propagating exceptions upward.

---

## ⚙️ Installation

**Requirements:** Python 3.10 or later. No third-party dependencies — the entire project runs on the Python standard library.

```bash
# 1. Clone the repository
git clone https://github.com/Behruz-Hojaniyazow/python-learning-journey.git

# 2. Navigate to the project folder
cd python-learning-journey/python_project/movie_recommender

# 3. Run the application
python main.py
```

On first launch, if `movies.json` does not yet exist, the app automatically bootstraps itself with a curated default library across five genres (*Action, Comedy, Horror, Drama, Sci-Fi*) — no manual setup required.

---

## 🚀 Usage

Launch the app and navigate using the numbered main menu:

```
╔══════════════════════════════════════════╗
║ 🎬 KRYOS MOVIE PROGRAM                    ║
╚══════════════════════════════════════════╝

┌─ 📋 MAIN MENU ──────────────────┐
   1 -> 🎯 Recommend Movie
   2 -> ➕️ Add Movie
   3 -> 🔍 Search Movie
   4 -> 🗑 Delete Movie
   5 -> 🍿 Show Movies
   6 -> 🚪 Exit App
──────────────────────────────────────────

➡️ Choose an action:
```

Every sub-menu is a self-contained loop — enter `0` or `stop` at any prompt to return safely to the main menu without losing your place in the program.

**Example — getting a recommendation:**

```
➡️ Choose an action: 1

┌─ 🎭 Choose a genre ─────────────
  1 -> Action
  2 -> Comedy
  3 -> Horror
  4 -> Drama
  5 -> Sci-Fi
──────────────────────────────────

Select a genre number (or '0'/'stop' to exit): 1

✅️ Movie Recommended successfully

┌─ 🍿 Recommended movie for you ──
  Genre: ACTION
  Movie: Inception
──────────────────────────────────
```

---

## 📁 Project Structure

```
movie_recommender/
│
├── main.py              # Entry point — menu loop & all UI-flow (ui_*) functions
├── movie_service.py      # Business logic layer — recommend, add, search, delete
├── storage.py            # Persistence layer — JSON load/save, default dataset
├── validators.py         # Input validation & normalization rules
├── status.py             # Centralized MovieStatus outcome codes
├── config.py             # Application-wide constants (file paths, log formats)
├── logger_config.py      # Centralized dual-handler (file + console) logger factory
├── ui_helpers.py          # Reusable console presentation helpers (headers, sections, etc.)
├── movies.json            # Auto-generated persistent movie database
└── movies_app.log         # Auto-generated log file (ERROR / CRITICAL history)
```

---

## 🧩 Design & Engineering Highlights

This project showcases several intermediate-to-advanced Python practices, deliberately applied even in a small-scale CLI tool:

- **🏛️ Layered OOP Architecture** — a clean four-layer separation (UI → Service → Validation/Storage → Cross-cutting), each independently reasoned about and independently testable.
- **💉 Dependency Injection** — `MovieService(storage)` decouples business logic from any specific persistence mechanism, so the JSON backend could be swapped for a database with zero changes to service logic.
- **🚦 Status-Code Driven Error Handling** — a single `MovieStatus` vocabulary flows consistently through validators, service methods, and the UI, avoiding scattered magic strings or inconsistent exception handling.
- **📝 Structured, Dual-Target Logging** — `logger_config.py` configures one logger with two handlers: a verbose file handler (timestamp, file, line number) for diagnostics, and a minimal console handler for clean user-facing feedback — a pattern taken directly from production logging setups.
- **🛡️ Defensive Persistence Layer** — `storage.py` anticipates and gracefully handles every realistic failure mode: missing files, corrupted JSON, and generic I/O errors, always degrading to a safe, predictable return value instead of crashing the program.
- **🔠 Case-Insensitive Data Integrity** — genre and movie matching (duplicates, search, deletion) is normalized and matched case-insensitively throughout, preventing "Action" and "action" from ever being treated as different entities.
- **📚 Google-Style Docstrings Throughout** — every module, class, and function is documented with purpose, arguments, and return contracts, making the codebase self-explanatory and IDE-friendly.

---

## 🗺 Roadmap

- [ ] Migrate `MovieStatus` to a true `enum.Enum` subclass for full `.name` / `.value` support
- [ ] Add a unit test suite (`pytest`) covering `MovieService` with a mocked `MovieStorage`
- [ ] Add movie metadata (release year, rating, director) and richer filtering
- [ ] Optional: pluggable storage backends (SQLite / remote API)
- [ ] Optional: export the movie library to `.csv` / `.pdf`

---

## 🤝 Contributing

This is a personal learning project, but suggestions, code reviews, and pull requests are always welcome — feel free to open an issue or fork the repository.

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

## 👤 Author

**Behruz Hojaniyazow**
Part of an ongoing, self-directed Python learning journey — [`python-learning-journey`](https://github.com/Behruz-Hojaniyazow/python-learning-journey)

---

<div align="center">

*If this project helped you or inspired your own learning journey, consider giving the repository a ⭐!*

</div>
