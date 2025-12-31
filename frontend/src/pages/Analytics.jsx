import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import { 
  Boxes, BarChart3, TrendingUp, Flame, Target,
  ChevronLeft, Award, Zap
} from "lucide-react";
import { API } from "../App";
import { ActivityCalendar } from "../components/ActivityCalendar";
import { ELOProgressChart, ProblemDistributionChart, CategoryDistributionChart } from "../components/Charts";

const Analytics = ({ user, token }) => {
  const [calendarData, setCalendarData] = useState([]);
  const [detailedStats, setDetailedStats] = useState(null);
  const [compareStats, setCompareStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const fetchAnalytics = async () => {
    try {
      const [calendar, detailed, compare] = await Promise.all([
        axios.get(`${API}/stats/activity-calendar`, {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }),
        axios.get(`${API}/stats/detailed`, {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }),
        axios.get(`${API}/stats/compare`, {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        })
      ]);

      setCalendarData(calendar.data.calendar);
      setDetailedStats(detailed.data);
      setCompareStats(compare.data);
    } catch (error) {
      console.error("Error fetching analytics:", error);
    } finally {
      setLoading(false);
    }
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
                <Link to="/analytics" className="text-foreground font-medium">Analytics</Link>
              </div>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8">
          <Link to="/dashboard">
            <Button variant="ghost" size="sm" className="mb-4">
              <ChevronLeft className="w-4 h-4 mr-1" />
              Back to Dashboard
            </Button>
          </Link>
          
          <h1 className="font-secondary text-3xl font-bold mb-2">
            Analytics & Insights
          </h1>
          <p className="text-muted-foreground">
            Deep dive into your learning journey
          </p>
        </div>

        {loading ? (
          <div className="space-y-6">
            {[...Array(4)].map((_, i) => (
              <div key={i} className="h-64 bg-secondary/50 rounded-lg animate-pulse" />
            ))}
          </div>
        ) : (
          <div className="space-y-8">
            {/* Activity Heatmap */}
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="font-secondary text-xl flex items-center gap-2">
                  <Flame className="w-5 h-5 text-orange-400" />
                  Activity Calendar
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ActivityCalendar activities={calendarData} />
                
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
                  <div className="text-center">
                    <p className="text-2xl font-bold text-primary">
                      {detailedStats?.current_streak || 0}
                    </p>
                    <p className="text-sm text-muted-foreground">Day Streak</p>
                  </div>
                  <div className="text-center">
                    <p className="text-2xl font-bold text-green-400">
                      {detailedStats?.week_solved || 0}
                    </p>
                    <p className="text-sm text-muted-foreground">This Week</p>
                  </div>
                  <div className="text-center">
                    <p className="text-2xl font-bold text-blue-400">
                      {detailedStats?.month_solved || 0}
                    </p>
                    <p className="text-sm text-muted-foreground">This Month</p>
                  </div>
                  <div className="text-center">
                    <p className="text-2xl font-bold text-purple-400">
                      {detailedStats?.success_rate || 0}%
                    </p>
                    <p className="text-sm text-muted-foreground">Success Rate</p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* ELO Progress */}
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="font-secondary text-xl flex items-center gap-2">
                  <TrendingUp className="w-5 h-5 text-purple-400" />
                  ELO Rating Progress (Last 30 Days)
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ELOProgressChart data={detailedStats?.elo_history || []} />
              </CardContent>
            </Card>

            {/* Problem Distribution */}
            <div className="grid md:grid-cols-2 gap-6">
              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="font-secondary text-xl flex items-center gap-2">
                    <Target className="w-5 h-5 text-yellow-400" />
                    By Difficulty
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <ProblemDistributionChart data={detailedStats?.by_difficulty || {}} />
                </CardContent>
              </Card>

              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="font-secondary text-xl flex items-center gap-2">
                    <BarChart3 className="w-5 h-5 text-blue-400" />
                    By Category
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <CategoryDistributionChart data={detailedStats?.by_category || {}} />
                </CardContent>
              </Card>
            </div>

            {/* Comparative Stats */}
            {compareStats && (
              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="font-secondary text-xl flex items-center gap-2">
                    <Award className="w-5 h-5 text-primary" />
                    How You Compare
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="space-y-2">
                      <p className="text-sm text-muted-foreground">Your ELO</p>
                      <p className="text-3xl font-bold text-primary">
                        {compareStats.user.elo}
                      </p>
                      <p className="text-sm">
                        {compareStats.comparison.elo_diff >= 0 ? (
                          <span className="text-green-400">
                            +{Math.round(compareStats.comparison.elo_diff)} above average
                          </span>
                        ) : (
                          <span className="text-orange-400">
                            {Math.round(compareStats.comparison.elo_diff)} below average
                          </span>
                        )}
                      </p>
                    </div>

                    <div className="space-y-2">
                      <p className="text-sm text-muted-foreground">Platform Average</p>
                      <p className="text-3xl font-bold text-muted-foreground">
                        {compareStats.platform_average.elo}
                      </p>
                      <p className="text-sm text-muted-foreground">
                        Average ELO rating
                      </p>
                    </div>

                    <div className="space-y-2">
                      <p className="text-sm text-muted-foreground">Your Percentile</p>
                      <p className="text-3xl font-bold text-purple-400">
                        {compareStats.user.percentile}%
                      </p>
                      <p className="text-sm text-muted-foreground">
                        Top {100 - compareStats.user.percentile}% of users
                      </p>
                    </div>
                  </div>

                  <div className="mt-6 p-4 bg-secondary/30 rounded-lg">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm text-muted-foreground mb-1">Problems Solved</p>
                        <p className="text-xl font-bold">{compareStats.user.problems_solved}</p>
                      </div>
                      <Zap className="w-8 h-8 text-yellow-400" />
                      <div className="text-right">
                        <p className="text-sm text-muted-foreground mb-1">Platform Average</p>
                        <p className="text-xl font-bold">{compareStats.platform_average.problems_solved}</p>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}
          </div>
        )}
      </main>
    </div>
  );
};

export default Analytics;
