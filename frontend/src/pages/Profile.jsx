import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Progress } from "../components/ui/progress";
import { 
  Boxes, Trophy, TrendingUp, Target, Code2,
  Award, Calendar, Clock, CheckCircle, XCircle,
  LogOut, User, Settings, Mail
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

const Profile = ({ user, token, onLogout }) => {
  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (user?.user_id) {
      fetchProfile();
    }
  }, [user]);

  const fetchProfile = async () => {
    try {
      const response = await axios.get(`${API}/users/${user.user_id}`);
      setProfileData(response.data);
    } catch (error) {
      console.error("Error fetching profile:", error);
    } finally {
      setLoading(false);
    }
  };

  const getStatusIcon = (status) => {
    return status === "passed" ? (
      <CheckCircle className="w-4 h-4 text-green-400" />
    ) : (
      <XCircle className="w-4 h-4 text-red-400" />
    );
  };

  const achievements = [
    { name: "First Blood", description: "Solve your first problem", unlocked: (profileData?.problems_solved || 0) >= 1 },
    { name: "Problem Solver", description: "Solve 10 problems", unlocked: (profileData?.problems_solved || 0) >= 10 },
    { name: "Rising Star", description: "Reach 1300 ELO", unlocked: (profileData?.elo_rating || 0) >= 1300 },
    { name: "Gas Optimizer", description: "Submit optimized code", unlocked: false },
    { name: "Security Expert", description: "Complete security track", unlocked: false },
    { name: "Hackathon Winner", description: "Win a hackathon", unlocked: false },
  ];

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="w-8 h-8 border-2 border-primary border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background" data-testid="profile-page">
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
                <Link to="/hackathons" className="text-muted-foreground hover:text-foreground transition-colors">Hackathons</Link>
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
          {/* Profile Header */}
          <Card className="mb-8 bg-card border-border overflow-hidden">
            <div className="h-32 bg-gradient-to-r from-primary/20 via-purple-500/20 to-primary/20" />
            <CardContent className="relative pt-0 pb-6">
              <div className="flex flex-col md:flex-row items-center md:items-end gap-6 -mt-16">
                <Avatar className="w-32 h-32 border-4 border-background">
                  <AvatarImage src={profileData?.picture} />
                  <AvatarFallback className="bg-primary/20 text-primary text-4xl">
                    {profileData?.name?.charAt(0) || "U"}
                  </AvatarFallback>
                </Avatar>
                
                <div className="flex-1 text-center md:text-left">
                  <h1 className="font-secondary text-3xl font-bold mb-1">{profileData?.name}</h1>
                  <div className="flex items-center justify-center md:justify-start gap-2 text-muted-foreground mb-3">
                    <Mail className="w-4 h-4" />
                    <span>{profileData?.email}</span>
                  </div>
                  <div className="flex flex-wrap justify-center md:justify-start gap-2">
                    <Badge className="bg-primary/20 text-primary border-primary/30">
                      {profileData?.subscription?.toUpperCase() || "BASIC"}
                    </Badge>
                    <Badge variant="outline">
                      <Calendar className="w-3 h-3 mr-1" />
                      Joined {new Date(profileData?.created_at).toLocaleDateString()}
                    </Badge>
                  </div>
                </div>

                <div className="flex gap-4 text-center">
                  <div className="px-6 py-3 rounded-lg bg-secondary/50">
                    <p className="font-secondary text-2xl font-bold text-primary">{profileData?.elo_rating || 1200}</p>
                    <p className="text-xs text-muted-foreground">ELO Rating</p>
                  </div>
                  <div className="px-6 py-3 rounded-lg bg-secondary/50">
                    <p className="font-secondary text-2xl font-bold text-green-400">#{profileData?.rank || "—"}</p>
                    <p className="text-xs text-muted-foreground">Global Rank</p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          <div className="grid lg:grid-cols-3 gap-6">
            {/* Stats */}
            <div className="lg:col-span-2 space-y-6">
              {/* Quick Stats */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <Card className="bg-card border-border">
                  <CardContent className="p-4 text-center">
                    <Target className="w-5 h-5 text-primary mx-auto mb-2" />
                    <p className="font-secondary text-2xl font-bold">{profileData?.problems_solved || 0}</p>
                    <p className="text-xs text-muted-foreground">Problems Solved</p>
                  </CardContent>
                </Card>
                <Card className="bg-card border-border">
                  <CardContent className="p-4 text-center">
                    <Code2 className="w-5 h-5 text-blue-400 mx-auto mb-2" />
                    <p className="font-secondary text-2xl font-bold">{profileData?.recent_submissions?.length || 0}</p>
                    <p className="text-xs text-muted-foreground">Submissions</p>
                  </CardContent>
                </Card>
                <Card className="bg-card border-border">
                  <CardContent className="p-4 text-center">
                    <Trophy className="w-5 h-5 text-yellow-400 mx-auto mb-2" />
                    <p className="font-secondary text-2xl font-bold">0</p>
                    <p className="text-xs text-muted-foreground">Hackathons</p>
                  </CardContent>
                </Card>
                <Card className="bg-card border-border">
                  <CardContent className="p-4 text-center">
                    <Award className="w-5 h-5 text-purple-400 mx-auto mb-2" />
                    <p className="font-secondary text-2xl font-bold">
                      {achievements.filter(a => a.unlocked).length}
                    </p>
                    <p className="text-xs text-muted-foreground">Achievements</p>
                  </CardContent>
                </Card>
              </div>

              {/* Recent Activity */}
              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="font-secondary text-xl">Recent Submissions</CardTitle>
                </CardHeader>
                <CardContent>
                  {profileData?.recent_submissions?.length > 0 ? (
                    <div className="space-y-3">
                      {profileData.recent_submissions.map((submission, i) => (
                        <div 
                          key={i} 
                          className="flex items-center justify-between p-3 rounded-lg bg-secondary/30"
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
                      <p className="text-muted-foreground">No submissions yet</p>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>

            {/* Achievements */}
            <div className="space-y-6">
              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="font-secondary text-xl flex items-center gap-2">
                    <Award className="w-5 h-5 text-purple-400" />
                    Achievements
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {achievements.map((achievement, i) => (
                      <div 
                        key={i} 
                        className={`p-3 rounded-lg border ${
                          achievement.unlocked 
                            ? "bg-primary/10 border-primary/30" 
                            : "bg-secondary/30 border-border opacity-50"
                        }`}
                      >
                        <div className="flex items-center gap-3">
                          <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
                            achievement.unlocked ? "bg-primary/20" : "bg-secondary"
                          }`}>
                            {achievement.unlocked ? (
                              <CheckCircle className="w-4 h-4 text-primary" />
                            ) : (
                              <Award className="w-4 h-4 text-muted-foreground" />
                            )}
                          </div>
                          <div>
                            <p className="font-medium text-sm">{achievement.name}</p>
                            <p className="text-xs text-muted-foreground">{achievement.description}</p>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Skill Progress */}
              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="font-secondary text-xl">Skill Progress</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div>
                    <div className="flex justify-between text-sm mb-1">
                      <span>Solidity</span>
                      <span className="text-muted-foreground">Intermediate</span>
                    </div>
                    <Progress value={45} className="h-2" />
                  </div>
                  <div>
                    <div className="flex justify-between text-sm mb-1">
                      <span>Security</span>
                      <span className="text-muted-foreground">Beginner</span>
                    </div>
                    <Progress value={20} className="h-2" />
                  </div>
                  <div>
                    <div className="flex justify-between text-sm mb-1">
                      <span>Gas Optimization</span>
                      <span className="text-muted-foreground">Beginner</span>
                    </div>
                    <Progress value={15} className="h-2" />
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </motion.div>
      </main>
    </div>
  );
};

export default Profile;
