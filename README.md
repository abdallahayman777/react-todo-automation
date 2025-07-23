# React Todo Automation

This project contains automated UI and API tests for a simple full-stack React + Node.js Todo app.

## 🧪 What’s Tested

### ✅ UI Tests (with Playwright & Python)
- Login with valid/invalid credentials
- Create a new todo
- Edit an existing todo
- Delete a todo
- Assert expected UI behavior

### ✅ API Tests (with Postman & Newman)
- POST `/login`
- GET `/todos`
- POST `/todos`
- PUT `/todos/:id`
- DELETE `/todos/:id`

Includes both **positive** and **negative** test cases.

---

## 🚀 How to Run Tests

### 📦 UI Tests
1. Install Python & Playwright
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
