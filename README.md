# GradeHub

GradeHub is a simple grade management system built in Python. It uses SQLite as the backend database to store information about students, subjects, and grades. The project provides a command-line interface (CLI) for basic CRUD operations and offers analysis features such as generating student rankings, subject averages, and individual report cards.

## Features

- **Student Management:** Insert and remove students.
- **Subject Management:** Insert and remove subjects.
- **Grade Management:** Insert and remove grades for students in specific subjects.
- **Reporting & Analysis:**
  - **Student Rankings:** View students ranked by their average grade.
  - **Subject Averages:** See the average score for each subject.
  - **Report Cards:** Generate a report card for a specific student showing all subjects and grades.


## Requirements

- Python 3.x
- SQLite (bundled with Python)
- [Pandas](https://pandas.pydata.org/)
- [Tabulate](https://pypi.org/project/tabulate/) (for formatting CLI tables)
- [Pytest](https://docs.pytest.org/) (for running tests)

## Installation

1. **Clone the Repository:**

   ```bash```
   ```git clone https://github.com/yourusername/GradeHub.git```
   ```cd GradeHub```

2. **Set Up a Virtual Environment (Recommended):**

```python -m venv myenv```
```source myenv/bin/activate```  # On Windows: myenv\Scripts\activate

3. **Install Dependencies:** 

```pip install -r requirements.txt```

## Contributing

Contributions are welcome. Feel welcome to fork the repository, make changes, and submit a pull request! 

## License 

This project is licensed under the MIT License. See the LICENSE file for details.





