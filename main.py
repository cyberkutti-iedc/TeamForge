"""
TeamForge - Effortlessly assign students to random teams from a CSV file.

USAGE (from command line):
    python main.py <input_file> -n <num_teams> [-s <students_per_team>] [-o <output_dir>]

Arguments:
    input_file                Path to the input CSV file containing student data.

Options:
    -n, --num-teams           Number of teams to create. (required)
    -s, --students-per-team   Number of students per team (default: 6).
    -o, --output-dir          Directory to save output CSV files (default: current directory).
    -h, --help                Show this help message and exit.

Example:
    python main.py students.csv -n 10 -s 5 -o output_teams

Description:
    This script reads a CSV file containing student information and randomly assigns students to the specified number of teams.
    It generates a 'teams.csv' file listing all students with their assigned teams, and also creates a separate CSV file for each team in the output directory.
"""

import pandas as pd
import random
import argparse
import sys
import os

def create_and_save_teams(input_file, num_teams, students_per_team=6, output_dir='.'):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # Extract relevant columns for team creation
    students = df[['Email Address', '1. Name of student', '2. Year of study', '3. Branch of study']]
    
    # Shuffle students randomly to ensure a fair distribution
    students = students.sample(frac=1).reset_index(drop=True)
    
    # Create a list of team names
    teams = [f"Team {i+1}" for i in range(num_teams)]
    
    # Initialize a dictionary to store the students in each team
    team_assignments = {team: [] for team in teams}
    
    # Distribute the students across teams
    team_idx = 0
    full_team_list = []  # List to store all students with their assigned teams
    
    for i, student in students.iterrows():
        team_name = teams[team_idx]
        student_data = student.to_dict()
        student_data['Team'] = team_name
        full_team_list.append(student_data)
        
        team_assignments[team_name].append(student_data)
        
        if len(team_assignments[team_name]) == students_per_team:
            team_idx += 1  # Move to the next team once a team reaches the specified number of students
            if team_idx == num_teams:
                team_idx = 0  # If we reach the last team, loop back to the first team
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a full team CSV file
    full_team_df = pd.DataFrame(full_team_list)
    full_team_file_path = os.path.join(output_dir, 'teams.csv')
    full_team_df.to_csv(full_team_file_path, index=False)
    
    # Create and save separate CSV files for each team
    team_files = {}
    for team, members in team_assignments.items():
        team_df = pd.DataFrame(members)
        team_file_path = os.path.join(output_dir, f'{team}.csv')  # Save with team name
        team_df.to_csv(team_file_path, index=False)
        team_files[team] = team_file_path
    
    print(f"Full team file saved: {full_team_file_path}")
    print(f"Team files saved: {team_files}")
    return full_team_file_path, team_files

def main():
    # Print help if no arguments are provided
    if len(sys.argv) == 1:
        print(__doc__)
        sys.exit(0)
        
    parser = argparse.ArgumentParser(
        description="TeamForge: Randomly assign students to teams from a CSV file."
    )
    parser.add_argument(
        'input_file',
        help='Path to the input CSV file containing student data.'
    )
    parser.add_argument(
        '-n', '--num-teams',
        type=int,
        required=True,
        help='Number of teams to create.'
    )
    parser.add_argument(
        '-s', '--students-per-team',
        type=int,
        default=6,
        help='Number of students per team (default: 6).'
    )
    parser.add_argument(
        '-o', '--output-dir',
        default='.',
        help='Directory to save output CSV files (default: current directory).'
    )
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
    if args.num_teams <= 0:
        print("Error: Number of teams must be positive.", file=sys.stderr)
        sys.exit(1)
    if args.students_per_team <= 0:
        print("Error: Students per team must be positive.", file=sys.stderr)
        sys.exit(1)

    create_and_save_teams(
        input_file=args.input_file,
        num_teams=args.num_teams,
        students_per_team=args.students_per_team,
        output_dir=args.output_dir
    )

if __name__ == "__main__":
    main()
