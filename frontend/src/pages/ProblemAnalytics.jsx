import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Progress } from "../components/ui/progress";
import { 
  Boxes, ChevronLeft, Target, Clock, Zap, 
  TrendingUp, Award, Users, CheckCircle, XCircle,
  BarChart3, Flame
} from "lucide-react";
import { API } from "../App";

const ProblemAnalytics = ({ user, token }) => {
  const { problemId } = useParams();
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAnalytics();
  }, [problemId]);

  const fetchAnalytics = async () => {
    try {
      const response = await axios.get(`${API}/problems/${problemId}/analytics`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setAnalytics(response.data);
    } catch (error) {
      console.error("Error fetching problem analytics:", error);
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = (difficulty) => {
    const colors = {
      junior: "text-green-400 border-green-400/50",
      middle: "text-yellow-400 border-yellow-400/50",
      senior: "text-orange-400 border-orange-400/50",
      expert: "text-red-400 border-red-400/50"
    };
    return colors[difficulty] || "text-zinc-400";
  };

  const getPerformanceRating = (score) => {
    if (score >= 80) return { label: "Excellent", color: "text-green-400", icon: "🏆" };
    if (score >= 60) return { label: "Good", color: "text-yellow-400", icon: "⭐" };
    if (score >= 40) return { label: "Average", color: "text-orange-400", icon: "📊" };
    return { label: "Below Average", color: "text-red-400", icon: "📉" };
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin w-12 h-12 border-4 border-primary border-t-transparent rounded-full mx-auto mb-4" />
          <p className="text-muted-foreground">Loading analytics...</p>
        </div>
      </div>
    );
  }

  if (!analytics) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <Card className="max-w-md w-full">
          <CardContent className="text-center py-12">
            <BarChart3 className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-muted-foreground mb-4">
              No analytics data available
            </p>
            <Link to="/problems">
              <Button>Browse Problems</Button>
            </Link>
          </CardContent>
        </Card>
      </div>
    );
  }

  const { problem, user_stats, global_stats } = analytics;
  const performance = user_stats.performance;
  const performanceRating = performance ? getPerformanceRating(performance.overall_efficiency_score) : null;

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
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Link to={`/problem/${problemId}`}>
          <Button variant="ghost" size="sm" className="mb-6">
            <ChevronLeft className="w-4 h-4 mr-1" />
            Back to Problem
          </Button>
        </Link>

        {/* Problem Header */}
        <Card className="bg-gradient-to-br from-primary/10 to-purple-500/10 border-primary/20 mb-8">
          <CardContent className="py-6">
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <h1 className="font-secondary text-3xl font-bold mb-3">{problem.title}</h1>
                <div className="flex items-center gap-3">
                  <Badge variant="outline" className={getDifficultyColor(problem.difficulty)}>
                    {problem.difficulty}
                  </Badge>
                  <Badge variant="outline">
                    {problem.category.toUpperCase()}
                  </Badge>
                  {user_stats.solved && (
                    <Badge variant="outline" className="text-green-400 border-green-400/50">
                      <CheckCircle className="w-3 h-3 mr-1" />
                      Solved
                    </Badge>
                  )}
                </div>
              </div>
              
              {user_stats.solved && performanceRating && (
                <div className="text-center">
                  <div className="text-4xl mb-2">{performanceRating.icon}</div>
                  <p className={`font-bold ${performanceRating.color}`}>
                    {performanceRating.label}
                  </p>
                  <p className="text-xs text-muted-foreground">Performance</p>
                </div>
              )}
            </div>
          </CardContent>
        </Card>

        <div className="grid lg:grid-cols-2 gap-6 mb-8">
          {/* Your Stats */}
          <Card className="bg-card border-border">
            <CardHeader>
              <CardTitle className="font-secondary text-xl flex items-center gap-2">
                <Target className="w-5 h-5 text-primary" />
                Your Performance
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Attempts</p>
                  <p className="text-2xl font-bold">
                    {user_stats.attempts}
                  </p>
                </div>
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Time Spent</p>
                  <p className="text-2xl font-bold">
                    {user_stats.time_spent_minutes ? `${user_stats.time_spent_minutes}m` : "—"}
                  </p>
                </div>
              </div>

              {!user_stats.solved && (
                <div className="p-4 rounded-lg bg-yellow-500/10 border border-yellow-500/30">
                  <p className="text-sm text-yellow-400 flex items-center gap-2">
                    <XCircle className="w-4 h-4" />
                    Not solved yet. Keep trying!
                  </p>
                </div>
              )}

              {performance && (
                <>
                  <div className="space-y-3 pt-4 border-t border-border">
                    <div>
                      <div className="flex items-center justify-between mb-2">
                        <p className="text-sm text-muted-foreground">Gas Efficiency</p>
                        <p className="text-sm font-bold">{Math.round(performance.gas_efficiency_percentile)}%</p>
                      </div>
                      <Progress value={performance.gas_efficiency_percentile} className="h-2" />
                    </div>

                    <div>
                      <div className="flex items-center justify-between mb-2">
                        <p className="text-sm text-muted-foreground">Time Efficiency</p>
                        <p className="text-sm font-bold">{Math.round(performance.time_efficiency_percentile)}%</p>
                      </div>
                      <Progress value={performance.time_efficiency_percentile} className="h-2" />
                    </div>
                  </div>

                  <div className="p-4 rounded-lg bg-primary/10 border border-primary/30">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm text-muted-foreground mb-1">Your Rank</p>
                        <p className="text-2xl font-bold text-primary">
                          #{performance.rank_among_solvers}
                        </p>
                      </div>
                      <div className="text-right">
                        <p className="text-sm text-muted-foreground mb-1">Out of</p>
                        <p className="text-2xl font-bold">
                          {performance.total_solvers}
                        </p>
                      </div>
                    </div>
                    <p className="text-xs text-muted-foreground mt-2">
                      solvers
                    </p>
                  </div>
                </>
              )}
            </CardContent>
          </Card>

          {/* Global Stats */}
          <Card className="bg-card border-border">
            <CardHeader>
              <CardTitle className="font-secondary text-xl flex items-center gap-2">
                <Users className="w-5 h-5 text-blue-400" />
                Global Statistics
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Total Attempts</p>
                  <p className="text-2xl font-bold text-blue-400">
                    {global_stats.total_attempts}
                  </p>
                </div>
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Solved</p>
                  <p className="text-2xl font-bold text-green-400">
                    {global_stats.success_count}
                  </p>
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between mb-2">
                  <p className="text-sm text-muted-foreground">Success Rate</p>
                  <p className="text-sm font-bold">{global_stats.success_rate}%</p>
                </div>
                <Progress value={global_stats.success_rate} className="h-2" />
              </div>

              <div className="space-y-3 pt-4 border-t border-border">
                <div className="flex items-center justify-between p-3 rounded-lg bg-secondary/30">
                  <div className="flex items-center gap-2">
                    <Zap className="w-4 h-4 text-yellow-400" />
                    <span className="text-sm">Avg Gas Used</span>
                  </div>
                  <span className="font-bold">{global_stats.avg_gas_used.toLocaleString()}</span>
                </div>

                <div className="flex items-center justify-between p-3 rounded-lg bg-secondary/30">
                  <div className="flex items-center gap-2">
                    <Clock className="w-4 h-4 text-blue-400" />
                    <span className="text-sm">Avg Time</span>
                  </div>
                  <span className="font-bold">{global_stats.avg_execution_time_ms}ms</span>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Detailed Performance Breakdown */}
        {performance && (
          <Card className="bg-card border-border mb-8">
            <CardHeader>
              <CardTitle className="font-secondary text-xl flex items-center gap-2">
                <BarChart3 className="w-5 h-5 text-purple-400" />
                Performance Breakdown
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid md:grid-cols-3 gap-6">
                <div className="text-center p-6 rounded-lg bg-gradient-to-br from-green-500/10 to-emerald-500/10 border border-green-500/30">
                  <Zap className="w-8 h-8 text-green-400 mx-auto mb-3" />
                  <p className="text-sm text-muted-foreground mb-2">Gas Used</p>
                  <p className="text-3xl font-bold text-green-400 mb-1">
                    {performance.gas_used.toLocaleString()}
                  </p>
                  <p className="text-xs text-muted-foreground">
                    Avg: {global_stats.avg_gas_used.toLocaleString()}
                  </p>
                </div>

                <div className="text-center p-6 rounded-lg bg-gradient-to-br from-blue-500/10 to-cyan-500/10 border border-blue-500/30">
                  <Clock className="w-8 h-8 text-blue-400 mx-auto mb-3" />
                  <p className="text-sm text-muted-foreground mb-2">Execution Time</p>
                  <p className="text-3xl font-bold text-blue-400 mb-1">
                    {performance.execution_time_ms}ms
                  </p>
                  <p className="text-xs text-muted-foreground">
                    Avg: {global_stats.avg_execution_time_ms}ms
                  </p>
                </div>

                <div className="text-center p-6 rounded-lg bg-gradient-to-br from-purple-500/10 to-pink-500/10 border border-purple-500/30">
                  <Award className="w-8 h-8 text-purple-400 mx-auto mb-3" />
                  <p className="text-sm text-muted-foreground mb-2">Overall Score</p>
                  <p className="text-3xl font-bold text-purple-400 mb-1">
                    {Math.round(performance.overall_efficiency_score)}
                  </p>
                  <p className="text-xs text-muted-foreground">
                    {performanceRating.label}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Recommendations */}
        {performance && performance.overall_efficiency_score < 80 && (
          <Card className="bg-card border-border">
            <CardHeader>
              <CardTitle className="font-secondary text-xl flex items-center gap-2">
                <TrendingUp className="w-5 h-5 text-orange-400" />
                Optimization Suggestions
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {performance.gas_efficiency_percentile < 70 && (
                  <div className="p-4 rounded-lg bg-yellow-500/10 border border-yellow-500/30">
                    <p className="font-semibold mb-2 flex items-center gap-2">
                      <Flame className="w-4 h-4 text-yellow-400" />
                      Gas Optimization
                    </p>
                    <p className="text-sm text-muted-foreground">
                      Your solution uses more gas than average. Consider optimizing storage operations, 
                      using memory instead of storage where possible, and minimizing loops.
                    </p>
                  </div>
                )}
                
                {performance.time_efficiency_percentile < 70 && (
                  <div className="p-4 rounded-lg bg-blue-500/10 border border-blue-500/30">
                    <p className="font-semibold mb-2 flex items-center gap-2">
                      <Clock className="w-4 h-4 text-blue-400" />
                      Execution Speed
                    </p>
                    <p className="text-sm text-muted-foreground">
                      Your solution takes longer to execute than average. Review your algorithm's 
                      time complexity and consider more efficient data structures.
                    </p>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        )}

        {/* Action Buttons */}
        <div className="flex items-center justify-center gap-4 mt-8">
          <Link to={`/problem/${problemId}`}>
            <Button variant="outline">
              <Target className="w-4 h-4 mr-2" />
              View Problem
            </Button>
          </Link>
          {user_stats.solved && (
            <Link to="/problems">
              <Button className="glow-primary">
                Next Challenge
                <ChevronLeft className="w-4 h-4 ml-2 rotate-180" />
              </Button>
            </Link>
          )}
        </div>
      </main>
    </div>
  );
};

export default ProblemAnalytics;
