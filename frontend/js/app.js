const API_BASE = "http://127.0.0.1:8000/api";

function getToken() {
  return localStorage.getItem("token");
}

function setAuthHeader(headers = {}) {
  const token = getToken();
  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }
  return headers;
}

async function apiRequest(path, options = {}) {
  const headers = setAuthHeader({ "Content-Type": "application/json", ...(options.headers || {}) });
  const response = await fetch(`${API_BASE}${path}`, { ...options, headers });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || "Request failed");
  }
  return data;
}

async function login(username, password) {
  const data = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  }).then((res) => res.json());
  if (!data.access_token) {
    throw new Error(data.detail || "Login failed");
  }
  localStorage.setItem("token", data.access_token);
  localStorage.setItem("role", data.role);
  localStorage.setItem("username", data.username);
  return data;
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "index.html";
}

function requireAuth() {
  const path = window.location.pathname;
  const isLoginPage = path.endsWith("/index.html") || path.endsWith("/login.html") || path.endsWith("index.html") || path.endsWith("login.html");
  if (!getToken() && !isLoginPage) {
    window.location.href = "index.html";
  }
}

if (document.getElementById("loginForm")) {
  document.getElementById("loginForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("loginMessage");
    try {
      await login(username, password);
      window.location.href = "dashboard.html";
    } catch (error) {
      message.textContent = error.message;
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const logoutBtn = document.getElementById("logoutBtn");
  if (logoutBtn) {
    logoutBtn.addEventListener("click", logout);
  }
});

document.addEventListener("click", (e) => {
  if (e.target && (e.target.id === "logoutBtn" || e.target.closest("#logoutBtn"))) {
    logout();
  }
});

requireAuth();
