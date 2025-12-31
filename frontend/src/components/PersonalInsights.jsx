import { useState, useEffect } from "react";
import axios from "axios";
import { motion } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Badge } from "./ui/badge";
import { 
  Lightbulb, TrendingUp, AlertCircle, 
  CheckCircle2, Sparkles
} from "lucide-react";
import { API } from "../App";

export const PersonalInsights = ({ token }) => {
  const [insights, setInsights] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchInsights();
  }, []);

  const fetchInsights = async () => {
    try {
      const response = await axios.get(`${API}/insights/personal`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setInsights(response.data.insights || []);
    } catch (error) {
      console.error("Error fetching insights:", error);
    } finally {
      setLoading(false);
    }
  };

  const getInsightStyle = (type) => {
    switch (type) {
      case "positive":
        return {
          bg: "bg-green-500/10",
          border: "border-green-500/30",
          text: "text-green-400"
        };
      case "reminder":
        return {
          bg: "bg-blue-500/10",
          border: "border-blue-500/30",
          text: "text-blue-400"
        };
      case "suggestion":
        return {
          bg: "bg-purple-500/10",
          border: "border-purple-500/30",
          text: "text-purple-400"
        };
      case "motivation":
        return {
          bg: "bg-yellow-500/10",
          border: "border-yellow-500/30",
          text: "text-yellow-400"
        };
      default:
        return {
          bg: "bg-secondary/30",
          border: "border-border",
          text: "text-muted-foreground"
        };
    }
  };

  const getInsightIcon = (type) => {
    switch (type) {
      case "positive":
        return CheckCircle2;
      case "reminder":
        return AlertCircle;
      case "suggestion":
        return Lightbulb;
      case "motivation":
        return TrendingUp;
      default:
        return Sparkles;
    }
  };

  if (loading) {
    return (
      <Card className="bg-card border-border">
        <CardHeader>
          <CardTitle className="font-secondary text-xl flex items-center gap-2">
            <Lightbulb className="w-5 h-5 text-primary" />
            Personal Insights
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {[1, 2].map((i) => (
              <div key={i} className="h-16 bg-secondary/50 rounded-lg animate-pulse" />
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="bg-card border-border">
      <CardHeader>
        <CardTitle className="font-secondary text-xl flex items-center gap-2">
          <Lightbulb className="w-5 h-5 text-primary" />
          Personal Insights
        </CardTitle>
      </CardHeader>
      
      <CardContent className="space-y-3">
        {insights.length > 0 ? (
          insights.map((insight, index) => {
            const style = getInsightStyle(insight.type);
            const Icon = getInsightIcon(insight.type);
            
            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                className={`p-4 rounded-lg border ${style.bg} ${style.border}`}
              >
                <div className="flex items-start gap-3">
                  <div className={`${style.text} mt-0.5`}>
                    <span className="text-xl">{insight.icon}</span>
                  </div>
                  
                  <div className="flex-1 min-w-0">
                    <div className="flex items-start justify-between gap-2 mb-1">
                      <h4 className={`font-semibold text-sm ${style.text}`}>
                        {insight.title}
                      </h4>
                      <Icon className={`w-4 h-4 ${style.text} shrink-0`} />
                    </div>
                    
                    <p className="text-xs text-muted-foreground">
                      {insight.message}
                    </p>
                  </div>
                </div>
              </motion.div>
            );
          })
        ) : (
          <div className="text-center py-6">
            <Lightbulb className="w-10 h-10 text-muted-foreground mx-auto mb-2" />
            <p className="text-sm text-muted-foreground">
              Keep solving to unlock insights
            </p>
          </div>
        )}
      </CardContent>
    </Card>
  );
};
