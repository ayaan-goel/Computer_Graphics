# 🧩 Physics Puzzle Game

A fun 2D **Physics Puzzle Game** built using **Pygame** and **Pymunk**.  
In this game, you can drop balls onto a static floor, reset the scene, and observe realistic physics interactions powered by the Pymunk physics engine.

---

## 🎮 Features
- Real-time **2D physics simulation**
- Drop colorful balls with mouse clicks
- Static floor collision using physics
- Reset the environment with one key press
- Simple and interactive user interface

---

## 🧱 Project Structure
CG Project/
│
├── assets/
│ └── background.png # Background image for the game
│
├── graphics.py # Handles drawing and rendering
├── physics_engine.py # Handles physics world and object creation
├── ui.py # Handles UI and text rendering
├── main.py # Main game loop
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone <your-repo-link>
cd "CG Project"
2️⃣ Create and activate a virtual environment (recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On macOS/Linux
3️⃣ Install the required packages
bash
Copy code
python -m pip install -r requirements.txt
This installs:

pygame==2.5.2

pymunk==6.7.0

▶️ How to Run the Game
Run the following command in your terminal:

bash
Copy code
python main.py
🕹️ Controls
Action	Key / Mouse
Drop a ball	Left Mouse Click
Reset simulation	R
Quit game	ESC

🧠 Code Overview
main.py
Handles the main game loop, events, and physics updates.

graphics.py
Draws the background and physics bodies using Pymunk’s DrawOptions.

physics_engine.py
Creates the Pymunk space, adds gravity, static floor, and ball physics.

ui.py
Displays the game title and instructions.

🧰 Requirements
Python 3.10 or later

Pygame 2.5.2

Pymunk 6.7.0

🖼️ Future Improvements
Add collision effects or sound

Add score or level system

Allow different shapes (boxes, triangles)

Implement interactive obstacles

👨‍💻 Author
Ayaan Goel
B.Tech Computer Engineering, PDEU
Computer Graphics Project, 3rd Semester
