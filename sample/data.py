from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import seaborn as sns

app = Flask(__name__)

# 데이터 읽기
data = pd.read_csv('cox-violent-parsed_filt_usable.csv')  # 파일 경로에 맞게 수정

# 성별 분포
gender_plot = BytesIO()
sns.countplot(x='sex', data=data)
plt.title('Gender Distribution')
plt.savefig(gender_plot, format='png')
gender_plot.seek(0)
gender_plot_url = base64.b64encode(gender_plot.getvalue()).decode()

# 나이 카테고리 분포
age_cat_plot = BytesIO()
sns.countplot(x='age_cat', data=data)
plt.title('Age Category Distribution')
plt.savefig(age_cat_plot, format='png')
age_cat_plot.seek(0)
age_cat_plot_url = base64.b64encode(age_cat_plot.getvalue()).decode()

# 인종 분포
race_plot = BytesIO()
sns.countplot(x='race', data=data)
plt.title('Race Distribution')
plt.savefig(race_plot, format='png')
race_plot.seek(0)
race_plot_url = base64.b64encode(race_plot.getvalue()).decode()

# 전과 여부에 따른 분포
priors_count_plot = BytesIO()
sns.countplot(x='priors_count', data=data)
plt.title('Priors Count Distribution')
plt.savefig(priors_count_plot, format='png')
priors_count_plot.seek(0)
priors_count_plot_url = base64.b64encode(priors_count_plot.getvalue()).decode()

@app.route("/")
def index():
    return render_template("index.html", 
                           gender_plot_url=gender_plot_url, 
                           age_cat_plot_url=age_cat_plot_url,
                           race_plot_url=race_plot_url,
                           priors_count_plot_url=priors_count_plot_url)

if __name__ == "__main__":
    app.run(debug=True)
