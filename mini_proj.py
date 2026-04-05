"""
mini_py.py  —  All 8 Python Mini Projects in one unified tkinter launcher.
Run: python mini_py.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import font as tkFont
import random
import math

# ──────────────────────────────────────────────────────────────────────────────
#  SHARED PALETTE  (launcher shell)
# ──────────────────────────────────────────────────────────────────────────────
L = {
    "bg":        "#0b0c14",
    "bg2":       "#10121e",
    "surface":   "#161929",
    "card":      "#1c1f32",
    "card2":     "#22263a",
    "border":    "#2a2f4a",
    "border2":   "#3a4060",
    "fg":        "#eef2ff",
    "muted":     "#7880a8",
    "muted2":    "#4f567a",
    "accent":    "#86e1fc",
    "accent2":   "#cba6f7",
    "accent3":   "#8bd5ca",
    "success":   "#a6e3a1",
    "danger":    "#f38ba8",
    "warning":   "#f9e2af",
}

APP_META = [
    {"id": "atm",      "icon": "🏧", "name": "ANTEIKU ATM",
        "sub": "Banking Simulator",      "color": "#2ec8ff", "tag": "BANKING"},
    {"id": "library",  "icon": "📚", "name": "Neo Library",
        "sub": "Book Management",        "color": "#00d084", "tag": "MGMT"},
    {"id": "periodic", "icon": "⚗️",  "name": "Periodic Table",
        "sub": "118 Elements Explorer",  "color": "#c77dff", "tag": "SCIENCE"},
    {"id": "phonebook", "icon": "📖", "name": "Modern Phonebook",
        "sub": "Contact Manager",        "color": "#86e1fc", "tag": "CONTACTS"},
    {"id": "quiz",     "icon": "🧠", "name": "Knowledge Arena",
        "sub": "Tech Trivia Quiz",       "color": "#cba6f7", "tag": "GAME"},
    {"id": "billing",  "icon": "🧾", "name": "Smart Billing",
        "sub": "Boutique POS Desk",      "color": "#ffbe0b", "tag": "RETAIL"},
    {"id": "casino",   "icon": "🎰", "name": "Lucky Casino",
        "sub": "Number Guess Game",      "color": "#ff006e", "tag": "GAME"},
    {"id": "guess",    "icon": "🎯", "name": "Mystery Number",
        "sub": "Guess in 3 Tries",       "color": "#00ff88", "tag": "PUZZLE"},
]


# ══════════════════════════════════════════════════════════════════════════════
#  APP 1 — ANTEIKU ATM
# ══════════════════════════════════════════════════════════════════════════════
ACCOUNTS = [
    {"card_code": "k", "name": "Ken Kaneki",
        "title": "Midnight Account", "pin": 1234, "balance": 50000},
    {"card_code": "s", "name": "Sasuke Uchiha",
        "title": "Storm Account",    "pin": 5678, "balance": 100000},
    {"card_code": "i", "name": "Itachi Uchiha",
        "title": "Shadow Account",   "pin": 9123, "balance": 60000},
    {"card_code": "l", "name": "Light Yagami",
        "title": "Nova Account",     "pin": 8123, "balance": 40000},
]


class ATMApp:
    def __init__(self, frame):
        self.frame = frame
        self.selected_account = None
        self.pin_attempts = 0
        self.session_unlocked = False
        self._build()

    def _build(self):
        C = {"bg": "#090f1c", "bg2": "#10192f", "bg3": "#0f1c36",
             "card": "#15284f", "sel": "#1d3f75", "pin": "#102245",
             "right": "#0b162b", "status": "#101d38",
             "cyan": "#2ec8ff", "teal": "#48f0b8", "text": "#f0f7ff",
             "muted": "#9fb9ff", "dim": "#8ea8d8"}
        self.C = C
        root = self.frame
        root.configure(bg=C["bg2"])

        # Header
        hdr = tk.Frame(root, bg="#111b33", padx=20, pady=12)
        hdr.pack(fill="x", padx=14, pady=(14, 8))
        tk.Label(hdr, text="ANTEIKU ATM v3", font=("Consolas", 18, "bold"),
                 fg=C["cyan"], bg="#111b33").pack(anchor="w")
        tk.Label(hdr, text="Neon Banking Interface — Select a card to begin",
                 font=("Consolas", 9), fg=C["muted"], bg="#111b33").pack(anchor="w", pady=(2, 0))

        body = tk.Frame(root, bg=C["bg2"])
        body.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        # Left panel
        self.left = tk.Frame(body, bg=C["bg3"], padx=14, pady=14)
        self.left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        # Right panel
        self.right = tk.Frame(body, bg=C["right"], padx=14, pady=14)
        self.right.pack(side="right", fill="y", padx=(8, 0))

        self._build_cards()
        self._build_pin()
        self._build_actions()
        self._build_status()

    def _build_cards(self):
        C = self.C
        tk.Label(self.left, text="Select Card", font=("Consolas", 13, "bold"),
                 fg=C["text"], bg=self.C["bg3"]).pack(anchor="w")
        tk.Label(self.left, text="Tap a profile to insert card",
                 font=("Consolas", 9), fg=C["dim"], bg=self.C["bg3"]).pack(anchor="w", pady=(2, 10))

        wrap = tk.Frame(self.left, bg=self.C["bg3"])
        wrap.pack(fill="x")
        self.card_frames = {}
        for idx, acc in enumerate(ACCOUNTS):
            card = tk.Frame(wrap, bg=C["card"], padx=10, pady=8)
            r, c = idx // 2, idx % 2
            card.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            wrap.grid_columnconfigure(c, weight=1)
            tk.Label(card, text=acc["name"], font=("Consolas", 10, "bold"),
                     fg=C["text"], bg=C["card"]).pack(anchor="w")
            tk.Label(card, text=f"{acc['title']}  |  {acc['card_code'].upper()}",
                     font=("Consolas", 8), fg=C["muted"], bg=C["card"]).pack(anchor="w", pady=(2, 6))
            btn = tk.Button(card, text="Insert Card", font=("Consolas", 9),
                            bg=C["cyan"], fg="#081324", relief="flat", cursor="hand2",
                            command=lambda a=acc: self.select_account(a))
            btn.pack(anchor="w")
            self.card_frames[acc["card_code"]] = card

    def _build_pin(self):
        C = self.C
        pf = tk.Frame(self.left, bg=C["pin"], padx=10, pady=10)
        pf.pack(fill="x", pady=(12, 0))
        tk.Label(pf, text="PIN Verification", font=("Consolas", 11, "bold"),
                 fg=C["text"], bg=C["pin"]).pack(anchor="w")
        self.pin_hint = tk.Label(pf, text="Select an account first",
                                 font=("Consolas", 9), fg=C["dim"], bg=C["pin"])
        self.pin_hint.pack(anchor="w", pady=(2, 6))
        row = tk.Frame(pf, bg=C["pin"])
        row.pack(fill="x")
        self.pin_entry = tk.Entry(row, show="*", font=("Consolas", 14),
                                  bg="#08152e", fg=C["cyan"], insertbackground=C["cyan"],
                                  relief="flat", width=12)
        self.pin_entry.pack(side="left")
        tk.Button(row, text="Unlock", font=("Consolas", 10),
                  bg=C["teal"], fg="#04241c", relief="flat", padx=10, cursor="hand2",
                  command=self.verify_pin).pack(side="left", padx=(8, 0))

    def _build_actions(self):
        C = self.C
        tk.Label(self.right, text="Session Actions", font=("Consolas", 13, "bold"),
                 fg=C["text"], bg=C["right"]).pack(anchor="w")
        self.acc_label = tk.Label(self.right, text="No card inserted",
                                  font=("Consolas", 9), fg=C["muted"], bg=C["right"])
        self.acc_label.pack(anchor="w", pady=(2, 10))
        tk.Label(self.right, text="Withdraw Amount", font=("Consolas", 9),
                 fg=C["muted"], bg=C["right"]).pack(anchor="w")
        self.wd_entry = tk.Entry(self.right, font=("Consolas", 12),
                                 bg="#091125", fg="#d8f7ff", insertbackground="#d8f7ff",
                                 relief="flat", width=16)
        self.wd_entry.pack(anchor="w", pady=(4, 10))
        self.bal_btn = tk.Button(self.right, text="Check Balance",
                                 font=("Consolas", 10), bg="#37a5ff", fg="#041428",
                                 relief="flat", padx=10, pady=5, cursor="hand2",
                                 state="disabled", command=self.check_balance)
        self.bal_btn.pack(fill="x", pady=(0, 6))
        self.wd_btn = tk.Button(self.right, text="Withdraw Cash",
                                font=("Consolas", 10), bg="#ff5588", fg="#0f0010",
                                relief="flat", padx=10, pady=5, cursor="hand2",
                                state="disabled", command=self.withdraw_cash)
        self.wd_btn.pack(fill="x")

    def _build_status(self):
        C = self.C
        sp = tk.Frame(self.right, bg="#101d38", padx=10, pady=10)
        sp.pack(fill="both", expand=True, pady=(14, 0))
        tk.Label(sp, text="Live Status", font=("Consolas", 11, "bold"),
                 fg=C["text"], bg="#101d38").pack(anchor="w")
        self.status_lbl = tk.Label(sp, text="Insert a card to begin.",
                                   font=("Consolas", 9), fg=C["muted"],
                                   bg="#101d38", justify="left", wraplength=220)
        self.status_lbl.pack(anchor="w", pady=(6, 0))
        self.receipt = tk.Text(sp, height=10, width=28, bg="#0a1428",
                               fg="#b9fff4", relief="flat", font=("Consolas", 9))
        self.receipt.pack(fill="both", expand=True, pady=(10, 0))
        self.receipt.configure(state="disabled")

    def _write_receipt(self, lines):
        self.receipt.configure(state="normal")
        self.receipt.delete("1.0", "end")
        self.receipt.insert("end", "\n".join(lines))
        self.receipt.configure(state="disabled")

    def _set_actions(self, on):
        s = "normal" if on else "disabled"
        self.bal_btn.configure(state=s)
        self.wd_btn.configure(state=s)

    def select_account(self, acc):
        self.selected_account = acc
        self.pin_attempts = 0
        self.session_unlocked = False
        self.pin_entry.delete(0, "end")
        self.wd_entry.delete(0, "end")
        self._set_actions(False)
        for code, card in self.card_frames.items():
            card.configure(bg=self.C["sel"] if code ==
                           acc["card_code"] else self.C["card"])
        self.acc_label.configure(text=f"Active: {acc['name']}")
        self.pin_hint.configure(text="Enter PIN and press Unlock")
        self.status_lbl.configure(
            text=f"Card inserted: {acc['name']}\nPIN attempts left: 3")
        self._write_receipt(["── ANTEIKU ATM ──", f"USER   : {acc['name']}",
                             f"ACCT   : {acc['title']}", "STATUS : Card inserted",
                             "", "Authenticate to continue."])

    def verify_pin(self):
        if not self.selected_account:
            self.status_lbl.configure(text="Select an account card first.")
            return
        t = self.pin_entry.get().strip()
        if not t.isdigit() or len(t) != 4:
            self.status_lbl.configure(text="PIN must be exactly 4 digits.")
            return
        if int(t) == self.selected_account["pin"]:
            self.session_unlocked = True
            self._set_actions(True)
            self.pin_hint.configure(text="Session unlocked ✓")
            self.status_lbl.configure(
                text=f"Access granted: {self.selected_account['name']}\nYou may check balance or withdraw.")
            return
        self.pin_attempts += 1
        left = 3 - self.pin_attempts
        self.pin_entry.delete(0, "end")
        if left <= 0:
            self.selected_account = None
            self.session_unlocked = False
            self._set_actions(False)
            self.acc_label.configure(text="No card inserted")
            self.pin_hint.configure(text="Session blocked. Re-insert card.")
            self.status_lbl.configure(text="PIN mismatch ×3. Session blocked.")
            self._write_receipt(
                ["── SECURITY ──", "AUTH FAILED", "3 wrong PINs", "Re-insert card."])
            return
        self.status_lbl.configure(text=f"PIN mismatch. Attempts left: {left}")

    def check_balance(self):
        if not self._ready():
            return
        b = self.selected_account["balance"]
        self.status_lbl.configure(text=f"Balance: {b}")
        self._write_receipt(["── BALANCE ──", f"USER    : {self.selected_account['name']}",
                             f"BALANCE : {b}", "", "Thank you."])

    def withdraw_cash(self):
        if not self._ready():
            return
        t = self.wd_entry.get().strip()
        if not t.isdigit():
            self.status_lbl.configure(text="Enter a valid numeric amount.")
            return
        amt = int(t)
        if amt <= 0:
            self.status_lbl.configure(text="Amount must be > 0.")
            return
        if amt > self.selected_account["balance"]:
            self.status_lbl.configure(text="Insufficient funds.")
            return
        self.selected_account["balance"] -= amt
        rem = self.selected_account["balance"]
        self.wd_entry.delete(0, "end")
        self.status_lbl.configure(text=f"Dispensed: {amt}\nRemaining: {rem}")
        self._write_receipt(["── RECEIPT ──", f"USER      : {self.selected_account['name']}",
                             f"WITHDRAWN : {amt}", f"REMAINING : {rem}", "", "Collect cash safely."])

    def _ready(self):
        if not self.selected_account:
            self.status_lbl.configure(text="Insert a card first.")
            return False
        if not self.session_unlocked:
            self.status_lbl.configure(text="Unlock session with PIN first.")
            return False
        return True


# ══════════════════════════════════════════════════════════════════════════════
#  APP 2 — LIBRARY MANAGER
# ══════════════════════════════════════════════════════════════════════════════
class LibraryApp:
    BOOKS = [
        {"title": "Introduction to C",              "author": "Dennis Ritchie",
            "pages": 280, "price": 350, "code": 123, "stock": 2},
        {"title": "Introduction to Python",         "author": "Guido Rossum",
            "pages": 320, "price": 420, "code": 456, "stock": 3},
        {"title": "Fundamentals of Thermodynamics", "author": "Moran",
            "pages": 510, "price": 670, "code": 153, "stock": 13},
    ]

    def __init__(self, frame):
        self.frame = frame
        self.books = [b.copy() for b in self.BOOKS]
        C = {"bg": "#0d2818", "side": "#1a3a2a", "card": "#1f4d38", "p": "#00d084",
             "s": "#00b8a9", "acc": "#f4d35e", "ok": "#06ffa5", "err": "#ff4757",
             "fg": "#ffffff", "mt": "#7a9e8f"}
        self.C = C
        frame.configure(bg=C["bg"])

        hdr = tk.Frame(frame, bg=C["p"])
        hdr.pack(fill="x")
        tk.Label(hdr, text="📚  NEO LIBRARY MANAGER", font=("Consolas", 16, "bold"),
                 bg=C["p"], fg=C["bg"]).pack(pady=10, padx=16, anchor="w")

        main = tk.Frame(frame, bg=C["bg"])
        main.pack(fill="both", expand=True)

        sb = tk.Frame(main, bg=C["side"], width=180)
        sb.pack(side="left", fill="y", padx=8, pady=8)
        sb.pack_propagate(False)

        self.content = tk.Frame(main, bg=C["bg"])
        self.content.pack(side="right", fill="both",
                          expand=True, padx=8, pady=8)

        for txt, cmd in [("📖  View Catalog", self.show_catalog),
                         ("🔍  Search Code",  self.show_search),
                         ("➕  Add Book",     self.show_add),
                         ("📊  Statistics",   self.show_stats)]:
            bg = C["p"] if "Catalog" in txt else C["s"] if "Search" in txt else C["ok"] if "Add" in txt else C["acc"]
            tk.Button(sb, text=txt, font=("Consolas", 9, "bold"), bg=bg, fg=C["bg"],
                      relief="flat", pady=10, cursor="hand2",
                      command=cmd).pack(fill="x", pady=6, padx=8)

        self.show_catalog()

    def _clear(self):
        for w in self.content.winfo_children():
            w.destroy()

    def show_catalog(self):
        self._clear()
        C = self.C
        tk.Label(self.content, text="📚  LIBRARY CATALOG", font=("Consolas", 12, "bold"),
                 bg=C["bg"], fg=C["p"]).pack(anchor="w", pady=(0, 8))
        cols = ("Code", "Title", "Author", "Pages", "Price", "Stock")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Lib.Treeview", background=C["card"], foreground=C["fg"],
                        fieldbackground=C["card"], borderwidth=0, rowheight=26)
        style.configure("Lib.Treeview.Heading",
                        background=C["s"], foreground=C["bg"], borderwidth=0)
        style.map("Lib.Treeview", background=[("selected", C["p"])])
        tree = ttk.Treeview(self.content, columns=cols, show="headings",
                            height=10, style="Lib.Treeview")
        widths = [60, 200, 130, 60, 70, 60]
        for col, w in zip(cols, widths):
            tree.heading(col, text=col)
            tree.column(col, width=w, anchor="center")
        for b in self.books:
            tree.insert("", "end", values=(b["code"], b["title"], b["author"],
                                           b["pages"], f"Rs {b['price']}",
                                           f"✓ {b['stock']}" if b["stock"] > 0 else "✗ 0"))
        tree.pack(fill="both", expand=True)
        total_s = sum(b["stock"] for b in self.books)
        tk.Label(self.content, text=f"Total: {len(self.books)} books · {total_s} units in stock",
                 font=("Consolas", 9), bg=C["bg"], fg=C["mt"]).pack(anchor="w", pady=8)

    def show_search(self):
        self._clear()
        C = self.C
        tk.Label(self.content, text="🔍  SEARCH BY CODE", font=("Consolas", 12, "bold"),
                 bg=C["bg"], fg=C["p"]).pack(anchor="w", pady=(0, 8))
        f = tk.Frame(self.content, bg=C["card"], padx=14, pady=14)
        f.pack(fill="x")
        tk.Label(f, text="Book Code:", font=("Consolas", 10),
                 bg=C["card"], fg=C["fg"]).pack(anchor="w")
        e = tk.Entry(f, font=("Consolas", 12), bg=C["bg"], fg=C["p"],
                     insertbackground=C["p"], relief="flat")
        e.pack(fill="x", ipady=7, pady=4)
        res = tk.Label(f, text="", font=("Consolas", 10), bg=C["card"],
                       fg=C["ok"], justify="left", wraplength=500)
        res.pack(anchor="w", pady=8)

        def search():
            try:
                code = int(e.get())
                found = next(
                    (b for b in self.books if b["code"] == code), None)
                if found:
                    res.configure(fg=C["ok"],
                                  text=f"✓ Found!\nTitle:  {found['title']}\nAuthor: {found['author']}\nPages:  {found['pages']}\nPrice:  Rs {found['price']}\nStock:  {found['stock']} copies")
                else:
                    res.configure(
                        fg=C["err"], text=f"✗ No book with code {code}")
            except ValueError:
                res.configure(fg=C["err"], text="✗ Enter a valid number")
        tk.Button(f, text="🔎  FIND BOOK", font=("Consolas", 10, "bold"),
                  bg=C["s"], fg=C["bg"], relief="flat", pady=7, cursor="hand2",
                  command=search).pack(fill="x", pady=4)

    def show_add(self):
        self._clear()
        C = self.C
        tk.Label(self.content, text="➕  ADD NEW BOOK", font=("Consolas", 12, "bold"),
                 bg=C["bg"], fg=C["p"]).pack(anchor="w", pady=(0, 8))
        f = tk.Frame(self.content, bg=C["card"], padx=14, pady=14)
        f.pack(fill="x")
        entries = {}
        for field in ["Title", "Author", "Pages", "Price", "Code", "Stock"]:
            tk.Label(f, text=field+":", font=("Consolas", 9, "bold"),
                     bg=C["card"], fg=C["fg"]).pack(anchor="w", pady=(6, 0))
            e = tk.Entry(f, font=("Consolas", 11), bg=C["bg"], fg=C["p"],
                         insertbackground=C["p"], relief="flat")
            e.pack(fill="x", ipady=6)
            entries[field.lower()] = e

        def add():
            try:
                nb = {"title": entries["title"].get().strip(),
                      "author": entries["author"].get().strip(),
                      "pages": int(entries["pages"].get()),
                      "price": int(entries["price"].get()),
                      "code":  int(entries["code"].get()),
                      "stock": int(entries["stock"].get())}
                if not nb["title"] or not nb["author"]:
                    messagebox.showwarning(
                        "Missing", "Title and Author required!")
                    return
                self.books.append(nb)
                messagebox.showinfo("Added", "✓ Book added to library!")
                for e in entries.values():
                    e.delete(0, tk.END)
            except ValueError:
                messagebox.showerror(
                    "Error", "Pages/Price/Code/Stock must be numbers!")
        tk.Button(f, text="✅  ADD TO LIBRARY", font=("Consolas", 10, "bold"),
                  bg=C["ok"], fg=C["bg"], relief="flat", pady=9, cursor="hand2",
                  command=add).pack(fill="x", pady=10)

    def show_stats(self):
        self._clear()
        C = self.C
        tk.Label(self.content, text="📊  LIBRARY STATISTICS", font=("Consolas", 12, "bold"),
                 bg=C["bg"], fg=C["p"]).pack(anchor="w", pady=(0, 8))
        total_stock = sum(b["stock"] for b in self.books)
        total_val = sum(b["price"] * b["stock"] for b in self.books)
        avg_price = sum(b["price"] for b in self.books) / \
            len(self.books) if self.books else 0
        for emoji, lbl, val, color in [
            ("📚", "Total Books",    str(len(self.books)), C["p"]),
            ("📦", "Total Stock",    str(total_stock),     C["s"]),
            ("💰", "Library Value",  f"Rs {total_val}",    C["acc"]),
            ("💵", "Avg Price",      f"Rs {int(avg_price)}", C["ok"]),
        ]:
            card = tk.Frame(self.content, bg=color, padx=16, pady=12)
            card.pack(fill="x", pady=5)
            lf = tk.Frame(card, bg=color)
            lf.pack(side="left")
            tk.Label(lf, text=emoji, font=("Consolas", 24), bg=color).pack()
            rf = tk.Frame(card, bg=color)
            rf.pack(side="left", padx=16)
            tk.Label(rf, text=lbl, font=("Consolas", 9, "bold"),
                     bg=color, fg=C["bg"]).pack(anchor="w")
            tk.Label(rf, text=val, font=("Consolas", 16, "bold"),
                     bg=color, fg=C["bg"]).pack(anchor="w")
        tk.Label(self.content, text="📈  Stock by Book", font=("Consolas", 10, "bold"),
                 bg=C["bg"], fg=C["p"]).pack(anchor="w", pady=(14, 6))
        for b in self.books:
            row = tk.Frame(self.content, bg=C["bg"])
            row.pack(fill="x", pady=3)
            tk.Label(row, text=f"{b['title'][:28]:28}", font=("Consolas", 8),
                     bg=C["bg"], fg=C["fg"], width=30).pack(side="left")
            bar = tk.Canvas(row, height=18, bg=C["card"], highlightthickness=0)
            bar.pack(side="left", fill="x", expand=True, padx=8)
            bar.update_idletasks()
            w = min(b["stock"] * 14, 280)
            bar.create_rectangle(0, 0, w, 18, fill=C["s"], outline="")
            bar.create_text(max(w/2, 12), 9, text=str(b["stock"]),
                            fill=C["bg"], font=("Consolas", 8, "bold"))


# ══════════════════════════════════════════════════════════════════════════════
#  APP 3 — PERIODIC TABLE
# ══════════════════════════════════════════════════════════════════════════════
_ELEMENTS_RAW = [
    (1, "H", "Hydrogen", 1.008, "Gas", "nonmetal"),
    (2, "He", "Helium", 4.003, "Gas", "noble_gas"),
    (3, "Li", "Lithium", 6.941, "Solid", "alkali_metal"),
    (4, "Be", "Beryllium", 9.012, "Solid", "alkaline_earth"),
    (5, "B", "Boron", 10.811, "Solid", "metalloid"),
    (6, "C", "Carbon", 12.011, "Solid", "nonmetal"),
    (7, "N", "Nitrogen", 14.007, "Gas", "nonmetal"),
    (8, "O", "Oxygen", 15.999, "Gas", "nonmetal"),
    (9, "F", "Fluorine", 18.998, "Gas", "nonmetal"),
    (10, "Ne", "Neon", 20.180, "Gas", "noble_gas"),
    (11, "Na", "Sodium", 22.990, "Solid", "alkali_metal"),
    (12, "Mg", "Magnesium", 24.305, "Solid", "alkaline_earth"),
    (13, "Al", "Aluminium", 26.982, "Solid", "metal"),
    (14, "Si", "Silicon", 28.086, "Solid", "metalloid"),
    (15, "P", "Phosphorus", 30.974, "Solid", "nonmetal"),
    (16, "S", "Sulfur", 32.065, "Solid", "nonmetal"),
    (17, "Cl", "Chlorine", 35.453, "Gas", "nonmetal"),
    (18, "Ar", "Argon", 39.948, "Gas", "noble_gas"),
    (19, "K", "Potassium", 39.098, "Solid", "alkali_metal"),
    (20, "Ca", "Calcium", 40.078, "Solid", "alkaline_earth"),
    (26, "Fe", "Iron", 55.845, "Solid", "transition_metal"),
    (29, "Cu", "Copper", 63.546, "Solid", "transition_metal"),
    (47, "Ag", "Silver", 107.868, "Solid", "transition_metal"),
    (79, "Au", "Gold", 196.967, "Solid", "transition_metal"),
    (80, "Hg", "Mercury", 200.592, "Liquid", "transition_metal"),
    (92, "U", "Uranium", 238.029, "Solid", "lanthanide"),
]
for i in range(21, 26):
    _ELEMENTS_RAW.append(
        (i, f"E{i}", f"Element-{i}", float(i), "Solid", "transition_metal"))
for i in range(30, 47):
    _ELEMENTS_RAW.append(
        (i, f"E{i}", f"Element-{i}", float(i), "Solid", "transition_metal"))
for i in range(48, 79):
    _ELEMENTS_RAW.append((i, f"E{i}", f"Element-{i}", float(i),
                         "Solid", "lanthanide" if i < 72 else "transition_metal"))
for i in range(81, 92):
    _ELEMENTS_RAW.append(
        (i, f"E{i}", f"Element-{i}", float(i), "Solid", "metal"))
for i in range(93, 119):
    _ELEMENTS_RAW.append(
        (i, f"E{i}", f"Element-{i}", float(i), "Solid", "lanthanide"))
ELEMENTS = sorted([{"n": r[0], "sym": r[1], "name": r[2], "mass": r[3], "state": r[4], "cat": r[5]}
                   for r in _ELEMENTS_RAW], key=lambda x: x["n"])
_ELEM_FACTS = {1: "Most abundant element in the universe", 6: "Forms diamond & graphite allotropes",
               7: "Essential for life and proteins", 8: "Required for respiration",
               26: "Main component of Earth's core", 79: "Most precious metal — never rusts",
               80: "Only metal liquid at room temperature", 92: "Heaviest naturally occurring element"}


class PeriodicApp:
    CAT_COLORS = {"nonmetal": "#e74c3c", "noble_gas": "#9b59b6", "alkali_metal": "#f39c12",
                  "alkaline_earth": "#d5a6bd", "metalloid": "#95a5a6", "transition_metal": "#3498db",
                  "lanthanide": "#1abc9c", "metal": "#c0392b"}

    def __init__(self, frame):
        self.frame = frame
        self.btns = {}
        frame.configure(bg="#0d0d0d")
        # Header
        hdr = tk.Frame(frame, bg="#ff6b35", height=52)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="⚛️   PERIODIC TABLE EXPLORER  ⚛️",
                 font=("Consolas", 14, "bold"), bg="#ff6b35", fg="#fff").pack(pady=12)

        main = tk.Frame(frame, bg="#0d0d0d")
        main.pack(fill="both", expand=True, padx=8, pady=8)

        # Left: controls + grid
        left = tk.Frame(main, bg="#0d0d0d")
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        ctrl = tk.Frame(left, bg="#1a1a1a")
        ctrl.pack(fill="x", pady=(0, 8))
        tk.Label(ctrl, text="🔍  Search:", font=("Consolas", 9),
                 bg="#1a1a1a", fg="#ff6b35").pack(side="left", padx=8, pady=8)
        self.sv = tk.StringVar()
        se = tk.Entry(ctrl, textvariable=self.sv, font=("Consolas", 11),
                      bg="#252525", fg="#ff6b35", insertbackground="#ff6b35", relief="flat", width=20)
        se.pack(side="left", ipady=4, pady=8)
        se.bind("<KeyRelease>", lambda e: self._search())
        for lbl, cat in [("All", "all"), ("Metals", "metal"), ("Non-metals", "nonmetal"),
                         ("Noble", "noble_gas"), ("Trans.", "transition_metal")]:
            tk.Button(ctrl, text=lbl, font=("Consolas", 8), bg="#353535",
                      fg="#fff", relief="flat", padx=6, pady=3, cursor="hand2",
                      command=lambda c=cat: self._filter(c)).pack(side="left", padx=2, pady=8)

        # Scrollable grid
        canvas_wrap = tk.Frame(left, bg="#0d0d0d")
        canvas_wrap.pack(fill="both", expand=True)
        cv = tk.Canvas(canvas_wrap, bg="#1a1a1a", highlightthickness=0)
        sb = tk.Scrollbar(canvas_wrap, orient="vertical", command=cv.yview)
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        gf = tk.Frame(cv, bg="#1a1a1a")
        cv.create_window((0, 0), window=gf, anchor="nw")
        gf.bind("<Configure>", lambda e: cv.configure(
            scrollregion=cv.bbox("all")))
        cv.bind("<MouseWheel>",
                lambda e: cv.yview_scroll(-1 if e.delta > 0 else 1, "units"))

        cols_per_row = 12
        for i, el in enumerate(ELEMENTS):
            r, c = i // cols_per_row, i % cols_per_row
            color = self.CAT_COLORS.get(el["cat"], "#555")
            b = tk.Button(gf, text=f"{el['sym']}\n{el['n']}",
                          font=("Consolas", 7, "bold"), bg=color, fg="#fff",
                          relief="raised", bd=1, width=4, height=3, cursor="hand2",
                          command=lambda e=el: self._show(e))
            b.grid(row=r, column=c, padx=1, pady=1)
            self.btns[el["n"]] = b

        # Right: detail panel
        right = tk.Frame(main, bg="#1a1a1a", width=240)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)
        tk.Label(right, text="ELEMENT DETAILS", font=("Consolas", 10, "bold"),
                 bg="#1a1a1a", fg="#ff6b35").pack(pady=8)
        self.detail = scrolledtext.ScrolledText(right, font=("Consolas", 9),
                                                bg="#0f0f0f", fg="#fff", relief="flat",
                                                padx=8, pady=8, state="disabled")
        self.detail.pack(fill="both", expand=True, padx=6, pady=6)
        self._welcome()

    def _welcome(self):
        self.detail.configure(state="normal")
        self.detail.delete("1.0", "end")
        self.detail.insert(
            "1.0", "⚛️  WELCOME!\n\nClick any element\ntile to see its\ndetailed info.\n\nSearch by symbol,\nname, or number.\n\nFilter by category\nusing the buttons.")
        self.detail.configure(state="disabled")

    def _show(self, el):
        fact = _ELEM_FACTS.get(el["n"], "An important chemical element.")
        state_icon = {"Gas": "💨", "Liquid": "💧",
                      "Solid": "🪨"}.get(el["state"], "🪨")
        txt = (f"╔══════════════╗\n"
               f"║  {el['sym']:^12}  ║\n"
               f"║  {el['name'][:12]:^12}  ║\n"
               f"╚══════════════╝\n\n"
               f"▪ NUMBER : {el['n']}\n"
               f"▪ SYMBOL : {el['sym']}\n"
               f"▪ MASS   : {el['mass']} u\n"
               f"▪ STATE  : {state_icon} {el['state']}\n"
               f"▪ CAT    : {el['cat'].replace('_', ' ').title()}\n\n"
               f"FACT:\n{fact}")
        self.detail.configure(state="normal")
        self.detail.delete("1.0", "end")
        self.detail.insert("1.0", txt)
        self.detail.configure(state="disabled")

    def _search(self):
        q = self.sv.get().lower().strip()
        for el in ELEMENTS:
            b = self.btns.get(el["n"])
            if not b:
                continue
            match = (q in el["sym"].lower()
                     or q in el["name"].lower() or q in str(el["n"]))
            b.configure(relief="sunken" if (q and match) else "raised")

    def _filter(self, cat):
        for el in ELEMENTS:
            b = self.btns.get(el["n"])
            if not b:
                continue
            if cat == "all" or el["cat"] == cat:
                b.grid()
            else:
                b.grid_remove()


# ══════════════════════════════════════════════════════════════════════════════
#  APP 4 — PHONEBOOK
# ══════════════════════════════════════════════════════════════════════════════
class PhonebookApp:
    def __init__(self, frame):
        self.frame = frame
        self.contacts = []
        self.filtered = []
        self.cur = None
        self.entries = {}
        self.search_var = tk.StringVar()
        self.total_var = tk.StringVar(value="0")
        self.vis_var = tk.StringVar(value="0")
        P = {"bg": "#1B1D2B", "bg2": "#232638", "panel": "#181A26", "card": "#2A2D41",
             "card2": "#32364D", "fg": "#EEF2FF", "sec": "#A8B0D6", "mt": "#7F88B4",
             "acc": "#86E1FC", "acc2": "#CBA6F7", "btn": "#7DC4E4", "btnH": "#99D6F7",
             "btnFg": "#10131E", "ok": "#8BD5CA", "err": "#F28FAD"}
        self.P = P
        frame.configure(bg=P["bg"])

        # Layout
        self.sidebar = tk.Frame(frame, bg=P["panel"], width=260)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        self.main = tk.Frame(frame, bg=P["bg"])
        self.main.pack(side="left", fill="both", expand=True)
        self._build_sidebar()
        self._build_main_area()
        self._refresh()
        self._empty()
        self.search_var.trace_add("write", lambda *_: self._refresh())

    def _build_sidebar(self):
        P = self.P
        hero = tk.Frame(self.sidebar, bg=P["panel"], padx=16, pady=18)
        hero.pack(fill="x")
        tk.Label(hero, text="Contacts", font=("Consolas", 16, "bold"),
                 bg=P["panel"], fg=P["acc"]).pack(anchor="w")
        tk.Label(hero, text="Search, select, manage contacts.",
                 font=("Consolas", 8), bg=P["panel"], fg=P["sec"],
                 wraplength=220, justify="left").pack(anchor="w", pady=(6, 0))

        stat_row = tk.Frame(hero, bg=P["panel"])
        stat_row.pack(fill="x", pady=(14, 0))
        for lbl, var, color in [("Total", self.total_var, P["acc"]),
                                ("Visible", self.vis_var, P["acc2"])]:
            chip = tk.Frame(stat_row, bg=P["card"], padx=10, pady=7)
            chip.pack(side="left", expand=True, fill="x", padx=(0, 6))
            tk.Label(chip, text=lbl, font=("Consolas", 8),
                     bg=P["card"], fg=P["sec"]).pack(anchor="w")
            tk.Label(chip, textvariable=var, font=("Consolas", 14, "bold"),
                     bg=P["card"], fg=color).pack(anchor="w")

        sf = tk.Frame(self.sidebar, bg=P["bg2"], padx=12, pady=12)
        sf.pack(fill="x", padx=12, pady=(4, 8))
        tk.Label(sf, text="Search", font=("Consolas", 8),
                 bg=P["bg2"], fg=P["sec"]).pack(anchor="w")
        se = tk.Entry(sf, textvariable=self.search_var, font=("Consolas", 10),
                      bg=P["card"], fg=P["fg"], insertbackground=P["fg"],
                      bd=0, highlightthickness=1, highlightbackground=P["card"],
                      highlightcolor=P["acc"], relief="flat")
        se.pack(fill="x", ipady=7, pady=(6, 0))

        tk.Label(self.sidebar, text="Saved contacts", font=("Consolas", 10, "bold"),
                 bg=P["panel"], fg=P["fg"]).pack(anchor="w", padx=14, pady=(8, 0))
        lw = tk.Frame(self.sidebar, bg=P["bg2"], padx=8, pady=8)
        lw.pack(fill="both", expand=True, padx=12, pady=8)
        self.listbox = tk.Listbox(lw, bg=P["bg2"], fg=P["fg"],
                                  selectbackground=P["card2"], selectforeground=P["acc"],
                                  bd=0, highlightthickness=0, font=("Consolas", 9),
                                  activestyle="none", relief="flat", height=12)
        self.listbox.pack(side="left", fill="both", expand=True)
        sc = tk.Scrollbar(lw, command=self.listbox.yview)
        sc.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=sc.set)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        tk.Button(self.sidebar, text="+ Add Contact", font=("Consolas", 9, "bold"),
                  bg=P["btn"], fg=P["btnFg"], bd=0, relief="flat", cursor="hand2",
                  command=self._show_add).pack(fill="x", padx=12, pady=(0, 12), ipady=10)

    def _build_main_area(self):
        P = self.P
        top = tk.Frame(self.main, bg=P["bg"], padx=22, pady=18)
        top.pack(fill="x")
        tk.Label(top, text="Modern Phonebook", font=("Consolas", 18, "bold"),
                 bg=P["bg"], fg=P["fg"]).pack(anchor="w")
        tk.Label(top, text="A focused contact manager with a calmer layout.",
                 font=("Consolas", 9), bg=P["bg"], fg=P["sec"]).pack(anchor="w", pady=(4, 0))
        self.host = tk.Frame(self.main, bg=P["bg"], padx=22, pady=4)
        self.host.pack(fill="both", expand=True)

    def _clear(self):
        for w in self.host.winfo_children():
            w.destroy()

    def _refresh(self):
        q = self.search_var.get().strip().lower()
        self.filtered = []
        self.listbox.delete(0, tk.END)
        for i, c in enumerate(self.contacts):
            if q and q not in f"{c.get('Name', '')} {c.get('Phone', '')}".lower():
                continue
            self.filtered.append(i)
            self.listbox.insert(
                tk.END, f"{c.get('Name', '?')}  ·  {c.get('Phone', '')}")
        self.total_var.set(str(len(self.contacts)))
        self.vis_var.set(str(len(self.filtered)))
        if not self.contacts or not self.filtered:
            self._empty()

    def _on_select(self, e):
        sel = self.listbox.curselection()
        if not sel:
            return
        vi = sel[0]
        if vi >= len(self.filtered):
            return
        self.cur = self.filtered[vi]
        self._show_detail(self.cur)

    def _show_detail(self, idx):
        P = self.P
        self._clear()
        d = self.contacts[idx]
        card = tk.Frame(self.host, bg=P["card"], padx=22, pady=20)
        card.pack(fill="both", expand=True)
        top = tk.Frame(card, bg=P["card"])
        top.pack(fill="x")
        av = tk.Canvas(top, width=90, height=90,
                       bg=P["card"], bd=0, highlightthickness=0)
        av.pack(side="left")
        av.create_oval(6, 6, 84, 84, fill=P["bg2"], outline=P["acc"], width=2)
        av.create_text(45, 45, text=(d.get("Name", "?")[0].upper()),
                       font=("Consolas", 28, "bold"), fill=P["acc"])
        hdr = tk.Frame(top, bg=P["card"])
        hdr.pack(side="left", padx=14)
        tk.Label(hdr, text=d.get("Name", "Unnamed"), font=("Consolas", 14, "bold"),
                 bg=P["card"], fg=P["fg"]).pack(anchor="w")
        tk.Label(hdr, text=d.get("Phone", ""), font=("Consolas", 12, "bold"),
                 bg=P["card"], fg=P["btn"]).pack(anchor="w", pady=(4, 0))
        det = tk.Frame(card, bg=P["bg2"], padx=16, pady=14)
        det.pack(fill="x", pady=14)
        for lbl, key in [("Age", "Age"), ("DOB", "DOB"), ("Address", "Address")]:
            row = tk.Frame(det, bg=P["bg2"])
            row.pack(fill="x", pady=5)
            tk.Label(row, text=lbl, font=("Consolas", 8), fg=P["sec"],
                     bg=P["bg2"], width=9, anchor="w").pack(side="left")
            tk.Label(row, text=d.get(key, "Not provided"), font=("Consolas", 9, "bold"),
                     fg=P["fg"], bg=P["bg2"]).pack(side="left")

    def _empty(self):
        P = self.P
        self._clear()
        panel = tk.Frame(self.host, bg=P["card"], padx=24, pady=24)
        panel.pack(fill="both", expand=True)
        tk.Label(panel, text="📖", font=("Consolas", 42),
                 bg=P["card"]).pack(pady=(8, 4))
        tk.Label(panel, text="No contact selected", font=("Consolas", 12, "bold"),
                 bg=P["card"], fg=P["fg"]).pack()
        tk.Label(panel, text="Add a contact or click a name from the list.",
                 font=("Consolas", 9), bg=P["card"], fg=P["sec"]).pack(pady=(6, 16))
        tk.Button(panel, text="Create Contact", font=("Consolas", 9, "bold"),
                  bg=P["btn"], fg=P["btnFg"], bd=0, relief="flat", cursor="hand2",
                  command=self._show_add).pack(ipady=9, ipadx=16)

    def _show_add(self):
        P = self.P
        self._clear()
        self.entries = {}
        card = tk.Frame(self.host, bg=P["card"], padx=22, pady=18)
        card.pack(fill="both", expand=True)
        tk.Label(card, text="Create Contact", font=("Consolas", 13, "bold"),
                 bg=P["card"], fg=P["fg"]).pack(anchor="w")
        tk.Label(card, text="Fill in details below.", font=("Consolas", 9),
                 bg=P["card"], fg=P["sec"]).pack(anchor="w", pady=(4, 12))
        form = tk.Frame(card, bg=P["card"])
        form.pack(fill="x")
        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=1)
        for row, col, lbl, ph, span in [
            (0, 0, "Name", "Full name…", 2), (1, 0, "Phone", "Phone number…", 2),
            (2, 0, "Age", "Age…", 1), (2, 1, "DOB", "DD-MM-YYYY", 1),
                (3, 0, "Address", "Address…", 2)]:
            wrap = tk.Frame(form, bg=P["card"])
            wrap.grid(row=row, column=col, columnspan=span,
                      sticky="nsew", padx=6, pady=5)
            tk.Label(wrap, text=lbl, font=("Consolas", 8),
                     bg=P["card"], fg=P["sec"]).pack(anchor="w")
            e = tk.Entry(wrap, font=("Consolas", 10), bg=P["bg2"], fg=P["fg"],
                         insertbackground=P["fg"], bd=0,
                         highlightthickness=1, highlightbackground=P["bg2"],
                         highlightcolor=P["acc"], relief="flat")
            e.pack(fill="x", ipady=7)
            self.entries[lbl] = e
        acts = tk.Frame(card, bg=P["card"])
        acts.pack(fill="x", pady=(14, 0))

        def save():
            d = {k: e.get().strip() for k, e in self.entries.items()}
            if not d.get("Name") or not d.get("Phone"):
                tk.Label(card, text="Name & Phone are required!",
                         font=("Consolas", 8), bg=P["card"], fg=P["err"]).pack()
                return
            self.contacts.append(d)
            self.cur = len(self.contacts)-1
            self._refresh()
            self._show_detail(self.cur)
        tk.Button(acts, text="Save Contact", font=("Consolas", 9, "bold"),
                  bg=P["btn"], fg=P["btnFg"], bd=0, relief="flat",
                  cursor="hand2", command=save).pack(side="left", fill="x", expand=True, ipady=10)


# ══════════════════════════════════════════════════════════════════════════════
#  APP 5 — QUIZ GAME
# ══════════════════════════════════════════════════════════════════════════════
QUIZ = [
    {"q": "Which was the first search engine on the internet?",
     "opts": ["Google", "Archie", "Wais", "Altavista"], "ans": 1},
    {"q": "Which browser was invented in 1990?",
     "opts": ["Internet Explorer", "Mosaic", "Mozilla", "Nexus"], "ans": 3},
    {"q": "The first computer virus is known as?",
     "opts": ["Rabbit", "Creeper virus", "Elk Cloner", "SCA virus"], "ans": 1},
    {"q": "Firewall in a computer is used for?",
     "opts": ["Security", "Data Transmission", "Monitoring", "Authentication"], "ans": 0},
    {"q": "Which one is NOT a database software?",
     "opts": ["MySQL", "Oracle", "COBOL", "Sybase"], "ans": 2},
]


class QuizApp:
    def __init__(self, frame):
        self.frame = frame
        self.score = 0
        self.qi = 0
        self.sel = tk.IntVar(value=-1)
        P = {"bg": "#151827", "surf": "#1D2133", "panel": "#242A40", "ps": "#2D3450",
             "acc": "#86E1FC", "acc2": "#CBA6F7", "acc3": "#8BD5CA", "fg": "#EEF2FF",
             "mt": "#A3ACD6", "btn": "#7DC4E4", "btnH": "#99D6F7", "ba": "#323A58",
             "ok": "#A6E3A1", "err": "#F38BA8", "warn": "#F9E2AF"}
        self.P = P
        frame.configure(bg=P["bg"])
        self.score_var = tk.StringVar(value="0")
        self.q_var = tk.StringVar(value=f"0 / {len(QUIZ)}")
        self.status = tk.StringVar(value="Ready to begin")

        # Sidebar
        sb = tk.Frame(frame, bg=P["surf"], width=240)
        sb.pack(side="left", fill="y")
        sb.pack_propagate(False)
        hdr = tk.Frame(sb, bg=P["surf"], padx=16, pady=18)
        hdr.pack(fill="x")
        tk.Label(hdr, text="Knowledge Arena", font=("Consolas", 12, "bold"),
                 bg=P["surf"], fg=P["acc"], wraplength=200, justify="left").pack(anchor="w")
        tk.Label(hdr, text="Tech trivia · 5 questions · +5 pts each",
                 font=("Consolas", 8), bg=P["surf"], fg=P["mt"],
                 wraplength=200, justify="left").pack(anchor="w", pady=(8, 0))
        for lbl, var, color in [("Score", self.score_var, P["acc2"]),
                                ("Question", self.q_var, P["acc3"])]:
            tile = tk.Frame(sb, bg=P["panel"], padx=12, pady=10)
            tile.pack(fill="x", padx=12, pady=(0, 6))
            tk.Label(tile, text=lbl, font=("Consolas", 8),
                     bg=P["panel"], fg=P["mt"]).pack(anchor="w")
            tk.Label(tile, textvariable=var, font=("Consolas", 15, "bold"),
                     bg=P["panel"], fg=color).pack(anchor="w", pady=(3, 0))
        sp = tk.Frame(sb, bg=P["panel"], padx=12, pady=12)
        sp.pack(fill="x", padx=12, pady=(0, 12))
        tk.Label(sp, text="Status", font=("Consolas", 8),
                 bg=P["panel"], fg=P["mt"]).pack(anchor="w")
        tk.Label(sp, textvariable=self.status, font=("Consolas", 9, "bold"),
                 bg=P["panel"], fg=P["fg"], wraplength=200, justify="left").pack(anchor="w", pady=(4, 0))
        ctrl = tk.Frame(sb, bg=P["surf"], padx=12)
        ctrl.pack(fill="x")
        tk.Button(ctrl, text="▶  Start Quiz", font=("Consolas", 9, "bold"),
                  bg=P["btn"], fg="#10131E", bd=0, relief="flat",
                  cursor="hand2", command=self.start).pack(fill="x", ipady=10, pady=(0, 8))
        tk.Button(ctrl, text="↺  Reset", font=("Consolas", 9),
                  bg=P["ba"], fg=P["fg"], bd=0, relief="flat",
                  cursor="hand2", command=self.reset).pack(fill="x", ipady=10)

        # Content
        self.content = tk.Frame(frame, bg=P["bg"])
        self.content.pack(side="left", fill="both", expand=True)
        self.show_intro()

        frame.bind_all("<Return>", lambda e: self._submit())

    def _clear(self):
        for w in self.content.winfo_children():
            w.destroy()

    def show_intro(self):
        self._clear()
        P = self.P
        card = tk.Frame(self.content, bg=P["panel"], padx=28, pady=28)
        card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9)
        badge = tk.Frame(card, bg=P["ps"], padx=12, pady=8)
        badge.pack(anchor="w")
        tk.Label(badge, text="ARCADE MODE", font=("Consolas", 8),
                 bg=P["ps"], fg=P["acc"]).pack()
        tk.Label(card, text="A clean quiz with clear feedback.",
                 font=("Consolas", 13, "bold"), bg=P["panel"], fg=P["fg"],
                 wraplength=500, justify="left").pack(anchor="w", pady=(14, 6))
        tk.Label(card, text=f"Questions: {len(QUIZ)}  ·  +5 per correct  ·  Max: {len(QUIZ)*5}",
                 font=("Consolas", 9), bg=P["panel"], fg=P["mt"]).pack(anchor="w", pady=(0, 18))
        tk.Button(card, text="Start Quiz", font=("Consolas", 10, "bold"),
                  bg=P["btn"], fg="#10131E", bd=0, relief="flat",
                  cursor="hand2", command=self.start).pack(anchor="w", ipady=10, ipadx=16)

    def start(self):
        self.score = 0
        self.qi = 0
        self.sel.set(-1)
        self.score_var.set("0")
        self.status.set("Question 1 — choose wisely.")
        self.show_question()

    def show_question(self):
        self._clear()
        P = self.P
        if self.qi >= len(QUIZ):
            self.show_result()
            return
        q = QUIZ[self.qi]
        self.q_var.set(f"{self.qi+1} / {len(QUIZ)}")
        card = tk.Frame(self.content, bg=P["panel"], padx=24, pady=24)
        card.place(relx=0.5, rely=0.5, anchor="center",
                   relwidth=0.92, relheight=0.9)
        tk.Label(card, text=f"Question {self.qi+1}", font=("Consolas", 9),
                 bg=P["panel"], fg=P["acc"]).pack(anchor="w")
        tk.Label(card, text=q["q"], font=("Consolas", 12, "bold"),
                 bg=P["panel"], fg=P["fg"], wraplength=580, justify="left").pack(anchor="w", pady=(8, 18))
        self.sel.set(-1)
        opts_frame = tk.Frame(card, bg=P["panel"])
        opts_frame.pack(fill="x")
        opts_frame.columnconfigure(0, weight=1)
        opts_frame.columnconfigure(1, weight=1)
        for i, opt in enumerate(q["opts"]):
            r, c = i // 2, i % 2
            of = tk.Frame(opts_frame, bg=P["ps"],
                          padx=12, pady=12, cursor="hand2")
            of.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)
            rb = tk.Radiobutton(of, text=opt, variable=self.sel, value=i,
                                font=("Consolas", 9, "bold"), bg=P["ps"], fg=P["fg"],
                                selectcolor=P["ps"], activebackground=P["ps"],
                                activeforeground=P["fg"], bd=0, anchor="w",
                                wraplength=240, highlightthickness=0)
            rb.pack(fill="x")
            of.bind("<Button-1>", lambda e, v=i: self.sel.set(v))
        btns = tk.Frame(card, bg=P["panel"], pady=16)
        btns.pack(fill="x")
        tk.Button(btns, text="Submit Answer", font=("Consolas", 10, "bold"),
                  bg=P["btn"], fg="#10131E", bd=0, relief="flat",
                  cursor="hand2", command=self._submit).pack(side="left", ipady=10, ipadx=14)
        tk.Button(btns, text="Back to Menu", font=("Consolas", 9),
                  bg=P["ba"], fg=P["fg"], bd=0, relief="flat",
                  cursor="hand2", command=self.show_intro).pack(side="left", padx=(10, 0), ipady=10, ipadx=14)

    def _submit(self):
        if self.sel.get() == -1:
            self.status.set("Pick an answer first!")
            return
        correct = QUIZ[self.qi]["ans"]
        if self.sel.get() == correct:
            self.score += 5
            self.status.set("Correct! +5 pts")
        else:
            self.status.set(f"Wrong. Correct: option {correct+1}")
        self.qi += 1
        self.score_var.set(str(self.score))
        self.frame.after(280, self.show_question)

    def show_result(self):
        self._clear()
        P = self.P
        mx = len(QUIZ) * 5
        acc = self.score / mx * 100 if mx else 0
        card = tk.Frame(self.content, bg=P["panel"], padx=28, pady=28)
        card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9)
        tk.Label(card, text="Scoreboard", font=("Consolas", 12, "bold"),
                 bg=P["panel"], fg=P["acc2"]).pack(anchor="w")
        tk.Label(card, text=f"{self.score} / {mx}", font=("Consolas", 24, "bold"),
                 bg=P["panel"], fg=P["fg"]).pack(anchor="w", pady=(8, 0))
        tk.Label(card, text=f"Accuracy: {acc:.0f}%", font=("Consolas", 10),
                 bg=P["panel"], fg=P["mt"]).pack(anchor="w", pady=(4, 14))
        verdict = ("Elite run. You owned the arena." if self.score >= 20
                   else "Strong session. Keep sharpening." if self.score >= 10
                   else "Warm-up tier. Re-enter and try again.")
        vcolor = P["ok"] if self.score >= 20 else P["warn"] if self.score >= 10 else P["err"]
        vf = tk.Frame(card, bg=P["ps"], padx=14, pady=14)
        vf.pack(fill="x", pady=(0, 18))
        tk.Label(vf, text=verdict, font=("Consolas", 10, "bold"),
                 bg=P["ps"], fg=vcolor, wraplength=500).pack(anchor="w")
        progress = ttk.Progressbar(
            card, orient="horizontal", mode="determinate", maximum=mx)
        progress.pack(fill="x", pady=(0, 16))
        progress["value"] = self.score
        acts = tk.Frame(card, bg=P["panel"])
        acts.pack(fill="x")
        tk.Button(acts, text="Play Again", font=("Consolas", 9, "bold"),
                  bg=P["btn"], fg="#10131E", bd=0, relief="flat",
                  cursor="hand2", command=self.start).pack(side="left", ipady=10, ipadx=14)
        tk.Button(acts, text="Main Menu", font=("Consolas", 9),
                  bg=P["ba"], fg=P["fg"], bd=0, relief="flat",
                  cursor="hand2", command=self.show_intro).pack(side="left", padx=(10, 0), ipady=10, ipadx=14)
        self.q_var.set(f"{len(QUIZ)} / {len(QUIZ)}")
        self.status.set("Session complete.")

    def reset(self):
        self.score = 0
        self.qi = 0
        self.sel.set(-1)
        self.score_var.set("0")
        self.q_var.set(f"0 / {len(QUIZ)}")
        self.status.set("Session reset.")
        self.show_intro()


# ══════════════════════════════════════════════════════════════════════════════
#  APP 6 — BILLING DESK
# ══════════════════════════════════════════════════════════════════════════════
PRICES = {
    "Cosmetics": {"Body Soap": 10, "Hair Cream": 25, "Hair Spray": 50, "Body Spray": 50},
    "Grocery": {"Sugar": 100, "Tea": 15, "Coffee": 50, "Rice": 150, "Wheat": 160},
    "Beverages": {"Pepsi": 30, "Sprite": 35, "Coke": 30, "Mojitos": 25, "Thumbs Up": 35},
}


class BillingApp:
    def __init__(self, frame):
        self.frame = frame
        self.qty_vars = {}
        self.total_vars = {k: tk.StringVar(value="Rs 0")
                           for k in ["Cosmetics", "Grocery", "Beverages", "Grand"]}
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.id_var = tk.StringVar()
        self.status_var = tk.StringVar(
            value="Fill details, set quantities, then generate invoice.")
        C = {"bg": "#fff9f0", "hdr": "#362c2a", "card": "#f7efdf", "prod": "#fff6ea",
             "item": "#fff1db", "act": "#f7efdf", "right": "#f1e6d6", "inv": "#fff7e9",
             "tot": "#fff3df", "acc": "#6f3f2e", "h": "#ffe9c8", "s": "#e5cfa7",
             "fg": "#463533", "mt": "#5b4a45", "pr": "#6c4e3f", "il": "#5f4a43",
             "btn": "#d7c4a6", "inv_bg": "#fffef9", "inv_fg": "#4f423d"}
        self.C = C
        frame.configure(bg=C["bg"])

        hdr = tk.Frame(frame, bg=C["hdr"], padx=18, pady=12)
        hdr.pack(fill="x", padx=14, pady=(14, 8))
        tk.Label(hdr, text="ANTEIKU SMART BILLING DESK",
                 font=("Georgia", 15, "bold"), fg=C["h"], bg=C["hdr"]).pack(anchor="w")
        tk.Label(hdr, text="Boutique Checkout Interface",
                 font=("Trebuchet MS", 9), fg=C["s"], bg=C["hdr"]).pack(anchor="w")

        body = tk.Frame(frame, bg=C["bg"])
        body.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        left = tk.Frame(body, bg=C["bg"])
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        right = tk.Frame(body, bg=C["right"], padx=12, pady=12)
        right.pack(side="right", fill="y", padx=(8, 0))

        # Customer card
        cf = tk.Frame(left, bg=C["card"], padx=12, pady=10)
        cf.pack(fill="x")
        tk.Label(cf, text="Customer Details", font=("Georgia", 11, "bold"),
                 fg=C["fg"], bg=C["card"]).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 6))
        for col, (lbl, var) in enumerate([(("Name", self.name_var), ("Phone", self.phone_var))]):
            for c2, (l2, v2) in enumerate(lbl if isinstance(lbl, list) else [(lbl, var)]):
                pass
        # Row layout
        for c, (lbl, var, w) in enumerate([("Name", self.name_var, 22), ("Phone", self.phone_var, 14)]):
            tk.Label(cf, text=lbl, font=("Trebuchet MS", 9), fg=C["mt"], bg=C["card"]).grid(
                row=1, column=c*2, sticky="w", padx=(0 if c == 0 else 12, 0))
            tk.Entry(cf, textvariable=var, font=("Trebuchet MS", 10), width=w).grid(
                row=1, column=c*2+1, padx=(6, 0))
        tk.Label(cf, text="Customer ID", font=("Trebuchet MS", 9), fg=C["mt"], bg=C["card"]).grid(
            row=2, column=0, sticky="w", pady=(6, 0))
        tk.Entry(cf, textvariable=self.id_var, font=("Trebuchet MS", 10), width=12).grid(
            row=2, column=1, sticky="w", padx=(6, 0), pady=(6, 0))

        # Products
        pf = tk.Frame(left, bg=C["prod"], padx=12, pady=10)
        pf.pack(fill="both", expand=True, pady=(10, 0))
        tk.Label(pf, text="Product Quantities", font=("Georgia", 11, "bold"),
                 fg=C["fg"], bg=C["prod"]).pack(anchor="w", pady=(0, 8))
        cats = tk.Frame(pf, bg=C["prod"])
        cats.pack(fill="both", expand=True)
        for col, (cat, items) in enumerate(PRICES.items()):
            card = tk.Frame(cats, bg=C["item"], padx=8, pady=8)
            card.grid(row=0, column=col, sticky="nsew", padx=4)
            cats.grid_columnconfigure(col, weight=1)
            tk.Label(card, text=cat, font=("Trebuchet MS", 10, "bold"),
                     fg=C["pr"], bg=C["item"]).pack(anchor="w", pady=(0, 6))
            for item, price in items.items():
                row = tk.Frame(card, bg=C["item"])
                row.pack(fill="x", pady=1)
                tk.Label(row, text=f"{item} (Rs {price})", font=("Trebuchet MS", 8),
                         fg=C["il"], bg=C["item"], width=18, anchor="w").pack(side="left")
                qty = tk.IntVar(value=0)
                sp = tk.Spinbox(row, from_=0, to=99, textvariable=qty, width=4,
                                command=self.update_totals, font=("Trebuchet MS", 9))
                sp.pack(side="right")
                sp.bind("<KeyRelease>", lambda e: self.update_totals())
                self.qty_vars[(cat, item)] = qty

        # Actions
        af = tk.Frame(left, bg=C["act"], padx=12, pady=10)
        af.pack(fill="x", pady=(10, 0))
        tk.Button(af, text="Generate Invoice", font=("Trebuchet MS", 10, "bold"),
                  bg=C["acc"], fg="#fff2de", relief="flat", padx=8, pady=5, cursor="hand2",
                  command=self.gen_invoice).pack(side="left")
        tk.Button(af, text="Clear All", font=("Trebuchet MS", 10),
                  bg=C["btn"], fg=C["fg"], relief="flat", padx=8, pady=5, cursor="hand2",
                  command=self.clear_all).pack(side="left", padx=(8, 0))
        tk.Label(af, textvariable=self.status_var, font=("Trebuchet MS", 8),
                 fg="#5e4e48", bg=C["act"], wraplength=380).pack(side="left", padx=(10, 0))

        # Totals
        tf = tk.Frame(right, bg=C["tot"], padx=10, pady=10)
        tf.pack(fill="x")
        tk.Label(tf, text="Totals", font=("Georgia", 11, "bold"),
                 fg="#4a362e", bg=C["tot"]).pack(anchor="w", pady=(0, 8))
        for lbl, key in [("Cosmetics", "Cosmetics"), ("Grocery", "Grocery"),
                         ("Beverages", "Beverages"), ("Grand Total", "Grand")]:
            row = tk.Frame(tf, bg=C["tot"])
            row.pack(fill="x", pady=2)
            tk.Label(row, text=lbl, font=("Trebuchet MS", 9), fg="#604841",
                     bg=C["tot"]).pack(side="left")
            tk.Label(row, textvariable=self.total_vars[key],
                     font=("Trebuchet MS", 9, "bold"), fg=C["acc"],
                     bg=C["tot"]).pack(side="right")

        # Invoice preview
        iv = tk.Frame(right, bg=C["inv"], padx=10, pady=10)
        iv.pack(fill="both", expand=True, pady=(10, 0))
        tk.Label(iv, text="Invoice Preview", font=("Georgia", 10, "bold"),
                 fg="#4a362e", bg=C["inv"]).pack(anchor="w", pady=(0, 6))
        self.inv_box = tk.Text(iv, width=32, height=20, bg=C["inv_bg"],
                               fg=C["inv_fg"], relief="flat", font=("Consolas", 8))
        self.inv_box.pack(fill="both", expand=True)
        self.inv_box.insert(
            "end", "ANTEIKU Billing\n──────────────\nInvoice will appear here.")
        self.inv_box.configure(state="disabled")

    def update_totals(self):
        totals = {"Cosmetics": 0, "Grocery": 0, "Beverages": 0}
        for (cat, item), var in self.qty_vars.items():
            try:
                q = max(0, int(var.get()))
            except:
                q = 0
            totals[cat] += PRICES[cat][item] * q
        grand = sum(totals.values())
        for k, v in totals.items():
            self.total_vars[k].set(f"Rs {v}")
        self.total_vars["Grand"].set(f"Rs {grand}")
        return totals["Cosmetics"], totals["Grocery"], totals["Beverages"], grand

    def gen_invoice(self):
        name = self.name_var.get().strip() or "Walk-in Customer"
        phone = self.phone_var.get().strip() or "N/A"
        cid = self.id_var.get().strip() or "N/A"
        ct, gt, bt, grand = self.update_totals()
        lines = ["ANTEIKU SMART BILLING", "──────────────────",
                 f"Customer : {name}", f"Phone    : {phone}",
                 f"ID       : {cid}", "──────────────────", "ITEMS"]
        any_items = False
        for cat, items in PRICES.items():
            lines.append(f"[{cat}]")
            for item, price in items.items():
                try:
                    q = max(0, int(self.qty_vars[(cat, item)].get()))
                except:
                    q = 0
                if q > 0:
                    any_items = True
                    lines.append(f"{item[:13]:13} x{q:<2} Rs {price*q}")
        if not any_items:
            lines.append("No products selected")
        lines += ["──────────────────",
                  f"Cosmetics : Rs {ct}", f"Grocery   : Rs {gt}",
                  f"Beverages : Rs {bt}", f"Grand     : Rs {grand}",
                  "──────────────────", "Thank you!"]
        self.inv_box.configure(state="normal")
        self.inv_box.delete("1.0", "end")
        self.inv_box.insert("end", "\n".join(lines))
        self.inv_box.configure(state="disabled")
        self.status_var.set("Invoice generated successfully.")

    def clear_all(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.id_var.set("")
        for var in self.qty_vars.values():
            var.set(0)
        self.update_totals()
        self.inv_box.configure(state="normal")
        self.inv_box.delete("1.0", "end")
        self.inv_box.insert(
            "end", "ANTEIKU Billing\n──────────────\nInvoice cleared.")
        self.inv_box.configure(state="disabled")
        self.status_var.set("Reset complete.")


# ══════════════════════════════════════════════════════════════════════════════
#  APP 7 — CASINO
# ══════════════════════════════════════════════════════════════════════════════
class CasinoApp:
    def __init__(self, frame):
        self.frame = frame
        self.player = ""
        self.balance = 0
        self.started = False
        C = {"bg": "#0f0f1e", "hdr": "#8338ec", "acc": "#ffbe0b", "ok": "#06ffa5",
             "err": "#ff006e", "fg": "#ffffff", "inp": "#1a1a2e"}
        self.C = C
        frame.configure(bg=C["bg"])

        hdr = tk.Frame(frame, bg=C["hdr"])
        hdr.pack(fill="x")
        tk.Label(hdr, text="🎰  LUCKY CASINO  🎰",
                 font=("Consolas", 18, "bold"), bg=C["hdr"], fg=C["fg"]).pack(pady=16)

        self.content = tk.Frame(frame, bg=C["bg"])
        self.content.pack(fill="both", expand=True, padx=20, pady=20)
        self.show_login()

    def _clear(self):
        for w in self.content.winfo_children():
            w.destroy()

    def show_login(self):
        self._clear()
        C = self.C
        tk.Label(self.content, text="Welcome to Lucky Casino",
                 font=("Consolas", 14, "bold"), bg=C["bg"], fg=C["acc"]).pack(pady=16)
        rules = tk.Frame(self.content, bg=C["bg"])
        rules.pack(pady=8)
        for line in ["🔹 Guess a number from 1 to 10",
                     "🔹 Correct guess wins 10× your bet",
                     "🔹 Wrong guess loses your bet",
                     "🔹 Play until balance hits $0"]:
            tk.Label(rules, text=line, font=("Consolas", 10),
                     bg=C["bg"], fg=C["fg"], anchor="w").pack(anchor="w", pady=2)
        tk.Label(self.content, text="👤  Player Name:", font=("Consolas", 10),
                 bg=C["bg"], fg=C["fg"]).pack(anchor="w", pady=(14, 0))
        self.name_e = tk.Entry(self.content, font=("Consolas", 11),
                               bg=C["inp"], fg=C["fg"], insertbackground=C["acc"],
                               relief="flat")
        self.name_e.pack(fill="x", ipady=8, pady=4)
        tk.Label(self.content, text="💰  Deposit Amount ($):", font=("Consolas", 10),
                 bg=C["bg"], fg=C["fg"]).pack(anchor="w", pady=(8, 0))
        self.dep_e = tk.Entry(self.content, font=("Consolas", 11),
                              bg=C["inp"], fg=C["fg"], insertbackground=C["acc"],
                              relief="flat")
        self.dep_e.pack(fill="x", ipady=8, pady=4)
        tk.Button(self.content, text="🚀  START PLAYING",
                  font=("Consolas", 11, "bold"), bg=C["err"], fg=C["fg"],
                  relief="flat", pady=10, cursor="hand2",
                  command=self.start_game).pack(fill="x", pady=20)

    def start_game(self):
        C = self.C
        name = self.name_e.get().strip()
        if not name:
            messagebox.showwarning("Missing", "Enter your name!")
            return
        try:
            bal = int(self.dep_e.get())
            if bal <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid deposit > 0")
            return
        self.player = name
        self.balance = bal
        self.started = True
        self.show_game()

    def show_game(self):
        self._clear()
        C = self.C
        info = tk.Frame(self.content, bg=C["hdr"])
        info.pack(fill="x", ipady=8)
        tk.Label(info, text=f"👤  {self.player}", font=("Consolas", 10, "bold"),
                 bg=C["hdr"], fg=C["fg"]).pack(side="left", padx=10)
        self.bal_lbl = tk.Label(info, text=f"💰  Balance: ${self.balance}",
                                font=("Consolas", 10, "bold"), bg=C["hdr"], fg=C["ok"])
        self.bal_lbl.pack(side="right", padx=10)

        tk.Label(self.content, text="💵  Bet Amount ($):", font=("Consolas", 10),
                 bg=C["bg"], fg=C["fg"]).pack(anchor="w", pady=(16, 0))
        self.bet_e = tk.Entry(self.content, font=("Consolas", 11),
                              bg=C["inp"], fg=C["fg"], insertbackground=C["acc"],
                              relief="flat")
        self.bet_e.pack(fill="x", ipady=7, pady=4)
        self.bet_e.insert(0, "10")

        tk.Label(self.content, text="🎲  Pick a Number (1–10):", font=("Consolas", 10),
                 bg=C["bg"], fg=C["fg"]).pack(anchor="w", pady=(12, 0))
        self.pick = tk.IntVar(value=1)
        btn_frame = tk.Frame(self.content, bg=C["bg"])
        btn_frame.pack(pady=8)
        for i in range(1, 11):
            tk.Radiobutton(btn_frame, text=str(i), variable=self.pick, value=i,
                           font=("Consolas", 10, "bold"), bg=C["bg"], fg=C["fg"],
                           selectcolor=C["err"], activebackground=C["hdr"],
                           activeforeground=C["fg"]).grid(row=(i-1)//5, column=(i-1) % 5,
                                                          padx=4, pady=4)

        tk.Button(self.content, text="🎯  SPIN & CLAIM",
                  font=("Consolas", 11, "bold"), bg=C["err"], fg=C["fg"],
                  relief="flat", pady=10, cursor="hand2",
                  command=self.play_round).pack(fill="x", pady=14)

        self.result_lbl = tk.Label(self.content, text="", font=("Consolas", 11, "bold"),
                                   bg=C["bg"], fg=C["ok"], wraplength=400)
        self.result_lbl.pack(pady=6)
        tk.Button(self.content, text="❌  QUIT",
                  font=("Consolas", 10), bg=C["err"], fg=C["fg"],
                  relief="flat", pady=8, cursor="hand2",
                  command=self.quit_game).pack(fill="x")

    def play_round(self):
        C = self.C
        try:
            bet = int(self.bet_e.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid bet!")
            return
        if bet <= 0 or bet > self.balance:
            messagebox.showwarning(
                "Invalid Bet", f"Bet must be $1 – ${self.balance}")
            return
        guess = self.pick.get()
        lucky = random.randint(1, 10)
        if guess == lucky:
            win = bet * 10
            self.balance += win
            self.result_lbl.configure(
                text=f"🎉 FANTASTIC!\nGuessed {guess} → Won ${win}!\nLucky: {lucky}", fg=C["ok"])
        else:
            self.balance -= bet
            self.result_lbl.configure(
                text=f"😢 UNLUCKY\nGuessed {guess} but it was {lucky}.\nLost ${bet}", fg=C["err"])
        self.bal_lbl.configure(text=f"💰  Balance: ${self.balance}")
        if self.balance <= 0:
            messagebox.showinfo(
                "Game Over", f"Balance hit $0!\nGood game, {self.player}!")
            self.show_login()

    def quit_game(self):
        messagebox.showinfo(
            "Bye!", f"Thanks, {self.player}!\nFinal: ${self.balance}")
        self.show_login()


# ══════════════════════════════════════════════════════════════════════════════
#  APP 8 — GUESS GAME
# ══════════════════════════════════════════════════════════════════════════════
class GuessApp:
    def __init__(self, frame):
        self.frame = frame
        self.secret = random.randint(1, 10)
        self.lives = 3
        self.count = 0
        self.over = False
        self.history = []
        C = {"bg": "#0a0e27", "card": "#1a1f3a", "acc": "#00d4ff", "ok": "#00ff88",
             "warn": "#ffaa00", "err": "#ff3366", "fg": "#ffffff", "inp": "#2a2f4a"}
        self.C = C
        frame.configure(bg=C["bg"])

        tk.Label(frame, text="🎯  MYSTERY NUMBER",
                 font=("Consolas", 16, "bold"), bg=C["bg"], fg=C["acc"]).pack(pady=(18, 4))
        tk.Label(frame, text="Guess the secret number — you have 3 lives",
                 font=("Consolas", 9), bg=C["bg"], fg="#88a0ff").pack(pady=(0, 14))

        card = tk.Frame(frame, bg=C["card"])
        card.pack(fill="both", expand=True, padx=16, pady=4)
        tk.Label(card, text="Pick a number between 1 and 10",
                 font=("Consolas", 10, "bold"), bg=C["card"], fg=C["acc"]).pack(pady=14)

        self.hearts_frame = tk.Frame(card, bg=C["card"])
        self.hearts_frame.pack()
        self._draw_hearts()

        tk.Label(card, text="Your Guess:", font=("Consolas", 10, "bold"),
                 bg=C["card"], fg=C["fg"]).pack(pady=(16, 4))
        self.entry = tk.Entry(card, font=("Consolas", 14, "bold"),
                              bg=C["inp"], fg=C["acc"], insertbackground=C["acc"],
                              relief="flat", justify="center")
        self.entry.pack(fill="x", padx=30, ipady=10, pady=6)
        self.entry.bind("<Return>", lambda e: self.guess())

        self.submit_btn = tk.Button(card, text="🔮  CHECK GUESS",
                                    font=("Consolas", 10, "bold"), bg=C["acc"],
                                    fg=C["bg"], relief="flat", pady=8, cursor="hand2",
                                    command=self.guess)
        self.submit_btn.pack(fill="x", padx=30, pady=10)

        self.feedback = tk.Label(card, text="", font=("Consolas", 10, "bold"),
                                 bg=C["card"], fg=C["warn"], wraplength=340, height=2)
        self.feedback.pack(pady=10)

        tk.Label(card, text="📊  Your Guesses:", font=("Consolas", 9, "bold"),
                 bg=C["card"], fg=C["fg"]).pack(pady=(14, 4))
        self.hist_lbl = tk.Label(card, text="No guesses yet", font=("Consolas", 9),
                                 bg=C["card"], fg="#6a7aaa")
        self.hist_lbl.pack()

        tk.Button(frame, text="🔄  NEW GAME", font=("Consolas", 9, "bold"),
                  bg=C["card"], fg=C["ok"], relief="flat", pady=8, cursor="hand2",
                  command=self.reset).pack(fill="x", padx=16, pady=12)

    def _draw_hearts(self):
        for w in self.hearts_frame.winfo_children():
            w.destroy()
        tk.Label(self.hearts_frame, text="Lives remaining:",
                 font=("Consolas", 8), bg=self.C["card"], fg="#88a0ff").pack()
        hf = tk.Frame(self.hearts_frame, bg=self.C["card"])
        hf.pack(pady=4)
        for _ in range(self.lives):
            tk.Label(hf, text="❤️", font=("Consolas", 16),
                     bg=self.C["card"]).pack(side="left", padx=3)
        tk.Label(self.hearts_frame, text=f"{self.count} / 3 guesses made",
                 font=("Consolas", 8), bg=self.C["card"],
                 fg=self.C["ok"] if self.lives > 1 else self.C["err"]).pack()

    def guess(self):
        if self.over:
            messagebox.showinfo("Game Over", "Start a new game!")
            return
        try:
            g = int(self.entry.get().strip())
            if g < 1 or g > 10:
                messagebox.showwarning("Invalid", "Guess between 1 and 10!")
                return
        except ValueError:
            messagebox.showerror("Invalid", "Enter a number!")
            return
        self.entry.delete(0, tk.END)
        self.count += 1
        self.lives -= 1
        self.history.append(g)
        if g == self.secret:
            self.feedback.configure(
                text=f"🎉 PERFECT! It was {self.secret}!", fg=self.C["ok"])
            self.over = True
            self.submit_btn.configure(state="disabled")
            messagebox.showinfo(
                "Victory!", f"🎯 You got it in {self.count} try(s)!")
        else:
            hint = "⬆️  Too low!" if g < self.secret else "⬇️  Too high!"
            self.feedback.configure(text=hint, fg=self.C["warn"])
            if self.lives <= 0:
                self.feedback.configure(
                    text=f"💔 Game Over! It was {self.secret}", fg=self.C["err"])
                self.over = True
                self.submit_btn.configure(state="disabled")
                messagebox.showinfo("Game Over",
                                    f"😔 Secret was {self.secret}\nGuesses: {', '.join(map(str, self.history))}")
        self._draw_hearts()
        self.hist_lbl.configure(text=" → ".join(
            map(str, self.history)) or "No guesses yet")

    def reset(self):
        self.secret = random.randint(1, 10)
        self.lives = 3
        self.count = 0
        self.over = False
        self.history = []
        self.entry.delete(0, tk.END)
        self.entry.configure(state="normal")
        self.submit_btn.configure(state="normal")
        self.feedback.configure(text="")
        self._draw_hearts()
        self.hist_lbl.configure(text="No guesses yet")


# ══════════════════════════════════════════════════════════════════════════════
#  LAUNCHER SHELL
# ══════════════════════════════════════════════════════════════════════════════
APP_BUILDERS = {
    "atm":       ATMApp,
    "library":   LibraryApp,
    "periodic":  PeriodicApp,
    "phonebook": PhonebookApp,
    "quiz":      QuizApp,
    "billing":   BillingApp,
    "casino":    CasinoApp,
    "guess":     GuessApp,
}


class MiniPyLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("mini_py — Python Mini Projects")
        self.geometry("1240x780")
        self.minsize(1100, 680)
        self.configure(bg=L["bg"])
        self.current_app_id = None
        self.app_instance = None
        self._build_ui()
        self._show_home()

    def _build_ui(self):
        # ── Left sidebar (nav)
        self.sidebar = tk.Frame(self, bg=L["surface"], width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo block
        logo_block = tk.Frame(self.sidebar, bg=L["bg2"], padx=18, pady=22)
        logo_block.pack(fill="x")
        tk.Label(logo_block, text="mini_py", font=("Courier", 17, "bold"),
                 bg=L["bg2"], fg=L["accent"]).pack(anchor="w")
        tk.Label(logo_block, text="Python Mini Projects", font=("Courier", 8),
                 bg=L["bg2"], fg=L["muted"]).pack(anchor="w", pady=(2, 0))

        # Home button
        home_btn = tk.Button(
            self.sidebar, text="  ⌂  Home", font=("Courier", 10, "bold"),
            bg=L["card2"], fg=L["fg"], relief="flat", anchor="w",
            padx=18, pady=12, cursor="hand2", bd=0,
            command=self._show_home)
        home_btn.pack(fill="x")
        self._hover(home_btn, L["card2"], L["border2"])

        # Divider label
        tk.Label(self.sidebar, text="  APPS", font=("Courier", 8),
                 bg=L["surface"], fg=L["muted2"]).pack(anchor="w", pady=(14, 4), padx=18)

        # App nav buttons
        self.nav_buttons = {}
        for meta in APP_META:
            btn = tk.Button(
                self.sidebar,
                text=f"  {meta['icon']}  {meta['name']}",
                font=("Courier", 9),
                bg=L["surface"], fg=L["muted"],
                relief="flat", anchor="w",
                padx=18, pady=10, cursor="hand2", bd=0,
                command=lambda m=meta: self._launch(m["id"]))
            btn.pack(fill="x")
            self._hover(btn, L["surface"], L["card"])
            self.nav_buttons[meta["id"]] = btn

        # Footer
        tk.Frame(self.sidebar, bg=L["border"], height=1).pack(
            fill="x", side="bottom", pady=0)
        tk.Label(self.sidebar, text="  tkinter · Python 3",
                 font=("Courier", 8), bg=L["surface"], fg=L["muted2"]).pack(
                     side="bottom", anchor="w", pady=10, padx=18)

        # ── Top bar
        self.topbar = tk.Frame(self, bg=L["bg2"], height=52)
        self.topbar.pack(side="top", fill="x")
        self.topbar.pack_propagate(False)

        self.breadcrumb = tk.Label(
            self.topbar, text="mini_py  /  Home",
            font=("Courier", 10), bg=L["bg2"], fg=L["muted"])
        self.breadcrumb.pack(side="left", padx=22, pady=16)

        self.app_badge = tk.Label(
            self.topbar, text="", font=("Courier", 8),
            bg=L["bg2"], fg=L["bg2"], padx=10, pady=4)
        self.app_badge.pack(side="right", padx=16)

        # ── Main content frame
        self.main = tk.Frame(self, bg=L["bg"])
        self.main.pack(side="right", fill="both", expand=True)

    def _hover(self, widget, normal, hover):
        widget.bind("<Enter>", lambda e: widget.configure(bg=hover))
        widget.bind("<Leave>", lambda e: widget.configure(bg=normal))

    def _clear_main(self):
        for w in self.main.winfo_children():
            w.destroy()

    def _set_active_nav(self, app_id):
        for aid, btn in self.nav_buttons.items():
            if aid == app_id:
                btn.configure(bg=L["card2"], fg=L["fg"])
            else:
                btn.configure(bg=L["surface"], fg=L["muted"])

    def _show_home(self):
        self._clear_main()
        self.current_app_id = None
        self._set_active_nav(None)
        self.breadcrumb.configure(text="mini_py  /  Home")
        self.app_badge.configure(text="", bg=L["bg2"])

        # Canvas for background glow
        canvas = tk.Canvas(self.main, bg=L["bg"], highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bind("<Configure>", lambda e: self._paint_home_bg(canvas))

        shell = tk.Frame(canvas, bg=L["bg"])
        canvas.create_window(0, 0, anchor="nw", window=shell, tags="shell")
        canvas.bind("<Configure>", lambda e, c=canvas, s=shell: (
            self._paint_home_bg(c),
            c.coords("shell", 0, 0),
            c.itemconfig("shell", width=e.width, height=e.height)
        ), add="+")

        # Hero text
        hero = tk.Frame(shell, bg=L["bg"], padx=44, pady=44)
        hero.pack(fill="x")

        badge_frame = tk.Frame(hero, bg=L["card2"], padx=12, pady=5)
        badge_frame.pack(anchor="w")
        tk.Label(badge_frame, text="● Python Mini Projects Collection",
                 font=("Courier", 9), bg=L["card2"], fg=L["accent"]).pack()

        tk.Label(hero, text="mini_py", font=("Courier", 46, "bold"),
                 bg=L["bg"], fg=L["fg"]).pack(anchor="w", pady=(18, 4))
        tk.Label(hero, text="Eight complete Python apps. One launcher. Click any card to run.",
                 font=("Courier", 11), bg=L["bg"], fg=L["muted"],
                 justify="left").pack(anchor="w")

        # Stats row
        stats_row = tk.Frame(hero, bg=L["bg"])
        stats_row.pack(anchor="w", pady=(22, 0))
        for num, lbl in [("8", "Apps"), ("3k+", "Lines of Code"), ("1", "Dependency")]:
            sf = tk.Frame(stats_row, bg=L["bg"], padx=22)
            sf.pack(side="left")
            tk.Label(sf, text=num, font=("Courier", 22, "bold"),
                     bg=L["bg"], fg=L["fg"]).pack(anchor="w")
            tk.Label(sf, text=lbl, font=("Courier", 8),
                     bg=L["bg"], fg=L["muted"]).pack(anchor="w")

        # App grid
        grid_frame = tk.Frame(shell, bg=L["bg"], padx=32, pady=12)
        grid_frame.pack(fill="both", expand=True)
        tk.Frame(shell, bg=L["border"], height=1).pack(fill="x", padx=32)
        tk.Label(grid_frame, text="// all projects",
                 font=("Courier", 9), bg=L["bg"], fg=L["muted2"]).pack(anchor="w", pady=(14, 14))

        cards_wrap = tk.Frame(grid_frame, bg=L["bg"])
        cards_wrap.pack(fill="both", expand=True)

        for col in range(4):
            cards_wrap.columnconfigure(col, weight=1)

        for idx, meta in enumerate(APP_META):
            r, c = idx // 4, idx % 4
            self._make_app_card(cards_wrap, meta, r, c)

    def _paint_home_bg(self, canvas):
        canvas.delete("bg_decor")
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        canvas.create_oval(w-320, -120, w+80, 280,
                           fill="#111726", outline="", tags="bg_decor")
        canvas.create_oval(-120, h-220, 280, h+80,
                           fill="#0f1420", outline="", tags="bg_decor")
        canvas.lower("bg_decor")

    def _make_app_card(self, parent, meta, row, col):
        card = tk.Frame(parent, bg=L["card"], padx=18, pady=18, cursor="hand2")
        card.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)

        accent = meta["color"]

        # accent top stripe (canvas line)
        stripe = tk.Canvas(card, height=2, bg=accent, highlightthickness=0)
        stripe.pack(fill="x", pady=(0, 12))

        # Icon + Tag row
        top_row = tk.Frame(card, bg=L["card"])
        top_row.pack(fill="x")
        tk.Label(top_row, text=meta["icon"], font=("Courier", 20),
                 bg=L["card"]).pack(side="left")
        tag_frame = tk.Frame(top_row, bg=L["bg2"], padx=7, pady=3)
        tag_frame.pack(side="right", anchor="ne")
        tk.Label(tag_frame, text=meta["tag"], font=("Courier", 7),
                 bg=L["bg2"], fg=accent).pack()

        tk.Label(card, text=meta["name"], font=("Courier", 11, "bold"),
                 bg=L["card"], fg=L["fg"], anchor="w").pack(fill="x", pady=(8, 2))
        tk.Label(card, text=meta["sub"], font=("Courier", 8),
                 bg=L["card"], fg=L["muted"], anchor="w").pack(fill="x")

        run_btn = tk.Button(
            card, text="▶  Launch",
            font=("Courier", 9, "bold"),
            bg=accent, fg="#0b0c14",
            relief="flat", padx=10, pady=6, cursor="hand2", bd=0,
            command=lambda m=meta: self._launch(m["id"]))
        run_btn.pack(anchor="w", pady=(14, 0))

        # Hover effects on whole card
        def on_enter(e):
            card.configure(bg=L["card2"])
            top_row.configure(bg=L["card2"])
            tag_frame.configure(bg=L["bg2"])
            for child in card.winfo_children():
                if isinstance(child, tk.Label):
                    child.configure(bg=L["card2"])

        def on_leave(e):
            card.configure(bg=L["card"])
            top_row.configure(bg=L["card"])
            for child in card.winfo_children():
                if isinstance(child, tk.Label):
                    child.configure(bg=L["card"])
        for widget in [card] + list(card.winfo_children()):
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)

    def _launch(self, app_id):
        self._clear_main()
        self.current_app_id = app_id
        self._set_active_nav(app_id)

        meta = next(m for m in APP_META if m["id"] == app_id)
        self.breadcrumb.configure(text=f"mini_py  /  {meta['name']}")
        self.app_badge.configure(text=f"  {meta['tag']}  ",
                                 bg=meta["color"], fg="#0b0c14")

        # App container frame
        app_frame = tk.Frame(self.main, bg="#0b0c14")
        app_frame.pack(fill="both", expand=True)

        # Instantiate the app inside its frame
        builder = APP_BUILDERS[app_id]
        self.app_instance = builder(app_frame)


def main():
    app = MiniPyLauncher()
    app.mainloop()


if __name__ == "__main__":
    main()
