import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Progress } from "../components/ui/progress";
import { Badge } from "../components/ui/badge";
import { 
  Boxes, Code2, Trophy, TrendingUp, Target, 
  ChevronRight, Clock, CheckCircle, XCircle,
  LogOut, User, Settings, Flame, Award, BarChart3
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import { DailyChallenges } from "../components/DailyChallenges";
import { PersonalInsights } from "../components/PersonalInsights";
import { RecommendedProblems } from "../components/RecommendedProblems";
import { NotificationCenter } from "../components/NotificationCenter";
import RankProgress from "../components/RankProgress";
import { API } from "../App";

const Dashboard = ({ user, token, onLogout }) => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboardStats();
  }, []);

  const fetchDashboardStats = async () => {
    try {
      const response = await axios.get(`${API}/stats/dashboard`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setStats(response.data);
    } catch (error) {
      console.error("Error fetching stats:", error);
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = (difficulty) => {
    const colors = {
      junior: "text-green-400",
      middle: "text-yellow-400",
      senior: "text-orange-400",
      expert: "text-red-400"
    };
    return colors[difficulty] || "text-zinc-400";
  };

  const getStatusIcon = (status) => {
    return status === "passed" ? (
      <CheckCircle className="w-4 h-4 text-green-400" />
    ) : (
      <XCircle className="w-4 h-4 text-red-400" />
    );
  };

  return (
    <div className="min-h-screen bg-background" data-testid="dashboard-page">
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
                <Link to="/dashboard" className="text-foreground font-medium">Dashboard</Link>
                <Link to="/problems" className="text-muted-foreground hover:text-foreground transition-colors">Problems</Link>
                <Link to="/leaderboard" className="text-muted-foreground hover:text-foreground transition-colors">Leaderboard</Link>
                <Link to="/achievements" className="text-muted-foreground hover:text-foreground transition-colors">Achievements</Link>
                <Link to="/analytics" className="text-muted-foreground hover:text-foreground transition-colors">Analytics</Link>
                <Link to="/hackathons" className="text-muted-foreground hover:text-foreground transition-colors">Hackathons</Link>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <NotificationCenter token={token} />
              
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" className="flex items-center gap-2" data-testid="user-menu-btn">
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
                <div className="px-2 py-1.5">
                  <p className="text-sm font-medium">{user?.name}</p>
                  <p className="text-xs text-muted-foreground">{user?.email}</p>
                </div>
                <DropdownMenuSeparator />
                <DropdownMenuItem asChild>
                  <Link to="/profile" className="flex items-center gap-2">
                    <User className="w-4 h-4" />
                    Profile
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuItem asChild>
                  <Link to="/certificates" className="flex items-center gap-2">
                    <Award className="w-4 h-4" />
                    Certificates
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuItem asChild>
                  <Link to="/pricing" className="flex items-center gap-2">
                    <Settings className="w-4 h-4" />
                    Upgrade Plan
                  </Link>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={onLogout} className="text-red-400" data-testid="logout-btn">
                  <LogOut className="w-4 h-4 mr-2" />
                  Logout
                </DropdownMenuItem>
              </DropdownMenuContent>
              </DropdownMenu>
            </div>
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
          {/* Welcome Section */}
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8">
            <div>
              <h1 className="font-secondary text-3xl font-bold mb-1">
                Welcome back, {user?.name?.split(" ")[0]}!
              </h1>
              <p className="text-muted-foreground">Continue your blockchain journey</p>
            </div>
            <Link to="/problems">
              <Button className="glow-primary" data-testid="start-practicing-btn">
                <Code2 className="w-4 h-4 mr-2" />
                Start Practicing
              </Button>
            </Link>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between mb-2">
                  <Trophy className="w-5 h-5 text-primary" />
                  <Badge variant="outline" className="text-xs">ELO</Badge>
                </div>
                <div className="font-secondary text-3xl font-bold text-primary">
                  {stats?.elo_rating || user?.elo_rating || 1200}
                </div>
                <p className="text-sm text-muted-foreground">Current Rating</p>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between mb-2">
                  <Target className="w-5 h-5 text-green-400" />
                  <Badge variant="outline" className="text-xs">Solved</Badge>
                </div>
                <div className="font-secondary text-3xl font-bold text-green-400">
                  {stats?.problems_solved || user?.problems_solved || 0}
                </div>
                <p className="text-sm text-muted-foreground">Problems Solved</p>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between mb-2">
                  <TrendingUp className="w-5 h-5 text-purple-400" />
                  <Badge variant="outline" className="text-xs">Rank</Badge>
                </div>
                <div className="font-secondary text-3xl font-bold text-purple-400">
                  #{stats?.rank || "—"}
                </div>
                <p className="text-sm text-muted-foreground">Global Ranking</p>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between mb-2">
                  <Flame className="w-5 h-5 text-orange-400" />
                  <Badge variant="outline" className="text-xs">Rate</Badge>
                </div>
                <div className="font-secondary text-3xl font-bold text-orange-400">
                  {stats?.success_rate || 0}%
                </div>
                <p className="text-sm text-muted-foreground">Success Rate</p>
              </CardContent>
            </Card>
          </div>

          {/* Rank and Streak Info */}
          <div className="grid md:grid-cols-2 gap-6 mb-8">
            {/* Rank Card */}
            <Card className="bg-gradient-to-br from-primary/10 to-purple-500/10 border-primary/20">
              <CardContent className="p-6">
                <div className="flex items-center gap-4">
                  <div className="text-5xl">
                    {stats?.current_rank?.icon || "👨‍💻"}
                  </div>
                  <div className="flex-1">
                    <p className="text-sm text-muted-foreground mb-1">Current Rank</p>
                    <h3 className="font-secondary text-2xl font-bold" style={{color: stats?.current_rank?.color}}>
                      {stats?.current_rank?.name || "Junior Developer"}
                    </h3>
                    <p className="text-xs text-muted-foreground mt-1">
                      Keep solving to reach the next rank!
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Streak Card */}
            <Card className="bg-gradient-to-br from-orange-500/10 to-red-500/10 border-orange-500/20">
              <CardContent className="p-6">
                <div className="flex items-center gap-4">
                  <Flame className="w-12 h-12 text-orange-400" />
                  <div className="flex-1">
                    <p className="text-sm text-muted-foreground mb-1">Daily Streak</p>
                    <div className="flex items-baseline gap-2">
                      <h3 className="font-secondary text-4xl font-bold text-orange-400">
                        {stats?.daily_streak || 0}
                      </h3>
                      <span className="text-sm text-muted-foreground">days</span>
                    </div>
                    <p className="text-xs text-muted-foreground mt-1">
                      {stats?.daily_streak > 0 
                        ? "Amazing consistency! Keep it up! 🔥" 
                        : "Solve a problem today to start your streak!"}
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Detailed Rank Progress */}
          <div className="mb-8">
            <RankProgress rankInfo={{
              current_rank: stats?.current_rank,
              next_rank: stats?.next_rank,
              progress: stats?.rank_progress,
              requirements: stats?.rank_requirements,
              current_stats: {
                elo: stats?.elo_rating || 1200,
                problems: stats?.problems_solved || 0
              }
            }} />
          </div>

          {/* Recent Achievements */}
          {stats?.recent_achievements?.length > 0 && (
            <Card className="bg-card border-border mb-8">
              <CardHeader className="flex flex-row items-center justify-between">
                <CardTitle className="font-secondary text-xl flex items-center gap-2">
                  <Trophy className="w-5 h-5 text-yellow-400" />
                  Recent Achievements
                </CardTitle>
                <Link to="/achievements">
                  <Button variant="ghost" size="sm">
                    View All <ChevronRight className="w-4 h-4 ml-1" />
                  </Button>
                </Link>
              </CardHeader>
              <CardContent>
                <div className="grid md:grid-cols-3 gap-4">
                  {stats.recent_achievements.map((ach, i) => (
                    <motion.div
                      key={i}
                      initial={{ opacity: 0, scale: 0.8 }}
                      animate={{ opacity: 1, scale: 1 }}
                      transition={{ delay: i * 0.1 }}
                      className="p-4 rounded-lg bg-gradient-to-br from-primary/10 to-purple-500/10 border border-primary/20"
                    >
                      <div className="text-3xl mb-2">{ach.icon}</div>
                      <h4 className="font-semibold mb-1">{ach.name}</h4>
                      <p className="text-xs text-muted-foreground mb-2">{ach.description}</p>
                      <Badge variant="outline" className="text-xs">
                        +{ach.points} pts
                      </Badge>
                    </motion.div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {/* New Widgets Section */}
          <div className="grid lg:grid-cols-3 gap-6 mb-8">
            {/* Daily Challenges */}
            <div className="lg:col-span-2">
              <DailyChallenges token={token} />
            </div>
            
            {/* Personal Insights */}
            <div>
              <PersonalInsights token={token} />
            </div>
          </div>

          {/* Recommended Problems */}
          <div className="mb-8">
            <RecommendedProblems token={token} />
          </div>

          <div className="grid lg:grid-cols-3 gap-6">
            {/* Recent Activity */}
            <Card className="lg:col-span-2 bg-card border-border">
              <CardHeader className="flex flex-row items-center justify-between">
                <CardTitle className="font-secondary text-xl">Recent Submissions</CardTitle>
                <Link to="/problems">
                  <Button variant="ghost" size="sm">
                    View All <ChevronRight className="w-4 h-4 ml-1" />
                  </Button>
                </Link>
              </CardHeader>
              <CardContent>
                {loading ? (
                  <div className="space-y-4">
                    {[...Array(5)].map((_, i) => (
                      <div key={i} className="h-12 bg-secondary/50 rounded animate-pulse" />
                    ))}
                  </div>
                ) : stats?.recent_submissions?.length > 0 ? (
                  <div className="space-y-3">
                    {stats.recent_submissions.map((submission, i) => (
                      <div 
                        key={i} 
                        className="flex items-center justify-between p-3 rounded-lg bg-secondary/30 hover:bg-secondary/50 transition-colors"
                      >
                        <div className="flex items-center gap-3">
                          {getStatusIcon(submission.status)}
                          <div>
                            <p className="font-medium text-sm">{submission.problem_id}</p>
                            <p className="text-xs text-muted-foreground">
                              {new Date(submission.created_at).toLocaleDateString()}
                            </p>
                          </div>
                        </div>
                        <div className="text-right">
                          {submission.elo_change > 0 && (
                            <span className="text-green-400 text-sm font-medium">
                              +{submission.elo_change} ELO
                            </span>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <div className="text-center py-8">
                    <Code2 className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
                    <p className="text-muted-foreground mb-4">No submissions yet</p>
                    <Link to="/problems">
                      <Button variant="outline">Solve Your First Problem</Button>
                    </Link>
                  </div>
                )}
              </CardContent>
            </Card>

            {/* Quick Actions */}
            <div className="space-y-6">
              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="font-secondary text-xl">Quick Start</CardTitle>
                </CardHeader>
                <CardContent className="space-y-3">
                  <Link to="/problems?difficulty=junior" className="block">
                    <div className="p-4 rounded-lg bg-green-500/10 border border-green-500/20 hover:border-green-500/40 transition-colors">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="font-medium text-green-400">Junior Problems</p>
                          <p className="text-sm text-muted-foreground">Perfect for beginners</p>
                        </div>
                        <ChevronRight className="w-5 h-5 text-green-400" />
                      </div>
                    </div>
                  </Link>
                  
                  <Link to="/problems?difficulty=middle" className="block">
                    <div className="p-4 rounded-lg bg-yellow-500/10 border border-yellow-500/20 hover:border-yellow-500/40 transition-colors">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="font-medium text-yellow-400">Middle Problems</p>
                          <p className="text-sm text-muted-foreground">Security & patterns</p>
                        </div>
                        <ChevronRight className="w-5 h-5 text-yellow-400" />
                      </div>
                    </div>
                  </Link>
                  
                  <Link to="/hackathons" className="block">
                    <div className="p-4 rounded-lg bg-purple-500/10 border border-purple-500/20 hover:border-purple-500/40 transition-colors">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="font-medium text-purple-400">Active Hackathons</p>
                          <p className="text-sm text-muted-foreground">Compete for prizes</p>
                        </div>
                        <ChevronRight className="w-5 h-5 text-purple-400" />
                      </div>
                    </div>
                  </Link>
                  
                  <Link to="/analytics" className="block">
                    <div className="p-4 rounded-lg bg-blue-500/10 border border-blue-500/20 hover:border-blue-500/40 transition-colors">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="font-medium text-blue-400">Analytics</p>
                          <p className="text-sm text-muted-foreground">Track your progress</p>
                        </div>
                        <BarChart3 className="w-5 h-5 text-blue-400" />
                      </div>
                    </div>
                  </Link>
                </CardContent>
              </Card>

              {/* Subscription Card */}
              <Card className="bg-card border-border">
                <CardContent className="p-6">
                  <div className="flex items-center justify-between mb-4">
                    <Badge className="bg-primary/20 text-primary border-primary/30">
                      {user?.subscription?.toUpperCase() || "BASIC"}
                    </Badge>
                    <Award className="w-5 h-5 text-primary" />
                  </div>
                  <p className="text-sm text-muted-foreground mb-4">
                    {user?.subscription === "basic" 
                      ? "Upgrade to unlock unlimited problems and advanced features"
                      : "Enjoy unlimited access to all features"}
                  </p>
                  {user?.subscription === "basic" && (
                    <Link to="/pricing">
                      <Button variant="outline" className="w-full">
                        Upgrade Plan
                      </Button>
                    </Link>
                  )}
                </CardContent>
              </Card>
            </div>
          </div>
        </motion.div>
      </main>
    </div>
  );
};

export default Dashboard;
