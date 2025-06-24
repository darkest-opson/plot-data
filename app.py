import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("PEG Hits Visualization Tool")
st.subheader("Enter Data Manually")

# Input for number of strains
num_strains = st.number_input("How many strains do you want to enter?", min_value=1, max_value=20, step=1)

# Input form
strains = []
hits = []

with st.form("manual_data_form"):
    for i in range(num_strains):
        col1, col2 = st.columns(2)
        with col1:
            strain = st.text_input(f"Strain {i + 1}", key=f"strain_{i}")
        with col2:
            hit = st.number_input(f"PEG Hits for Strain {i + 1}", min_value=0, step=1, key=f"hits_{i}")
        strains.append(strain)
        hits.append(hit)
    submitted = st.form_submit_button("Generate Plots")

if submitted:
    df = pd.DataFrame({
        'Strain': strains,
        'PEG Hits': hits
    }).dropna()

    # Filter out empty strain names or missing values
    df = df[df['Strain'] != ""]
    
    if df.empty:
        st.error("Please enter at least one valid strain with a PEG hit value.")
    else:
        x = df['Strain']
        y = df['PEG Hits']
        colors = plt.cm.Paired.colors[:len(df)]

        st.subheader("Data Table")
        st.dataframe(df)

        def plot_bar_chart():
            fig, ax = plt.subplots()
            ax.bar(x, y, color=colors)
            ax.set_title("Number of PEG Hits from Different Strains")
            ax.set_xlabel("Different Strains")
            ax.set_ylabel("Number of PEG Hits")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        def plot_horizontal_bar():
            fig, ax = plt.subplots()
            ax.barh(x, y, color=colors)
            ax.set_title("Number of PEG Hits from Different Strains")
            ax.set_xlabel("Number of PEG Hits")
            ax.set_ylabel("Different Strains")
            st.pyplot(fig)

        def plot_pie_chart():
            fig, ax = plt.subplots()
            ax.pie(y, labels=[f"{strain} ({count})" for strain, count in zip(x, y)], startangle=140)
            ax.set_title("Number of PEG Hits from Different Strains")
            ax.axis('equal')
            st.pyplot(fig)

        def plot_line_chart():
            fig, ax = plt.subplots()
            ax.plot(x, y, marker='o', linestyle='-', color='darkblue')
            ax.set_title("Number of PEG Hits from Different Strains")
            ax.set_xlabel("Different Strains")
            ax.set_ylabel("Number of PEG Hits")
            ax.grid(True)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        def plot_scatter_chart():
            fig, ax = plt.subplots()
            ax.scatter(x, y, s=100, color='darkgreen')
            ax.set_title("Number of PEG Hits from Different Strains")
            ax.set_xlabel("Different Strains")
            ax.set_ylabel("Number of PEG Hits")
            ax.grid(True)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        def plot_radar_chart():
            angles = np.linspace(0, 2 * np.pi, len(x), endpoint=False).tolist()
            angles += angles[:1]
            radar_values = y.tolist() + y.tolist()[:1]

            fig = plt.figure(figsize=(6, 6))
            ax = plt.subplot(111, polar=True)
            ax.plot(angles, radar_values, marker='o', linestyle='-', linewidth=2)
            ax.fill(angles, radar_values, alpha=0.25)
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(x)
            ax.set_title("Number of PEG Hits from Different Strains", y=1.1)
            st.pyplot(fig)

        
        plot_bar_chart()
        plot_horizontal_bar()
        plot_pie_chart()
        plot_line_chart()
        plot_scatter_chart()
        plot_radar_chart()
