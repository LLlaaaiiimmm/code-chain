import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { GitBranch, ChevronRight, Lock, CheckCircle, TrendingUp } from "lucide-react";
import { API } from "../App";

export const SkillChainPreview = ({ token }) => {
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSkills();
  }, []);

  const fetchSkills = async () => {
    try {
      const response = await axios.get(`${API}/skills/user-progress`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      
      // Get top 6 skills by progress for preview
      const sortedSkills = (response.data.skills || [])
        .sort((a, b) => b.progress - a.progress)
        .slice(0, 6);
      
      setSkills(sortedSkills);
    } catch (error) {
      console.error("Error fetching skills:", error);
    } finally {
      setLoading(false);
    }
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

  const getCategoryColor = (category) => {
    const colors = {
      solidity: "border-purple-500/30 bg-purple-500/5",
      rust: "border-orange-500/30 bg-orange-500/5",
      tvm: "border-blue-500/30 bg-blue-500/5",
      move: "border-cyan-500/30 bg-cyan-500/5",
      general: "border-zinc-500/30 bg-zinc-500/5"
    };
    return colors[category] || "border-zinc-500/30 bg-zinc-500/5";
  };

  const stats = {
    unlocked: skills.filter(s => s.unlocked).length,
    inProgress: skills.filter(s => s.progress > 0 && s.progress < 100).length,
    total: skills.length
  };

  if (loading) {
    return (
      <Card className="bg-card border-border">
        <CardContent className="p-6">
          <div className="h-48 bg-secondary/50 rounded animate-pulse" />
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="bg-card border-border">
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle className="font-secondary text-xl flex items-center gap-2">
          <GitBranch className="w-5 h-5 text-primary" />
          Skill Chain Progress
        </CardTitle>
        <Link to="/skills">
          <Button variant="ghost" size="sm">
            View All <ChevronRight className="w-4 h-4 ml-1" />
          </Button>
        </Link>
      </CardHeader>
      <CardContent>
        {/* Quick Stats */}
        <div className="grid grid-cols-3 gap-3 mb-6">
          <div className="text-center p-3 rounded-lg bg-green-500/10 border border-green-500/20">
            <div className="text-2xl font-bold text-green-400">{stats.unlocked}</div>
            <div className="text-xs text-muted-foreground">Unlocked</div>
          </div>
          <div className="text-center p-3 rounded-lg bg-yellow-500/10 border border-yellow-500/20">
            <div className="text-2xl font-bold text-yellow-400">{stats.inProgress}</div>
            <div className="text-xs text-muted-foreground">In Progress</div>
          </div>
          <div className="text-center p-3 rounded-lg bg-primary/10 border border-primary/20">
            <div className="text-2xl font-bold text-primary">{stats.total}</div>
            <div className="text-xs text-muted-foreground">Total</div>
          </div>
        </div>

        {/* Top Skills Preview */}
        <div className="space-y-3">
          {skills.map((skill, index) => (
            <motion.div
              key={skill.skill_id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.05 }}
              className={`p-3 rounded-lg border ${getCategoryColor(skill.category)} 
                hover:border-opacity-50 transition-all`}
            >
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-2">
                  <span className="text-xl">{getCategoryIcon(skill.category)}</span>
                  <div>
                    <p className="font-medium text-sm flex items-center gap-1.5">
                      {skill.name}
                      {skill.unlocked ? (
                        <CheckCircle className="w-3.5 h-3.5 text-green-400" />
                      ) : skill.progress > 0 ? (
                        <TrendingUp className="w-3.5 h-3.5 text-yellow-400" />
                      ) : (
                        <Lock className="w-3.5 h-3.5 text-muted-foreground" />
                      )}
                    </p>
                    <p className="text-xs text-muted-foreground">
                      Level {skill.level}
                    </p>
                  </div>
                </div>
                <Badge variant="outline" className="text-xs">
                  {skill.progress}%
                </Badge>
              </div>
              
              {/* Progress Bar */}
              <div className="h-1.5 bg-secondary rounded-full overflow-hidden">
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
            </motion.div>
          ))}
        </div>

        {skills.length === 0 && (
          <div className="text-center py-8">
            <GitBranch className="w-12 h-12 text-muted-foreground mx-auto mb-3" />
            <p className="text-muted-foreground text-sm mb-4">
              Start solving problems to unlock skills!
            </p>
            <Link to="/problems">
              <Button size="sm">Browse Problems</Button>
            </Link>
          </div>
        )}

        {skills.length > 0 && (
          <Link to="/skills">
            <Button variant="outline" className="w-full mt-4">
              <GitBranch className="w-4 h-4 mr-2" />
              Explore Full Skill Tree
            </Button>
          </Link>
        )}
      </CardContent>
    </Card>
  );
};
