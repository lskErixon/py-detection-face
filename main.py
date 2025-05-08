import face_recognition
import tkinter as tk
from tkinter import filedialog, messagebox

class FaceCompareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")
        self.root.geometry("340x270")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")  # Light gray background

        self.image1_path = None
        self.image2_path = None

        self.create_widgets()

    def create_widgets(self):
        btn_style = {
            "font": ("Helvetica", 11, "bold"),
            "bg": "#dddddd",
            "fg": "black",
            "activebackground": "#cccccc",
            "activeforeground": "black",
            "width": 25,
            "height": 2,
            "bd": 1,
            "relief": "ridge",
            "cursor": "hand2"
        }

        tk.Button(self.root, text="📁 Select Image 1", command=self.load_image1, **btn_style).pack(pady=10)
        tk.Button(self.root, text="📁 Select Image 2", command=self.load_image2, **btn_style).pack(pady=10)
        tk.Button(self.root, text="🧠 Compare Faces", command=self.compare_faces, **btn_style).pack(pady=10)

        tk.Button(
            self.root,
            text="ℹ️ Info",
            command=self.show_info,
            font=("Helvetica", 10, "bold"),
            bg="#eeeeee",
            fg="black",
            activebackground="#dddddd",
            activeforeground="black",
            width=10,
            height=1,
            bd=1,
            relief="ridge",
            cursor="hand2"
        ).pack(pady=5)

    def load_image1(self):
        self.image1_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if self.image1_path:
            messagebox.showinfo("Image 1", f"Selected:\n{self.image1_path}")

    def load_image2(self):
        self.image2_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if self.image2_path:
            messagebox.showinfo("Image 2", f"Selected:\n{self.image2_path}")

    def compare_faces(self):
        if not self.image1_path or not self.image2_path:
            messagebox.showwarning("Missing Images", "Please select both images.")
            return

        try:
            image1 = face_recognition.load_image_file(self.image1_path)
            image2 = face_recognition.load_image_file(self.image2_path)

            encodings1 = face_recognition.face_encodings(image1)
            encodings2 = face_recognition.face_encodings(image2)

            if not encodings1 or not encodings2:
                messagebox.showerror("Face Error", "Could not detect a face in one of the images.")
                return

            match = face_recognition.compare_faces([encodings1[0]], encodings2[0])[0]

            if match:
                messagebox.showinfo("Result", "✅ Person recognized")
            else:
                messagebox.showinfo("Result", "❌ Different persons")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_info(self):
        messagebox.showinfo(
            "How to Use",
            "1. Click 'Select Image 1' to choose the first photo.\n"
            "2. Click 'Select Image 2' to choose the second photo.\n"
            "3. Click 'Compare Faces' to see if it's the same person.\n\n"
            "Make sure both images clearly show a face."
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceCompareApp(root)
    root.mainloop()
