# Fish-weight-estimation

### Overview
This repository contains the Python code and dataset used for real-time fish weight estimation, combining image processing with resistivity measurements.

### Code Structure
- **`main_cam.py`:** Captures and processes images of fish using a web camera. It utilizes the YOLO algorithm to detect fish and extract relevant dimensions (width, height) from the images.
- **`main_scope.py`:** Handles resistivity measurements, capturing the electrical resistance data as fish swim by the electrodes.
- **`df.csv`:** A dataset that includes manually collected fish weights, resistivity measurements, and dimensions obtained from images. This dataset is used to train and test the machine learning models.

### Dependencies
To run the code, you’ll need the following Python packages:
- OpenCV
- YOLOv3 (for object detection)
- Scikit-learn
- Pandas
- NumPy

You can install all dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Getting Started
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Prepare the environment:**
   Install the required Python packages using the provided `requirements.txt` or manually:
   ```bash
   pip install opencv-python scikit-learn pandas numpy
   ```

3. **Using the Image Processing Script:**
   Run `main_cam.py` to capture and process fish images:
   ```bash
   python main_cam.py
   ```
   This script will detect fish in the images and extract their dimensions for further analysis.

4. **Using the Resistivity Measurement Script:**
   Run `main_scope.py` to capture resistivity data:
   ```bash
   python main_scope.py
   ```
   This script will collect and log the resistivity measurements, which will later be used in the model.

5. **Working with the Dataset:**
   - The `df.csv` file contains data used for training and testing the machine learning models.
   - To use this dataset with your models, you can load it using Pandas:
     ```python
     import pandas as pd
     df = pd.read_csv('df.csv')
     ```
   - You can then split the data into training and testing sets, and apply machine learning models to predict fish weights based on the features.

### Example Usage
Here’s a simple example of how to load the dataset and train a basic model:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv('df.csv')

# Split into features and target
X = df[['width', 'height', 'resistivity']]
y = df['weight']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f'Model accuracy: {accuracy * 100:.2f}%')
```
