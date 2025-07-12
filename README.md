# TeamForge

![TeamForge Logo](https://img.shields.io/badge/TeamForge-Random%20Team%20Generator-blueviolet?style=for-the-badge)

**TeamForge** is an open-source Python tool that helps you quickly and fairly generate random teams from a list of students or participants. It's perfect for educators, event organizers, hackathons, and anyone who needs to split a group into balanced teams with minimal effort.

---

## 🚀 Features

- Randomly assigns participants to teams for fairness
- Supports custom team sizes and number of teams
- Outputs a master CSV and individual team CSV files
- Simple command-line interface
- Works with standard CSV files (e.g., Google Forms exports)
- Cross-platform and easy to use

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cyberkutti-iedc/teamforge.git
   cd teamforge
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas
   ```

---

## 📝 Usage

Prepare your CSV file with the following columns (as exported from Google Forms):

- `Email Address`
- `1. Name of student`
- `2. Year of study`
- `3. Branch of study`

**Run TeamForge from the command line:**

```bash
python main.py <input_file> -n <num_teams> [-s <students_per_team>] [-o <output_dir>]
```

### Arguments

- `<input_file>`: Path to your CSV file.
- `-n`, `--num-teams`: Number of teams to create. **(required)**
- `-s`, `--students-per-team`: Number of students per team (default: 6).
- `-o`, `--output-dir`: Directory to save output files (default: current directory).

### Example

```bash
python main.py students.csv -n 8 -s 5 -o teams_output
```

This will create:
- `teams_output/teams.csv` (all teams in one file)
- `teams_output/Team 1.csv`, `teams_output/Team 2.csv`, ..., one file per team

---

## 🤔 Why Use TeamForge?

- **Fairness:** Ensures unbiased, random team assignments.
- **Simplicity:** No Excel formulas or manual shuffling.
- **Automation:** Instantly generates all team files for you.
- **Open Source:** Free to use and modify for your needs.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

> Made with ❤️ for educators and organizers.
