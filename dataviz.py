import matplotlib.pyplot as plt

# Your grades over time

lessons = [ "Week 1", "Week 2", "Week 3", "Week 4", "Week 5" ]
grades = [85, 90, 78, 92, 88]

plt.figure(figsize=(10,6))
plt.plot(lessons, grades, color="#1D9E75", linewidth=2, marker="o", markersize=8)
plt.fill_between(lessons, grades, alpha=0.1, color="#1D9E75")

plt.title("My Learning Progress", fontsize=16)
plt.xlabel("Week")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Bar Chart
subjects = ["Python", "Flask", "git", "APIs", "React", "Databases"]
scores = [90, 85, 80, 88, 92, 87]

plt.figure(figsize=(10,6))
plt.bar(subjects, scores, color="#1D9E75", alpha=0.8)

plt.title("Skills Progress", fontsize=16)
plt.xlabel("Skill")
plt.ylabel("Confidence Level")
plt.ylim(0, 100)

for i, score in enumerate(scores):
    plt.text(i, score + 1, str(score), ha="center", fontsize=11)

plt.tight_layout()
plt.show()

# Pie chart - time spent on each topic
topics = ["Python", "Web Dev", "Git & APIs", "AI Engineering", "Projects"]
time_spent = [35, 25, 20, 10, 10]
colors = ["#1D9E75", "#3498db", "#e74c3c", "#9b59b6", "#f39c12"]

plt.figure(figsize=(8, 8))
plt.pie(time_spent, labels=topics, colors=colors, autopct="%1.1f%%", startangle=90)
plt.title("Time Spent Learning", fontsize=16)

plt.tight_layout()
plt.show()