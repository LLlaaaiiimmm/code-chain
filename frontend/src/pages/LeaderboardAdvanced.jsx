import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import { Badge } from "../components/ui/badge";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import { 
  Boxes, Trophy, TrendingUp, Users, Calendar,
  Code, Flame, Sparkles, Medal, Crown,
  ChevronLeft
} from "lucide-react";
import { API } from "../App";

const LeaderboardAdvanced = ({ user, token }) => {
  const [globalLeaderboard, setGlobalLeaderboard] = useState([]);
  const [categoryLeaderboards, setCategoryLeaderboards] = useState({});
  const [periodLeaderboards, setPeriodLeaderboards] = useState({});
  const [friendsLeaderboard, setFriendsLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedTab, setSelectedTab] = useState("global");
  const [selectedCategory, setSelectedCategory] = useState("solidity");
  const [selectedPeriod, setSelectedPeriod] = useState("week");

  useEffect(() => {
    fetchLeaderboards();
  }, []);

  useEffect(() => {
    if (selectedTab === "category" && !categoryLeaderboards[selectedCategory]) {
      fetchCategoryLeaderboard(selectedCategory);
    }
  }, [selectedTab, selectedCategory]);

  useEffect(() => {
    if (selectedTab === "period" && !periodLeaderboards[selectedPeriod]) {
      fetchPeriodLeaderboard(selectedPeriod);
    }
  }, [selectedTab, selectedPeriod]);

  const fetchLeaderboards = async () => {
    try {
      const [global, friends] = await Promise.all([
        axios.get(`${API}/leaderboard`, {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }),
        axios.get(`${API}/friends/list`, {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        })
      ]);

      setGlobalLeaderboard(global.data);
      
      // Get friends leaderboard from friends list
      const friendsList = friends.data.friends || [];
      const sortedFriends = [...friendsList, {
        user_id: user.user_id,
        name: user.name,
        picture: user.picture,
        elo_rating: user.elo_rating,
        problems_solved: user.problems_solved
      }].sort((a, b) => b.elo_rating - a.elo_rating);
      
      setFriendsLeaderboard(sortedFriends.map((friend, index) => ({
        rank: index + 1,
        ...friend
      })));
    } catch (error) {
      console.error("Error fetching leaderboards:", error);
    } finally {
      setLoading(false);
    }
  };

  const fetchCategoryLeaderboard = async (category) => {
    try {
      const response = await axios.get(`${API}/leaderboard/by-category/${category}`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setCategoryLeaderboards(prev => ({
        ...prev,
        [category]: response.data.leaderboard
      }));
    } catch (error) {
      console.error("Error fetching category leaderboard:", error);
    }
  };

  const fetchPeriodLeaderboard = async (period) => {
    try {
      const response = await axios.get(`${API}/leaderboard/by-period/${period}`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setPeriodLeaderboards(prev => ({
        ...prev,
        [period]: response.data.leaderboard
      }));
    } catch (error) {
      console.error("Error fetching period leaderboard:", error);
    }
  };

  const getRankIcon = (rank) => {
    if (rank === 1) return <Crown className="w-5 h-5 text-yellow-400" />;
    if (rank === 2) return <Medal className="w-5 h-5 text-zinc-400" />;
    if (rank === 3) return <Medal className="w-5 h-5 text-orange-400" />;
    return <span className="text-muted-foreground font-bold">#{rank}</span>;
  };

  const LeaderboardTable = ({ data, showProblems = false, showPeriodStats = false }) => (
    <div className="space-y-2">
      {data.map((entry, index) => (
        <motion.div
          key={entry.user_id}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.05 }}
        >
          <div className={`p-4 rounded-lg ${
            entry.user_id === user?.user_id 
              ? 'bg-primary/10 border-2 border-primary' 
              : 'bg-secondary/30 border border-border'
          } hover:bg-secondary/50 transition-all`}>
            <div className="flex items-center gap-4">
              {/* Rank */}
              <div className="flex items-center justify-center w-12">
                {getRankIcon(entry.rank)}
              </div>

              {/* Avatar */}
              <Avatar className="w-10 h-10">
                <AvatarImage src={entry.picture} />
                <AvatarFallback className="bg-primary/20 text-primary">
                  {entry.name?.charAt(0) || "U"}
                </AvatarFallback>
              </Avatar>

              {/* User Info */}
              <div className="flex-1 min-w-0">
                <p className="font-semibold truncate">
                  {entry.name}
                  {entry.user_id === user?.user_id && (
                    <Badge variant="outline" className="ml-2 text-xs">You</Badge>
                  )}
                </p>
                {showProblems && (
                  <p className="text-sm text-muted-foreground">
                    {entry.category_problems_solved || entry.problems_solved} problems solved
                  </p>
                )}
                {showPeriodStats && (
                  <p className="text-sm text-muted-foreground">
                    {entry.period_problems_solved} problems • +{entry.period_elo_gained} ELO
                  </p>
                )}
              </div>

              {/* ELO */}
              <div className="text-right">
                <div className="flex items-center gap-2">
                  <Trophy className="w-4 h-4 text-primary" />
                  <span className="font-bold text-lg text-primary">
                    {entry.elo_rating}
                  </span>
                </div>
                <p className="text-xs text-muted-foreground">ELO</p>
              </div>
            </div>
          </div>
        </motion.div>
      ))}
      
      {data.length === 0 && (
        <div className="text-center py-12">
          <Users className="w-12 h-12 text-muted-foreground mx-auto mb-3" />
          <p className="text-muted-foreground">No data available</p>
        </div>
      )}
    </div>
  );

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
                <Link to="/leaderboard" className="text-foreground font-medium">Leaderboard</Link>
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
            Leaderboards
          </h1>
          <p className="text-muted-foreground">
            Compete with the best blockchain developers
          </p>
        </div>

        <Tabs value={selectedTab} onValueChange={setSelectedTab}>
          <TabsList className="grid grid-cols-4 w-full max-w-2xl">
            <TabsTrigger value="global" className="flex items-center gap-2">
              <Trophy className="w-4 h-4" />
              Global
            </TabsTrigger>
            <TabsTrigger value="category" className="flex items-center gap-2">
              <Code className="w-4 h-4" />
              By Tech
            </TabsTrigger>
            <TabsTrigger value="period" className="flex items-center gap-2">
              <Calendar className="w-4 h-4" />
              By Period
            </TabsTrigger>
            <TabsTrigger value="friends" className="flex items-center gap-2">
              <Users className="w-4 h-4" />
              Friends
            </TabsTrigger>
          </TabsList>

          {/* Global Leaderboard */}
          <TabsContent value="global" className="mt-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="font-secondary text-xl flex items-center gap-2">
                  <TrendingUp className="w-5 h-5 text-primary" />
                  Global Rankings
                </CardTitle>
              </CardHeader>
              <CardContent>
                {loading ? (
                  <div className="space-y-3">
                    {[...Array(10)].map((_, i) => (
                      <div key={i} className="h-20 bg-secondary/50 rounded-lg animate-pulse" />
                    ))}
                  </div>
                ) : (
                  <LeaderboardTable data={globalLeaderboard} showProblems={true} />
                )}
              </CardContent>
            </Card>
          </TabsContent>

          {/* Category Leaderboard */}
          <TabsContent value="category" className="mt-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <CardTitle className="font-secondary text-xl flex items-center gap-2">
                    <Code className="w-5 h-5 text-blue-400" />
                    Technology Rankings
                  </CardTitle>
                  <div className="flex gap-2">
                    {["solidity", "rust", "tvm", "crypto"].map((cat) => (
                      <Button
                        key={cat}
                        variant={selectedCategory === cat ? "default" : "outline"}
                        size="sm"
                        onClick={() => setSelectedCategory(cat)}
                      >
                        {cat.charAt(0).toUpperCase() + cat.slice(1)}
                      </Button>
                    ))}
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                {categoryLeaderboards[selectedCategory] ? (
                  <LeaderboardTable 
                    data={categoryLeaderboards[selectedCategory]} 
                    showProblems={true} 
                  />
                ) : (
                  <div className="text-center py-12">
                    <div className="animate-spin w-8 h-8 border-4 border-primary border-t-transparent rounded-full mx-auto mb-3" />
                    <p className="text-muted-foreground">Loading {selectedCategory} leaderboard...</p>
                  </div>
                )}
              </CardContent>
            </Card>
          </TabsContent>

          {/* Period Leaderboard */}
          <TabsContent value="period" className="mt-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <CardTitle className="font-secondary text-xl flex items-center gap-2">
                    <Calendar className="w-5 h-5 text-green-400" />
                    Time Period Rankings
                  </CardTitle>
                  <div className="flex gap-2">
                    {["week", "month", "year"].map((period) => (
                      <Button
                        key={period}
                        variant={selectedPeriod === period ? "default" : "outline"}
                        size="sm"
                        onClick={() => setSelectedPeriod(period)}
                      >
                        {period.charAt(0).toUpperCase() + period.slice(1)}
                      </Button>
                    ))}
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                {periodLeaderboards[selectedPeriod] ? (
                  <LeaderboardTable 
                    data={periodLeaderboards[selectedPeriod]} 
                    showPeriodStats={true} 
                  />
                ) : (
                  <div className="text-center py-12">
                    <div className="animate-spin w-8 h-8 border-4 border-primary border-t-transparent rounded-full mx-auto mb-3" />
                    <p className="text-muted-foreground">Loading {selectedPeriod} leaderboard...</p>
                  </div>
                )}
              </CardContent>
            </Card>
          </TabsContent>

          {/* Friends Leaderboard */}
          <TabsContent value="friends" className="mt-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="font-secondary text-xl flex items-center gap-2">
                  <Users className="w-5 h-5 text-purple-400" />
                  Friends Rankings
                </CardTitle>
              </CardHeader>
              <CardContent>
                {friendsLeaderboard.length > 0 ? (
                  <LeaderboardTable data={friendsLeaderboard} showProblems={true} />
                ) : (
                  <div className="text-center py-12">
                    <Users className="w-12 h-12 text-muted-foreground mx-auto mb-3" />
                    <p className="text-muted-foreground mb-4">
                      You don't have any friends yet
                    </p>
                    <Button variant="outline">Find Friends</Button>
                  </div>
                )}
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </main>
    </div>
  );
};

export default LeaderboardAdvanced;
