import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import { 
  Boxes, GitBranch, Target, Lock, CheckCircle, 
  ChevronLeft, TrendingUp, Award, Zap
} from "lucide-react";
import { API } from "../App";
import { SkillTree } from "../components/SkillTree";

const SkillCard = ({ skill }) => {
  const getCategoryColor = (category) => {
    const colors = {
      solidity: "border-purple-500 bg-purple-500/10",
      rust: "border-orange-500 bg-orange-500/10",
      tvm: "border-blue-500 bg-blue-500/10",
      move: "border-cyan-500 bg-cyan-500/10",
      general: "border-zinc-500 bg-zinc-500/10"
    };
    return colors[category] || "border-zinc-500 bg-zinc-500/10";
  };

  const getCategoryIcon = (category) => {
    const icons = {
      solidity: "💎",
      rust: "🦀",
      tvm: "💠",
      move: "🌊",
      general: "⚡"
    };
    return icons[category] || "📚";
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ scale: skill.unlocked ? 1.02 : 1 }}
      transition={{ duration: 0.2 }}
    >
      <Card className={`${getCategoryColor(skill.category)} border-2 ${skill.unlocked ? '' : 'opacity-60'}`}>
        <CardContent className="p-5">
          <div className="flex items-start justify-between mb-3">
            <div className="flex items-center gap-3">
              <span className="text-3xl">{getCategoryIcon(skill.category)}</span>
              <div>
                <h3 className="font-semibold flex items-center gap-2">
                  {skill.name}
                  {skill.unlocked && <CheckCircle className="w-4 h-4 text-green-400" />}
                  {!skill.unlocked && <Lock className="w-4 h-4 text-muted-foreground" />}
                </h3>
                <p className="text-xs text-muted-foreground">Level {skill.level}</p>
              </div>
            </div>
          </div>
          
          <p className="text-sm text-muted-foreground mb-4">
            {skill.description}
          </p>
          
          {/* Progress Bar */}
          <div className="mb-4">
            <div className="flex items-center justify-between text-xs text-muted-foreground mb-1">
              <span>Progress</span>
              <span>{skill.progress}%</span>
            </div>
            <div className="h-2 bg-secondary rounded-full overflow-hidden">
              <div 
                className={`h-full transition-all ${
                  skill.progress === 100 ? 'bg-green-500' :
                  skill.progress >= 50 ? 'bg-yellow-500' :
                  skill.progress > 0 ? 'bg-blue-500' :
                  'bg-zinc-700'
                }`}
                style={{ width: `${skill.progress}%` }}
              />
            </div>
          </div>
          
          {/* Dependencies */}
          {skill.dependencies && skill.dependencies.length > 0 && (
            <div className="flex items-center gap-2 text-xs">
              <span className="text-muted-foreground">Requires:</span>
              <div className="flex flex-wrap gap-1">
                {skill.dependencies.map((dep, i) => (
                  <Badge key={i} variant="outline" className="text-xs">
                    {dep}
                  </Badge>
                ))}
              </div>
            </div>
          )}
          
          {skill.unlocked && skill.unlocked_at && (
            <p className="text-xs text-green-400 mt-3">
              ✓ Unlocked {new Date(skill.unlocked_at).toLocaleDateString()}
            </p>
          )}
        </CardContent>
      </Card>
    </motion.div>
  );
};

