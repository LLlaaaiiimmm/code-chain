import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import { Button } from "../components/ui/button";
import { Card, CardContent } from "../components/ui/card";
import { 
  Code2, Trophy, Users, Zap, Shield, Terminal, 
  ChevronRight, Star, TrendingUp, Award, Boxes
} from "lucide-react";

const Landing = ({ user }) => {
  const features = [
    {
      icon: <Terminal className="w-6 h-6" />,
      title: "Real Solidity Sandbox",
      description: "Execute smart contracts in an isolated environment with instant feedback"
    },
    {
      icon: <Trophy className="w-6 h-6" />,
      title: "ELO Rating System",
      description: "Dynamic rating that reflects your true skill level across all challenges"
    },
    {
      icon: <Users className="w-6 h-6" />,
      title: "Global Leaderboards",
      description: "Compete with developers worldwide and climb the rankings"
    },
    {
      icon: <Zap className="w-6 h-6" />,
      title: "Hackathon Engine",
      description: "Participate in sponsored competitions with real prize pools"
    },
    {
      icon: <Shield className="w-6 h-6" />,
      title: "Security Challenges",
      description: "Master vulnerability detection and secure coding practices"
    },
    {
      icon: <Award className="w-6 h-6" />,
      title: "NFT Certificates",
      description: "Earn verifiable on-chain credentials for your achievements"
    }
  ];

  const stats = [
    { value: "10,000+", label: "Developers" },
    { value: "500+", label: "Challenges" },
    { value: "$250K+", label: "Prize Pool" },
    { value: "50+", label: "Partners" }
  ];

  const difficulties = [
    { level: "Junior", color: "text-green-400", problems: 150 },
    { level: "Middle", color: "text-yellow-400", problems: 180 },
    { level: "Senior", color: "text-orange-400", problems: 120 },
    { level: "Expert", color: "text-red-400", problems: 50 }
  ];

  return (
    <div className="min-h-screen bg-background relative overflow-hidden">
      {/* Noise overlay */}
      <div className="noise-overlay fixed inset-0 pointer-events-none z-0" />
      
      {/* Grid pattern */}
      <div className="grid-pattern fixed inset-0 pointer-events-none z-0 opacity-50" />

      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 glass">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <Link to="/" className="flex items-center gap-2">
              <Boxes className="w-8 h-8 text-primary" />
              <span className="font-secondary text-xl font-bold">CodeChain</span>
            </Link>
            
            <div className="hidden md:flex items-center gap-8">
              <Link to="/problems" className="text-muted-foreground hover:text-foreground transition-colors">
                Problems
              </Link>
              <Link to="/leaderboard" className="text-muted-foreground hover:text-foreground transition-colors">
                Leaderboard
              </Link>
              <Link to="/hackathons" className="text-muted-foreground hover:text-foreground transition-colors">
                Hackathons
              </Link>
              <Link to="/pricing" className="text-muted-foreground hover:text-foreground transition-colors">
                Pricing
              </Link>
            </div>

            <div className="flex items-center gap-3">
              {user ? (
                <Link to="/dashboard">
                  <Button data-testid="dashboard-btn" className="glow-primary">
                    Dashboard
                  </Button>
                </Link>
              ) : (
                <>
                  <Link to="/login">
                    <Button variant="ghost" data-testid="login-btn">Login</Button>
                  </Link>
                  <Link to="/register">
                    <Button data-testid="register-btn" className="glow-primary">
                      Get Started
                    </Button>
                  </Link>
                </>
              )}
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative pt-32 pb-20 px-4">
        <div className="max-w-7xl mx-auto">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-center max-w-4xl mx-auto"
          >
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-8">
              <Star className="w-4 h-4 text-primary" />
              <span className="text-sm text-primary font-medium">The #1 Platform for Web3 Developers</span>
            </div>
            
            <h1 className="font-secondary text-5xl md:text-7xl font-bold tracking-tight leading-none mb-6">
              Master Blockchain
              <br />
              <span className="text-primary">Development</span>
            </h1>
            
            <p className="text-lg md:text-xl text-zinc-400 max-w-2xl mx-auto mb-10">
              Practice real-world smart contract challenges, compete in hackathons, 
              and get hired by top Web3 companies. All in one platform.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link to="/register">
                <Button size="lg" data-testid="hero-cta-btn" className="text-lg px-8 py-6 glow-primary">
                  Start Coding Free
                  <ChevronRight className="w-5 h-5 ml-2" />
                </Button>
              </Link>
              <Link to="/problems">
                <Button size="lg" variant="outline" className="text-lg px-8 py-6">
                  Browse Problems
                </Button>
              </Link>
            </div>
          </motion.div>

          {/* Stats */}
          <motion.div 
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-20"
          >
            {stats.map((stat, i) => (
              <div key={i} className="text-center p-6 rounded-lg bg-card/50 border border-border">
                <div className="font-secondary text-3xl md:text-4xl font-bold text-primary mb-1">
                  {stat.value}
                </div>
                <div className="text-sm text-muted-foreground">{stat.label}</div>
              </div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Code Preview Section */}
      <section className="py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <h2 className="font-secondary text-3xl md:text-5xl font-semibold tracking-tight mb-6">
                Write. Test. Deploy.
                <br />
                <span className="text-muted-foreground">All in Browser.</span>
              </h2>
              <p className="text-zinc-400 text-lg mb-8">
                Our integrated development environment supports Solidity, Rust, and Move. 
                Get instant feedback on your code with automated testing and gas analysis.
              </p>
              
              <div className="space-y-4">
                {difficulties.map((d, i) => (
                  <div key={i} className="flex items-center gap-4">
                    <div className={`w-3 h-3 rounded-full ${d.color.replace('text-', 'bg-')}`} />
                    <span className={`font-medium ${d.color}`}>{d.level}</span>
                    <span className="text-muted-foreground">{d.problems} problems</span>
                  </div>
                ))}
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="relative"
            >
              <div className="bg-card rounded-lg border border-border overflow-hidden">
                <div className="flex items-center gap-2 px-4 py-3 bg-secondary/50 border-b border-border">
                  <div className="w-3 h-3 rounded-full bg-red-500" />
                  <div className="w-3 h-3 rounded-full bg-yellow-500" />
                  <div className="w-3 h-3 rounded-full bg-green-500" />
                  <span className="ml-2 text-sm text-muted-foreground font-mono">SimpleToken.sol</span>
                </div>
                <pre className="p-4 text-sm font-mono overflow-x-auto">
                  <code className="text-zinc-300">
{`// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleToken {
    mapping(address => uint256) private balances;
    
    function mint(uint256 amount) public {
        balances[msg.sender] += amount;
    }
    
    function transfer(address to, uint256 amount) 
        public 
    {
        require(balances[msg.sender] >= amount);
        balances[msg.sender] -= amount;
        balances[to] += amount;
    }
}`}
                  </code>
                </pre>
              </div>
              
              {/* Floating badges */}
              <div className="absolute -top-4 -right-4 px-3 py-1 bg-green-500/20 text-green-400 text-sm font-medium rounded-full border border-green-500/30">
                All tests passed
              </div>
              <div className="absolute -bottom-4 -left-4 px-3 py-1 bg-purple-500/20 text-purple-400 text-sm font-medium rounded-full border border-purple-500/30">
                Gas: 21,000
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="py-20 px-4 bg-card/30">
        <div className="max-w-7xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="font-secondary text-3xl md:text-5xl font-semibold tracking-tight mb-4">
              Everything You Need to Excel
            </h2>
            <p className="text-zinc-400 text-lg max-w-2xl mx-auto">
              From learning basics to mastering advanced DeFi patterns, we've got you covered.
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((feature, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: i * 0.1 }}
              >
                <Card className="h-full bg-card/50 border-border hover:border-primary/50 transition-all duration-300 group cursor-pointer">
                  <CardContent className="p-6">
                    <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4 group-hover:scale-110 transition-transform">
                      {feature.icon}
                    </div>
                    <h3 className="font-secondary text-xl font-semibold mb-2">{feature.title}</h3>
                    <p className="text-muted-foreground">{feature.description}</p>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Hackathon Section */}
      <section className="py-20 px-4 relative">
        <div 
          className="absolute inset-0 opacity-10"
          style={{
            backgroundImage: `url(https://images.unsplash.com/photo-1560439514-0fc9d2cd5e1b?crop=entropy&cs=srgb&fm=jpg&q=85)`,
            backgroundSize: 'cover',
            backgroundPosition: 'center'
          }}
        />
        <div className="max-w-7xl mx-auto relative z-10">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/20 border border-purple-500/30 mb-6">
                <Trophy className="w-4 h-4 text-purple-400" />
                <span className="text-sm text-purple-400 font-medium">Hackathons</span>
              </div>
              
              <h2 className="font-secondary text-3xl md:text-5xl font-semibold tracking-tight mb-6">
                Compete. Win. Get Hired.
              </h2>
              <p className="text-zinc-400 text-lg mb-8">
                Join hackathons sponsored by leading blockchain companies. 
                Solve real problems, win prizes, and get noticed by top recruiters.
              </p>
              
              <div className="flex flex-wrap gap-4">
                <div className="px-4 py-2 rounded-lg bg-card border border-border">
                  <div className="text-2xl font-bold text-primary">$25K</div>
                  <div className="text-sm text-muted-foreground">DeFi Security Challenge</div>
                </div>
                <div className="px-4 py-2 rounded-lg bg-card border border-border">
                  <div className="text-2xl font-bold text-orange-400">$15K</div>
                  <div className="text-sm text-muted-foreground">Gas Wars 2024</div>
                </div>
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              className="relative"
            >
              <Card className="bg-card/80 backdrop-blur border-border">
                <CardContent className="p-6">
                  <div className="flex items-center gap-4 mb-6">
                    <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
                      <Shield className="w-6 h-6 text-white" />
                    </div>
                    <div>
                      <h3 className="font-secondary text-xl font-semibold">DeFi Security Challenge</h3>
                      <p className="text-sm text-muted-foreground">Starts in 7 days</p>
                    </div>
                  </div>
                  
                  <div className="space-y-3 mb-6">
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Prize Pool</span>
                      <span className="font-semibold text-primary">$25,000</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Participants</span>
                      <span className="font-semibold">342 / 500</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Duration</span>
                      <span className="font-semibold">7 days</span>
                    </div>
                  </div>
                  
                  <Link to="/hackathons">
                    <Button className="w-full glow-purple bg-purple-600 hover:bg-purple-700">
                      Register Now
                    </Button>
                  </Link>
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="font-secondary text-3xl md:text-5xl font-semibold tracking-tight mb-6">
              Ready to Level Up?
            </h2>
            <p className="text-zinc-400 text-lg mb-10">
              Join thousands of developers mastering blockchain technology.
              Start your journey today - it's free.
            </p>
            
            <Link to="/register">
              <Button size="lg" data-testid="cta-register-btn" className="text-lg px-10 py-6 glow-primary">
                Create Free Account
                <ChevronRight className="w-5 h-5 ml-2" />
              </Button>
            </Link>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border py-12 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center gap-6">
            <div className="flex items-center gap-2">
              <Boxes className="w-6 h-6 text-primary" />
              <span className="font-secondary text-lg font-bold">CodeChain</span>
            </div>
            
            <div className="flex items-center gap-6 text-sm text-muted-foreground">
              <Link to="/problems" className="hover:text-foreground transition-colors">Problems</Link>
              <Link to="/leaderboard" className="hover:text-foreground transition-colors">Leaderboard</Link>
              <Link to="/hackathons" className="hover:text-foreground transition-colors">Hackathons</Link>
              <Link to="/pricing" className="hover:text-foreground transition-colors">Pricing</Link>
            </div>
            
            <div className="text-sm text-muted-foreground">
              © 2024 CodeChain. All rights reserved.
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Landing;
