# 🎧 Speech Processing GUI Application

A Python-based desktop application for speech processing, visualization, and educational exploration. This intuitive GUI allows users to load audio files, apply signal processing algorithms, adjust parameters, and understand the underlying mathematics behind common speech analysis techniques.

---

## 📌 Features

- ✅ **User-Friendly GUI** built with PyQt5
- 🎵 **Load and analyze audio files** (WAV, MP3)
- 📈 **Visualizations**:
  - Time-domain waveform
  - Spectrogram with selectable window types (Hann, Hamming, Blackman)
  - MFCC (Mel-Frequency Cepstral Coefficients)
- 🧠 **Mathematical Insights**:
  - View and explore formulas for STFT, MFCC, LPC, and more
- 📊 Dynamic update of graphs based on user selections
- 🧰 Easily extensible for new algorithms (LPC, VAD, etc.)

---

## 🖼 Screenshots

<img src="screenshots/waveform.png" width="400" />
<img src="screenshots/spectrogram.png" width="400" />
<img src="screenshots/mfcc.png" width="400" />

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/speech-processing-gui.git
   cd speech-processing-gui
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python speech_processing_app.py
📦 Requirements
Python 3.7+

PyQt5

Librosa

NumPy

Matplotlib

Install them manually (if not using requirements.txt):

bash
Copy
Edit
pip install PyQt5 librosa numpy matplotlib
📚 Educational Purpose
This project is designed not only as a tool for speech signal analysis but also as an educational platform for students, researchers, and audio engineers who want to:

Understand the math behind common signal processing techniques.

Experiment with parameters and instantly visualize the results.

Build upon a modular and extensible codebase for further development.

🚀 Future Enhancements
 Add Linear Predictive Coding (LPC) visualization

 Voice Activity Detection (VAD)

 Live microphone input support

 Export processed data and visualizations

 Add LaTeX-rendered math or interactive formula explorer

🧑‍💻 Contributing
Contributions are welcome! Feel free to fork the repo, open issues, and submit pull requests. Let's build a great educational tool together!

📄 License
MIT License

🙌 Acknowledgements
Librosa for audio processing

Matplotlib for plotting

PyQt5 for GUI framework
