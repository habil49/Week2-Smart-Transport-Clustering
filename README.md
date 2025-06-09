# 🚍 SDG 11: Smart Transport Clustering

This project uses **unsupervised machine learning** (K-Means Clustering) to optimize transport routes in urban settings. It supports **SDG 11: Sustainable Cities and Communities** by identifying patterns in GPS-like transit data for smarter route planning.

## 💡 Objective
Cluster synthetic transport data to suggest better route hubs and reduce congestion/emissions.

## 📁 Project Structure
- `sdg11_transport_clustering.py`: Main script with data processing, clustering, and visualization.
- `data.csv`: Sample dataset mimicking GPS or transport hub usage data.
- `README.md`: Project intro and instructions.
- `output/`: Folder for saved plots.

## 🛠️ How to Run (VS Code)
1. Install requirements: `pip install pandas scikit-learn matplotlib seaborn`
2. Run: `python sdg11_transport_clustering.py`

## 📊 Results
Visual clusters show how unsupervised learning groups transport points to improve planning.

## 🧠 ML Approach
- **Algorithm**: KMeans Clustering
- **Metrics**: Inertia, Silhouette Score
- **Tools**: Python, scikit-learn, pandas, matplotlib

## 📌 Disclaimer
This project uses synthetic data for educational purposes.

