# movie-sentiment-analysis

This repository implements a simple movie review sentiment analysis project using a single recurrent neural network architecture: a SimpleRNN. The repo is intentionally small and focused training and experimentation are captured in a Jupyter notebook, and a small app demonstrates inference.

Project summary

- Model: SimpleRNN (no LSTM or GRU are used)
- Files included: a notebook with training/experiments, a minimal app for inference, and a requirements.txt to install dependencies

Folder structure

- Simple RNN/
  - simple_rnn.ipynb   # Jupyter notebook that contains data loading, preprocessing, SimpleRNN model definition, training loops, and evaluation
  - app.py             # Minimal application for loading a saved model and running inference on new reviews
  - requirements.txt   # Python dependencies needed to run the notebook and the app

Quick start

1. Clone the repository:

   git clone https://github.com/shajiyakhan1309/movie-sentiment-analysis.git
   cd movie-sentiment-analysis

2. Install dependencies (the requirements file is inside the Simple RNN folder):

   python -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   pip install -r "Simple RNN/requirements.txt"

3. Open and run the notebook:

   - Launch Jupyter and open `Simple RNN/simple_rnn.ipynb` to view data preprocessing, model code, training, and evaluation. The notebook contains the code and narrative to reproduce experiments.

   jupyter notebook

4. Run the app:

   - The `app.py` file provides a minimal example to load a trained model checkpoint and run inference on new review text. Example:

   python "Simple RNN/app.py" --text "That movie was surprisingly good and moving"

   (Adjust the command-line flags as implemented in `app.py`.)

Notes and recommendations

- This project focuses exclusively on a SimpleRNN implementation as a compact baseline for sequence modeling. If you later want to try LSTM or GRU variants, the notebook is a good place to add and compare those models.
- Keep `requirements.txt` pinned to specific versions to ensure reproducibility.
- Save model checkpoints from the notebook (for example into a `models/` folder) so `app.py` can load them for inference.

If you'd like, I can:
- Update this README further with framework-specific commands (TensorFlow/Keras or PyTorch) if you tell me which one you used,
- Extract the exact dependency versions from `Simple RNN/requirements.txt` and include them in the README, or
- Commit additional files (example saved model, a short example input/output) if you provide them.
