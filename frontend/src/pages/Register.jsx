import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Label } from "../components/ui/label";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../components/ui/card";
import { toast } from "sonner";
import { Boxes, Mail, Lock, User, Loader2, Wallet } from "lucide-react";
import { API } from "../App";
import { ethers } from "ethers";

const Register = ({ onLogin }) => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [metamaskLoading, setMetamaskLoading] = useState(false);
  const [showNameInput, setShowNameInput] = useState(false);
  const [metamaskName, setMetamaskName] = useState("");
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: ""
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.password.length < 6) {
      toast.error("Password must be at least 6 characters");
      return;
    }
    
    setLoading(true);

    try {
      const response = await axios.post(`${API}/auth/register`, formData);
      onLogin(response.data.user, response.data.token);
      toast.success("Account created successfully!");
      navigate("/dashboard");
    } catch (error) {
      toast.error(error.response?.data?.detail || "Registration failed");
    } finally {
      setLoading(false);
    }
  };

  const handleMetaMaskSignup = async (name = null) => {
    setMetamaskLoading(true);

    try {
      // Check if MetaMask is installed
      if (!window.ethereum) {
        toast.error("Please install MetaMask to use this feature");
        setMetamaskLoading(false);
        return;
      }

      // Request account access
      const provider = new ethers.BrowserProvider(window.ethereum);
      const accounts = await provider.send("eth_requestAccounts", []);
      const walletAddress = accounts[0];

      // If name is not provided, show name input
      if (name === null && !showNameInput) {
        setShowNameInput(true);
        setMetamaskLoading(false);
        return;
      }

      // Create message to sign
      const message = `Sign this message to create an account on CodeChain.\n\nWallet: ${walletAddress}\nTimestamp: ${Date.now()}`;

      // Request signature
      const signer = await provider.getSigner();
      const signature = await signer.signMessage(message);

      // Send to backend
      const response = await axios.post(`${API}/auth/metamask`, {
        wallet_address: walletAddress,
        signature: signature,
        message: message,
        name: name || metamaskName || undefined
      });

      onLogin(response.data.user, response.data.token);
      toast.success("Account created with MetaMask!");
      navigate("/dashboard");
    } catch (error) {
      console.error("MetaMask auth error:", error);
      if (error.code === 4001) {
        toast.error("MetaMask connection rejected");
      } else {
        toast.error(error.response?.data?.detail || "MetaMask authentication failed");
      }
    } finally {
      setMetamaskLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-4 relative overflow-hidden">
      {/* Background effects */}
      <div className="noise-overlay fixed inset-0 pointer-events-none z-0" />
      <div className="grid-pattern fixed inset-0 pointer-events-none z-0 opacity-30" />
      
      {/* Glow effects */}
      <div className="absolute top-1/4 right-1/4 w-96 h-96 bg-primary/20 rounded-full blur-3xl opacity-20" />
      <div className="absolute bottom-1/4 left-1/4 w-96 h-96 bg-purple-500/20 rounded-full blur-3xl opacity-20" />

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="w-full max-w-md relative z-10"
      >
        <div className="text-center mb-8">
          <Link to="/" className="inline-flex items-center gap-2 mb-6">
            <Boxes className="w-10 h-10 text-primary" />
            <span className="font-secondary text-2xl font-bold">CodeChain</span>
          </Link>
        </div>

        <Card className="bg-card/80 backdrop-blur border-border">
          <CardHeader className="text-center pb-2">
            <CardTitle className="font-secondary text-2xl">Create Account</CardTitle>
            <CardDescription>Join the Web3 developer community</CardDescription>
          </CardHeader>
          
          <CardContent className="space-y-6">
            {/* MetaMask */}
            <div className="space-y-3">
              <Button
                variant="outline"
                className="w-full h-12 text-base"
                onClick={() => handleMetaMaskSignup()}
                disabled={metamaskLoading}
                data-testid="metamask-signup-btn"
              >
                {metamaskLoading ? (
                  <>
                    <Loader2 className="w-5 h-5 mr-3 animate-spin" />
                    Connecting...
                  </>
                ) : (
                  <>
                    <Wallet className="w-5 h-5 mr-3" />
                    Connect with MetaMask
                  </>
                )}
              </Button>

              {/* Optional name input for MetaMask */}
              {showNameInput && (
                <motion.div
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  className="space-y-2"
                >
                  <Label htmlFor="metamask-name">Name (Optional)</Label>
                  <div className="flex gap-2">
                    <Input
                      id="metamask-name"
                      type="text"
                      placeholder="Enter your name"
                      className="h-12"
                      value={metamaskName}
                      onChange={(e) => setMetamaskName(e.target.value)}
                    />
                    <Button
                      onClick={() => handleMetaMaskSignup(metamaskName)}
                      disabled={metamaskLoading}
                      className="h-12"
                    >
                      Continue
                    </Button>
                  </div>
                </motion.div>
              )}
            </div>

            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-border"></div>
              </div>
              <div className="relative flex justify-center text-xs">
                <span className="bg-card px-4 text-muted-foreground">or continue with email</span>
              </div>
            </div>

            {/* Registration Form */}
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="name">Name</Label>
                <div className="relative">
                  <User className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
                  <Input
                    id="name"
                    type="text"
                    placeholder="Satoshi Nakamoto"
                    className="pl-10 h-12"
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                    required
                    data-testid="register-name-input"
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <div className="relative">
                  <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
                  <Input
                    id="email"
                    type="email"
                    placeholder="developer@example.com"
                    className="pl-10 h-12"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    required
                    data-testid="register-email-input"
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="password">Password</Label>
                <div className="relative">
                  <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
                  <Input
                    id="password"
                    type="password"
                    placeholder="••••••••"
                    className="pl-10 h-12"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                    required
                    minLength={6}
                    data-testid="register-password-input"
                  />
                </div>
                <p className="text-xs text-muted-foreground">Minimum 6 characters</p>
              </div>

              <Button
                type="submit"
                className="w-full h-12 text-base glow-primary"
                disabled={loading}
                data-testid="register-submit-btn"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                    Creating account...
                  </>
                ) : (
                  "Create Account"
                )}
              </Button>
            </form>

            <p className="text-center text-sm text-muted-foreground">
              Already have an account?{" "}
              <Link to="/login" className="text-primary hover:underline" data-testid="login-link">
                Sign in
              </Link>
            </p>
          </CardContent>
        </Card>
      </motion.div>
    </div>
  );
};

export default Register;
