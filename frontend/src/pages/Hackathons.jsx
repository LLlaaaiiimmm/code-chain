import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import { toast } from "sonner";
import {
  Boxes, Trophy, Calendar, Clock, Users, 
  DollarSign, ChevronRight, Shield, Zap,
  LogOut, User, CheckCircle
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

const Hackathons = ({ user, token, onLogout }) => {
  const [hackathons, setHackathons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [joining, setJoining] = useState(null);

  useEffect(() => {
    fetchHackathons();
  }, []);

  const fetchHackathons = async () => {
    try {
      const response = await axios.get(`${API}/hackathons`);
      setHackathons(response.data);
    } catch (error) {
      console.error("Error fetching hackathons:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleJoin = async (hackathonId) => {
    setJoining(hackathonId);
    try {
      await axios.post(
        `${API}/hackathons/${hackathonId}/join`,
        {},
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );
      toast.success("Successfully joined the hackathon!");
      fetchHackathons();
    } catch (error) {
      toast.error(error.response?.data?.detail || "Failed to join");
    } finally {
      setJoining(null);
    }
  };

  const getStatusBadge = (hackathon) => {
    const now = new Date();
    const start = new Date(hackathon.start_date);
    const end = new Date(hackathon.end_date);

    if (now < start) {
      return <Badge className="bg-blue-500/20 text-blue-400 border-blue-500/30">Upcoming</Badge>;
    } else if (now > end) {
      return <Badge className="bg-zinc-500/20 text-zinc-400 border-zinc-500/30">Completed</Badge>;
    } else {
      return <Badge className="bg-green-500/20 text-green-400 border-green-500/30">Active</Badge>;
    }
  };

  const formatDate = (dateStr) => {
    return new Date(dateStr).toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric"
    });
  };

  const getDaysUntil = (dateStr) => {
    const now = new Date();
    const target = new Date(dateStr);
    const diff = Math.ceil((target - now) / (1000 * 60 * 60 * 24));
    if (diff < 0) return "Ended";
    if (diff === 0) return "Today";
    if (diff === 1) return "Tomorrow";
    return `${diff} days`;
  };

  return (
    <div className="min-h-screen bg-background" data-testid="hackathons-page">
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
                <Link to="/hackathons" className="text-foreground font-medium">Hackathons</Link>
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
          <div className="text-center mb-12">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-purple-500/10 border border-purple-500/20 mb-6">
              <Trophy className="w-4 h-4 text-purple-400" />
              <span className="text-sm text-purple-400 font-medium">Compete & Win</span>
            </div>
            <h1 className="font-secondary text-4xl md:text-5xl font-bold mb-4">Hackathons</h1>
            <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
              Participate in sponsored competitions, solve real challenges, and win prizes from top blockchain companies.
            </p>
          </div>

          {/* Hackathons Tabs */}
          <Tabs defaultValue="all" className="w-full">
            <TabsList className="w-full justify-start mb-8 bg-card">
              <TabsTrigger value="all" className="flex-1 md:flex-none">All</TabsTrigger>
              <TabsTrigger value="active" className="flex-1 md:flex-none">Active</TabsTrigger>
              <TabsTrigger value="upcoming" className="flex-1 md:flex-none">Upcoming</TabsTrigger>
              <TabsTrigger value="completed" className="flex-1 md:flex-none">Completed</TabsTrigger>
            </TabsList>

            <TabsContent value="all">
              {loading ? (
                <div className="grid md:grid-cols-2 gap-6">
                  {[...Array(4)].map((_, i) => (
                    <div key={i} className="h-64 bg-card rounded-lg animate-pulse" />
                  ))}
                </div>
              ) : hackathons.length > 0 ? (
                <div className="grid md:grid-cols-2 gap-6">
                  {hackathons.map((hackathon, i) => (
                    <motion.div
                      key={hackathon.hackathon_id}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 0.3, delay: i * 0.1 }}
                    >
                      <Card className="bg-card border-border hover:border-purple-500/30 transition-all duration-300 h-full">
                        <CardContent className="p-6">
                          <div className="flex items-start justify-between mb-4">
                            <div className="flex items-center gap-3">
                              <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
                                {hackathon.title.includes("Security") ? (
                                  <Shield className="w-6 h-6 text-white" />
                                ) : (
                                  <Zap className="w-6 h-6 text-white" />
                                )}
                              </div>
                              <div>
                                <h3 className="font-secondary text-xl font-semibold">{hackathon.title}</h3>
                                {getStatusBadge(hackathon)}
                              </div>
                            </div>
                          </div>

                          <p className="text-muted-foreground text-sm mb-6 line-clamp-2">
                            {hackathon.description}
                          </p>

                          <div className="grid grid-cols-2 gap-4 mb-6">
                            <div className="flex items-center gap-2 text-sm">
                              <DollarSign className="w-4 h-4 text-primary" />
                              <span className="font-semibold text-primary">${hackathon.prize_pool?.toLocaleString()}</span>
                            </div>
                            <div className="flex items-center gap-2 text-sm text-muted-foreground">
                              <Users className="w-4 h-4" />
                              <span>{hackathon.participants?.length || 0} / {hackathon.max_participants}</span>
                            </div>
                            <div className="flex items-center gap-2 text-sm text-muted-foreground">
                              <Calendar className="w-4 h-4" />
                              <span>{formatDate(hackathon.start_date)}</span>
                            </div>
                            <div className="flex items-center gap-2 text-sm text-muted-foreground">
                              <Clock className="w-4 h-4" />
                              <span>{getDaysUntil(hackathon.start_date)}</span>
                            </div>
                          </div>

                          {hackathon.participants?.includes(user?.user_id) ? (
                            <Button className="w-full" variant="outline" disabled>
                              <CheckCircle className="w-4 h-4 mr-2" />
                              Registered
                            </Button>
                          ) : (
                            <Button
                              className="w-full glow-purple bg-purple-600 hover:bg-purple-700"
                              onClick={() => handleJoin(hackathon.hackathon_id)}
                              disabled={joining === hackathon.hackathon_id}
                              data-testid={`join-hackathon-${hackathon.hackathon_id}`}
                            >
                              {joining === hackathon.hackathon_id ? (
                                <>
                                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin mr-2" />
                                  Joining...
                                </>
                              ) : (
                                <>
                                  Register Now
                                  <ChevronRight className="w-4 h-4 ml-2" />
                                </>
                              )}
                            </Button>
                          )}
                        </CardContent>
                      </Card>
                    </motion.div>
                  ))}
                </div>
              ) : (
                <Card className="bg-card border-border">
                  <CardContent className="py-12 text-center">
                    <Trophy className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                    <h3 className="font-secondary text-xl font-semibold mb-2">No hackathons available</h3>
                    <p className="text-muted-foreground">Check back soon for new competitions!</p>
                  </CardContent>
                </Card>
              )}
            </TabsContent>

            <TabsContent value="active">
              <div className="text-center py-12">
                <Zap className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                <p className="text-muted-foreground">Active hackathons will appear here</p>
              </div>
            </TabsContent>

            <TabsContent value="upcoming">
              <div className="text-center py-12">
                <Calendar className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                <p className="text-muted-foreground">Upcoming hackathons will appear here</p>
              </div>
            </TabsContent>

            <TabsContent value="completed">
              <div className="text-center py-12">
                <Trophy className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                <p className="text-muted-foreground">Completed hackathons will appear here</p>
              </div>
            </TabsContent>
          </Tabs>
        </motion.div>
      </main>
    </div>
  );
};

export default Hackathons;
