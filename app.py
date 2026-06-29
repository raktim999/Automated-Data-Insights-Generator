import streamlit as st
import matplotlib.pyplot as plt
st.title('E-commerce Company Insights')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

categories = ['Intimates', 'Jeans', 'Fashion Hoodies & Sweatshirts']
returns = [1337, 1233, 1153]
return_percentages = [106.7, 103.96, 102.85]

fig, ax1 = plt.subplots(figsize=(8, 5))

color = 'tab:blue'
ax1.set_xlabel('Product Category')
ax1.set_ylabel('Number of Returns', color=color)
bar = ax1.bar(categories, returns, color=color, alpha=0.7, label='Number of Returns')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Return Percentage (%)', color=color)
ax2.plot(categories, return_percentages, color=color, marker='o', label='Return Percentage')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Top 3 Product Categories by Number of Returns')
fig.tight_layout()

fig = plt.gcf()
st.pyplot(fig)
