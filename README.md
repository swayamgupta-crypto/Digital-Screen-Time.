# Digital Screen Time Analyzer

**Author:** Udit Agarwal
**Course:** Python Essentials 

Hi! This is my project for the Python Essentials flipped course evaluation. I built a simple command-line tool to track screen time and calculate productivity. I chose this topic because as students, it's really hard to keep track of how much time we waste on YouTube or games compared to actual studying.

The project is fully executable via the command line and does not rely on any GUI-based setup[cite: 1]. It runs entirely in the terminal!

## Technical Details
- **Language:** Python 3
- **Storage:** I used the built-in `csv` module to save the logs row-by-row in a `data.csv` file. This means your data is saved locally and won't get deleted when you close the program.
- **Modules used:** `csv`, `os`, `datetime`

There are no external libraries, so you do not need to use `pip install` for anything.

## How to setup and run

1. Clone this repository to your system:
   `git clone https://github.com/uditagarwal0708/screen_tracker_project`
2. Open your terminal or command prompt.
3. Navigate into the downloaded project folder.
4. Run the main script using the following command:
   `python main.py` (or `python3 main.py` depending on your system)
5. A menu will pop up in the terminal. Just follow the on-screen numbers to log your screen time, view your health report, or see the text-based bar chart.