import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class IMCCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de IMC")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.weight_input = QLineEdit()
        self.height_input = QLineEdit()
        self.result_label = QLabel()

        calculate_button = QPushButton("Calcular IMC")
        calculate_button.clicked.connect(self.calculate_imc)

        layout.addWidget(QLabel("Peso (kg):"))
        layout.addWidget(self.weight_input)
        layout.addWidget(QLabel("Altura (m):"))
        layout.addWidget(self.height_input)
        layout.addWidget(calculate_button)
        layout.addWidget(self.result_label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def calculate_imc(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            imc = weight / (height ** 2)
            self.result_label.setText(f"IMC: {imc:.2f}")

            # Classificação do IMC
            if imc < 18.5:
                self.result_label.setText(f"IMC: {imc:.2f} (Abaixo do peso)")
            elif 18.5 <= imc < 24.9:
                self.result_label.setText(f"IMC: {imc:.2f} (Normal)")
            elif 25 <= imc < 29.9:
                self.result_label.setText(f"IMC: {imc:.2f} (Sobrepeso)")
            else:
                self.result_label.setText(f"IMC: {imc:.2f} (Obesidade)")

        except ValueError:
            self.result_label.setText("Insira valores válidos para peso e altura.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IMCCalculator()
    window.show()
    sys.exit(app.exec())