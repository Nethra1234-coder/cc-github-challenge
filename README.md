# cc-github-challenge

# Predictive Maintenance Code Challenge: The "Broken" Engine Model

This repository contains a machine learning pipeline designed to predict engine health.

**The catch?** The current codebase is intentionally riddled with **16 errors**—ranging from simple syntax typos to deep logical flaws that will prevent the model from training correctly.

---

##  Your Challenge
Your goal is to transform the broken script into a production-ready ML pipeline. To complete the challenge, you should:

1.  **Identify and Fix:** Find all 16 errors in the `predict_engine.py` script.
2.  **Optimize:** Once the code runs, try to improve the accuracy or F1-score of the model.
3.  **Contribute:** Submit your fixes via a **Pull Request (PR)**.
    * *Note: Please include a list of the errors you found in your PR description.*

---

## About the Dataset
The model uses real-world engine sensor data to classify whether an engine is in good or bad condition. Predictive maintenance helps in identifying potential failures before they occur, saving costs and improving safety.

### Column Descriptions:
| Column Name | Description |
| :--- | :--- |
| **Engine rpm** | The rotational speed of the engine (RPM). |
| **Lub oil pressure** | The pressure of the lubricating oil (in bar). |
| **Fuel pressure** | The pressure of the fuel being delivered to the engine. |
| **Coolant pressure** | The pressure within the engine's cooling system. |
| **lub oil temp** | The temperature of the lubricating oil (°C). |
| **Coolant temp** | The temperature of the engine coolant (°C). |
| **Engine Condition** | **Target Variable:** (0 = Normal / 1 = Potential Failure). |

---

##  Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed. You will need to install the following dependencies:

```bash


pip install pandas xgboost scikit-learn
```

### 2. Installation, Setup & How to Submit
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/engine-challenge-repo.git](https://github.com/YOUR_USERNAME/engine-challenge-repo.git)
   cd engine-challenge-repo
   ```

1.  **Fork** this repository to your own account.
2.  **Create a new branch** to work on your fixes:
    ```bash
    git checkout -b fix/my-solution
    ```
3.  **Commit your fixes** with a descriptive message:
    ```bash
    git commit -m "Fixed 16 errors and improved model performance"
    ```
4.  **Push to the branch** on your forked repository:
    ```bash
    git push origin fix/my-solution
    ```
5.  **Open a Pull Request** (PR) from your fork back to the main repository. 
    * *In the PR description, please list the specific errors you identified and the steps you took to optimize the model.*
