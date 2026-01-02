import { motion } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Progress } from "./ui/progress";
import { Badge } from "./ui/badge";
import { Trophy, TrendingUp, Target, Lock, CheckCircle } from "lucide-react";

const RankProgress = ({ rankInfo }) => {
  if (!rankInfo || !rankInfo.current_rank) {
    return null;
  }

  const { current_rank, next_rank, progress, requirements, current_stats } = rankInfo;
  const isMaxRank = !next_rank;

  return (
    <Card className="bg-gradient-to-br from-primary/10 via-purple-500/5 to-primary/10 border-primary/30 overflow-hidden relative">
      {/* Decorative background */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute top-0 right-0 w-64 h-64 bg-primary rounded-full blur-3xl" />
        <div className="absolute bottom-0 left-0 w-64 h-64 bg-purple-500 rounded-full blur-3xl" />
      </div>

      <CardHeader className="relative z-10">
        <CardTitle className="font-secondary text-xl flex items-center gap-2">
          <Trophy className="w-5 h-5 text-yellow-400" />
          Rank Progression
        </CardTitle>
      </CardHeader>

      <CardContent className="relative z-10 space-y-6">
        {/* Current Rank Display */}
        <motion.div
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.5 }}
          className="flex items-center gap-4 p-4 rounded-lg bg-card/50 backdrop-blur-sm border border-primary/20"
        >
          <motion.div
            animate={{ 
              scale: [1, 1.1, 1],
              rotate: [0, 5, -5, 0]
            }}
            transition={{ 
              duration: 3,
              repeat: Infinity,
              repeatDelay: 5
            }}
            className="text-6xl"
          >
            {current_rank.icon}
          </motion.div>
          
          <div className="flex-1">
            <div className="flex items-center gap-2 mb-1">
              <h3 
                className="font-secondary text-2xl font-bold"
                style={{ color: current_rank.color }}
              >
                {current_rank.name}
              </h3>
              <CheckCircle className="w-5 h-5 text-green-400" />
            </div>
            <p className="text-sm text-muted-foreground mb-2">
              {current_rank.description}
            </p>
            
            {/* Current Stats */}
            <div className="flex items-center gap-4 text-xs">
              <div className="flex items-center gap-1">
                <Trophy className="w-3 h-3 text-primary" />
                <span className="text-muted-foreground">ELO:</span>
                <span className="font-bold text-primary">{current_stats?.elo || 0}</span>
              </div>
              <div className="flex items-center gap-1">
                <Target className="w-3 h-3 text-green-400" />
                <span className="text-muted-foreground">Solved:</span>
                <span className="font-bold text-green-400">{current_stats?.problems || 0}</span>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Progress to Next Rank */}
        {!isMaxRank && next_rank && (
          <div className="space-y-4">
            {/* Progress Overview */}
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <TrendingUp className="w-4 h-4 text-primary" />
                <span className="text-sm font-medium">Progress to {next_rank.name}</span>
              </div>
              <span className="text-sm font-bold text-primary">
                {Math.round(progress.overall)}%
              </span>
            </div>

            {/* Overall Progress Bar */}
            <div className="space-y-1">
              <Progress value={progress.overall} className="h-3" />
            </div>

            {/* Next Rank Preview */}
            <motion.div
              initial={{ x: 20, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              transition={{ delay: 0.3 }}
              className="flex items-center gap-4 p-4 rounded-lg bg-secondary/30 border border-border"
            >
              <div className="text-5xl opacity-50 grayscale">
                {next_rank.icon}
              </div>
              
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <Lock className="w-4 h-4 text-muted-foreground" />
                  <h4 
                    className="font-semibold"
                    style={{ color: next_rank.color }}
                  >
                    {next_rank.name}
                  </h4>
                </div>
                <p className="text-xs text-muted-foreground mb-3">
                  {next_rank.description}
                </p>
                
                {/* Requirements */}
                <div className="space-y-2">
                  {requirements.elo > 0 && (
                    <div className="space-y-1">
                      <div className="flex items-center justify-between text-xs">
                        <span className="text-muted-foreground">ELO Required</span>
                        <span className="font-medium">
                          <span className="text-orange-400">+{requirements.elo}</span>
                          <span className="text-muted-foreground"> more</span>
                        </span>
                      </div>
                      <Progress value={progress.elo} className="h-1.5" />
                    </div>
                  )}
                  
                  {requirements.problems > 0 && (
                    <div className="space-y-1">
                      <div className="flex items-center justify-between text-xs">
                        <span className="text-muted-foreground">Problems Required</span>
                        <span className="font-medium">
                          <span className="text-orange-400">+{requirements.problems}</span>
                          <span className="text-muted-foreground"> more</span>
                        </span>
                      </div>
                      <Progress value={progress.problems} className="h-1.5" />
                    </div>
                  )}
                </div>
              </div>
            </motion.div>

            {/* Benefits Preview */}
            {next_rank.benefits && next_rank.benefits.length > 0 && (
              <div className="p-3 rounded-lg bg-primary/5 border border-primary/10">
                <p className="text-xs font-medium text-primary mb-2">
                  🎁 Benefits when you reach {next_rank.name}:
                </p>
                <ul className="text-xs text-muted-foreground space-y-1">
                  {next_rank.benefits.slice(0, 3).map((benefit, i) => (
                    <li key={i} className="flex items-start gap-2">
                      <span className="text-primary">•</span>
                      <span>{benefit}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}

        {/* Max Rank Achieved */}
        {isMaxRank && (
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="p-6 rounded-lg bg-gradient-to-br from-yellow-500/20 to-orange-500/20 border-2 border-yellow-500/30 text-center"
          >
            <div className="text-6xl mb-3">🏆</div>
            <h3 className="font-secondary text-2xl font-bold text-yellow-400 mb-2">
              Maximum Rank Achieved!
            </h3>
            <p className="text-sm text-muted-foreground mb-3">
              You've reached the pinnacle of CodeChain! Continue solving to maintain your legendary status.
            </p>
            <div className="flex items-center justify-center gap-2 text-xs text-yellow-400">
              <Trophy className="w-4 h-4" />
              <span className="font-medium">Elite Status: Active</span>
            </div>
          </motion.div>
        )}

        {/* Current Rank Benefits */}
        {current_rank.benefits && current_rank.benefits.length > 0 && (
          <div className="p-3 rounded-lg bg-secondary/20 border border-border">
            <p className="text-xs font-medium mb-2">✨ Your Current Benefits:</p>
            <ul className="text-xs text-muted-foreground space-y-1">
              {current_rank.benefits.map((benefit, i) => (
                <li key={i} className="flex items-start gap-2">
                  <CheckCircle className="w-3 h-3 text-green-400 mt-0.5" />
                  <span>{benefit}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default RankProgress;
