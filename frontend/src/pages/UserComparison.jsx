import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import { Progress } from "../components/ui/progress";
import { 
  Boxes, Trophy, Target, TrendingUp, Flame, 
  ChevronLeft, ArrowRight, ArrowUp, ArrowDown,
  Equal, Users
} from "lucide-react";
import { API } from "../App";

const UserComparison = ({ user, token }) => {
  const { userId } = useParams();
  const [comparison, setComparison] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchComparison();
  }, [userId]);

  const fetchComparison = async () => {
    try {
      const response = await axios.get(`${API}/friends/compare/${userId}`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setComparison(response.data);
    } catch (error) {
      console.error("Error fetching comparison:", error);
    } finally {
      setLoading(false);
    }
  };

  const getDifferenceIndicator = (value) => {
    if (value > 0) return { icon: ArrowUp, color: "text-green-400", text: `+${value}` };
    if (value < 0) return { icon: ArrowDown, color: "text-red-400", text: value };
    return { icon: Equal, color: "text-muted-foreground", text: "0" };
  };

  const StatComparisonCard = ({ title, icon: Icon, userValue, friendValue, difference, suffix = "" }) => {
    const diff = getDifferenceIndicator(difference);
    const DiffIcon = diff.icon;

    return (
      <Card className="bg-card border-border">
        <CardHeader>
          <CardTitle className="font-secondary text-lg flex items-center gap-2">
            <Icon className="w-5 h-5 text-primary" />
            {title}
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-3 gap-4 items-center">
            {/* User */}
            <div className="text-center">
              <p className="text-3xl font-bold text-primary">{userValue}{suffix}</p>
              <p className="text-xs text-muted-foreground mt-1">You</p>
            </div>

            {/* Difference */}
            <div className="flex flex-col items-center">
              <div className={`flex items-center gap-1 ${diff.color}`}>
                <DiffIcon className="w-4 h-4" />
                <span className="font-bold">{diff.text}{suffix}</span>
              </div>
              <p className="text-xs text-muted-foreground mt-1">Difference</p>
            </div>

            {/* Friend */}
            <div className="text-center">
              <p className="text-3xl font-bold text-blue-400">{friendValue}{suffix}</p>
              <p className="text-xs text-muted-foreground mt-1">Friend</p>
            </div>
          </div>

          {/* Progress Bar */}
          <div className="mt-4">
            <div className="flex gap-2">
              <div className="flex-1">
                <Progress 
                  value={(userValue / Math.max(userValue, friendValue)) * 100} 
                  className="h-2 bg-secondary"
                />
              </div>
              <div className="flex-1">
                <Progress 
                  value={(friendValue / Math.max(userValue, friendValue)) * 100} 
                  className="h-2 bg-blue-500/30"
                />
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    );
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin w-12 h-12 border-4 border-primary border-t-transparent rounded-full mx-auto mb-4" />
          <p className="text-muted-foreground">Loading comparison...</p>
        </div>
      </div>
    );
  }

  if (!comparison) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <Card className="max-w-md w-full">
          <CardContent className="text-center py-12">
            <Users className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-muted-foreground mb-4">
              Unable to load comparison
            </p>
            <Link to="/dashboard">
              <Button>Back to Dashboard</Button>
            </Link>
          </CardContent>
        </Card>
      </div>
    );
  }

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
      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Link to="/leaderboard">
          <Button variant="ghost" size="sm" className="mb-6">
            <ChevronLeft className="w-4 h-4 mr-1" />
            Back to Leaderboard
          </Button>
        </Link>

        {/* Header with User Avatars */}
        <Card className="bg-gradient-to-br from-primary/10 to-purple-500/10 border-primary/20 mb-8">
          <CardContent className="py-8">
            <div className="flex items-center justify-center gap-8">
              {/* User */}
              <motion.div
                initial={{ opacity: 0, x: -50 }}
                animate={{ opacity: 1, x: 0 }}
                className="flex flex-col items-center"
              >
                <Avatar className="w-24 h-24 mb-3 ring-4 ring-primary/30">
                  <AvatarImage src={comparison.user.picture} />
                  <AvatarFallback className="bg-primary/20 text-primary text-2xl">
                    {comparison.user.name?.charAt(0) || "U"}
                  </AvatarFallback>
                </Avatar>
                <h3 className="font-bold text-xl">{comparison.user.name}</h3>
                <Badge variant="outline" className="mt-1">You</Badge>
              </motion.div>

              {/* VS */}
              <div className="text-4xl font-bold text-muted-foreground">VS</div>

              {/* Friend */}
              <motion.div
                initial={{ opacity: 0, x: 50 }}
                animate={{ opacity: 1, x: 0 }}
                className="flex flex-col items-center"
              >
                <Avatar className="w-24 h-24 mb-3 ring-4 ring-blue-500/30">
                  <AvatarImage src={comparison.friend.picture} />
                  <AvatarFallback className="bg-blue-500/20 text-blue-400 text-2xl">
                    {comparison.friend.name?.charAt(0) || "F"}
                  </AvatarFallback>
                </Avatar>
                <h3 className="font-bold text-xl">{comparison.friend.name}</h3>
                <Badge variant="outline" className="mt-1 text-blue-400 border-blue-400/50">
                  Friend
                </Badge>
              </motion.div>
            </div>
          </CardContent>
        </Card>

        {/* Comparison Stats */}
        <div className="grid gap-6">
          <StatComparisonCard
            title="ELO Rating"
            icon={Trophy}
            userValue={comparison.user.elo}
            friendValue={comparison.friend.elo}
            difference={comparison.differences.elo}
          />

          <StatComparisonCard
            title="Problems Solved"
            icon={Target}
            userValue={comparison.user.problems_solved}
            friendValue={comparison.friend.problems_solved}
            difference={comparison.differences.problems_solved}
          />

          <StatComparisonCard
            title="Daily Streak"
            icon={Flame}
            userValue={comparison.user.daily_streak}
            friendValue={comparison.friend.daily_streak}
            difference={comparison.differences.streak}
            suffix=" days"
          />

          <StatComparisonCard
            title="Total Submissions"
            icon={TrendingUp}
            userValue={comparison.user.submissions_count}
            friendValue={comparison.friend.submissions_count}
            difference={comparison.user.submissions_count - comparison.friend.submissions_count}
          />
        </div>

        {/* Summary */}
        <Card className="bg-card border-border mt-8">
          <CardHeader>
            <CardTitle className="font-secondary text-xl">Summary</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {comparison.differences.elo > 0 && (
                <p className="text-green-400 flex items-center gap-2">
                  <ArrowUp className="w-4 h-4" />
                  You have {comparison.differences.elo} more ELO points
                </p>
              )}
              {comparison.differences.elo < 0 && (
                <p className="text-blue-400 flex items-center gap-2">
                  <ArrowRight className="w-4 h-4" />
                  {comparison.friend.name} has {Math.abs(comparison.differences.elo)} more ELO points
                </p>
              )}
              
              {comparison.differences.problems_solved > 0 && (
                <p className="text-green-400 flex items-center gap-2">
                  <ArrowUp className="w-4 h-4" />
                  You have solved {comparison.differences.problems_solved} more problems
                </p>
              )}
              {comparison.differences.problems_solved < 0 && (
                <p className="text-blue-400 flex items-center gap-2">
                  <ArrowRight className="w-4 h-4" />
                  {comparison.friend.name} has solved {Math.abs(comparison.differences.problems_solved)} more problems
                </p>
              )}
              
              {comparison.differences.streak > 0 && (
                <p className="text-green-400 flex items-center gap-2">
                  <Flame className="w-4 h-4" />
                  Your streak is {comparison.differences.streak} days longer
                </p>
              )}
              {comparison.differences.streak < 0 && (
                <p className="text-blue-400 flex items-center gap-2">
                  <Flame className="w-4 h-4" />
                  {comparison.friend.name}'s streak is {Math.abs(comparison.differences.streak)} days longer
                </p>
              )}
            </div>
          </CardContent>
        </Card>

        {/* Challenge Button */}
        <div className="mt-8 text-center">
          <Link to="/problems">
            <Button size="lg" className="glow-primary">
              <Target className="w-5 h-5 mr-2" />
              Start Competing
            </Button>
          </Link>
        </div>
      </main>
    </div>
  );
};

export default UserComparison;
