# ESG Score and Sustainability Analytics Dashboard

## Overview
This project predicts the Overall ESG (Environmental, Social, and Governance) Score using Machine Learning and presents the results through a Flask web application.

## Features
- ESG Score Prediction using Linear Regression
- Interactive Flask Web Application
- Dashboard with KPI Cards
- ESG Distribution Analysis
- Industry-wise ESG Analysis
- Region-wise ESG Analysis
- Top 10 Companies Visualization

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Flask
- HTML
- CSS

## Dataset
Company ESG Financial Dataset

## Machine Learning
- Algorithm: Linear Regression
- MAE: ~0.026
- R² Score: ~0.999995

## Project Structure

ESG_Project/
├── app.py
├── esg.ipynb
├── model.pkl
├── company_esg_financial_dataset.csv
├── templates/
├── static/

## Installation

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Future Enhancements
- Cloud Deployment
- Real-time ESG Data
- Interactive Charts
- Advanced Machine Learning Models

## Author

Rohan S
## Screenshots

### Home Page

![Home](images/home.png)

### Dashboard

![Dashboard](images/dashboard.png)

### Prediction

![Prediction](images/prediction.png)