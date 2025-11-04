# 🖼️ Image Slideshow Viewer (Tkinter + PIL)

A simple Python GUI application that displays an automatic **image slideshow** using **Tkinter** and **Pillow (PIL)**.
You can load multiple images, set their display duration, and view them in a looping slideshow format.

---

## 🚀 Features

* Displays images in a clean Tkinter window
* Automatic resizing of images
* Customizable slideshow delay
* Simple and easy-to-modify code

---

## 🧰 Requirements

Make sure you have **Python 3.x** installed.
Install the required libraries with:

```bash
pip install pillow
```

*(Tkinter comes preinstalled with Python.)*

---

## 📂 How to Use

1. **Clone this repository**

   ```bash
    git clone https://github.com/samriddhsaxena/mini-projects.git
    cd mini-projects/Image Slideshow App
   ```

2. **Add your image paths** inside the `image_paths` list in the script:

   ```python
   image_paths = [
       "images/photo1.jpg",
       "images/photo2.jpg",
       "images/photo3.png",
   ]
   ```

3. **Run the program**

   ```bash
   python slideshow.py
   ```

4. Click the **“Play Slideshow”** button to start viewing your images.

---


## ⚙️ Customization

* **Change image size:** Edit the `image_size` tuple.
* **Change delay time:** Modify the `time.sleep(3)` value (in seconds).
* **Looping behavior:** You can replace the manual loop with an infinite cycle using `itertools.cycle`.

---

Run → Click **Play Slideshow** → Enjoy the full-screen image view!

---

## 🧾 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

**Author:** Samriddh Saxena
🌐 GitHub: [@samriddhsaxena](https://github.com/samriddhsaxena)