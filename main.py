import ctypes
import tkinter as tk

from linked_cpp import CppLinkedList
from linked_py import PyLinkedList

cpp_lib = ctypes.CDLL("./lib.dll", winmode=0)
stl_lib = ctypes.CDLL("./stl.dll")
cpp = CppLinkedList(cpp_lib)
stl = CppLinkedList(stl_lib)
py = PyLinkedList()


root = tk.Tk()
selection = tk.StringVar(root, "C++")

index = tk.StringVar(root, "0")
value = tk.StringVar(root, "0")


# Get current list
def current():
    sl = selection.get().lower()
    if sl == "py":
        return py
    elif sl == "stl":
        return stl

    return cpp


BG_COLOR = "#2b2b2b"

BTN_STYLE = {
    "font": ("Segoe UI", 11, "bold"),
    "bg": "#2563EB",
    "fg": "#FFFFFF",
    "activebackground": "#1D4ED8",
    "activeforeground": "#FFFFFF",
    "bd": 0,
    "padx": 8,
    "pady": 4,
    "cursor": "hand2",
}

BTN_STYLE2 = {
    "font": ("Segoe UI", 10, "bold"),
    "bg": "#475569",
    "fg": "#000000",
    "activebackground": "#334155",
    "activeforeground": "#475569",
    "bd": 0,
    "padx": 5,
    "pady": 2,
    "cursor": "hand2",
    "indicatoron": False,
}

LBL_STYLE = {
    "font": ("Segoe UI", 10, "bold"),
    "bg": BG_COLOR,
    "fg": "#FFFFFF",
}

ENT_STYLE = {
    "font": ("Segoe UI", 10, "bold"),
    "bg": BG_COLOR,
    "fg": "#FFFFFF",
}

root["bg"] = BG_COLOR
root.geometry("800x400")
root.resizable(False, False)

NODE_W = 100  # px
NODE_H = 50  # px
W = 800
H = 200
X0 = 15
Y0 = H / 2
D = 30
# max nodes in row
MXW = W // (NODE_W + D)


# render list
def render():
    global canv, frame
    canv.delete("all")

    c = current()
    for i, v in enumerate(c.iter()):
        x1 = X0 + i * (NODE_W + D)
        y1 = Y0 - NODE_H / 2
        x2 = x1 + NODE_W
        y2 = y1 + NODE_H

        canv.create_rectangle(
            x1, y1, x2, y2, fill="#e1f5fe", outline="#0288d1", width=2
        )

        canv.create_text(x1 + NODE_W / 2, Y0, text=v)


def on_selected():
    render()


def on_button(p: str, ty: str | None):
    c = current()
    id = int(index.get())

    if p == "push":
        v = int(value.get())
        if ty is None:
            c.insert(id, v)
        elif ty == "head":
            c.pushHead(v)
        elif ty == "back":
            c.pushBack(v)
    elif p == "pop":
        if not (0 <= id < len(c)):
            return

        if ty is None:
            c.pop(id)
        elif ty == "head":
            c.popHead()
        elif ty == "back":
            c.popBack()

    render()


group = tk.Frame(background=BG_COLOR)
insertBtn = tk.Button(
    group, text="Insert", **BTN_STYLE, command=lambda: on_button("push", None)
)
insertBtn.pack(side="left", padx=10, pady=5)

pushHeadBtn = tk.Button(
    group, text="Push Head", **BTN_STYLE, command=lambda: on_button("push", "head")
)
pushHeadBtn.pack(side="left", padx=5, pady=5)

pushBackBtn = tk.Button(
    group, text="Push Back", **BTN_STYLE, command=lambda: on_button("push", "back")
)
pushBackBtn.pack(side="left", padx=10, pady=5)

popBtn = tk.Button(
    group, text="Pop", **BTN_STYLE, command=lambda: on_button("pop", None)
)
popBtn.pack(side="left", padx=5, pady=5)

popHeadBtn = tk.Button(
    group, text="Pop Head", **BTN_STYLE, command=lambda: on_button("pop", "head")
)
popHeadBtn.pack(side="left", padx=10, pady=5)

popBackBtn = tk.Button(
    group, text="Pop Back", **BTN_STYLE, command=lambda: on_button("pop", "back")
)
popBackBtn.pack(side="left", padx=5, pady=5)

group2 = tk.Frame(background=BG_COLOR)
cppBtn = tk.Radiobutton(
    group2,
    text="C++",
    variable=selection,
    value="C++",
    command=on_selected,
    **BTN_STYLE2,
)
cppBtn.pack(side="left", padx=5, pady=5)

pythonBtn = tk.Radiobutton(
    group2,
    text="Py",
    variable=selection,
    value="Py",
    command=on_selected,
    **BTN_STYLE2,
)
pythonBtn.pack(side="left", padx=5, pady=5)

stlBtn = tk.Radiobutton(
    group2,
    text="Stl",
    variable=selection,
    value="Stl",
    command=on_selected,
    **BTN_STYLE2,
)
stlBtn.pack(side="left", padx=5, pady=5)

group3 = tk.Frame(background=BG_COLOR)
valueEntry = tk.Entry(group3, textvariable=value, **ENT_STYLE)
valueEntry.pack(side="bottom", padx=5, pady=5)

indexEntry = tk.Entry(group3, textvariable=index, **ENT_STYLE)
indexEntry.pack(side="bottom", padx=5, pady=5)

group4 = tk.Frame(background=BG_COLOR)
valueLabel = tk.Label(group4, text="Value:", **LBL_STYLE)
valueLabel.pack(side="bottom", padx=5, pady=5)

indexLabel = tk.Label(group4, text="Index:", **LBL_STYLE)
indexLabel.pack(side="bottom", padx=5, pady=5)

group.pack(anchor="e", expand=True)
group2.place(anchor="w", width=150, height=100, x=5, y=25)

group4.place(anchor="w", width=50, height=75, x=5, y=80)
group3.place(anchor="w", width=50, height=75, x=55, y=80)

canv = tk.Canvas(root, bg=BG_COLOR, height=H)

canv.pack(expand=True, fill="both", anchor="s")
root.mainloop()
