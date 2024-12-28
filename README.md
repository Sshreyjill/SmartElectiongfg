# Face Recognition Voting System

The **Face Recognition Voting System** is an advanced solution for secure and efficient voting. It uses facial recognition technology combined with the KNN algorithm to authenticate voters, prevent duplicate voting, and ensure fair election processes.

---

## Features

- **Real-Time Face Detection:** Detects faces using OpenCV's Haar Cascade Classifier.
- **Voter Authentication:** Recognizes voters using a pre-trained KNN model.
- **Duplicate Vote Prevention:** Ensures each voter casts their vote only once.
- **Secure Data Logging:** Records voter details, selected party, date, and timestamp in a CSV file.
- **Interactive Feedback:** Provides real-time audio guidance during the voting process.

---

## Technologies Used

- **Python**: Core programming language.
- **OpenCV**: For face detection and image processing.
- **K-Nearest Neighbors (KNN)**: For facial recognition.
- **CSV Module**: For secure data storage.
- **Win32com**: For text-to-speech functionality.

---

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/Sshreyjill/face-recognition-voting.git
   ```

2. Navigate to the project directory:
   ```bash
   cd face-recognition-voting
   ```

3. Install required dependencies:
   ```bash
   pip install opencv-python numpy
   ```

4. Place the `background.png` file in the project directory.

5. Train the system with facial data and save it as `names.pkl` and `faces_data.pkl` in the `data/` folder.

6. Run the program:
   ```bash
   python voting_system.py
   ```

---

## How It Works

1. The system captures live video feed from the webcam.
2. Voter's face is detected and matched with the pre-trained dataset using KNN.
3. The system verifies if the voter has already cast their vote by checking the `Votes.csv` file.
4. If verified, the voter can cast their vote by pressing the corresponding key for their chosen party:
   - `1`: BJP
   - `2`: Congress
   - `3`: TDP
   - `4`: NOTA
5. The vote is recorded in the `Votes.csv` file, and audio feedback confirms the action.

---

## Sample Output

- **CSV File Entry Example:**
  ```csv
  NAME,VOTE,DATE,TIME
  John Doe,BJP,28-12-2024,14:30:15
  ```

---

## Contributions

Contributions are welcome! If you have ideas to improve the project, feel free to fork the repository, create a branch, and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

Developed by [Sai Shreya Jillella](https://github.com/Sshreyjill).

---

## Future Improvements

- Integration with cloud storage for data.
- Multi-language support for a broader audience.
- Enhanced security features using advanced face recognition algorithms.
