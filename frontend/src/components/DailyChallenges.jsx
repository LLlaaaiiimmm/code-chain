import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { motion, AnimatePresence } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { Progress } from "./ui/progress";
import { 
  Target, CheckCircle, Clock, Trophy, ArrowRight,
  Sparkles, Flame, Code2
} from "lucide-react";
import { API } from "../App";

export const DailyChallenges = ({ token }) => {
  const [challenges, setChallenges] = useState([]);
  const [loading, setLoading] = useState(true);
  const [claimingId, setClaimingId] = useState(null);

  useEffect(() => {
    fetchChallenges();
  }, []);

  const fetchChallenges = async () => {
    try {
      const response = await axios.get(`${API}/challenges/daily`, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true
      });
      setChallenges(response.data.challenges || []);
    } catch (error) {
      console.error("Error fetching daily challenges:", error);
    } finally {
      setLoading(false);
    }
  };

  const claimReward = async (challengeId) => {
    setClaimingId(challengeId);
    try {
      await axios.post(
        `${API}/daily-challenges/${challengeId}/claim`,
        {},
        {
          headers: { Authorization: `Bearer ${token}` },
          withCredentials: true
        }
      );
      // Refresh challenges
      await fetchChallenges();
    } catch (error) {
      console.error("Error claiming reward:", error);
    } finally {
      setClaimingId(null);
    }
  };

  const getChallengeIcon = (type) => {
    switch (type) {
      case "solve_problem":
        return <Target className="w-5 h-5" />;
      case "solve_count":
        return <Flame className="w-5 h-5" />;
      case "category_focus":
        return <Code2 className="w-5 h-5" />;
      default:
        return <Sparkles className="w-5 h-5" />;
    }
  };

  const completedCount = challenges.filter(c => c.completed).length;
  const totalChallenges = challenges.length;

  if (loading) {
    return (
      <Card className="bg-card border-border">
        <CardHeader>
          <CardTitle className="font-secondary text-xl flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-yellow-400" />
            Daily Challenges
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
    <Card className="bg-gradient-to-br from-yellow-500/5 to-orange-500/5 border-yellow-500/20">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle className="font-secondary text-xl flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-yellow-400" />
            Daily Challenges
          </CardTitle>
          <Badge variant="outline" className="text-yellow-400 border-yellow-400/50">
            <Clock className="w-3 h-3 mr-1" />
            Resets in {24 - new Date().getHours()}h
          </Badge>
        </div>
        
        {totalChallenges > 0 && (
          <div className="mt-3">
            <div className="flex items-center justify-between text-sm mb-2">
              <span className="text-muted-foreground">Progress</span>
              <span className="text-yellow-400 font-medium">
                {completedCount} / {totalChallenges}
              </span>
            </div>
            <Progress 
              value={(completedCount / totalChallenges) * 100} 
              className="h-2"
            />
          </div>
        )}
      </CardHeader>
      
      <CardContent className="space-y-3">
        <AnimatePresence>
          {challenges.map((challenge, index) => (
            <motion.div
              key={challenge.challenge_id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 20 }}
              transition={{ delay: index * 0.1 }}
            >
              <div 
                className={`p-4 rounded-lg border transition-all ${
                  challenge.completed 
                    ? 'bg-green-500/10 border-green-500/30' 
                    : 'bg-secondary/30 border-border hover:border-yellow-400/30'
                }`}
              >
                <div className="flex items-start gap-3">
                  <div className={`p-2 rounded-lg ${
                    challenge.completed ? 'bg-green-500/20 text-green-400' : 'bg-yellow-500/20 text-yellow-400'
                  }`}>
                    {challenge.completed ? (
                      <CheckCircle className="w-5 h-5" />
                    ) : (
                      getChallengeIcon(challenge.type)
                    )}
                  </div>
                  
                  <div className="flex-1 min-w-0">
                    <div className="flex items-start justify-between gap-2 mb-1">
                      <h4 className="font-semibold text-sm">{challenge.title}</h4>
                      {!challenge.completed && challenge.reward_points && (
                        <Badge variant="outline" className="text-xs text-yellow-400 border-yellow-400/50 shrink-0">
                          <Trophy className="w-3 h-3 mr-1" />
                          +{challenge.reward_points}
                        </Badge>
                      )}
                    </div>
                    
                    <p className="text-xs text-muted-foreground mb-2">
                      {challenge.description}
                    </p>
                    
                    {/* Progress bar for count-based challenges */}
                    {(challenge.type === "solve_count" || challenge.type === "category_focus") && !challenge.completed && (
                      <div className="mb-2">
                        <Progress 
                          value={(challenge.progress / challenge.target) * 100} 
                          className="h-1.5"
                        />
                        <p className="text-xs text-muted-foreground mt-1">
                          {challenge.progress} / {challenge.target} completed
                        </p>
                      </div>
                    )}
                    
                    {/* Action buttons */}
                    {challenge.completed && !challenge.claimed && (
                      <Button
                        size="sm"
                        variant="outline"
                        className="text-xs mt-2"
                        onClick={() => claimReward(challenge.challenge_id)}
                        disabled={claimingId === challenge.challenge_id}
                      >
                        {claimingId === challenge.challenge_id ? (
                          "Claiming..."
                        ) : (
                          <>
                            <Trophy className="w-3 h-3 mr-1" />
                            Claim Reward
                          </>
                        )}
                      </Button>
                    )}
                    
                    {challenge.completed && challenge.claimed && (
                      <Badge variant="outline" className="text-xs text-green-400 border-green-400/50 mt-2">
                        <CheckCircle className="w-3 h-3 mr-1" />
                        Claimed
                      </Badge>
                    )}
                    
                    {!challenge.completed && challenge.problem_id && (
                      <Link to={`/problem/${challenge.problem_id}`}>
                        <Button
                          size="sm"
                          variant="ghost"
                          className="text-xs mt-2 text-yellow-400 hover:text-yellow-300"
                        >
                          Start Challenge
                          <ArrowRight className="w-3 h-3 ml-1" />
                        </Button>
                      </Link>
                    )}
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
        
        {challenges.length === 0 && (
          <div className="text-center py-8">
            <Sparkles className="w-12 h-12 text-muted-foreground mx-auto mb-3" />
            <p className="text-muted-foreground text-sm">
              No challenges available yet
            </p>
          </div>
        )}
        
        {completedCount === totalChallenges && totalChallenges > 0 && (
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            className="mt-4 p-4 rounded-lg bg-gradient-to-r from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 text-center"
          >
            <Trophy className="w-8 h-8 text-yellow-400 mx-auto mb-2" />
            <p className="font-semibold text-yellow-400 mb-1">
              All Challenges Complete! 🎉
            </p>
            <p className="text-xs text-muted-foreground">
              Come back tomorrow for new challenges
            </p>
          </motion.div>
        )}
      </CardContent>
    </Card>
  );
};