const Skills = ({ user, token }) => {
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(true);
  const [viewMode, setViewMode] = useState("tree"); // "tree" or "grid"
  const [selectedCategory, setSelectedCategory] = useState("all");

  useEffect(() => {
    fetchSkills();
  }, []);

  const fetchSkills = async () => {
    try {
      const response = await axios.get(`${API}/skills/user-progress`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setSkills(response.data.skills || []);
    } catch (error) {
      console.error("Error fetching skills:", error);
    } finally {
      setLoading(false);
    }
  };

  const filterByCategory = (skillsList, category) => {
    if (category === "all") return skillsList;
    return skillsList.filter(s => s.category === category);
  };

  const categories = [
    { value: "all", label: "All", icon: "🌐" },
    { value: "solidity", label: "Solidity", icon: "💎" },
    { value: "rust", label: "Rust/Solana", icon: "🦀" },
    { value: "tvm", label: "TVM/TON", icon: "💠" },
    { value: "move", label: "Move", icon: "🌊" },
    { value: "general", label: "General", icon: "⚡" }
  ];

  const stats = {
    total: skills.length,
    unlocked: skills.filter(s => s.unlocked).length,
    inProgress: skills.filter(s => s.progress > 0 && s.progress < 100).length,
    mastered: skills.filter(s => s.progress === 100).length
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
                <Link to="/skills" className="text-foreground font-medium">Skills</Link>
                <Link to="/analytics" className="text-muted-foreground hover:text-foreground transition-colors">Analytics</Link>
              </div>
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
          {/* Header */}
          <div className="mb-8">
            <Link to="/dashboard">
              <Button variant="ghost" size="sm" className="mb-4">
                <ChevronLeft className="w-4 h-4 mr-1" />
                Back to Dashboard
              </Button>
            </Link>
            
            <div className="flex items-center justify-between mb-4">
              <div>
                <h1 className="font-secondary text-3xl font-bold mb-2 flex items-center gap-3">
                  <GitBranch className="w-8 h-8 text-primary" />
                  Skill Chain
                </h1>
                <p className="text-muted-foreground">
                  Track your blockchain development skills and unlock new abilities
                </p>
              </div>
              
              {/* View Mode Toggle */}
              <div className="flex gap-2">
                <Button
                  variant={viewMode === "tree" ? "default" : "outline"}
                  size="sm"
                  onClick={() => setViewMode("tree")}
                >
                  <GitBranch className="w-4 h-4 mr-2" />
                  Tree View
                </Button>
                <Button
                  variant={viewMode === "grid" ? "default" : "outline"}
                  size="sm"
                  onClick={() => setViewMode("grid")}
                >
                  <Target className="w-4 h-4 mr-2" />
                  Grid View
                </Button>
              </div>
            </div>

            {/* Stats Cards */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <Card className="bg-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-2xl font-bold text-primary">{stats.total}</p>
                      <p className="text-xs text-muted-foreground">Total Skills</p>
                    </div>
                    <Target className="w-8 h-8 text-primary opacity-50" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-2xl font-bold text-green-400">{stats.unlocked}</p>
                      <p className="text-xs text-muted-foreground">Unlocked</p>
                    </div>
                    <CheckCircle className="w-8 h-8 text-green-400 opacity-50" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-2xl font-bold text-yellow-400">{stats.inProgress}</p>
                      <p className="text-xs text-muted-foreground">In Progress</p>
                    </div>
                    <TrendingUp className="w-8 h-8 text-yellow-400 opacity-50" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-2xl font-bold text-purple-400">{stats.mastered}</p>
                      <p className="text-xs text-muted-foreground">Mastered</p>
                    </div>
                    <Award className="w-8 h-8 text-purple-400 opacity-50" />
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>

          {loading ? (
            <div className="h-[600px] bg-secondary/50 rounded-lg animate-pulse" />
          ) : (
            <>
              {viewMode === "tree" ? (
                /* Tree View */
                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="font-secondary text-xl flex items-center gap-2">
                      <GitBranch className="w-5 h-5 text-primary" />
                      Interactive Skill Tree
                    </CardTitle>
                    <p className="text-sm text-muted-foreground">
                      Explore your skill progression. Green nodes are unlocked, grey nodes are locked. 
                      Hover over nodes to see details.
                    </p>
                  </CardHeader>
                  <CardContent>
                    <SkillTree skills={skills} />
                  </CardContent>
                </Card>
              ) : (
                /* Grid View */
                <>
                  {/* Category Filter */}
                  <Tabs value={selectedCategory} onValueChange={setSelectedCategory} className="mb-6">
                    <TabsList className="bg-card">
                      {categories.map(cat => (
                        <TabsTrigger key={cat.value} value={cat.value}>
                          <span className="mr-2">{cat.icon}</span>
                          {cat.label}
                        </TabsTrigger>
                      ))}
                    </TabsList>
                  </Tabs>

                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {filterByCategory(skills, selectedCategory).map(skill => (
                      <SkillCard key={skill.skill_id} skill={skill} />
                    ))}
                  </div>

                  {filterByCategory(skills, selectedCategory).length === 0 && (
                    <div className="text-center py-12">
                      <Target className="w-16 h-16 text-muted-foreground mx-auto mb-4" />
                      <p className="text-muted-foreground">No skills in this category yet</p>
                    </div>
                  )}
                </>
              )}
            </>
          )}

          {/* How Skills Work */}
          <Card className="bg-card border-border mt-8">
            <CardHeader>
              <CardTitle className="font-secondary text-xl flex items-center gap-2">
                <Zap className="w-5 h-5 text-yellow-400" />
                How Skills Work
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-start gap-3">
                <div className="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center flex-shrink-0">
                  <span className="text-primary font-bold">1</span>
                </div>
                <div>
                  <h4 className="font-semibold mb-1">Solve Problems to Unlock Skills</h4>
                  <p className="text-sm text-muted-foreground">
                    Each problem you solve contributes to related skills. Complete more problems to increase skill progress.
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3">
                <div className="w-8 h-8 rounded-full bg-green-500/20 flex items-center justify-center flex-shrink-0">
                  <span className="text-green-400 font-bold">2</span>
                </div>
                <div>
                  <h4 className="font-semibold mb-1">Dependencies Matter</h4>
                  <p className="text-sm text-muted-foreground">
                    Some skills require mastery of prerequisite skills. Follow the skill tree to see dependencies.
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3">
                <div className="w-8 h-8 rounded-full bg-purple-500/20 flex items-center justify-center flex-shrink-0">
                  <span className="text-purple-400 font-bold">3</span>
                </div>
                <div>
                  <h4 className="font-semibold mb-1">Master Skills for Achievements</h4>
                  <p className="text-sm text-muted-foreground">
                    Reaching 100% on skills unlocks achievements and increases your rank. Aim for mastery!
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>
      </main>
    </div>
  );
};

export default Skills;
