# Step-by-Step Deployment Guide

This guide walks you through getting the dashboard from your laptop to a
public URL you can put on your CV. It assumes no prior Python or GitHub
experience.

Total time: about 45 minutes if everything goes smoothly.

---

## Part 1: Get the project running on your laptop (15 minutes)

### Step 1.1 Install Python

If you do not have Python, download it from <https://www.python.org/downloads/>
and install it. **During installation, tick the box that says "Add Python
to PATH"** on Windows.

To confirm it works, open a terminal (Command Prompt on Windows, Terminal
on Mac) and type:

```bash
python --version
```

You should see `Python 3.10.x` or higher.

### Step 1.2 Open the project folder

Unzip the project folder I gave you. Open a terminal and navigate into it:

```bash
cd path/to/infineon-distribution-dashboard
```

Replace `path/to/` with the actual location.

### Step 1.3 Install the required packages

Run this single command:

```bash
pip install -r requirements.txt
```

This downloads Streamlit, pandas, and Plotly. Takes about a minute.

### Step 1.4 Run the dashboard

```bash
streamlit run app.py
```

Your default browser opens automatically with the dashboard running at
`http://localhost:8501`. Click around, change the filters, confirm
everything works.

When done, press `Ctrl+C` in the terminal to stop it.

---

## Part 2: Push the project to GitHub (15 minutes)

### Step 2.1 Create a GitHub account

If you do not have one, sign up at <https://github.com>. Free is fine.

### Step 2.2 Install Git

Download from <https://git-scm.com/downloads>. Use default settings.

Confirm with:

```bash
git --version
```

### Step 2.3 Create a new repository on GitHub

1. Go to <https://github.com/new>
2. Repository name: `infineon-distribution-dashboard`
3. Description: `Interactive dashboard analyzing Infineon Technologies revenue and global semiconductor distribution landscape`
4. Set to **Public**
5. **Do not** tick "Add a README file" - we already have one
6. Click "Create repository"

### Step 2.4 Push your code

GitHub shows you commands after you create the repo. The ones you need are
roughly these (run them inside your project folder in the terminal):

```bash
git init
git add .
git commit -m "Initial commit: distribution dashboard"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/infineon-distribution-dashboard.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

The first push asks for credentials. Use a personal access token, not your
password. Create one at <https://github.com/settings/tokens> with the
`repo` scope.

Refresh your GitHub repo page. You should see all the files.

---

## Part 3: Deploy to Streamlit Cloud (15 minutes)

### Step 3.1 Sign up for Streamlit Cloud

Go to <https://share.streamlit.io> and sign in with your GitHub account.
Free, no credit card needed.

### Step 3.2 Connect your repository

1. Click **"New app"**
2. Repository: select `YOUR-USERNAME/infineon-distribution-dashboard`
3. Branch: `main`
4. Main file path: `app.py`
5. Click **"Deploy"**

Streamlit installs the dependencies and starts the app. First deployment
takes about 2 to 3 minutes. You will see a build log on screen.

### Step 3.3 Get your public URL

When the build finishes, you get a URL like:

```
https://YOUR-USERNAME-infineon-distribution-dashboard-app-xyz123.streamlit.app
```

This is the link you put on your CV. Test it in an incognito browser to
confirm it loads for visitors.

---

## Part 4: Add the link to your CV

In your LaTeX CV, under the PROJECTS section, add a new entry like this:

```latex
\resumeOneRowHeading{Infineon Distribution Dashboard \href{https://share.streamlit.io/YOUR-LINK}{[Live Demo]} \href{https://github.com/YOUR-USERNAME/infineon-distribution-dashboard}{[GitHub]}}{\textit{2026 | Self-initiated}}
\resumeItemListStart
\resumeItem{Built an interactive Python and Streamlit dashboard consolidating Infineon's FY2020 to FY2024 revenue across regions and segments to surface distribution KPIs and Go-to-Market insights.}
\resumeItem{Conducted competitive research on the top 10 global electronic component distributors using public industry reports and visualised year-over-year shifts in channel leadership.}
\resumeItemListEnd
```

Adjust the wording to match your CV's existing style.

---

## Troubleshooting

**Streamlit Cloud says "App is in sleep mode"**
Free apps sleep after 7 days of no traffic. Visitors can wake them by
clicking once and waiting 30 seconds. Mention "Live demo (may take 30s
to wake)" on your CV if you want to manage expectations.

**Build fails with a package error**
Open `requirements.txt` and check the versions. Streamlit Cloud uses
Python 3.11 by default. If something breaks, remove version pins and
let pip pick the latest.

**Charts are blank**
Confirm the data files are inside the `data/` folder in the repo. The
`load_*` functions read from a relative path that depends on this.

**You changed something locally and want to redeploy**
Just push to GitHub. Streamlit Cloud auto-redeploys on every push to
the main branch.

---

## What to say in the interview

If a recruiter or hiring manager asks about this project, here is the
honest, defensible version:

> I wanted to demonstrate that I can do the kind of work the role
> describes, so I built a small dashboard using Infineon's public
> annual report data. I consolidated revenue figures by region and
> segment from FY2020 to FY2024, layered in industry data on the top
> global distributors, and added an illustrative partner KPI view to
> show how a distribution marketing team would track channel
> performance. The synthetic partner data is clearly flagged. The
> stack is Python with Streamlit and Plotly, hosted free on Streamlit
> Cloud. It took a weekend.

This is true, modest, and shows you know the difference between real
data and illustrative data. That is the kind of judgement an analyst
employer wants to see.
