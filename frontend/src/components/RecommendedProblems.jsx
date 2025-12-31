import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { 
  Sparkles, ArrowRight, Code2, BookOpen, Target
} from "lucide-react";
import { API } from "../App";

export const RecommendedProblems = ({ token }) => {
  const [recommendations, setRecommendations] = useState([]);
  const [reason, setReason] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchRecommendations();
  }, []);

  const fetchRecommendations = async () => {
    try {
      const response = await axios.get(`${API}/recommendations/next-problem`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setRecommendations(response.data.recommendations || []);
      setReason(response.data.reason || "");
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = (difficulty) => {
    const colors = {
      junior: "text-green-400 bg-green-400/10 border-green-400/30",
      middle: "text-yellow-400 bg-yellow-400/10 border-yellow-400/30",
      senior: "text-orange-400 bg-orange-400/10 border-orange-400/30",
      expert: "text-red-400 bg-red-400/10 border-red-400/30"
    };
    return colors[difficulty] || colors.junior;
  };

  const getCategoryIcon = (category) => {
    const icons = {
      solidity: "⚡",
      rust: "🦀",
      tvm: "💎",
      crypto: "🔐"
    };
    return icons[category] || "📝";
  };

  if (loading) {
    return (
      <Card className="bg-card border-border">
        <CardHeader>
          <CardTitle className="font-secondary text-xl flex items-center gap-2">
            <Target className="w-5 h-5 text-primary" />
            Recommended for You
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {[1, 2, 3].map((i) => (
              <div key={i} className="h-20 bg-secondary/50 rounded-lg animate-pulse" />
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="bg-card border-border">
      <CardHeader>
        <div className="flex items-start justify-between gap-2 mb-2">
          <CardTitle className="font-secondary text-xl flex items-center gap-2">
            <Target className="w-5 h-5 text-primary" />
            Recommended for You
          </CardTitle>
          <Sparkles className="w-5 h-5 text-yellow-400" />
        </div>
        {reason && (
          <p className="text-xs text-muted-foreground">
            {reason}
          </p>
        )}
      </CardHeader>
      
      <CardContent className="space-y-3">
        {recommendations.length > 0 ? (
          recommendations.slice(0, 3).map((problem, index) => (
            <motion.div
              key={problem.problem_id}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
            >
              <Link to={`/problem/${problem.problem_id}`}>
                <div className="p-4 rounded-lg border border-border bg-secondary/30 hover:bg-secondary/50 hover:border-primary/30 transition-all group">
                  <div className="flex items-start gap-3">
                    <div className="text-2xl mt-0.5">
                      {getCategoryIcon(problem.category)}
                    </div>
                    
                    <div className="flex-1 min-w-0">
                      <div className="flex items-start justify-between gap-2 mb-2">
                        <h4 className="font-semibold text-sm group-hover:text-primary transition-colors">
                          {problem.title}
                        </h4>
                        <ArrowRight className="w-4 h-4 text-muted-foreground group-hover:text-primary transition-colors shrink-0" />
                      </div>
                      
                      <p className="text-xs text-muted-foreground line-clamp-2 mb-3">
                        {problem.description}
                      </p>
                      
                      <div className="flex items-center gap-2 flex-wrap">
                        <Badge 
                          variant="outline" 
                          className={`text-xs ${getDifficultyColor(problem.difficulty)}`}
                        >
                          {problem.difficulty}
                        </Badge>
                        
                        <Badge variant="outline" className="text-xs">
                          {problem.category}
                        </Badge>
                        
                        {problem.tags && problem.tags.slice(0, 2).map((tag, i) => (
                          <Badge 
                            key={i}
                            variant="outline" 
                            className="text-xs text-muted-foreground"
                          >
                            {tag}
                          </Badge>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </Link>
            </motion.div>
          ))
        ) : (
          <div className="text-center py-8">
            <BookOpen className="w-12 h-12 text-muted-foreground mx-auto mb-3" />
            <p className="text-sm text-muted-foreground mb-2">
              No recommendations available
            </p>
            <Link to="/problems">
              <Button variant="outline" size="sm">
                Browse All Problems
              </Button>
            </Link>
          </div>
        )}
        
        {recommendations.length > 3 && (
          <Link to="/problems">
            <Button variant="ghost" className="w-full mt-2">
              <Code2 className="w-4 h-4 mr-2" />
              View All Recommendations
              <ArrowRight className="w-4 h-4 ml-2" />
            </Button>
          </Link>
        )}
      </CardContent>
    </Card>
  );
};
