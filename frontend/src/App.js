import { useEffect, useState, useRef } from "react";
import { BrowserRouter, Routes, Route, Navigate, useLocation, useNavigate } from "react-router-dom";
import axios from "axios";
import { Toaster } from "./components/ui/sonner";

// Pages
import Landing from "./pages/Landing";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Problems from "./pages/Problems";
import ProblemSolver from "./pages/ProblemSolver";
import Leaderboard from "./pages/Leaderboard";
import Profile from "./pages/Profile";
import Hackathons from "./pages/Hackathons";
import Pricing from "./pages/Pricing";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;

// Auth Context
export const AuthContext = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [token, setToken] = useState(localStorage.getItem("token"));

  const checkAuth = async () => {
    try {
      const response = await axios.get(`${API}/auth/me`, {
        withCredentials: true,
        headers: token ? { Authorization: `Bearer ${token}` } : {}
      });
      setUser(response.data);
    } catch (error) {
      setUser(null);
      localStorage.removeItem("token");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkAuth();
  }, [token]);

  const login = (userData, authToken) => {
    setUser(userData);
    if (authToken) {
      setToken(authToken);
      localStorage.setItem("token", authToken);
    }
  };

  const logout = async () => {
    try {
      await axios.post(`${API}/auth/logout`, {}, { withCredentials: true });
    } catch (e) {
      console.error(e);
    }
    setUser(null);
    setToken(null);
    localStorage.removeItem("token");
  };

  return children({ user, loading, login, logout, token, checkAuth });
};

// Auth Callback for Google OAuth
// REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
const AuthCallback = ({ onLogin }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const hasProcessed = useRef(false);

  useEffect(() => {
    if (hasProcessed.current) return;
    hasProcessed.current = true;

    const processSession = async () => {
      const hash = location.hash;
      const sessionId = new URLSearchParams(hash.replace('#', '?')).get('session_id');
      
      if (sessionId) {
        try {
          const response = await axios.get(`${API}/auth/session`, {
            headers: { "X-Session-ID": sessionId },
            withCredentials: true
          });
          onLogin(response.data);
          navigate("/dashboard", { replace: true, state: { user: response.data } });
        } catch (error) {
          console.error("Auth error:", error);
          navigate("/login", { replace: true });
        }
      } else {
        navigate("/login", { replace: true });
      }
    };

    processSession();
  }, []);

  return (
    <div className="min-h-screen bg-background flex items-center justify-center">
      <div className="text-center">
        <div className="w-8 h-8 border-2 border-primary border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p className="text-muted-foreground">Authenticating...</p>
      </div>
    </div>
  );
};

// Protected Route
const ProtectedRoute = ({ children, user, loading }) => {
  const location = useLocation();

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="w-8 h-8 border-2 border-primary border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
};

// App Router
const AppRouter = ({ user, loading, login, logout, token }) => {
  const location = useLocation();

  // Check for session_id in URL hash (Google OAuth callback)
  if (location.hash?.includes('session_id=')) {
    return <AuthCallback onLogin={login} />;
  }

  return (
    <Routes>
      <Route path="/" element={<Landing user={user} />} />
      <Route path="/login" element={user ? <Navigate to="/dashboard" /> : <Login onLogin={login} />} />
      <Route path="/register" element={user ? <Navigate to="/dashboard" /> : <Register onLogin={login} />} />
      <Route path="/pricing" element={<Pricing user={user} />} />
      <Route path="/leaderboard" element={<Leaderboard user={user} token={token} />} />
      
      <Route path="/dashboard" element={
        <ProtectedRoute user={user} loading={loading}>
          <Dashboard user={user} token={token} onLogout={logout} />
        </ProtectedRoute>
      } />
      <Route path="/problems" element={
        <ProtectedRoute user={user} loading={loading}>
          <Problems user={user} token={token} onLogout={logout} />
        </ProtectedRoute>
      } />
      <Route path="/problems/:problemId" element={
        <ProtectedRoute user={user} loading={loading}>
          <ProblemSolver user={user} token={token} onLogout={logout} />
        </ProtectedRoute>
      } />
      <Route path="/hackathons" element={
        <ProtectedRoute user={user} loading={loading}>
          <Hackathons user={user} token={token} onLogout={logout} />
        </ProtectedRoute>
      } />
      <Route path="/profile" element={
        <ProtectedRoute user={user} loading={loading}>
          <Profile user={user} token={token} onLogout={logout} />
        </ProtectedRoute>
      } />
      <Route path="/profile/:userId" element={
        <Profile user={user} token={token} onLogout={logout} />
      } />
      
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
};

function App() {
  return (
    <AuthContext>
      {(authProps) => (
        <BrowserRouter>
          <Toaster position="top-right" theme="dark" />
          <AppRouter {...authProps} />
        </BrowserRouter>
      )}
    </AuthContext>
  );
}

export default App;
