# Catch the Ball – A Simple Game Using Python and OpenCV

## 📌 Project Overview

**Catch the Ball** is a beginner-friendly mini game developed using **Python** and **OpenCV**. In this project, a ball continuously falls from the top of the window. When it reaches the bottom, it resets to the top at a random horizontal position. The project demonstrates basic animation, randomness, and real-time rendering using computer vision concepts.

## 🎯 Objectives

* Learn how to use OpenCV for real-time graphics
* Understand animation using loops
* Work with random positions and velocities
* Practice basic game logic in Python

## 🛠️ Technologies Used

* **Python 3**
* **OpenCV (cv2)**
* **NumPy**
* **Random module**

## ⚙️ Requirements

Make sure the following libraries are installed:

```bash
pip install opencv-python numpy
```

---

## ▶️ How to Run the Project

1. Save the Python file as `catch_the_ball.py`
2. Open terminal / command prompt
3. Run the command:

```bash
python catch_the_ball.py
```

4. Press **Q** to exit the game window

---

## 🧠 Algorithm

1. Initialize window size and ball properties
2. Generate a random horizontal position for the ball
3. Move the ball downward using velocity
4. If the ball reaches the bottom:

   * Reset its position to the top
   * Generate a new random x-coordinate
5. Draw the ball on the window
6. Repeat the process until the user presses **Q**

---

## 📸 Output Description

* A black window of size **500 × 500** appears
* A red ball falls vertically from the top
* The ball resets when it touches the bottom

---

## 🚀 Future Enhancements

* Add a player-controlled catcher
* Implement mouse or keyboard control
* Add score counter
* Increase difficulty over time
* Multiple falling balls


