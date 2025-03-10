# Hand Tracking Calculator

## Overview
This project implements a hand gesture-based calculator using OpenCV and MediaPipe. The program captures real-time hand movements via a webcam and recognizes gestures to perform arithmetic operations or detect special hand signs like a 'thumbs up'.

## Features
- Uses hand tracking to recognize number gestures (0-9)
- Supports basic arithmetic operations (+, -, *, /)
- Evaluates expressions using real-time gesture inputs
- Recognizes 'thumbs up' as a special gesture
- Displays detected gestures on-screen in real-time

## Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy

## Installation
```sh
# Clone the repository
git clone https://github.com/TheVinnay/hand-tracking-calculator.git
cd hand-tracking-calculator

# Install dependencies
pip install opencv-python mediapipe numpy
```

## Usage
```sh
python hand_tracking_calculator.py
```
- Show numbers (1-5) with your fingers to input digits
- Perform arithmetic operations using specific gestures
- Show a 'thumbs up' to trigger a predefined action
- Press 'q' to exit the program

## Project Structure
```
hand-tracking-calculator/
├── hand_tracking_calculator.py  # Main script for gesture recognition
├── README.md                     # Project documentation
├── requirements.txt               # Dependencies
```

## Future Improvements
- Enhance accuracy of gesture recognition
- Add support for additional hand gestures
- Integrate speech recognition for hybrid input

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to submit issues and pull requests to improve the project!

## Contact
For any inquiries, contact [vinaytati64@gmail.com](mailto:vinaytati64@gmail.com).

