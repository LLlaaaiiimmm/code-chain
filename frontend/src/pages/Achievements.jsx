import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Progress } from "../components/ui/progress";
import { Badge } from "../components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import { 
  Boxes, Trophy, Award, Target, Flame, Zap, 
  Lock, CheckCircle, ChevronLeft 
} from "lucide-react";
import { API } from "../App";

const AchievementCard = ({ achievement, unlocked, unlockedAt, progress }) => {
  const getRarityColor = (rarity) => {
    const colors = {
      common: "border-zinc-500 text-zinc-400",
      rare: "border-blue-500 text-blue-400",
      epic: "border-purple-500 text-purple-400",
      legendary: "border-yellow-500 text-yellow-400"
    };
    return colors[rarity] || colors.common;
  };

  const getCategoryIcon = (category) => {
    const icons = {
      progress: Trophy,
      technical: Target,
      efficiency: Zap,
      streak: Flame
    };
    const Icon = icons[category] || Award;
    return <Icon className="w-5 h-5" />;
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ scale: unlocked ? 1.02 : 1 }}
      transition={{ duration: 0.2 }}
    >
      <Card className={`${unlocked ? 'bg-card border-primary/50' : 'bg-card/50 border-border'} 
        relative overflow-hidden`}>
        {unlocked && (
          <div className="absolute top-2 right-2">
            <CheckCircle className="w-5 h-5 text-green-400" />
          </div>
        )}
        
        {!unlocked && (
          <div className="absolute top-2 right-2">
            <Lock className="w-4 h-4 text-muted-foreground" />
          </div>
        )}

        <CardContent className="p-6">
          <div className="flex items-start gap-4">
            <div className={`text-5xl ${unlocked ? '' : 'opacity-50 grayscale'}`}>
              {achievement.icon}
            </div>
            
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-2">
                {getCategoryIcon(achievement.category)}
                <h3 className="font-semibold">{achievement.name}</h3>
                <Badge 
                  variant="outline" 
                  className={getRarityColor(achievement.rarity)}
                >
                  {achievement.rarity}
                </Badge>
              </div>
              
              <p className="text-sm text-muted-foreground mb-3">
                {achievement.description}
              </p>
              
              {!unlocked && progress && (
                <div className="space-y-1">
                  <div className="flex items-center justify-between text-xs text-muted-foreground">
                    <span>Progress</span>
                    <span>{progress.current} / {progress.required}</span>
                  </div>
                  <Progress value={progress.percentage} className="h-2" />
                </div>
              )}
              
              {unlocked && unlockedAt && (
                <p className="text-xs text-green-400">
                  Unlocked {new Date(unlockedAt).toLocaleDateString()}
                </p>
              )}
              
              <div className="flex items-center gap-2 mt-3">
                <Trophy className="w-4 h-4 text-yellow-400" />
                <span className="text-sm font-medium text-yellow-400">
                  +{achievement.points} points
                </span>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  );
};

const Achievements = ({ user, token, onLogout }) => {
  const [achievements, setAchievements] = useState({ unlocked: [], locked: [], total: 0 });
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState("all");

  useEffect(() => {
    fetchAchievements();
  }, []);

  const fetchAchievements = async () => {
    try {
      const response = await axios.get(`${API}/achievements/user`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setAchievements(response.data);
    } catch (error) {
      console.error("Error fetching achievements:", error);
    } finally {
      setLoading(false);
    }
  };

  const filterByCategory = (achievementsList, category) => {
    if (category === "all") return achievementsList;
    return achievementsList.filter(a => a.category === category);
  };

  const categories = [
    { value: "all", label: "All", icon: Trophy },
    { value: "progress", label: "Progress", icon: Target },
    { value: "technical", label: "Technical", icon: Award },
    { value: "efficiency", label: "Efficiency", icon: Zap },
    { value: "streak", label: "Streak", icon: Flame }
  ];

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
                <Link to="/achievements" className="text-foreground font-medium">Achievements</Link>
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
          
          <div className="flex items-center justify-between">
            <div>
              <h1 className="font-secondary text-3xl font-bold mb-2">
                Achievements
              </h1>
              <p className="text-muted-foreground">
                Track your progress and unlock rewards
              </p>
            </div>
            
            <div className="text-right">
              <p className="text-2xl font-bold text-primary">
                {achievements.unlocked_count} / {achievements.total}
              </p>
              <p className="text-sm text-muted-foreground">Unlocked</p>
            </div>
          </div>
        </div>

        {/* Category Filter */}
        <Tabs value={selectedCategory} onValueChange={setSelectedCategory} className="mb-6">
          <TabsList className="bg-card">
            {categories.map(cat => {
              const Icon = cat.icon;
              return (
                <TabsTrigger key={cat.value} value={cat.value}>
                  <Icon className="w-4 h-4 mr-2" />
                  {cat.label}
                </TabsTrigger>
              );
            })}
          </TabsList>
        </Tabs>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="h-40 bg-secondary/50 rounded-lg animate-pulse" />
            ))}
          </div>
        ) : (
          <>
            {/* Unlocked Achievements */}
            {filterByCategory(achievements.unlocked, selectedCategory).length > 0 && (
              <div className="mb-8">
                <h2 className="font-secondary text-xl font-bold mb-4 flex items-center gap-2">
                  <Trophy className="w-5 h-5 text-yellow-400" />
                  Unlocked
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {filterByCategory(achievements.unlocked, selectedCategory).map(achievement => (
                    <AchievementCard
                      key={achievement.achievement_id}
                      achievement={achievement}
                      unlocked={true}
                      unlockedAt={achievement.unlocked_at}
                    />
                  ))}
                </div>
              </div>
            )}

            {/* Locked Achievements */}
            {filterByCategory(achievements.locked, selectedCategory).length > 0 && (
              <div>
                <h2 className="font-secondary text-xl font-bold mb-4 flex items-center gap-2">
                  <Lock className="w-5 h-5 text-muted-foreground" />
                  Locked
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {filterByCategory(achievements.locked, selectedCategory).map(achievement => (
                    <AchievementCard
                      key={achievement.achievement_id}
                      achievement={achievement}
                      unlocked={false}
                      progress={achievement.progress}
                    />
                  ))}
                </div>
              </div>
            )}

            {filterByCategory(achievements.unlocked, selectedCategory).length === 0 && 
             filterByCategory(achievements.locked, selectedCategory).length === 0 && (
              <div className="text-center py-12">
                <Trophy className="w-16 h-16 text-muted-foreground mx-auto mb-4" />
                <p className="text-muted-foreground">No achievements in this category yet</p>
              </div>
            )}
          </>
        )}
      </main>
    </div>
  );
};

export default Achievements;
