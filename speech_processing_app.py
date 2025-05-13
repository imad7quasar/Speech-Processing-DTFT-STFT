import sys
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog,
    QComboBox, QHBoxLayout, QTextEdit, QTabWidget
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SpeechProcessingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speech Processing GUI")
        self.setGeometry(100, 100, 1000, 700)

        self.audio_path = None
        self.y = None
        self.sr = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Load button and window type selection
        self.load_button = QPushButton("Load Audio File")
        self.load_button.clicked.connect(self.load_audio)

        self.window_label = QLabel("Window Type:")
        self.window_select = QComboBox()
        self.window_select.addItems(["hann", "hamming", "blackman"])
        self.window_select.currentTextChanged.connect(self.update_spectrogram)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.load_button)
        hlayout.addWidget(self.window_label)
        hlayout.addWidget(self.window_select)

        # Tabs for different visualizations
        self.tabs = QTabWidget()
        self.wave_tab = QWidget()
        self.spec_tab = QWidget()
        self.mfcc_tab = QWidget()
        self.formula_tab = QWidget()

        self.tabs.addTab(self.wave_tab, "Waveform")
        self.tabs.addTab(self.spec_tab, "Spectrogram")
        self.tabs.addTab(self.mfcc_tab, "MFCC")
        self.tabs.addTab(self.formula_tab, "Formulas")

        # Canvas for waveform
        self.wave_fig, self.wave_ax = plt.subplots(figsize=(8, 4))
        self.wave_canvas = FigureCanvas(self.wave_fig)
        self.wave_layout = QVBoxLayout()
        self.wave_layout.addWidget(self.wave_canvas)
        self.wave_tab.setLayout(self.wave_layout)

        # Canvas for spectrogram
        self.spec_fig, self.spec_ax = plt.subplots(figsize=(8, 4))
        self.spec_canvas = FigureCanvas(self.spec_fig)
        self.spec_layout = QVBoxLayout()
        self.spec_layout.addWidget(self.spec_canvas)
        self.spec_tab.setLayout(self.spec_layout)

        # Canvas for MFCC
        self.mfcc_fig, self.mfcc_ax = plt.subplots(figsize=(8, 4))
        self.mfcc_canvas = FigureCanvas(self.mfcc_fig)
        self.mfcc_layout = QVBoxLayout()
        self.mfcc_layout.addWidget(self.mfcc_canvas)
        self.mfcc_tab.setLayout(self.mfcc_layout)

        # Formula text
        self.formula_text = QTextEdit()
        self.formula_text.setReadOnly(True)
        self.formula_text.setText(self.get_formulas())
        self.formula_layout = QVBoxLayout()
        self.formula_layout.addWidget(self.formula_text)
        self.formula_tab.setLayout(self.formula_layout)

        layout.addLayout(hlayout)
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def load_audio(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Audio File", "", "Audio Files (*.wav *.mp3);;All Files (*)"
        )
        if file_path:
            self.audio_path = file_path
            self.y, self.sr = librosa.load(file_path)
            self.plot_waveform()
            self.plot_spectrogram()
            self.plot_mfcc()

    def plot_waveform(self):
        self.wave_ax.clear()
        librosa.display.waveshow(self.y, sr=self.sr, ax=self.wave_ax)
        self.wave_ax.set_title("Waveform")
        self.wave_canvas.draw()

    def plot_spectrogram(self):
        self.spec_ax.clear()
        window = self.window_select.currentText()
        D = librosa.stft(self.y, window=window)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
        img = librosa.display.specshow(S_db, sr=self.sr, x_axis='time', y_axis='hz', ax=self.spec_ax)
        self.spec_ax.set_title(f"Spectrogram - {window} window")
        self.spec_fig.colorbar(img, ax=self.spec_ax, format="%+2.0f dB")
        self.spec_canvas.draw()

    def plot_mfcc(self):
        self.mfcc_ax.clear()
        mfccs = librosa.feature.mfcc(y=self.y, sr=self.sr, n_mfcc=13)
        img = librosa.display.specshow(mfccs, x_axis='time', ax=self.mfcc_ax)
        self.mfcc_ax.set_title("MFCC (Mel-Frequency Cepstral Coefficients)")
        self.mfcc_fig.colorbar(img, ax=self.mfcc_ax)
        self.mfcc_canvas.draw()

    def update_spectrogram(self):
        if self.y is not None:
            self.plot_spectrogram()

    def get_formulas(self):
        return (
            "Short-Time Fourier Transform (STFT):\n"
            "X(m, k) = ∑ x[n] · w[n - mH] · e^{-j2πkn/N}\n\n"
            "MFCC Calculation Steps:\n"
            "1. Compute FFT of the signal\n"
            "2. Apply Mel filterbank\n"
            "3. Take log of filterbank energies\n"
            "4. Apply DCT to decorrelate\n\n"
            "Linear Predictive Coding (LPC):\n"
            "s[n] = -∑ a_k · s[n - k] + G · e[n]\n"
            "(Predict current sample using past samples)"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeechProcessingApp()
    window.show()
    sys.exit(app.exec_())
