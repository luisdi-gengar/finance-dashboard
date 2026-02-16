# 💀 Finance Dashboard 👻

*A spooktacular Django finance tracker that haunts your spending habits* 🕷️

Built with synthetic transaction data because even ghosts need to track their ca$h 💵

---

## ✨ Features

- 📊 **Interactive Charts** — Monthly cash flow, expense categories, daily spending patterns
- 🧪 **Data Processing** — Pandas-powered data transformation & categorization  
- 🌑 **Dark Theme** — Spooky Twitter/X inspired design
- 📱 **Responsive** — Works on desktop & mobile

---

## 🛠️ Tech Stack

- **Backend:** Django 6.0 👻
- **Data Analysis:** Pandas, NumPy 🐼
- **Visualization:** Plotly 📈
- **Package Manager:** UV ⚡
- **Python:** 3.12+

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/luisdi-gengar/finance-dashboard.git
cd finance-dashboard

# Install dependencies with UV
uv sync

# Summon the server
uv run python manage.py runserver
```

Open http://localhost:8000 to see your haunted finances 👀

---

## 📁 Project Structure

```
finance-dashboard/
├── pyproject.toml              # UV project config
├── finance_data.csv            # 💰 Your financial data
├── manage.py                   # Django management
├── dashboard/
│   ├── views.py                # Main dashboard logic
│   ├── config.py               # Category config
│   ├── management/
│   │   └── commands/
│   │       └── generate_data.py  # 🎲 Data generator
│   └── templates/
│       └── dashboard/
│           └── index.html      # 🎃 Frontend with Plotly
└── financeproject/
    ├── settings.py             # Django settings
    └── urls.py                 # URL routing
```

---

## 🧠 How It Works

### 1️⃣ Data Generation (`generate_data.py`)

Creates 500 synthetic transactions with:
- **timestamp** — Random datetime over the past year
- **description** — Category-specific transaction descriptions  
- **amount** — Positive = income � income = good, Negative = expenses 👻

Categories include:
- 💵 Income — Salary, Freelance, Dividends
- 🛒 Shopping — Amazon, Electronics, Groceries
- 🍔 Food & Dining — Restaurants, Coffee, Delivery
- 🚗 Transportation — Gas, Uber, Insurance
- 🎬 Entertainment — Netflix, Concerts, Gaming
- 📄 Bills & Utilities — Rent, Electric, Internet
- 🏥 Healthcare — Doctor, Pharmacy, Gym
- ✈️ Travel — Flights, Hotels, Airbnb

### 2️⃣ Data Processing (`views.py`)

When you visit:
1. CSV loads into Pandas DataFrame 🐼
2. Timestamps parsed, months/days extracted
3. Transactions categorized by keywords
4. Aggregates calculated (income, expenses, net, categories, daily avg)

### 3️⃣ Visualization (`index.html`)

Three Plotly charts:
- 📈 **Line Chart** — Monthly cash flow over time
- 🍩 **Pie Chart** — Expense distribution by category  
- 📊 **Bar Chart** — Average daily spending

---

## ⚡ UV Commands

```bash
uv sync                    # 📦 Install dependencies
uv add django              # ➕ Add package
uv remove django           # ➖ Remove package
uv run python manage.py runserver  # 🏃 Run server
uv run python manage.py generate_data  # 🎲 Regenerate data
uv run python manage.py shell  # 🐚 Django shell
```

---

## 🎨 Customization

### Add Your Own Data

Replace `finance_data.csv` with your real data. Required columns:
- `timestamp` — Date/time
- `description` — What you spent on
- `amount` — USD (positive = income, negative = expense)

### Modify Categories

Edit `dashboard/config.py` to add custom categories.

### Change Colors

Edit Plotly trace configs in `dashboard/templates/dashboard/index.html`

---

## 🌐 Deployment

Want to deploy? Check out:
- [Render.com](https://render.com) — Free tier available
- [Railway](https://railway.app) — Nice UI
- [Tailscale](https://tailscale.com) — Access from anywhere! 🕵️

---

## 📜 License

MIT — Use it, fork it, haunt it! 🦇

---

*Built with Django + Plotly + 💀 Gengar energy* 

👾👻🕷️
