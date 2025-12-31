import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger, DialogDescription } from "../components/ui/dialog";
import { toast } from "sonner";
import {
  Boxes, Award, Trophy, Shield, Zap, Star, LogOut, User,
  ExternalLink, Copy, CheckCircle, Lock
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import { API } from "../App";

const Certificates = ({ user, token, onLogout }) => {
  const [certificates, setCertificates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [minting, setMinting] = useState(false);
  const [selectedCert, setSelectedCert] = useState(null);

  useEffect(() => {
    fetchCertificates();
  }, []);

  const fetchCertificates = async () => {
    try {
      const response = await axios.get(`${API}/certificates`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setCertificates(response.data);
    } catch (error) {
      console.error("Error fetching certificates:", error);
    } finally {
      setLoading(false);
    }
  };

  const availableCertificates = [
    {
      id: "problem_master",
      name: "Problem Master",
      description: "Complete 50+ problems with 1500+ ELO rating",
      icon: <Trophy className="w-8 h-8 text-yellow-400" />,
      requirements: { min_problems: 50, min_rating: 1500 },
      color: "from-yellow-500/20 to-orange-500/20 border-yellow-500/30"
    },
    {
      id: "expert_rating",
      name: "Elite Developer",
      description: "Achieve 2000+ ELO rating",
      icon: <Star className="w-8 h-8 text-purple-400" />,
      requirements: { min_rating: 2000 },
      color: "from-purple-500/20 to-pink-500/20 border-purple-500/30"
    },
    {
      id: "security_expert",
      name: "Security Expert",
      description: "Master 20+ security challenges",
      icon: <Shield className="w-8 h-8 text-blue-400" />,
      requirements: { category: "security", min_problems: 20 },
      color: "from-blue-500/20 to-cyan-500/20 border-blue-500/30"
    },
    {
      id: "gas_optimizer",
      name: "Gas Optimizer",
      description: "Complete 15+ optimization challenges",
      icon: <Zap className="w-8 h-8 text-green-400" />,
      requirements: { category: "optimization", min_problems: 15 },
      color: "from-green-500/20 to-emerald-500/20 border-green-500/30"
    }
  ];

  const checkEligibility = (cert) => {
    const reqs = cert.requirements;
    if (reqs.min_problems && user?.problems_solved < reqs.min_problems) return false;
    if (reqs.min_rating && user?.elo_rating < reqs.min_rating) return false;
    return true;
  };

  const handleMint = async (certType) => {
    if (user?.subscription !== "expert") {
      toast.error("Expert subscription required for NFT certificates");
      return;
    }

    setMinting(true);
    try {
      const response = await axios.post(
        `${API}/certificates/mint`,
        {
          certificate_type: certType,
          metadata: {}
        },
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );

      toast.success("Certificate minted successfully!");
      setCertificates([...certificates, response.data]);
    } catch (error) {
      toast.error(error.response?.data?.detail || "Failed to mint certificate");
    } finally {
      setMinting(false);
    }
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    toast.success("Copied to clipboard!");
  };

  const formatDate = (dateStr) => {
    return new Date(dateStr).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 glass border-b border-border">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-8">
              <Link to="/" className="flex items-center gap-2">
                <Boxes className="w-8 h-8 text-primary" />
                <span className="font-secondary text-xl font-bold">CodeChain</span>
              </Link>
              
              <div className="hidden md:flex items-center gap-6">
                <Link to="/dashboard" className="text-muted-foreground hover:text-foreground transition-colors">Dashboard</Link>
                <Link to="/problems" className="text-muted-foreground hover:text-foreground transition-colors">Problems</Link>
                <Link to="/leaderboard" className="text-muted-foreground hover:text-foreground transition-colors">Leaderboard</Link>
                <Link to="/certificates" className="text-foreground font-medium">Certificates</Link>
              </div>
            </div>

            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="flex items-center gap-2">
                  <Avatar className="w-8 h-8">
                    <AvatarImage src={user?.picture} />
                    <AvatarFallback className="bg-primary/20 text-primary">
                      {user?.name?.charAt(0) || "U"}
                    </AvatarFallback>
                  </Avatar>
                  <span className="hidden md:inline">{user?.name}</span>
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" className="w-56">
                <DropdownMenuItem asChild>
                  <Link to="/profile" className="flex items-center gap-2">
                    <User className="w-4 h-4" />
                    Profile
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={onLogout} className="text-red-400">
                  <LogOut className="w-4 h-4 mr-2" />
                  Logout
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
        >
          {/* Header */}
          <div className="mb-8">
            <div className="flex items-center gap-3 mb-2">
              <Award className="w-8 h-8 text-primary" />
              <h1 className="font-secondary text-3xl font-bold">NFT Certificates</h1>
            </div>
            <p className="text-muted-foreground">
              Earn verifiable on-chain credentials for your blockchain development achievements
            </p>
          </div>

          {user?.subscription !== "expert" && (
            <Card className="mb-8 border-yellow-500/30 bg-yellow-500/5">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-yellow-400">
                  <Lock className="w-5 h-5" />
                  Expert Subscription Required
                </CardTitle>
                <CardDescription>
                  Upgrade to Expert plan to mint NFT certificates on Polygon blockchain
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Link to="/pricing">
                  <Button className="glow-primary">
                    Upgrade to Expert
                  </Button>
                </Link>
              </CardContent>
            </Card>
          )}

          {/* My Certificates */}
          {certificates.length > 0 && (
            <div className="mb-12">
              <h2 className="font-secondary text-2xl font-bold mb-4">My Certificates</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {certificates.map((cert) => (
                  <Dialog key={cert.certificate_id}>
                    <DialogTrigger asChild>
                      <motion.div
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                      >
                        <Card className={`cursor-pointer bg-gradient-to-br ${availableCertificates.find(c => c.id === cert.type)?.color || 'from-zinc-900/50 to-zinc-800/50'} border hover:shadow-lg transition-all`}>
                          <CardHeader>
                            <div className="flex items-start justify-between">
                              {availableCertificates.find(c => c.id === cert.type)?.icon || <Award className="w-8 h-8" />}
                              <Badge className="bg-green-500/20 text-green-400 border-green-500/30">
                                <CheckCircle className="w-3 h-3 mr-1" />
                                Minted
                              </Badge>
                            </div>
                            <CardTitle className="mt-4">
                              {availableCertificates.find(c => c.id === cert.type)?.name || cert.type}
                            </CardTitle>
                            <CardDescription>
                              Issued {formatDate(cert.created_at)}
                            </CardDescription>
                          </CardHeader>
                          <CardContent>
                            <div className="space-y-2 text-sm">
                              <div className="flex items-center gap-2 text-muted-foreground">
                                <span>Token ID:</span>
                                <code className="text-primary">{cert.token_id}</code>
                              </div>
                              <div className="flex items-center gap-2 text-muted-foreground">
                                <span>Blockchain:</span>
                                <Badge variant="outline" className="text-xs">{cert.blockchain}</Badge>
                              </div>
                            </div>
                          </CardContent>
                        </Card>
                      </motion.div>
                    </DialogTrigger>
                    <DialogContent className="max-w-2xl">
                      <DialogHeader>
                        <DialogTitle className="flex items-center gap-2">
                          {availableCertificates.find(c => c.id === cert.type)?.icon}
                          {availableCertificates.find(c => c.id === cert.type)?.name}
                        </DialogTitle>
                        <DialogDescription>
                          Certificate Details
                        </DialogDescription>
                      </DialogHeader>
                      <div className="space-y-4">
                        <div className="grid grid-cols-2 gap-4">
                          <div>
                            <label className="text-sm text-muted-foreground">Certificate ID</label>
                            <div className="flex items-center gap-2 mt-1">
                              <code className="text-sm bg-zinc-900 px-2 py-1 rounded">{cert.certificate_id}</code>
                              <Button
                                variant="ghost"
                                size="sm"
                                onClick={() => copyToClipboard(cert.certificate_id)}
                              >
                                <Copy className="w-4 h-4" />
                              </Button>
                            </div>
                          </div>
                          <div>
                            <label className="text-sm text-muted-foreground">Token ID</label>
                            <div className="flex items-center gap-2 mt-1">
                              <code className="text-sm bg-zinc-900 px-2 py-1 rounded">{cert.token_id}</code>
                              <Button
                                variant="ghost"
                                size="sm"
                                onClick={() => copyToClipboard(cert.token_id.toString())}
                              >
                                <Copy className="w-4 h-4" />
                              </Button>
                            </div>
                          </div>
                        </div>
                        
                        <div>
                          <label className="text-sm text-muted-foreground">Transaction Hash</label>
                          <div className="flex items-center gap-2 mt-1">
                            <code className="text-xs bg-zinc-900 px-2 py-1 rounded flex-1 overflow-hidden text-ellipsis">
                              {cert.transaction_hash}
                            </code>
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => copyToClipboard(cert.transaction_hash)}
                            >
                              <Copy className="w-4 h-4" />
                            </Button>
                            <Button
                              variant="ghost"
                              size="sm"
                              asChild
                            >
                              <a
                                href={`https://polygonscan.com/tx/${cert.transaction_hash}`}
                                target="_blank"
                                rel="noopener noreferrer"
                              >
                                <ExternalLink className="w-4 h-4" />
                              </a>
                            </Button>
                          </div>
                        </div>

                        <div>
                          <label className="text-sm text-muted-foreground">Contract Address</label>
                          <div className="flex items-center gap-2 mt-1">
                            <code className="text-xs bg-zinc-900 px-2 py-1 rounded flex-1">
                              {cert.contract_address}
                            </code>
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => copyToClipboard(cert.contract_address)}
                            >
                              <Copy className="w-4 h-4" />
                            </Button>
                          </div>
                        </div>

                        <div className="grid grid-cols-3 gap-4 pt-4 border-t">
                          <div>
                            <label className="text-sm text-muted-foreground">Problems Solved</label>
                            <p className="text-2xl font-bold text-primary">{cert.metadata?.problems_solved}</p>
                          </div>
                          <div>
                            <label className="text-sm text-muted-foreground">ELO Rating</label>
                            <p className="text-2xl font-bold text-primary">{cert.metadata?.elo_rating}</p>
                          </div>
                          <div>
                            <label className="text-sm text-muted-foreground">Issue Date</label>
                            <p className="text-sm font-medium">{formatDate(cert.metadata?.issue_date)}</p>
                          </div>
                        </div>
                      </div>
                    </DialogContent>
                  </Dialog>
                ))}
              </div>
            </div>
          )}

          {/* Available Certificates */}
          <div>
            <h2 className="font-secondary text-2xl font-bold mb-4">Available Certificates</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {availableCertificates.map((cert) => {
                const eligible = checkEligibility(cert);
                const alreadyMinted = certificates.some(c => c.type === cert.id);

                return (
                  <motion.div
                    key={cert.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    whileHover={eligible && !alreadyMinted ? { scale: 1.02 } : {}}
                  >
                    <Card className={`bg-gradient-to-br ${cert.color} border ${!eligible || alreadyMinted ? 'opacity-60' : ''}`}>
                      <CardHeader>
                        <div className="flex items-start justify-between">
                          {cert.icon}
                          {alreadyMinted && (
                            <Badge className="bg-green-500/20 text-green-400 border-green-500/30">
                              <CheckCircle className="w-3 h-3 mr-1" />
                              Owned
                            </Badge>
                          )}
                        </div>
                        <CardTitle className="mt-4">{cert.name}</CardTitle>
                        <CardDescription>{cert.description}</CardDescription>
                      </CardHeader>
                      <CardContent>
                        <div className="space-y-3">
                          <div className="text-sm">
                            <p className="text-muted-foreground mb-2">Requirements:</p>
                            <ul className="space-y-1">
                              {cert.requirements.min_problems && (
                                <li className="flex items-center gap-2">
                                  <CheckCircle className={`w-4 h-4 ${user?.problems_solved >= cert.requirements.min_problems ? 'text-green-400' : 'text-zinc-600'}`} />
                                  <span className={user?.problems_solved >= cert.requirements.min_problems ? 'text-foreground' : 'text-muted-foreground'}>
                                    {cert.requirements.min_problems}+ problems solved ({user?.problems_solved || 0})
                                  </span>
                                </li>
                              )}
                              {cert.requirements.min_rating && (
                                <li className="flex items-center gap-2">
                                  <CheckCircle className={`w-4 h-4 ${user?.elo_rating >= cert.requirements.min_rating ? 'text-green-400' : 'text-zinc-600'}`} />
                                  <span className={user?.elo_rating >= cert.requirements.min_rating ? 'text-foreground' : 'text-muted-foreground'}>
                                    {cert.requirements.min_rating}+ ELO rating ({user?.elo_rating || 1200})
                                  </span>
                                </li>
                              )}
                            </ul>
                          </div>

                          <Button
                            className="w-full"
                            disabled={!eligible || alreadyMinted || minting || user?.subscription !== "expert"}
                            onClick={() => handleMint(cert.id)}
                          >
                            {alreadyMinted ? "Already Minted" : minting ? "Minting..." : eligible ? "Mint NFT" : "Requirements Not Met"}
                          </Button>
                        </div>
                      </CardContent>
                    </Card>
                  </motion.div>
                );
              })}
            </div>
          </div>
        </motion.div>
      </main>
    </div>
  );
};

export default Certificates;
