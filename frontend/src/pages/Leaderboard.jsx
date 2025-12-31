import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import { 
  Boxes, Trophy, Medal, TrendingUp, Crown, 
  Star, ChevronRight, Users
} from "lucide-react";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import { API } from "../App";

const Leaderboard = ({ user, token }) => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [userRank, setUserRank] = useState(null);

  useEffect(() => {
    fetchLeaderboard();
    if (user) {
      fetchUserRank();
    }
  }, [user]);

  const fetchLeaderboard = async () => {
    try {
      const response = await axios.get(`${API}/leaderboard?limit=100`);
      setLeaderboard(response.data);
    } catch (error) {
      console.error("Error fetching leaderboard:", error);
    } finally {
      setLoading(false);
    }
  };

  const fetchUserRank = async () => {
    if (!user?.user_id) return;
    try {
      const response = await axios.get(`${API}/leaderboard/user/${user.user_id}`);
      setUserRank(response.data);
    } catch (error) {
      console.error("Error fetching user rank:", error);
    }
  };

  const getRankIcon = (rank) => {
    if (rank === 1) return <Crown className="w-5 h-5 text-yellow-400" />;
    if (rank === 2) return <Medal className="w-5 h-5 text-zinc-300" />;
    if (rank === 3) return <Medal className="w-5 h-5 text-orange-400" />;
    return <span className="text-muted-foreground font-mono">#{rank}</span>;
  };

  const getRankBg = (rank) => {
    if (rank === 1) return "bg-yellow-500/10 border-yellow-500/30";
    if (rank === 2) return "bg-zinc-400/10 border-zinc-400/30";
    if (rank === 3) return "bg-orange-500/10 border-orange-500/30";
    return "bg-card border-border";
  };

  return (
    <div className="min-h-screen bg-background" data-testid="leaderboard-page">
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
                {user ? (
                  <>
                    <Link to="/dashboard" className="text-muted-foreground hover:text-foreground transition-colors">Dashboard</Link>
                    <Link to="/problems" className="text-muted-foreground hover:text-foreground transition-colors">Problems</Link>
                  </>
                ) : null}
                <Link to="/leaderboard" className="text-foreground font-medium">Leaderboard</Link>
                <Link to="/hackathons" className="text-muted-foreground hover:text-foreground transition-colors">Hackathons</Link>
              </div>
            </div>

            {user ? (
              <Link to="/profile">
                <Button variant="ghost" className="flex items-center gap-2">
                  <Avatar className="w-8 h-8">
                    <AvatarImage src={user?.picture} />
                    <AvatarFallback className="bg-primary/20 text-primary">
                      {user?.name?.charAt(0) || "U"}
                    </AvatarFallback>
                  </Avatar>
                  <span className="hidden md:inline">{user?.name}</span>
                </Button>
              </Link>
            ) : (
              <div className="flex items-center gap-3">
                <Link to="/login">
                  <Button variant="ghost">Login</Button>
                </Link>
                <Link to="/register">
                  <Button className="glow-primary">Get Started</Button>
                </Link>
              </div>
            )}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
        >
          {/* Header */}
          <div className="text-center mb-12">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-6">
              <Trophy className="w-4 h-4 text-primary" />
              <span className="text-sm text-primary font-medium">Global Rankings</span>
            </div>
            <h1 className="font-secondary text-4xl md:text-5xl font-bold mb-4">Leaderboard</h1>
            <p className="text-muted-foreground text-lg">Top blockchain developers worldwide</p>
          </div>

          {/* User's Rank Card */}
          {user && userRank && (
            <Card className="mb-8 bg-primary/5 border-primary/20">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center">
                      <Star className="w-6 h-6 text-primary" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Your Rank</p>
                      <p className="font-secondary text-2xl font-bold">#{userRank.rank}</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="text-sm text-muted-foreground">ELO Rating</p>
                    <p className="font-secondary text-2xl font-bold text-primary">{userRank.elo_rating}</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          )}

          {/* Leaderboard Tabs */}
          <Tabs defaultValue="global" className="w-full">
            <TabsList className="w-full justify-start mb-6 bg-card">
              <TabsTrigger value="global" className="flex-1 md:flex-none">
                <Users className="w-4 h-4 mr-2" />
                Global
              </TabsTrigger>
              <TabsTrigger value="solidity" className="flex-1 md:flex-none">Solidity</TabsTrigger>
              <TabsTrigger value="weekly" className="flex-1 md:flex-none">This Week</TabsTrigger>
            </TabsList>

            <TabsContent value="global">
              {loading ? (
                <div className="space-y-3">
                  {[...Array(10)].map((_, i) => (
                    <div key={i} className="h-16 bg-card rounded-lg animate-pulse" />
                  ))}
                </div>
              ) : (
                <div className="space-y-3">
                  {/* Top 3 */}
                  <div className="grid md:grid-cols-3 gap-4 mb-6">
                    {leaderboard.slice(0, 3).map((entry, i) => (
                      <motion.div
                        key={entry.user_id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.3, delay: i * 0.1 }}
                      >
                        <Card className={`border ${getRankBg(entry.rank)} ${i === 0 ? "md:col-span-1 md:scale-105" : ""}`}>
                          <CardContent className="p-6 text-center">
                            <div className="mb-3">
                              {getRankIcon(entry.rank)}
                            </div>
                            <Avatar className="w-16 h-16 mx-auto mb-3">
                              <AvatarImage src={entry.picture} />
                              <AvatarFallback className="bg-primary/20 text-primary text-xl">
                                {entry.name?.charAt(0) || "?"}
                              </AvatarFallback>
                            </Avatar>
                            <h3 className="font-secondary font-semibold mb-1">{entry.name}</h3>
                            <p className="text-2xl font-bold text-primary mb-1">{entry.elo_rating}</p>
                            <p className="text-sm text-muted-foreground">{entry.problems_solved} solved</p>
                          </CardContent>
                        </Card>
                      </motion.div>
                    ))}
                  </div>

                  {/* Rest of leaderboard */}
                  {leaderboard.slice(3).map((entry, i) => (
                    <motion.div
                      key={entry.user_id}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ duration: 0.3, delay: (i + 3) * 0.03 }}
                    >
                      <Card className="bg-card border-border hover:border-primary/30 transition-colors">
                        <CardContent className="p-4">
                          <div className="flex items-center justify-between">
                            <div className="flex items-center gap-4">
                              <span className="w-10 text-center font-mono text-muted-foreground">
                                #{entry.rank}
                              </span>
                              <Avatar className="w-10 h-10">
                                <AvatarImage src={entry.picture} />
                                <AvatarFallback className="bg-primary/20 text-primary">
                                  {entry.name?.charAt(0) || "?"}
                                </AvatarFallback>
                              </Avatar>
                              <div>
                                <p className="font-medium">{entry.name}</p>
                                <p className="text-sm text-muted-foreground">{entry.problems_solved} problems solved</p>
                              </div>
                            </div>
                            <div className="text-right">
                              <p className="font-secondary text-lg font-bold text-primary">{entry.elo_rating}</p>
                              <p className="text-xs text-muted-foreground">ELO</p>
                            </div>
                          </div>
                        </CardContent>
                      </Card>
                    </motion.div>
                  ))}
                </div>
              )}
            </TabsContent>

            <TabsContent value="solidity">
              <div className="text-center py-12">
                <Trophy className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                <p className="text-muted-foreground">Solidity-specific rankings coming soon</p>
              </div>
            </TabsContent>

            <TabsContent value="weekly">
              <div className="text-center py-12">
                <TrendingUp className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                <p className="text-muted-foreground">Weekly rankings coming soon</p>
              </div>
            </TabsContent>
          </Tabs>
        </motion.div>
      </main>
    </div>
  );
};

export default Leaderboard;
